from django.contrib import admin
from products.models import Product

class ProductAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Title of a product',          {'fields':['title']}),
        ('Parameters of a product',     {'fields':['height', 'weight', 'color']}),
        ('Upload photo',                {'fields':['photo']}),
        ('Photo',                       {'fields':['display_photo']}),
    ]
    list_display = ['title', 'height', 'weight', 'color']
    readonly_fields = ('display_photo',)

admin.site.register(Product, ProductAdmin)