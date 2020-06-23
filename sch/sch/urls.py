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
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    url('admin/', admin.site.urls),
    path('', include('luogu.urls')),
    path('blog/', include('blog.urls')),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'/static/favicon.ico')),


    # url('index$', luogu.index),
    # url('index.html$', luogu.index),
    # url(r'^login/$', luogu.login),
    # url('logout$', luogu.logout),
    # url('^404$', luogu.error),
    # # url('login$', 'django.contrib.auth.views.login'),
    # # url('login/submit$', loginSubmit),
    # url('register$', luogu.register),
    # url('register/enter$', luogu.registerEnter),
    # url('forgetPassword$', luogu.forgetPassword),
    # url('changePassword$', luogu.changePassword),
    # url('makeNews$', luogu.makeNewQuestion),
    # url('makeNews/submit$', luogu.makeNews),
    # url(r'^hub/$', luogu.hub),
    # url('feedback$', luogu.feedback),
    # url(r'^hub/M[0-9]{4}', luogu.detail),
    # url('^$', luogu.index),
    # url('user/', luogu.personalPage),
    #
    # url(r'^accounts/login/', LoginView.as_view(template_name="/login/")),
    # url(r'^test/$', luogu.test),


    # url(r"^blog/$", blog.index, name='index'),
    # # path('', blog.index, name='index'),#网站首页
    # # path('', include('blog.urls', namespace='index')),#网站首页
    # path('blog/list-<int:lid>.html', blog.list, name='list'),#列表页
    # path('blog/show-<int:sid>.html', blog.show, name='show'),#内容页
    # path('tag/<tag>', blog.tag, name='tags'),#标签列表页
    # path('s/', blog.search, name='search'),#搜索列表页
    # path('about/', blog.about, name='about'),#联系我们单页
    # path('writeblog', blog.write, name='write'),#联系我们单页
    # # path('ueditor/', include('DjangoUeditor.urls')),
    # # re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    #
    #
    #
    # path(r'mdeditor/', include('mdeditor.urls'))
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)