from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def home(request):
    return render(request,'shop/index.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def discount_product(request):
    discounted_products = Product.objects.filter(discount__gt=0)
    return render(request, 'shop/discounted-products.html', {'discounted_products' : discounted_products})
