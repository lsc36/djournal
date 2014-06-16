from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from articles import views

urlpatterns = patterns('',
    url(r'^(?P<volume_number>\d*)/?$', views.index, name='index'),
    url(r'^(?P<volume_number>\d*)/category/(?P<category_name>[\w|\W]+)/$', views.view_category, name='view_category'),
    url(r'^(?P<volume_number>\d*)/article/(?P<article_id>\d+)-(.*)$', views.view_article, name='view_article'),
    url(r'^volumes$', views.list_volumes, name='list_volumes')
)
