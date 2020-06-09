from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import User, Question, myUser, Status
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request, "tmp.html")


def 垃圾(request):
    ls = Question.objects.get(no="P0004")
    return render(request, "垃圾.html", {"question": ls})



def logout(request):
    auth.logout(request)
    return render(request, "tmp.html")


def login(request):
    message = "傻逼"
    result = False
    if request.method == "POST":
        username = request.POST.get('id')
        password = request.POST.get('psw')
        if username and password:
            try:
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    request.session['is_login'] = True
                    request.session['user_id'] = str(user.id)
                    request.session['user_name'] = str(user)
                    return JsonResponse({"result": True, "message": message})
                else:
                    message = "密码不正确!"
            except:
                message = "用户不存在!"
            return JsonResponse({"result": False, "message": message})

        return JsonResponse({"result": False, "message": message})

    return render(request, "login.html")



def register(request):
    return render(request, "register.html")


def forgetPassword(request):
    return render(request, "forgetPassword.html")


@login_required
def changePassword(request):
    return render(request, "changePassword.html")


@login_required
def makeNewQuestion(request):
    return render(request, "makeNewQuestion.html")


def hub(request):
    ls = Question.objects.all()
    attemped = Status.objects.filter(username=request.user.username)
    return render(request, "hub.html", {"questions": ls, "attemped": attemped})


def detail(request):
    try:
        ls = Question.objects.get(no=int(request.path.split('/')[1][1:]))
    except:
        return render(request, "error.html")
    return render(request, "detail.html", {"question": ls})


def feedback(request):
    print(0)
    if request.method == "POST":
        try:
            subject = request.POST.get('subject').split()[0]
            no = int(request.POST.get('no').split()[0])
            status = request.POST.get('status')
            username = request.user.username
            print(request.POST)
            print(1)
            try:
                tS = Status.objects.get(subject=subject, no=no, username=username)
                if tS is not None:
                    if tS.status == 1:
                        print(3)
                        return JsonResponse({"result": True})
                    if status == 'ac':
                        print(4)
                        Status.objects.filter(subject=subject, no=no, username=username).update(status=1)
            except:
                try:
                    print(2)
                    if status == 'ac':
                        print(5)
                        S = Status(status=1, subject=subject, no=no, username=username)
                    else:
                        print(6)
                        S = Status(status=0, subject=subject, no=no, username=username)
                    S.save()
                    print(7)
                    Question.objects.get(subject=subject, no=no).update(attempted=Question.objects.get(subject=subject, no=no).attempted+1)
                    return JsonResponse({"result": True})
                except:
                    print(8)
                    return render(request, "error.html")
        except:
            return render(request, "error.html")
    else:
        return render(request, "error.html")


def registerEnter(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    try:
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        myUser.objects.create(user=user)
    except Exception as err:
        result = False
        message = str(err)
    else:
        result = True
        message = "Register success"

    return JsonResponse({"result": result, "message": message})


@login_required
def makeNews(request):
    subject = 'M'
    question = request.POST.get('question')
    answer = request.POST.get('answer')
    title = request.POST.get('title')
    No = len(Question.objects.all())+1
    if question.split() == [] or answer.split() == [] or title.split() == []:
        return JsonResponse({"result": False})

    try:
        Q = Question(subject=subject, no=No, title=title, question=question, answer=answer)
        Q.save()
    except Exception as err:
        print(3)
        result = False
        message = str(err)
    else:
        print(4)
        result = True
        message = "Register success"
    return JsonResponse({"result": True})


@login_required
def personalPage(request):
    if request.method == "POST":
        img = request.FILES.get('img_file')
        path = request.user.username
        url = "luogu/static/image/personalHead/" + path + ".jpg"

        with open(url, 'wb') as f:
            for chunk in img.chunks():
                f.write(chunk)
        return JsonResponse({"result": True})
    try:
        user = User.objects.get(username=request.path.split('/')[2])
        if user:
            return render(request, "personalPage.html", {"user": user})
        else:
            return render(request, "error.html")
    except:
        return render(request, "error.html")
    return JsonResponse({"result": True})

