from django.http import HttpResponse
from django.shortcuts import render
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
