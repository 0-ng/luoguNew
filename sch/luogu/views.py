from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import User, Question, myUser, Status
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from fuzzywuzzy import fuzz
# Create your views here.

# def search(request):




def index(request):
    return render(request, "tmp.html")
    return render(request, "error.html")


def logout(request):
    auth.logout(request)
    return render(request, "tmp.html")
    return render(request, "error.html")



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
    return render(request, "error.html")


def register(request):
    return render(request, "register.html")
    return render(request, "error.html")


def forgetPassword(request):
    return render(request, "forgetPassword.html")
    return render(request, "error.html")


@login_required
def changePassword(request):
    return render(request, "changePassword.html")


@login_required
def makeNewQuestion(request):
    return render(request, "makeNewQuestion.html")
    return render(request, "error.html")


def hub(request):
    print(1)
    ls = Question.objects.all()
    print(2)
    no = request.GET.get('no')
    print(3)
    if no:
        print(1)
        print(no)
        for q in ls:
            ls.filter(no=q.no).update(score=fuzz.token_sort_ratio(no, q.no))
        ls = ls.order_by("-score")
        print(ls)
    print(ls)
    attemped = Status.objects.filter(username=request.user.username)
    for i in attemped:
        ls.filter(no=i.no).update(status=i.status)
    print(ls)
    return render(request, "hub.html", {"questions": ls})
    return render(request, "error.html")


def detail(request):
    try:
        # print(request.path)
        # print(request.path.split('/'))
        ls = Question.objects.get(no=request.path.split('/')[-1])
    except:
        # print("???")
        return render(request, "error.html")
    return render(request, "detail.html", {"question": ls})
    return render(request, "error.html")



def feedback(request):
    if request.method == "POST":
        try:
            subject = request.POST.get('subject')
            no = request.POST.get('no')
            status = request.POST.get('status')
            username = request.user.username
            try:
                tS = Status.objects.get(subject=subject, no=subject+no, username=username)
                if tS is not None:
                    if tS.status == 1:
                        return JsonResponse({"result": True})
                    if status == 'ac':
                        Status.objects.filter(subject=subject, no=subject+no, username=username).update(status=1)
            except:
                try:
                    if status == 'ac':
                        S = Status(status=1, subject=subject, no=subject+no, username=username)
                    else:
                        S = Status(status=2, subject=subject, no=subject+no, username=username)
                    S.save()
                    Question.objects.get(subject=subject, no=subject+no).update(attempted=Question.objects.get(subject=subject, no=subject+no).attempted+1)
                    return JsonResponse({"result": True})
                except:
                    return render(request, "error.html")
        except:
            return render(request, "error.html")
    else:
        return render(request, "error.html")
    return render(request, "error.html")


def registerEnter(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    print(username)
    print(password)
    print(email)

    try:
        print(1)
        user = User(username=username, email=email)
        print(2)
        user.set_password(password)
        print(3)
        user.save()
        print(4)
        myUser.objects.create(user=user)
        print(5)
    except Exception as err:
        result = False
        message = str(err)
    else:
        result = True
        message = "Register success"

    return JsonResponse({"result": result, "message": message})
    return render(request, "error.html")


@login_required
def makeNews(request):
    subject = 'M'
    question = request.POST.get('question')
    answer = request.POST.get('answer')
    title = request.POST.get('title')
    No = "%04d" % (Question.objects.count()+1)
    print(No)
    if question.split() == [] or answer.split() == [] or title.split() == []:
        return JsonResponse({"result": False})

    try:
        Q = Question(subject=subject, no=subject+No, title=title, question=question, answer=answer)
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
    return render(request, "error.html")


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
    return render(request, "error.html")

