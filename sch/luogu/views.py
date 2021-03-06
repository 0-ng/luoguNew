import json
import random

import markdown
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import User, Question, myUser, Status, Contributions, Tag, History, Note
from django.contrib import auth
from fuzzywuzzy import fuzz
from .myforms import CreateArticleForm, CreateQuestion
import datetime
# Create your views here.

dev = True
# dev = False



def index(request):
    try:
        '''猜你在做'''
        choices = {
            '函数与极限': 1,
            '导数与微分': 2,
            '微分中值定理与导数的应用': 3,
            '不定积分': 4,
            '定积分': 5,
            '微分方程': 6,
            '向量代数与空间解析几何': 7,
            '多元函数微分法及其应用': 8,
            '重积分': 9,
            '曲线积分与曲面积分': 10,
            '无穷级数': 11
        }
        tags = Tag.objects.all()
        ls = list(set([i.name for i in tags]))
        tagls = []
        num = min(len(ls), 4)
        for i in range(num):
            if i%2 == 0:
                tagls.append([])
            tagls[-1].append({"name": ls[i], "num": choices[ls[i]]})


        '''推荐'''
        username = request.user.username
        recommend = None
        if username:
            # print(username)
            try:
                pre = History.objects.filter(username=username)
                if pre:
                    pre = pre.latest("date").question.tag.all()
                    rd = random.choice(pre)
                    q = Question.objects.filter(tag__name=rd)
                    # print(q)
                    for i in range(5):
                        recommend = question = random.choice(q)
                        status = Status.objects.filter(username=username, no=question.no)
                        if status and status[0].status == 1:
                            continue
                        recommend = question
                        break
            except:
                pass
        # print(recommend)

        '''实时'''
        his = History.objects.all().order_by("-date")
        his = his[:min(15, his.count())]
        print(his)
        return render(request, r"luogu/index.html", {'tagls': tagls, 'recommend': recommend, 'his': his})
    except:
        return render(request, "luogu/error.html")


def logout(request):
    auth.logout(request)
    return redirect('/')



def login(request):
    message = "傻逼"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            try:
                print(username)
                print(password)
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
    else:
        return render(request, "luogu/login.html")


def register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        print(name)
        print(password)
        print(email)

        try:
            user = User(username=name, email=email)
            user.set_password(password)
            user.save()
            myUser.objects.create(user=user)
            result = True
            message = "Register success"

            if dev:
                with open("C:/luogu/luogu/sch/static/luogu/image/personalHead/none.jpg", 'rb') as f:
                    with open("C:/luogu/luogu/sch/static/luogu/image/personalHead/{}.jpg".format(username), 'wb') as f2:
                        f2.write(f.read())
            else:
                with open("/www/wwwroot/0ng.run/static/luogu/image/personalHead/none.jpg", 'rb') as f:
                    with open("/www/wwwroot/0ng.run/static/luogu/image/personalHead/{}.jpg".format(name), 'wb') as f2:
                        f2.write(f.read())

        except Exception as err:
            result = True
            message = str(err)

        return JsonResponse({"result": result, "message": message})
    else:
        return render(request, "luogu/register.html")



def forgetPassword(request):
    return render(request, "luogu/forgetPassword.html")


@login_required
def changePassword(request):
    return render(request, "luogu/changePassword.html")


def error(request):
    return render(request, "luogu/error.html")


# @login_required
# def makeNewQuestion(request):
#     if request.method =='POST':
#         try:
#             subject = 'M'
#             question = request.POST.get('question')
#             answer = request.POST.get('answer')
#             title = request.POST.get('title')
#             tags = json.loads(request.POST.get('tags'))
#             print(question)
#             print(answer)
#             print(title)
#             print(tags)
#             No = "%04d" % (Question.objects.count()+1)
#             if question.split() == [] or answer.split() == [] or title.split() == []:
#                 return JsonResponse({"result": False})
#             print(1)
#             try:
#                 Q = Question(subject=subject, no=subject+No, title=title, question=question, answer=answer)
#                 # print(1)
#                 Q.save()
#                 print(2)
#                 choices = [
#                     "",
#                     '函数与极限',
#                     '导数与微分',
#                     '微分中值定理与导数的应用',
#                     '不定积分',
#                     '定积分',
#                     '微分方程',
#                     '向量代数与空间解析几何',
#                     '多元函数微分法及其应用',
#                     '重积分',
#                     '曲线积分与曲面积分',
#                     '无穷级数'
#                 ]
#                 for i in tags:
#                     print("i=", i)
#                     try:
#                         tag = Tag.objects.get(name=choices[int(i)])
#                     except:
#                         print(choices[int(i)])
#                         Tag.objects.create(name=choices[int(i)])
#                         print("???")
#                         tag = Tag.objects.get(name=choices[int(i)])
#                         # tag.save()
#                     print(tag.name)
#                     print("tag ok ")
#                     Q.tag.add(tag)
#                     print("Q ok")
#                 result = True
#             except:
#                 result = False
#             return JsonResponse({"result": result})
#         except:
#             return render(request, "luogu/error.html")
#     else:
#         form = CreateQuestion()
#         return render(request, "luogu/makeNewQuestion.html", {'form': form})


