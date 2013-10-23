from products.c_models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response
from Sit_test import settings

def home(request):

    prods = Product.objects.all()
    paginator = Paginator(prods, 3)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        products = paginator.page(1)
    return render_to_response('index.html', {"prods":products})