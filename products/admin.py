from django.contrib import admin
from products.models import Product

class ProductAdmin(admin.ModelAdmin):
    # fields = ['title', 'height', 'weight', 'color']
    fieldsets = [
        ('Title of a product',                  {'fields':['title']}),
        ('Parameters of a product', {'fields':['height', 'weight', 'color']}),
    ]
    list_display = ['title', 'height', 'weight', 'color']

admin.site.register(Product, ProductAdmin)