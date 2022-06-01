from unicodedata import name
from django.urls import path
from .import views

app_name='app1'

urlpatterns = [
    path('',views.products, name='products'),
    path('products/edit/<int:pk>/',views.products_edit, name='products-edit'),
    path('products/delete/<int:pk>/',views.product_delete, name='products-delete'),
    path('products/detail/<int:pk>/',views.product_detail, name='products-detail'),
    
    ]