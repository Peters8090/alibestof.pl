from django import forms

from .models import Product


class ProductSearchForm(forms.ModelForm):
    query = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control mr-sm-2',
               'placeholder': 'Search',
               'aria-label': 'Search',
               }))

    class Meta:
        model = Product
        fields = []


class ProductAdminListEditForm(forms.ModelForm):
    description = forms.CharField(max_length=5000, widget=forms.Textarea(attrs={'rows': 1, 'cols': 20}))
    product_link = forms.CharField(max_length=5000)
    photos_link = forms.CharField(max_length=5000)

    class Meta:
        model = Product
        fields = {'description', 'product_link', 'photos_link'}
