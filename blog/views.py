from django.shortcuts import render
from blog.models import *

def blogpost (request, article_id):
    blog = Blog.objects.get(id=article_id)
    return render(request, 'article/blogpost.html', locals())