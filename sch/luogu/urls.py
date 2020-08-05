"""sch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from . import views as luogu
from django.contrib.auth.views import LoginView

app_name = 'luogu'
urlpatterns = [
    # url('index$', luogu.index),
    # url('index.html$', luogu.index),
    url('^$', luogu.index),
    url(r'^login/$', luogu.login),
    url('logout$', luogu.logout),
    url('^404$', luogu.error),
    url('register$', luogu.register),
    # url('register/enter$', luogu.registerEnter),
    url('forgetPassword$', luogu.forgetPassword),
    url('changePassword$', luogu.changePassword),
    # url('makeNews$', luogu.makeNewQuestion),
    # url('makeNews/submit$', luogu.makeNews),
    url(r'^scratchpaper/$', luogu.scratchpaper),
    url(r'^hub/$', luogu.hub),
    path(r'detail/', luogu.detail),
    url('feedback$', luogu.feedback),
    path('hub/<hubno>', luogu.detail),
    path('user/<name>/', luogu.personalPage),
    path('write_note/<no>/', luogu.write_note),
    path('notes/<name>/', luogu.notes_list),
    path('show-<int:sid>.html', luogu.note_show, name='show'),  # 内容页
    path('delete_note', luogu.delete_note),  # 删除笔记

    path('test', luogu.test)
    # url(r'^accounts/login/', LoginView.as_view(template_name="/login/")),

]