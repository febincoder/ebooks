from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,get_user_model,logout
from django.contrib.auth.decorators import login_required
import json
from.models import Product
# Create your views here.
def index(request): 
    language = request.GET.get('language', '')  
    author = request.GET.get('author', '')  
    price_range = request.GET.get('price', '')  
    publisher = request.GET.get('publisher', '') 
    year= request.GET.get('year', '')  
    products = Product.objects.all()
    
    if language:
        products = products.filter(language=language) 
    
    if author:
        products = products.filter(author=author) 
    if price_range:
        min_price, max_price = map(int, price_range.split('-'))  
        products = products.filter(price__gte=min_price, price__lte=max_price)  
    
    if publisher:
        products = products.filter(publisher=publisher)
    if year:
        products = products.filter(year=year) 
    
    context = {
        'product': products,
    }
    return render(request, 'web/shop-grid.html', context)

def register_1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if(pass1!=pass2):
            print('password not equal'*20)
            return redirect('web:register')
        else:
            if User.objects.filter(username=username).exists():
                print('user already exist')
                return redirect('web:register')
            else:
                customer = User.objects.create_user(username=username,password=pass1)
                return redirect('web:login')
           

    return render(request,"web/register.html")

def login_1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('web:index')
        else:  
            print('hi')
            return redirect('web:register')
    return render(request,"web/login.html")







