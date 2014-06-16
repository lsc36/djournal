from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

# Create your models here.

class Volume(models.Model):

    number = models.IntegerField('期數')
    published = models.BooleanField('已出版')

    class Meta:
        verbose_name = verbose_name_plural = '期數'
        ordering = ['-number']

    def __str__(self):
        return settings.VOLUME_SHOW_NAME % self.number

    def get_absolute_url(self):
        return reverse('articles.views.index', args=[str(self.number)])


class Category(models.Model):

    name = models.CharField('分類', max_length=30)
    order = models.IntegerField('順序')

    class Meta:
        verbose_name = verbose_name_plural = '分類'
        ordering = ['order']

    def __str__(self):
        return self.name


class Article(models.Model):

    volume = models.ForeignKey(Volume, verbose_name='期數')
    category = models.ForeignKey(Category, verbose_name='分類')
    title = models.CharField('標題', max_length=100)
    author = models.CharField('作者', max_length=100, blank=True)
    content = models.TextField('內文')
    last_mod = models.DateTimeField('最後修改時間', auto_now=True)

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-last_mod']

    def __str__(self):
        return '[%s] %s' % (self.category, self.title)

    def get_absolute_url(self):
        return reverse('articles.views.view_article',
            args=[self.volume.number, self.id, self.title])
