from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import *
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        if password==request.POST.get('confirm_password'):
            user=User.objects.create(name=name,email=email)
            user.set_password(password)
            return redirect('login/')
        else:
            messages.error(request,'Password and Confirm Password does not match')    
    
    return render(request, 'signup.html')

def login_page(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        
        if User.objects.filter(name=name).exists():
            user=User.objects.get(name=name)
            is_valid=check_password(password,user.password) #first argument is password and second is hash password
            if is_valid:
                #login(request,user)
                return redirect('/')
            else:
                messages.error(request,'Invalid Password')
        else:
            messages.error(request, 'Invalid Username ')
                
    return render(request, 'login.html')
