# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-05 22:43
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=60, verbose_name='Заголовок')),
                ('article_text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст статьи')),
                ('short_text', models.TextField(blank=True, null=True, verbose_name='Краткое описание')),
                ('article_date', models.DateTimeField(verbose_name='Дата и время')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'статьи',
                'ordering': ['-article_date'],
                'db_table': 'blog',
                'verbose_name': 'статьи',
            },
        ),
    ]