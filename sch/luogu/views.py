from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import LuoguUser, User, Question
# Create your views here.

def index(request):
    return render(request, "tmp.html")

def 垃圾(request):
    ls = Question.objects.get(no="P0004")
    return render(request, "垃圾.html", {"question": ls})


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
    # ls = [
    #     {"status": 0,
    #      "no": "P1000",
    #      "title": "超级玛丽游戏",
    #      "link": "https://www.luogu.com.cn/problem/P1000",
    #      "tag": "傻逼题",
    #      "difficulty": "入门",
    #      "pass": 0.4
    #      },
    #     {"status": 0,
    #      "no": "P1001",
    #      "title": "A+B Problem",
    #      "link": "https://www.luogu.com.cn/problem/P1001",
    #      "tag": "傻逼题",
    #      "difficulty": "入门",
    #      "pass": 0.6
    #      },
    #     {"status": 0,
    #      "no": "P1002",
    #      "title": "过河卒",
    #      "link": "https://www.luogu.com.cn/problem/P1002",
    #      "tag": "NOIp普及组",
    #      "difficulty": "普及-",
    #      "pass": 0.3
    #      },
    #     {"status": 0,
    #      "no": "P1003",
    #      "title": "铺地毯",
    #      "link": "https://www.luogu.com.cn/problem/P1003",
    #      "tag": "NOIp提高组",
    #      "difficulty": "普及-",
    #      "pass": 0.4
    #      },
    #     {"status": 0,
    #      "no": "P1003",
    #      "title": "铺地毯",
    #      "link": "https://www.luogu.com.cn/problem/P1003",
    #      "tag": "NOIp提高组",
    #      "difficulty": "普及-",
    #      "pass": 0.4
    #      },
    #     {"status": 0,
    #      "no": "P1003",
    #      "title": "铺地毯",
    #      "link": "https://www.luogu.com.cn/problem/P1003",
    #      "tag": "NOIp提高组",
    #      "difficulty": "普及-",
    #      "pass": 0.4
    #      },
    #     {"status": 0,
    #      "no": "P1003",
    #      "title": "铺地毯",
    #      "link": "https://www.luogu.com.cn/problem/P1003",
    #      "tag": "NOIp提高组",
    #      "difficulty": "普及-",
    #      "pass": 0.4
    #      },
    #     {"status": 0,
    #      "no": "P1003",
    #      "title": "铺地毯",
    #      "link": "https://www.luogu.com.cn/problem/P1003",
    #      "tag": "NOIp提高组",
    #      "difficulty": "普及-",
    #      "pass": 0.4
    #      },
    # ]
    ls = Question.objects.all()
    # print(ls)
    return render(request, "hub.html", {"questions": ls})


def detail(request):
    print(request.path.split('/'))
    # for i in Question.objects.all():
    #     print(i.no)
    try:
        ls = Question.objects.get(no=request.path.split('/')[1])
    except:
        return render(request, "error.html")
    return render(request, "detail.html", {"question": ls})


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