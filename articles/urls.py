from django.urls import path
from . import views # Импортируем наш файл views.py

urlpatterns = [
    path('', views.article_list, name='article_list'), # Проверьте это имя
    path('create/', views.article_create, name='article_create'),
    path('<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('news-api/', views.external_news, name='external_news'),
]