from django.conf.urls import url
from products.views import products
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # #конкретная статья
    url(r'^product/get/(?P<product_id>\d+)/$', products, name='products'),
     ]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)