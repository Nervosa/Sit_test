from django.contrib import admin
from products.c_models import Product
from products.c_forms import ProductForm


class ProductAdmin(admin.ModelAdmin):

    form = ProductForm
    fieldsets = [
        ('Title of a product',          {'fields': ['title']}),
        ('Description of a product',    {'fields': ['description']}),
        ('Parameters of a product',     {'fields': ['height', 'weight', 'color']}),
        ('Upload photo',                {'fields': ['photo']}),
        ('Photo',                       {'fields': ['display_photo', ]}),
    ]
    list_display = ['title', 'height', 'weight', 'color']
    readonly_fields = ('display_photo', )

admin.site.register(Product, ProductAdmin)