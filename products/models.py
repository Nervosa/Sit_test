from django.db import models
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Product(models.Model):
    title = models.CharField(max_length=50)
    height = models.FloatField(max_length=10)
    weight = models.FloatField(max_length=10)
    color = models.CharField(max_length=7)
    photo = models.ImageField(upload_to='products_photo', blank=True)
    description = models.TextField(max_length=1000)

    def __unicode__(self):
        return self.title

    def display_photo(self):
        return '<img src="%s" />' % (self.photo.url)

    display_photo.short_description = 'Photo of a product'
    display_photo.allow_tags = True
    saved_file.connect(generate_aliases_global)

@receiver(post_delete, sender=Product)
def photo_post_delete(sender, **kwargs):
    prod = kwargs['instance']
    storage, path = prod.photo.storage, prod.photo.path
    storage.delete(path)