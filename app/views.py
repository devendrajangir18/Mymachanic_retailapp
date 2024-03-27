from django.shortcuts import render, redirect, HttpResponse
from app.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.views import View
from app.forms import RegistrationForm


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
        profile = profile(name= name, address= address, address2= address2, city = city, state = state, pin= pin)
        profile.save()
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

   
def auth_login(request):
    print("dfd")
    print(request.method)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        
        # check if user has entered correct credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            print("jkdfiuod")
            login(request,user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request, 'app/login.html')
    
    return render(request, 'app/login.html')

class RegistrationView(View):
    template_name = 'app/register.html'

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print("here")
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/login')  # Redirect to login page
        else:
            print(form.error_messages, form.errors)
        return render(request, self.template_name, {'form': form})

# def customerregistration(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customerregistration = customerregistration(username= username, email= email, password= password,)
#         customerregistration.save()
#         messages.success(request, 'Your message has been sent')
 
#     return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
