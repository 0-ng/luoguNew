from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import LuoguUser, User
# Create your views here.

def index(request):
    return render(request, "tmp.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def forgetPassword(request):
    return render(request, "forgetPassword.html")


def changePassword(request):
    return render(request, "changePassword.html")


def registerEnter(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    print(username)
    print(password)
    print(email)
    try:
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        LuoguUser.objects.create(user=user)
    except Exception as err:
        result = False
        message = str(err)
    else:
        result = True
        message = "Register success"

    return JsonResponse({"result": result, "message": message})