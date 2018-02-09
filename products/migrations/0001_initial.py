# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-18 21:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=60, verbose_name='Заголовок')),
                ('product_text', models.TextField(verbose_name='Текст статьи')),
                ('product_date', models.DateTimeField(verbose_name='Дата и время')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'product',
                'verbose_name': 'Услуги',
                'verbose_name_plural': 'Услуги',
                'ordering': ['-product_date'],
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/product/', verbose_name='Изображение')),
                ('is_main', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('article', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'db_table': 'product_images',
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]