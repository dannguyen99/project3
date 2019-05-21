from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    return render(request, "orders/index.html")

def home(request):
    return render(request, "orders/index.html")

def menu(request):
    context = {
    "pizzas":Pizza.objects.all(),
    "toppings":Topping.objects.all(),
    "pastas":Pasta.objects.all(),
    "subs":Sub.objects.all(),
    "salads":Salad.objects.all(),
    "dinner_platters":Dinner_Platter.objects.all()
    }
    return render(request, "orders/menu.html", context)

def sign_up(request):
    return render(request, 'orders/sign_up.html')

def signup_view(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    try:
        user = User.objects.create_user(username, email, password)
        user.save()
        message = "You have succesfully sign up"
    except Exception as e:
        message = e
    context = {
    "message":message
    }
    return render(request, 'orders/sign_up.html', context)
