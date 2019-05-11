from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Project 3: TODO")

def home(request):
    return render(request, "orders/index.html")

def menu(request):
    return render(request, "orders/menu.html")
