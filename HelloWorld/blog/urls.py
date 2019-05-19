import blog.views
from django.urls import path, include
urlpatterns = [
    path('index', blog.views.index),
    # url(r'^article/(?P<article_id>[0-9]+)$', views.article_page), # 把匹配到的数字，以article_id作为组名相匹配
    path('article/<int:article_id>', blog.views.article_page),
]