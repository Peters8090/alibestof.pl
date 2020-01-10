from django.db import models
from django.shortcuts import get_object_or_404


class Configuration(models.Model):
    products_per_page = models.IntegerField(default=20)

    def __str__(self):
        return 'Site configuration'

    @staticmethod
    def get_configuration():
        return get_object_or_404(Configuration)