def hub(request):
    ls = Question.objects.all()

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
        ls = ls.filter(tag__name=choices[int(select_tag)])
        print("fill ok")

    attemped = Status.objects.filter(username=request.user.username)
    ret = []
    for i in ls:
        question = dict()
        question["no"] = i.no
        question["title"] = i.title
        question["tag"] = [j for j in i.tag.all()]
        question["difficulty"] = i.difficulty
        question["pass_ratio"] = i.pass_ratio
        # print(i.no)
        try:
            question["status"] = attemped.get(no=i.no).status
        except:
            question["status"] = 0
        ret.append(question)


    orderBy = request.GET.get('orderBy')
    order = request.GET.get('order')
    if orderBy:
        print(ret[0])
        print(order)
        print(orderBy)
        if order == "asc":
            ret.sort(key=lambda x: x[orderBy], reverse=True)
            # ls = ls.order_by("-" + orderBy)
        elif order == "desc":
            ret.sort(key=lambda x: x[orderBy])
            # ls = ls.order_by(orderBy)
    else:
        orderBy = "none"
        order = "none"


    no = request.GET.get('no')
    if no:
        for question in ret:
            question["score"]=fuzz.token_sort_ratio(no, question['no'])
        ret.sort(key=lambda x: -x['score'])


    return render(request, "luogu/hub.html", {"questions": ret, "order": order, "orderBy": orderBy})
    return render(request, "luogu/error.html")


def detail(request, hubno=None):
    try:
        goto = request.GET.get("goto")
        if goto:
            no = request.GET.get("no")
            return redirect("/hub/{}".format(no))

        gotorandom = request.GET.get("gotorandom")
        if gotorandom:
            no = random.choice(Question.objects.all()).no
            return redirect("/hub/{}".format(no))
    except:
        return render(request, "luogu/error.html")

    try:
        ls = Question.objects.get(no=hubno)
        print(request.user)
        if request.user:
            print(1)
            try:
                print(hubno)
                User.objects.get(username=request.user)
                print(0.5)
                note = Note.objects.get(question_no=hubno, user=User.objects.get(username=request.user))
                print(2)
                note = note.body
                print(3)
            except:
                note = None
    except:
        return render(request, "luogu/error.html")
    return render(request, "luogu/detail.html", {"question": ls, 'note': note})
    return render(request, "luogu/error.html")


@login_required
def feedback(request):
    if request.method == "POST":
        try:
            '''获取post信息'''
            subject = request.POST.get('subject')
            no = request.POST.get('no')
            status = request.POST.get('status')
            username = request.user.username

            '''更新该题正确数目'''
            if status == 'ac':
                num = Question.objects.get(subject=subject, no=subject + no).accepted
                Question.objects.filter(subject=subject, no=subject + no).update(accepted=num+1)
                '''更新个人做题历史'''
                print("准备更新正确")
                his = History.objects.filter(username=username, question__no=subject + no).last()
                History.objects.filter(username=username, question__no=subject + no, date=his.date).update(status=1)
                print("更新正确")

            else:
                '''更新个人contributions数目'''
                try:
                    num = Contributions.objects.get(username=username, date=datetime.date.today()).num
                    Contributions.objects.filter(username=username, date=datetime.date.today()).update(num=num+1)
                    print("更新ok")
                    pass
                except:
                    Contributions(username=username, num=1).save()
                    print("创建ok")

                '''更新该题尝试数目'''
                num = Question.objects.get(subject=subject, no=subject + no).attempted
                Question.objects.filter(subject=subject, no=subject + no).update(attempted=num+1)

                '''更新个人做题历史'''
                print("准备创建历史")
                History(username=username, question=Question.objects.get(subject=subject, no=subject + no), status=0).save()
                print("创建历史成功")

            '''更新正确率'''
            Question.objects.filter(subject=subject, no=subject + no).update(
                pass_ratio=100*Question.objects.get(subject=subject, no=subject + no).accepted/Question.objects.get(subject=subject, no=subject + no).attempted)

            '''更新个人正确错误状态'''
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
                    return render(request, "luogu/error.html")
        except:
            print("大")
            return render(request, "luogu/error.html")
    else:
        return render(request, "luogu/error.html")
    return render(request, "luogu/error.html")



