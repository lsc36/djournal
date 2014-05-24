from django.shortcuts import (
    render, redirect,
    get_object_or_404, get_list_or_404,
    )
from django.http import Http404
from articles.models import *
from django.conf import settings


def _get_category_list_of_volume(volume):
    article_list = Article.objects.filter(volume=volume).order_by('category')
    visited = set()
    return [article.category for article in article_list \
        if article.category not in visited \
        and not visited.add(article.category)]


def _build_context(**kwargs):
    context = {
        'settings': settings,
        }
    for key in kwargs.keys():
        context[key] = kwargs[key]
    return context


def _build_context_with_volume(volume, **kwargs):
    kwargs['volume'] = volume
    kwargs['category_list'] = _get_category_list_of_volume(volume)
    return _build_context(**kwargs)


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
    context = _build_context_with_volume(volume)
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
    context = _build_context_with_volume(volume,
        category=category,
        article_list=article_list,
        )
    return render(request, 'view_category.html', context)


def view_article(request, volume_number, article_id):
    volume = get_object_or_404(Volume, published=True, number=volume_number)
    article = get_object_or_404(Article, volume=volume, id=article_id)
    context = _build_context_with_volume(volume,
        article=article,
        category=article.category,
        )
    return render(request, 'view_article.html', context)


def list_volumes(request):
    volume_list = get_list_or_404(Volume, published=True)
    context = _build_context(volume_list=volume_list)
    return render(request, 'list_volumes.html', context)
