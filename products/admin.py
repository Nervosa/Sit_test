from django.contrib import admin
from products.models import Product

class ProductAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Title of a product',         {'fields':['title']}),
        ('Parameters of a product',    {'fields':['height', 'weight', 'color']}),
        ('Photo and thumbnail',        {'fields':['display_photo', 'photo']}),
    ]
    list_display = ['title', 'height', 'weight', 'color']
    readonly_fields = ('display_photo',)

admin.site.register(Product, ProductAdmin)