from django.shortcuts import render
from .models import News


# Create your views here.


def index(request):
    return render(request, 'basics/templates/index.html')


def about(request):
    return render(request, 'basics/templates/blocks/about.html')


def news(request):
    try:
        all_articles = News.objects.all()[1:]  # Все кроме 1
        last_article = News.objects.all().order_by('-pub_date')[0]  # Самый первый элемент по Дате публикации!!
    except:
        return render(request, 'basics/templates/news.html')

    return render(request, 'basics/templates/news.html', {'all_articles': all_articles, 'last_article': last_article})


def article(request, pk):
    return render(request, 'basics/templates/blocks/article.html', {'pk': pk})
