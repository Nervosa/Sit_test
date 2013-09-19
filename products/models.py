from django.db import models
from colorfield import fields

class Product(models.Model):
    title = models.CharField(max_length=50)
    height = models.FloatField(max_length=10)
    weight = models.FloatField(max_length=10)
    color = fields.ColorField()