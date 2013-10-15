from products import c_models, c_widgets
from django import forms
from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:
        model = c_models.Product

    color = forms.CharField(widget=c_widgets.ColorWidget(attrs={'class': 'span1', 'id': 'color-input'}))