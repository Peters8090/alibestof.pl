from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class Configuration(models.Model):
    products_per_page = models.IntegerField(default=20, verbose_name='Products Per Page')
    product_duplication_superuser = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True,
                                                      verbose_name='Product Duplication Superuser')
    product_link_validator = models.TextField(max_length=1000)
    photos_link_validator = models.TextField(max_length=1000)

    def __str__(self):
        return 'Site configuration'

    @staticmethod
    def get_configuration():
        return get_object_or_404(Configuration)
