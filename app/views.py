from django.shortcuts import render, HttpResponse
from app.models import *
from django.contrib import messages

def home(request):
 return render(request, 'app/home.html')

def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = int(request.POST.get('pin'))
        contact = profile(name= name, address= address, address2= address2, city = city, state = state, pin= pin)
        contact.save()
        messages.success(request, 'Your message has been sent')
    
    return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('phone')
        register = Register(name= name, email= email, password= password,)
        register.save()
        messages.success(request, 'Your message has been sent')
 
    return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
