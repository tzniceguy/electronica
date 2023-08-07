from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shop'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('discounted-products/', views.discount_product, name='discounted-products'),
]
