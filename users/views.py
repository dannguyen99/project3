from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			pswd = form.cleaned_data.get('password1')
			messages.success(request, f'Account successsfully created for {username}')
			user = authenticate(username=username, password=pswd)
			login(request, user)
			return redirect('index')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form' : form})
