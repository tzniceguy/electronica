from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUSerCreationForm

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUSerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
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

def profile(request):
    return render(request, 'profile.html')

def user_logout(request):
    logout(request)
    return redirect('login')
