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


def question(request):
    return render(request, "question.html")


def hub(request):
    ls = [
        {"status": 0,
         "no": "P1000",
         "title": "超级玛丽游戏",
         "link": "https://www.luogu.com.cn/problem/P1000",
         "tag": "傻逼题",
         "difficulty": "入门",
         "pass": 0.4
         },
        {"status": 0,
         "no": "P1001",
         "title": "A+B Problem",
         "link": "https://www.luogu.com.cn/problem/P1001",
         "tag": "傻逼题",
         "difficulty": "入门",
         "pass": 0.6
         },
        {"status": 0,
         "no": "P1002",
         "title": "过河卒",
         "link": "https://www.luogu.com.cn/problem/P1002",
         "tag": "NOIp普及组",
         "difficulty": "普及-",
         "pass": 0.3
         },
        {"status": 0,
         "no": "P1003",
         "title": "铺地毯",
         "link": "https://www.luogu.com.cn/problem/P1003",
         "tag": "NOIp提高组",
         "difficulty": "普及-",
         "pass": 0.4
         },
        {"status": 0,
         "no": "P1003",
         "title": "铺地毯",
         "link": "https://www.luogu.com.cn/problem/P1003",
         "tag": "NOIp提高组",
         "difficulty": "普及-",
         "pass": 0.4
         },
        {"status": 0,
         "no": "P1003",
         "title": "铺地毯",
         "link": "https://www.luogu.com.cn/problem/P1003",
         "tag": "NOIp提高组",
         "difficulty": "普及-",
         "pass": 0.4
         },
        {"status": 0,
         "no": "P1003",
         "title": "铺地毯",
         "link": "https://www.luogu.com.cn/problem/P1003",
         "tag": "NOIp提高组",
         "difficulty": "普及-",
         "pass": 0.4
         },
        {"status": 0,
         "no": "P1003",
         "title": "铺地毯",
         "link": "https://www.luogu.com.cn/problem/P1003",
         "tag": "NOIp提高组",
         "difficulty": "普及-",
         "pass": 0.4
         },
    ]
    return render(request, "hub.html", {"questions": ls})


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