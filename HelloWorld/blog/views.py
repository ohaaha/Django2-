from django.shortcuts import render
from . import models
from django.core.paginator import Paginator

def index(request):
    page = request.GET.get('page') # 获取路由里面page值
    # 取出来是字符串，需要转换为int
    if page:
        page = int(page)
    else:
        page = 1
    article = models.Article.objects.all()
    # 最新文章
    top4_article = models.Article.objects.order_by('-public_date')[:4] #按时间排序取4个
    # 分页
    paginator = Paginator(article, 4) # 每页为4
    page_num = paginator.num_pages # 获取总共几页
    page_list = paginator.page(page)
    next_page = page+1 if(page_list.has_next()) else page
    prevoius_page = page-1 if (page_list.has_previous()) else page

    return render(request, 'blog/index.html', {'article': page_list,
                                               'page_num': range(1, page_num+1),
                                               'cur_page': page,
                                               'next_page': next_page,
                                               'previous_page': prevoius_page,
                                               'top4_article': top4_article})

def article_page(request, article_id):
    articles = models.Article.objects.all()
    article = articles[article_id]
    temp = article.id;
    if(temp == 0):
        last_id = 0
        next_id = temp+1
        last_title = "无"
        next_title = articles[next_id].title
    elif (temp == len(articles)-1):
        last_id = temp-1
        next_id = temp
        last_title = articles[last_id].title
        next_title = "无"
    else:
        last_id = temp-1
        next_id = temp+1
        last_title = articles[last_id].title
        next_title = articles[next_id].title
    section_list = article.content.split('\n')  # 把文章内容用换行符隔开
    return render(request, 'blog/article_page.html', {'article': article,
                                                      'section_list': section_list,
                                                      'last_id': last_id,
                                                      'next_id': next_id,
                                                      'last_title': last_title,
                                                      'next_title': next_title})