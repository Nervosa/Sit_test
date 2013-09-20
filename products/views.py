from django.http import HttpResponse
from django.template import RequestContext, loader
from products.models import Product
from django.shortcuts import render_to_response

def home(request):
    # template = loader.get_template('index.html')
    # context = RequestContext()
    prods = Product.objects.all()
    res = ', '.join([prod.title for prod in prods])
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'prods':prods,
    })
    return HttpResponse(template.render(context))
    # return render_to_response(template, context_instance=RequestContext(request))