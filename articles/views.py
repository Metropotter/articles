import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.conf import settings

def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'articles/list.html', {'articles': articles})

# 2. Создание
def article_create(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, 'articles/form.html', {'form': form})

# 3. Редактирование
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, 'articles/form.html', {'form': form, 'article': article})

def external_news(request):
    # Берем ключ из settings.py
    api_key = settings.NEWS_API_KEY 
    
    # URL для получения топовых новостей России
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    
    try:
        response = requests.get(url)
        data = response.json()
        # API возвращает список в ключе 'articles'
        news = data.get('articles', [])
    except Exception as e:
        print(f"Ошибка при запросе к API: {e}")
        news = []
        
    return render(request, 'articles/external_news.html', {'news': news})