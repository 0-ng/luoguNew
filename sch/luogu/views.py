import json
import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import User, Question, myUser, Status, Contributions, Tag
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from fuzzywuzzy import fuzz
import datetime
# Create your views here.

def test(request):
    return render(request, "垃圾.html")


def acc_login(request):
    return render(request, "login.html")




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

def error(request):
    return render(request, "error.html")


@login_required
def makeNewQuestion(request):
    return render(request, "makeNewQuestion.html")
    return render(request, "error.html")


def hub(request):
    ls = Question.objects.all()

    orderBy = request.GET.get('orderBy')
    order = request.GET.get('order')
    if orderBy:
        if order == "asc":
            ls = ls.order_by("-" + orderBy)
        elif order == "desc":
            ls = ls.order_by(orderBy)
    else:
        orderBy == "none"
        order == "none"


    select_tag = request.GET.get('select_tag')
    print("select_tag", select_tag)
    if select_tag:
        choices = [
            "",
            '函数与极限',
            '导数与微分',
            '微分中值定理与导数的应用',
            '不定积分',
            '定积分',
            '微分方程',
            '向量代数与空间解析几何',
            '多元函数微分法及其应用',
            '重积分',
            '曲线积分与曲面积分',
            '无穷级数'
        ]
        print("tag ", select_tag)
        ls = ls.filter(tag__name__contains=choices[int(select_tag)])
        print("fill ok")

    no = request.GET.get('no')
    print(no)
    if no:
        print(1)
        for q in ls:
            print(2)
            ls.filter(no=q.no).update(score=fuzz.token_sort_ratio(no, q.no))
        print(ls)
        ls = ls.order_by("-score")

    attemped = Status.objects.filter(username=request.user.username)
    for i in attemped:
        ls.filter(no=i.no).update(status=i.status)
    ls = list(ls)
    for i in range(len(ls)):
        ls[i] = model_to_dict(ls[i])
    return render(request, "hub.html", {"questions": ls, "order": order, "orderBy": orderBy})
    return render(request, "error.html")


def detail(request):
    try:
        ls = Question.objects.get(no=request.path.split('/')[-1])
    except:
        return render(request, "error.html")
    return render(request, "detail.html", {"question": ls})
    return render(request, "error.html")


@login_required
def feedback(request):
    if request.method == "POST":
        try:
            subject = request.POST.get('subject')
            no = request.POST.get('no')
            status = request.POST.get('status')
            username = request.user.username
            if status == 'ac':
                num = Question.objects.get(subject=subject, no=subject + no).accepted
                Question.objects.filter(subject=subject, no=subject + no).update(accepted=num+1)
            else:
                try:
                    num = Contributions.objects.get(username=username, date=datetime.date.today()).num
                    Contributions.objects.filter(username=username, date=datetime.date.today()).update(num=num+1)
                    print("更新ok")
                except:
                    Contributions(username=username, num=1).save()
                    print("创建ok")
                num = Question.objects.get(subject=subject, no=subject + no).attempted
                Question.objects.filter(subject=subject, no=subject + no).update(attempted=num+1)

            Question.objects.filter(subject=subject, no=subject + no).update(
                pass_ratio=100*Question.objects.get(subject=subject, no=subject + no).accepted/Question.objects.get(subject=subject, no=subject + no).attempted)
            try:
                tS = Status.objects.get(subject=subject, no=subject+no, username=username)
                if tS is not None:  # 做过了
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
    tags = json.loads(request.POST.get('tags'))
    No = "%04d" % (Question.objects.count()+1)
    # print("tags:", tags)
    # for i in tags:
    #     print(i)
    # print()
    # print(No)
    if question.split() == [] or answer.split() == [] or title.split() == []:
        return JsonResponse({"result": False})

    try:
        Q = Question(subject=subject, no=subject+No, title=title, question=question, answer=answer)
        # print(1)
        Q.save()
        choices = [
            "",
            '函数与极限',
            '导数与微分',
            '微分中值定理与导数的应用',
            '不定积分',
            '定积分',
            '微分方程',
            '向量代数与空间解析几何',
            '多元函数微分法及其应用',
            '重积分',
            '曲线积分与曲面积分',
            '无穷级数'
        ]
        for i in tags:
            try:
                tag = Tag.objects.get(name=choices[int(i)])
            except:
                tag = Tag(name=choices[int(i)])
                tag.save()
            # print(tag.name)
            # print("tag ok ")
            Q.tag.add(tag)
            # print("Q ok")

        # print(2)
    except Exception as err:
        # print(3)
        result = False
        message = str(err)
    else:
        # print(4)
        result = True
        message = "Register success"
    return JsonResponse({"result": result})
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
            # print(1)
            # ls = Contributions.objects.filter(username=user.username)
            # print(2)
            # ls = ls.order_by("date")
            # print(ls)
            # print(3)
            ls = []
            now = datetime.datetime.now().date()
            monday = now + datetime.timedelta(days=-now.weekday())
            offset = datetime.timedelta(days=-51*7)
            last_year = monday+offset
            one_day = datetime.timedelta(days=1)
            for i in range(52):
                tmpls = {
                    "ls":[],
                    "offset": i*16
                }
                if i == 51:
                    for j in range(now.weekday()+1):
                        tmp = dict()
                        tmp['date'] = last_year.__str__()
                        tmp['num'] = random.randint(0, 35)
                        tmp['y'] = j*15
                        last_year += one_day
                        tmpls["ls"].append(tmp)
                else:
                    for j in range(7):
                        tmp = dict()
                        tmp['date'] = last_year.__str__()
                        tmp['num'] = random.randint(0, 35)
                        tmp['y'] = j*15
                        last_year += one_day
                        tmpls["ls"].append(tmp)
                ls.append(tmpls)

            # print(ls)

            return render(request, "personalPage.html", {"user": user, "a": ls})
        else:
            return render(request, "error.html")
    except:
        return render(request, "error.html")
    return render(request, "error.html")

