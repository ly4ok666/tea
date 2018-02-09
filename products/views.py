from django.shortcuts import render
from products.models import *

def products (request, product_id):
    products = Product.objects.get(id=product_id)
    return render(request, 'product/product-page.html', locals())