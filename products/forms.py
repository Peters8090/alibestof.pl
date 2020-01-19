from django import forms

from .models import Product


class ProductSearchForm(forms.ModelForm):
    query = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Search for products...',
               'aria-label': 'Search for products...',
               }))

    class Meta:
        model = Product
        fields = []
