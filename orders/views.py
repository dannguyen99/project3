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
    "i":0
    }
    return render(request, "orders/menu.html", context)
