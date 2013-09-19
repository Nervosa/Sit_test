from django.http import HttpResponse
from django.template import RequestContext, loader
from products.models import Product
from django.shortcuts import render_to_response

def home(request, template = 'index.html'):
    # template = loader.get_template('index.html')
    # context = RequestContext()
    return render_to_response(template, context_instance=RequestContext(request))