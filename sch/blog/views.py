from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Banner, Tag, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown
# Create your views here.


#首页
def index(request):
    print(1)
    allcategory = Category.objects.all()
    banner = Banner.objects.filter(is_active=True)#查询所有幻灯图数据，并进行切片
    tui = Article.objects.filter(tui__id=1)[:3]#查询推荐位ID为1的文章
    allarticle = Article.objects.all().order_by('-id')[0:10]
    #hot = Article.objects.all().order_by('?')[:10]#随机推荐
    #hot = Article.objects.filter(tui__id=3)[:10]   #通过推荐进行查询，以推荐ID是3为例
    hot = Article.objects.all().order_by('-views')[:10]#通过浏览数进行排序
    remen = Article.objects.filter(tui__id=2)[:6]
    print(remen)
    tags = Tag.objects.all()
    link = Link.objects.all()
    context = {
        'allcaltegory': allcategory,
        'banner': banner,
        'tui': tui,
        'allarticle': allarticle,
        'hot': hot,
        'remen': remen,
        'tags': tags,
        'link': link
    }
    return render(request, "blog/index.html", context)
    pass


#列表页
def list(request, lid):
    print(1)
    lists = Article.objects.filter(category_id=lid)#获取通过URL传进来的lid，然后筛选出对应文章
    cname = Category.objects.get(id=lid)#获取当前文章的栏目名
    remen = Article.objects.filter(tui__id=2)[:6]#右侧的热门推荐
    allcategory = Category.objects.all()#导航所有分类
    tags = Tag.objects.all()#右侧所有文章标签
    page = request.GET.get('page')  # 在URL中获取当前页面数
    paginator = Paginator(lists, 5)  # 对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        lists = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        lists = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'blog/list.html', locals())


#内容页
def show(request, sid):
    print("???")
    print(sid)
    print("???")
    show = Article.objects.get(id=sid)#查询指定ID的文章
    print(2)
    allcategory = Category.objects.all()#导航上的分类
    print(3)
    tags = Tag.objects.all()#右侧所有标签
    print(3)
    remen = Article.objects.filter(tui__id=2)[:6]#右侧热门推荐
    print(5)
    hot = Article.objects.all().order_by('?')[:10]#内容下面的您可能感兴趣的文章，随机推荐
    print(5)
    # previous_blog = Article.objects.filter(created_time__gt=show.created_time,category=show.category.id).first()
    print(5)
    # netx_blog = Article.objects.filter(created_time__lt=show.created_time,category=show.category.id).last()
    show.views = show.views + 1
    show.save()


    show.body = markdown.markdown(show.body,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])

    return render(request, 'blog/show.html', locals())
    pass


#标签页
def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)#通过文章标签进行查询文章
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    tname = Tag.objects.get(name=tag)#获取当前搜索的标签名
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'blog/tags.html', locals())


# 搜索页
def search(request):
    ss=request.GET.get('search')#获取搜索的关键词
    list = Article.objects.filter(title__icontains=ss)#获取到搜索关键词通过标题进行匹配
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page) # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1) # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages) # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'blog/search.html', locals())


# 关于我们
def about(request):
    allcategory = Category.objects.all()
    return render(request, 'blog/page.html',locals())


@login_required
def write(request):
    # article = get_object_or_404(Article)
    # article = Article.objects.get()
    # article.body = markdown.markdown(article.body,
    #                                  extensions=[
    #                                      'markdown.extensions.extra',
    #                                      'markdown.extensions.codehilite',
    #                                      'markdown.extensions.toc',
    #                                  ])
    if request.method == 'POST':
        try:
            content = request.POST.get('content')
            title = request.POST.get('title')

            if content.split() == [] or title.split() == []:
                return JsonResponse({"result": False})


            user = User.objects.get(username=request.user)
            A = Article(title=title, body=content, user=user)
            # print(1)
            A.save()

            print(content)
            print(title)
            return JsonResponse({"result": True})
        except:
            return render(request, 'luogu/error.html')
    else:
        return render(request, 'blog/write.html')


def personal(request, name):
    print(name)
    benren = True if request.user == name else False
    try:
        user = User.objects.get(username=name)
        ls = Article.objects.filter(user=user)
        # for i in ls:
        #     i.body = markdown.markdown(i.body,
        #                                  extensions=[
        #                                      'markdown.extensions.extra',
        #                                      'markdown.extensions.codehilite',
        #                                      'markdown.extensions.toc',
        #                                  ])
        return render(request, "blog/personalPage.html",
                      {"user": user, "a": ls, 'benren': benren})
    except:
        pass
    return render(request, 'luogu/error.html')
