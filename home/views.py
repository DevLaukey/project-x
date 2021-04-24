from django.shortcuts import render

from django.http import HttpResponse


def landing(request):
    return render(request, 'home/landing.html')
def personnel_index(request):
    return render(request, 'home/Personnel/index.html')

def roles_index(request):
    return render(request,'home/Personnel/Roles/index.html')