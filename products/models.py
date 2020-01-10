from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=False)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=True)
    image = models.ImageField(upload_to='')
    reflink = models.URLField(max_length=1000, blank=True)
    link = models.URLField(max_length=1000, blank=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return f'({self.user.username}) {self.name}'
