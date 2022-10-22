from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, '1_home.html')

def login(request):
    return render(request, '2_login.html')

def register(request):
    return render(request, 'register.html')

