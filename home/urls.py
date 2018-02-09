from django.conf.urls import url
from home.views import home
from home.views import about
from home.views import faq
from home.views import products, product
# from home.views import article
from home.views import contact
from home.views import blog
from home.views import blogpost
from home.views import services, service
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # стартовая страница
    url(r'^$', home, name='home'),
    # страница о компании
    url(r'^about/$', about, name='about'),
    # Вопрс/ответ
    url(r'^faq/$', faq, name='faq'),
    #конкретная статья
    url(r'^product/get/(?P<product_id>\d+)/$', product, name='product'),
    #Все статьи
     url(r'^product/$', products, name='products'),
    # Все статьи блога
    url(r'^articles/$', blog, name='blog'),
    #Статьи по страницам блога
    url(r'^articles/page/(\d+)/$', blog),
    #конкретная статья блога
    url(r'^articles/get/(?P<article_id>\d+)/$', blogpost, name='post'),
    #Страница с контактами
    url(r'^contact/$', contact, name='contact'),
    # url(r'^articles/$', , name='blog'),
    # конкретная статья
    url(r'^service/get/(?P<product_id>\d+)/$', service, name='service'),
    # Все статьи
    url(r'^service/$', services, name='services'),
     ]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)