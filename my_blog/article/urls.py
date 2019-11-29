# 引入path
from . import views
from django.urls import path

# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),

    # 文章详情
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),

    # 写文件
    path('article-create/', views.article_create, name='article_create'),

    # 删除文章
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    
    path('article-safe-delete/<int:id>/', views.article_safe_delete, name='article_safe_delete'),
]
