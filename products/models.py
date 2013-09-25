from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global
from easy_thumbnails.files import get_thumbnailer

class Product(models.Model):
    title = models.CharField(max_length=50)
    height = models.FloatField(max_length=10)
    weight = models.FloatField(max_length=10)
    color = models.CharField(max_length=7)
    photo = models.ImageField(upload_to='uploads/products_photo', blank=True)
    thumbnail = ThumbnailerImageField(upload_to='uploads/products_photo_hurr', blank=True)

    def __unicode__(self):
        return self.title

    def display_photo(self):
        return '<img src="%s" />' % (self.photo.url)


    display_photo.short_description = 'Photo of a product'
    display_photo.allow_tags = True
    saved_file.connect(generate_aliases_global)