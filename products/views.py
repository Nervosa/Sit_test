from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext
from products.c_models import Product
from products.c_forms import ProductForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response, render
from registration.forms import RegistrationForm


def login(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
        else:
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


def edit_product(request, product_id):

    current_instance = Product.objects.get(id=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            if     current_instance.title == request.POST.get('title')\
               and current_instance.height == request.POST.get('height')\
               and current_instance.weight == request.POST.get('weight')\
               and current_instance.height == request.POST.get('description')\
               and current_instance.photo == request.POST.get('photo')\
               and current_instance.color == request.POST.get('color'):
               pass
            else:
                current_instance.title = request.POST.get('title')
                current_instance.height = request.POST.get('height')
                current_instance.weight = request.POST.get('weight')
                current_instance.description = request.POST.get('description')
                if request.POST.get('photo'):
                    current_instance.photo = request.POST.get('photo')
                else:
                    current_instance.photo = None
                current_instance.color = request.POST.get('color')
                current_instance.save()
            return HttpResponseRedirect('/')

    else:
        form = ProductForm({'title':current_instance.title,
                            'height':current_instance.height,
                            'weight':current_instance.weight,
                            'photo':request.FILES,
                            'color':current_instance.color ,
                            'description':current_instance.description})

    return render_to_response("product_edit.html", RequestContext(request,
                                                                        {"form": form,
                                                                        "product": current_instance,
                                                                   }))