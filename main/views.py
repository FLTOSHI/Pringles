from dbm import error

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.http import response

from main.forms import RegistrationForm


def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', data)

def about(request):
    data = {
        'title': 'О нас',
    }
    return render(request, 'main/about.html', data)

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'main/signup.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'main/login.html', {'error': 'неверный логин или пароль'})
    return render(request, 'main/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')