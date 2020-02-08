from django import forms

from .models import Product, Subcategory


class ProductSearchForm(forms.ModelForm):
    query = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control mr-sm-2',
               'placeholder': 'Search',
               'aria-label': 'Search',
               }))

    class Meta:
        model = Product
        fields = []