@login_required
def write_note(request, no):
    print(1)
    if request.method == 'POST':
        print(2)
        try:
            form = CreateArticleForm(request.POST)
            print(3)
            if form.is_valid():
                body = form.save(commit=False).body
                try:
                    article = Note.objects.get(user=User.objects.get(username=request.user), question_no=no)
                    article.body = body
                    article.save()
                except:
                    article = Note(user=User.objects.get(username=request.user), question_no=no, body=body)
                    article.save()
                return redirect("/hub/{}".format(no))

                return JsonResponse({"result": True})
            else:
                return JsonResponse({"result": False})
        except:
            return render(request, 'luogu/error.html')
    else:
        form = CreateArticleForm()
        try:
            user = User.objects.get(username=request.user)
            note = Note.objects.get(user=user, question_no=no)
            form.fields['body'].initial = note.body
        except:
            pass
        return render(request, 'luogu/write11.html', {'form': form, 'no': no})

    return render(request, 'luogu/write.html')


def notes_list(request, name):
    benren = True if request.user.username == name else False
    try:
        user = User.objects.get(username=name)
        # notes = Note.objects.filter(user=user).order_by('-created_time')
        notes = Note.objects.filter(user=user)
        return render(request, "luogu/notes_list.html",
                      {"user": user, "notes": notes, 'benren': benren})
    except:
        pass
    return render(request, 'luogu/error.html')

#内容页
def note_show(request, sid):
    try:
        note = Note.objects.get(id=sid)#查询指定ID的文章
        no = note.question_no
        question = Question.objects.get(no=no)
        return render(request, "luogu/note_show.html",{'note': note, 'question': question})
    except:
        return render(request, 'luogu/error.html')


@login_required
def delete_note(request):
    if request.method == 'POST':
        no = request.POST.get('id')
        try:
            note = Note.objects.get(id=no)
            if note.user.username == request.user.username:
                note.delete()
                return JsonResponse({"result": True})
            else:
                return redirect('/')
        except:
            return JsonResponse({"result": False})


@login_required
def makeNews(request):
    return render(request, "luogu/error.html")


def personalPage(request, name):
    if request.method == "POST":
        print(name)
        print(request.user.username)
        if request.user.username != name:
            return JsonResponse({"result": False})
        img = request.FILES.get('img_file')
        path = name
        if dev:
            url = "C:/luogu/luogu/sch/static/luogu/image/personalHead/" + path + ".jpg"
        else:
            url = "/www/wwwroot/0ng.run/static/luogu/image/personalHead/" + path + ".jpg"


        with open(url, 'wb') as f:
            for chunk in img.chunks():
                f.write(chunk)
        return JsonResponse({"result": True})
    try:
        benren = True if request.user.username == name else False
        user = User.objects.get(username=name)
        if user:
            contributions = Contributions.objects.filter(username=user.username)
            ls = []
            now = datetime.datetime.now().date()
            monday = now + datetime.timedelta(days=-now.weekday())
            offset = datetime.timedelta(days=-51*7)
            last_year = monday+offset
            one_day = datetime.timedelta(days=1)
            sum = 0
            for i in range(52):
                tmpls = {
                    "ls":[],
                    "offset": i*16
                }
                if i == 51:
                    for j in range(now.weekday()+1):
                        tmp = dict()
                        tmp['date'] = last_year.__str__()
                        # a = random.randint(0, 35)
                        # tmp['num'] = a
                        # sum += a
                        try:
                            a = contributions.get(date=last_year).num
                            tmp['num'] = a
                            sum += a
                        except:
                            tmp['num'] = 0
                        tmp['y'] = j*15
                        last_year += one_day
                        tmpls["ls"].append(tmp)
                else:
                    for j in range(7):
                        tmp = dict()
                        tmp['date'] = last_year.__str__()
                        # a = random.randint(0, 35)
                        # tmp['num'] = a
                        # sum += a
                        try:
                            a = contributions.get(date=last_year).num
                            tmp['num'] = a
                            sum += a
                        except:
                            tmp['num'] = 0
                        tmp['y'] = j*15
                        last_year += one_day
                        tmpls["ls"].append(tmp)
                ls.append(tmpls)
            his = History.objects.filter(username=user).order_by("-date")
            date = request.GET.get('date')
            print(date)
            if date:
                year, month, day = date.split('-')
                print(date.split('-'))
                his = his.filter(date__contains=datetime.date(int(year), int(month), int(day)))
            # else:
            #     his = his[:min(10, his.count())]

            return render(request, "luogu/personalPage.html", {"username": name, "user": user, "a": ls, "his": his, "sum": sum, 'benren': benren})
        else:
            return render(request, "luogu/error.html")
    except:
        return render(request, "luogu/error.html")
    return render(request, "luogu/error.html")


def scratchpaper(request):
    return render(request, "luogu/scratchpaper.html")


def test(request):
    return render(request, "luogu/垃圾.html")
