
from django.shortcuts import (get_object_or_404,
                              render,redirect,
                              HttpResponseRedirect)
from .models import Product
from .forms import ProductForm
from django.contrib import messages

# Create your views here.
def products(request):
    product = Product.objects.all()
    product_count = product.count()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('/')
    else:
        form = ProductForm()
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'app1/product.html',context)

def product_detail(request, pk):
    context = {
    }
    return render(request, 'app1/product_detail.html', context)

def products_edit(request, pk):
    item = Product.objects.get(id= pk)
    context ={}
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm(instance=item)
    context = { 'form': form}
    return render(request, 'app1/product_edit.html', context)

def product_delete(request, pk):
    if request.method == 'POST':
        item = Product.objects.get(id=pk)
        item.delete()
        return redirect('/')
    return render(request, 'app1/product_delete.html')