from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import CustomUSerCreationForm, UpdateUserForm
from .models import Product

def register(request):
    if request.method == 'POST':
        form = CustomUSerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return HttpResponseRedirect('/login')
    else:
        form = CustomUSerCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('profile')
    else:
        form = UpdateUserForm()
    return render(request, 'profile.html', {'form':form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request,'index.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def discount_product(request):
    discounted_products = Product.objects.filter(discount__gt=0)
    return render(request, 'discounted-products.html', {'discounted_products' : discounted_products})

