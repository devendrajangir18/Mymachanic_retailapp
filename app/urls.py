from django.contrib import admin
from django.urls import path
from app import views
from .views import RegistrationView

urlpatterns = [
    path('', views.home),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('login/', views.auth_login, name='login'),
    path('register', RegistrationView.as_view(), name='register'),
    # path('registration', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
]
