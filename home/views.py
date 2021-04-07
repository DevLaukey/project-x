from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return render(request, 'home/home.html')

def dashboard(request):
    return render(request, 'home/sidebar.html')


def navbar(request):
    return render(request, 'home/navbar.html')