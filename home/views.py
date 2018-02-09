from django.shortcuts import render
from home.models import *
from django.shortcuts import render_to_response
from products.models import *
from about.models import *
from faq.models import Faq
from .forms import ContactForm
from service.models import *
from blog.models import *

def home(request,article_id=1):
    """Домашняя страница нашего проекта"""
    contexts = Home.objects.all()
    images_main = HomeImage.objects.filter(is_active=True, is_main=True)
    # """Вывод категорий, большой список меню услуг"""
    abouts = ShortAbout.objects.all()
    product = ProductImage.objects.filter(is_active=True, is_main=True)
    service = ServiceImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'index.html',locals())

def products(request,product_id=1):
    """Вывод всех услуг на странице """
    images_main = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'products.html', locals())

def product(request,product_id=1):
    # """Вывод категорий, большой список меню услуг"""
    images_main = ProductImage.objects.filter(is_active=True, is_main=True)
    # """Вывод одной конкретной услуги на новой странице """
    return render_to_response('product/product-page.html', {'products': Product.objects.get(id=product_id),'images':images_main, 'product': Product.objects.all()})

def services(request,product_id=1):
    """Вывод всех услуг на странице """
    images_main = ServiceImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'products.html', locals())

def service(request,product_id=1):
    # """Вывод категорий, большой список меню услуг"""
    images_main = ServiceImage.objects.filter(is_active=True, is_main=True)
    # """Вывод одной конкретной услуги на новой странице """
    return render_to_response('service/service-page.html', {'services': Service.objects.get(id=product_id), 'images':images_main, 'service': Service.objects.all()})


def about(request):
    """Страница о компании"""
    about = About.objects.all()
    product = ProductImage.objects.filter(is_active=True, is_main=True)
    service = ServiceImage.objects.filter(is_active=True, is_main=True)
    # """Вывод категорий, большой список меню услуг"""
    # about = ProductImage.objects.filter(is_active=True, is_main=True)
    # краткое о нас
    # abouts = ShortAbout.objects.all()
    return render(request, 'about/about.html', locals())

def faq(request):
    """Страница Вопрос/ответ"""
    context = Faq.objects.all()
    # """Вывод категорий, большой список меню услуг"""
    images_main = ProductImage.objects.filter(is_active=True, is_main=True)
    # abouts = ShortAbout.objects.all()
    return render(request, 'faqs.html', locals())

from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template

    # our view
def contact(request):
    # """Вывод категорий, большой список меню услуг"""
    images_main = ProductImage.objects.filter(is_active=True, is_main=True)
    # Страница для обратной связи (дописать функцию прикрепить файл)
    form_class = ContactForm
         # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
                # Email the profile with the
                # contact information
            template = get_template('contact_template.txt')
            context = {'contact_name': contact_name, 'contact_email': contact_email, 'form_content': form_content}
            content = template.render(context)
            email = EmailMessage("New contact form submission", content, "Your website" + '', ['gidrosave@gmail.com'], headers={'Reply-To': contact_email})
            email.send()
        # return render('contact')
        # Переходим на другую страницу, если сообщение отправлено
#         return HttpResponseRedirect('/contacts/thanks/')
    return render(request, 'contact.html', {
        'form': form_class,})

def blog(request):
    # article = {'article': Article.objects.get(id=article_id)}
    #Вывод всех статей и пагинация (2 статьи на страницу)"""
    # краткое о нас
    # images_main = ContentImages.objects.filter(is_active=True, is_main=True)
    abouts = ShortAbout.objects.all()
    blog = BlogImages.objects.filter(is_active=True, is_main=True)
    # paginator = Paginator(all_Articles, 1)
    # page = request.GET.get('page')
    #
    # try:
    #     articles = paginator.page(page)
    # except PageNotAnInteger:
    #     articles = paginator.page(1)
    # except EmptyPage:
    #     articles = paginator.page(paginator.num_pages)
    # context = {'articles': articles}
    return render(request, 'blog.html', locals())

def blogpost(request,article_id=1):
    """Вывод одной конкретной статьи """
    # краткое о нас
    abouts = ShortAbout.objects.all()
    # articles = Article.objects.get(id=article_id)
    # features = Features.objects.filter(features_article_id=article_id)
    # return render(request, 'home/article.html', locals())
    return render_to_response('article/blogpost.html', {'articles': Blog.objects.get(id=article_id),'abouts': abouts, 'article': Blog.objects.all()})