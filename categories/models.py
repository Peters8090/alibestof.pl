from django.db import models

from ordered_model.models import OrderedModel


class Category(OrderedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta(OrderedModel.Meta):
        verbose_name_plural = 'Categories'
        ordering = ['order']


class Subcategory(OrderedModel):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='parent_category')

    order_with_respect_to = 'parent_category'

    def __str__(self):
        return f'({self.parent_category}) {self.name}'

    class Meta(OrderedModel.Meta):
        verbose_name_plural = 'Subcategories'
        ordering = ['parent_category', 'order']
