from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Logout de usuário
def user_logout(request):
    logout(request)
    return redirect('home')
