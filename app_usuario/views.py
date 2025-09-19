
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('usuario_pad')
		else:
			messages.error(request, 'Invalid credentials')
	return render(request, 'login.html')

from .models import Usuario

def register_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		confirm_password = request.POST.get('confirm_password')
		if password != confirm_password:
			messages.error(request, 'Passwords do not match')
		elif Usuario.objects.filter(username=username).exists():
			messages.error(request, 'Username already exists')
		else:
			user = Usuario(username=username)
			user.set_password(password)
			user.save()
			messages.success(request, 'Registration successful! You can now log in.')
			return redirect('login')
	return render(request, 'register.html')
def usuario_pad(request):
	return render(request, 'usuario.html')

# Create your views here.

from django.shortcuts import render

def notepad(request):
	return render(request, 'index.html')
