from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class Configuration(models.Model):
    home_page_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='home_page_user', blank=False,
                                       null=True)
    product_duplication_superuser = models.ForeignKey(User, on_delete=models.SET_NULL,
                                                      related_name='product_duplication_superuser', blank=False,
                                                      null=True)
    products_per_page = models.IntegerField(default=20)
    product_link_validator = models.TextField(max_length=1000)
    photos_link_validator = models.TextField(max_length=1000)

    def __str__(self):
        return 'Site configuration'

    @staticmethod
    def get_configuration():
        return get_object_or_404(Configuration)
