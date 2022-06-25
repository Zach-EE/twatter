from django.shortcuts import render

def homepage(request):
    return render(request, 'base/homepage.html')

def login(request):
    return render(request, 'base/login.html')

def signup(request):
    return render(request, 'base/signup.html')
