from django.shortcuts import render
from service.models import *

def service (request, product_id):
    service = Service.objects.get(id=product_id)
    return render(request, 'service/servicedetail.html', locals())