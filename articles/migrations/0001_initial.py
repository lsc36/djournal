# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='標題', max_length=100)),
                ('author', models.CharField(verbose_name='作者', blank=True, max_length=100)),
                ('content', models.TextField(verbose_name='內文')),
                ('last_mod', models.DateTimeField(auto_now=True, verbose_name='最後修改時間')),
            ],
            options={
                'ordering': ['-last_mod'],
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='分類', max_length=30)),
                ('order', models.IntegerField(verbose_name='順序')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': '分類',
                'verbose_name_plural': '分類',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('number', models.IntegerField(verbose_name='期數')),
                ('published', models.BooleanField(verbose_name='已出版', default=False)),
            ],
            options={
                'ordering': ['-number'],
                'verbose_name': '期數',
                'verbose_name_plural': '期數',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='articles.Category', verbose_name='分類'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='volume',
            field=models.ForeignKey(to='articles.Volume', verbose_name='期數'),
            preserve_default=True,
        ),
    ]
