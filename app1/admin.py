from django.contrib import admin
from app1.models import Order, Product

# Register your models here.

admin.site.register(Order)

@admin.register(Product)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','quantity','category']