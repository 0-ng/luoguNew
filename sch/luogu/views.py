from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index(request):
    return render(request, "tmp.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")