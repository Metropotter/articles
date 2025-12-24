import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# 1. Список ваших статей
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

# 4. БОНУС: Новости РФ из внешнего API
def external_news(request):
    # Получи ключ на newsapi.org (бесплатно для разработчиков)
    api_key = 'ВАШ_API_KEY_ЗДЕСЬ' 
    url = f'https://newsapi.org/v2/top-headlines?country=ru&apiKey={api_key}'
    
    try:
        data = requests.get(url).json()
        news = data.get('articles', [])
    except:
        news = []
        
    return render(request, 'articles/external_news.html', {'news': news})