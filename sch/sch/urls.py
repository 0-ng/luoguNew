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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
import django
from luogu.views import *
from django.contrib.auth.views import LoginView


urlpatterns = [
    url('admin/', admin.site.urls),
    url('index$', index),
    url('index.html$', index),
    url(r'^login/$', login),
    url('logout$', logout),
    url('^404$', error),
    # url('login$', 'django.contrib.auth.views.login'),
    # url('login/submit$', loginSubmit),
    url('register$', register),
    url('register/enter$', registerEnter),
    url('forgetPassword$', forgetPassword),
    url('changePassword$', changePassword),
    url('makeNews$', makeNewQuestion),
    url('makeNews/submit$', makeNews),
    url(r'^hub/$', hub),
    # url(r'^blob/$', blob),
    url('feedback$', feedback),
    # url(r'hub/P([0-9]{4})/$', hub),
    url(r'^hub/M[0-9]{4}', detail),
    url('^$', index),

    url('user/', personalPage),
    # url('headimgChange', headimgChange)
    url(r'^accounts/login/', LoginView.as_view(template_name="/login/")),
    url(r'^test/$', test),
]
