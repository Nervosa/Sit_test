from django.http import HttpResponse
from django.template import RequestContext, loader
from products.models import Product
from django.shortcuts import render_to_response

def home(request):

    prods = Product.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'prods':prods,
    })
    return HttpResponse(template.render(context))