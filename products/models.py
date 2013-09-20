from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    height = models.FloatField(max_length=10)
    weight = models.FloatField(max_length=10)
    color = models.CharField(max_length=7)

    def __unicode__(self):
        return self.title