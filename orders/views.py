from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from .models import *

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html")
    context = {
        "pizzas": Pizza.objects.all(),
        "toppings": Topping.objects.all(),
        "pastas": Pasta.objects.all(),
        "subs": Sub.objects.all(),
        "salads": Salad.objects.all(),
        "dinner_platters": Dinner_Platter.objects.all()
    }
    return render(request, "orders/index.html", context)


def menu(request):
    context = {
        "pizzas": Pizza.objects.all(),
        "toppings": Topping.objects.all(),
        "pastas": Pasta.objects.all(),
        "subs": Sub.objects.all(),
        "salads": Salad.objects.all(),
        "dinner_platters": Dinner_Platter.objects.all()
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
        c = Cart(username=user)
        c.save()
    except Exception as e:
        message = e
    context = {
        "message": message
    }
    return render(request, 'orders/sign_up.html', context)


def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'orders/login.html')


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def cart(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html")
    c = request.user.cart.first()
    context = {
        "pizzas": c.pizzas.all(),
        "pastas": c.pastas.all(),
        "salads": c.salads.all(),
        "dinner_platters": c.dinner_platters.all()
    }
    return render(request, 'orders/cart.html', context)


def order(request):
    try:
        name = request.GET['name']
        category = request.GET['category']
        p = Pizza.objects.filter(name=name, type=category).first()
        c = request.user.cart.first()
        c.pizzas.add(p)
        c.save()
        return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)})



def about(request):
    return render(request, 'orders/about.html')
