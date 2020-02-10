from PIL import Image
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from base.models import Configuration
from categories.models import Subcategory


def product_link_validator(value):
    if not any(ext in value for ext in Configuration.get_configuration().product_link_validator.split('\r\n')):
        raise ValidationError(
            'You must include ' + Configuration.get_configuration().product_link_validator.replace('\r\n',
                                                                                                   ' or ') + ' in your product link')


def photos_link_validator(value):
    if not any(ext in value for ext in Configuration.get_configuration().photos_link_validator.split('\r\n')):
        raise ValidationError(
            'You must include ' + Configuration.get_configuration().photos_link_validator.replace('\r\n',
                                                                                                  ' or ') + ' in your photos link')


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', editable=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='author', editable=False)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Subcategory, related_name='category', blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True, max_length=5000)
    image = models.ImageField(upload_to='products/product')
    product_link = models.URLField(max_length=5000, validators=[product_link_validator])
    photos_link = models.URLField(max_length=5000, validators=[photos_link_validator])
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_modified']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        # On create
        if not self.pk:
            # If there is no author, assign one
            if not self.author:
                self.author = self.user

            # Auto product duplication
            if self.published and not self.user.is_superuser:
                p = Product(
                    user=Configuration.get_configuration().product_duplication_superuser,
                    author=self.author,
                    name=self.name,
                    category=self.category,
                    description=self.description,
                    image=self.image,
                    product_link=self.product_link,
                    photos_link=self.photos_link,
                    date_created=self.date_created,
                    date_modified=self.date_modified,
                    published=False
                )
                p.save()
        super(Product, self).save(*args, *kwargs)

        # Image compression
        Image.open(self.image.path).save(self.image.path, quality=50, optimize=True)
