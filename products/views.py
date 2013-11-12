from django.http.response import HttpResponseRedirect
from products.c_models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response, redirect, render
from registration.forms import RegistrationForm

def login(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
        else:
            regform = RegistrationForm()
            return render(request, 'registration/login.html')

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
        return render_to_response('products_list.html', {"prods": products,
                                                         "current_user_activeness": request.user.is_active,
                                                         "current_user": request.user,
                                                         })
