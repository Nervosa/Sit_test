from django.core.mail import mail_admins
from django.db import models
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global
from django.db.models.signals import post_delete, post_save, post_init, pre_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


class Product(models.Model):
    title = models.CharField(max_length=50)
    height = models.FloatField(max_length=10)
    weight = models.FloatField(max_length=10)
    color = models.CharField(max_length=7, validators=[RegexValidator(regex='^\#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$', message='Enter valid color value prepended by "#"')])
    photo = models.ImageField(upload_to='products_photo', blank=True)
    description = models.TextField(max_length=1000)

    def __unicode__(self):
        return self.title

    def display_photo(self):
        return '<img src="%s" />' % self.photo.url

    display_photo.short_description = 'Photo of a product'
    display_photo.allow_tags = True
    saved_file.connect(generate_aliases_global)

@receiver(post_delete, sender=Product)
def photo_post_delete(sender, **kwargs):
    prod = kwargs['instance']
    try:
        storage, path = prod.photo.storage, prod.photo.path
        storage.delete(path)
    except:
        pass
    mail_admins(subject="An object " + prod.title + " deleted.", message="An object " + prod.title + " deleted.")
    print "An object " + prod.title + " deleted."

@receiver(post_save, sender=Product)
def send_email_when_something_changed(sender, **kwargs):
    prod = kwargs['instance']
    new_title = prod.title
    try:
        if kwargs['created']:
            mail_admins(subject="An object " + prod.title + " created.", message="An object " + prod.title + " created.")
            print "An object " + prod.title + " created."
        if not kwargs['created']:
            mail_admins(subject="An object " + prod.title +" resaved.", message="An object " + prod.title + " changed.")
            print "An object " + prod.title + " resaved."
    except:
        mail_admins(subject="Warning", message="Something happened!")
        print "Warning! Something has happened!"