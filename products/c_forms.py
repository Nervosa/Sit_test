from products import c_models, c_widgets
from django import forms
from django.forms import ModelForm


class ProductForm(ModelForm):

    class Media:
        js = {
            'http://malsup.github.com/jquery.form.js',
        }

    class Meta:
        model = c_models.Product

    title = forms.CharField()
    height = forms.FloatField()
    weight = forms.FloatField()
    description = forms.Textarea()
    photo = forms.ImageField()
    color = forms.CharField(widget=c_widgets.ColorWidget(attrs={'class': 'span1', 'id': 'color-input'}))