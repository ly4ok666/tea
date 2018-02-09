from django.conf.urls import url
from service.views import service
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # #конкретная статья
    url(r'^service/get/(?P<service_id>\d+)/$', service, name='service'),
     ]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)