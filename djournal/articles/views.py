from django.shortcuts import (
    render, redirect,
    get_object_or_404, get_list_or_404,
    )
from django.http import Http404
from articles.models import *
from django.conf import settings


def index(request, volume_number):
    if not volume_number:
        try:
            latest_volume = Volume.objects \
                .filter(published=True) \
                .order_by('-number') \
                .first()
            if not latest_volume:
                raise
            return redirect(latest_volume)
        except:
            raise Http404
    volume = get_object_or_404(Volume, published=True, number=volume_number)
    category_list = Category.objects.all().order_by('order')
    context = {
        'site_name': settings.SITE_NAME,
        'volume': volume,
        'category_list': category_list,
        }
    return render(request, 'index.html', context)


def view_category(request, volume_number, category_name):
    volume = get_object_or_404(Volume, published=True, number=volume_number)
    if category_name == 'all':
        category = 'all'
        article_list = Article.objects.filter(volume=volume)
    else:
        category = get_object_or_404(Category, name=category_name)
        article_list = Article.objects.filter(volume=volume, category=category)
    article_list = article_list.order_by('category', 'title')
    context = {
        'site_name': settings.SITE_NAME,
        'volume': volume,
        'category': category,
        'article_list': article_list,
        }
    return render(request, 'view_category.html', context)


def view_article(request, volume_number, article_id):
    volume = get_object_or_404(Volume, published=True, number=volume_number)
    article = get_object_or_404(Article, volume=volume, id=article_id)
    context = {
        'site_name': settings.SITE_NAME,
        'volume': volume,
        'article': article,
        }
    return render(request, 'view_article.html', context)


def list_volumes(request):
    volume_list = get_list_or_404(Volume, published=True)
    context = {
        'site_name': settings.SITE_NAME,
        'volume_list': volume_list,
        }
    return render(request, 'list_volumes.html', context)
