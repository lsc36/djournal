from django.contrib import admin
from articles.models import Volume, Category, Article

from django_summernote.admin import SummernoteModelAdmin

class ArticleModelAdmin(SummernoteModelAdmin):
    pass

admin.site.register(Volume)
admin.site.register(Category)
admin.site.register(Article, ArticleModelAdmin)
