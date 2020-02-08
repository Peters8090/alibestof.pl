from PIL import Image
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from ordered_model.models import OrderedModel

from base.models import Configuration


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
        ordering = ['order']


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', editable=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='author', editable=False)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Subcategory, related_name='category', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/product')
    product_link = models.URLField(max_length=1000, validators=[product_link_validator])
    photos_link = models.URLField(max_length=1000, validators=[photos_link_validator])
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['date_modified']

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
                p = Product(user=Configuration.get_configuration().product_duplication_superuser,
                            author=self.author,
                            name=self.name,
                            description=self.description,
                            image=self.image,
                            product_link=self.product_link,
                            photos_link=self.photos_link,
                            date_created=self.date_created,
                            date_modified=self.date_modified,
                            published=False)
                p.save()
        super(Product, self).save(*args, *kwargs)

        # Image compression
        Image.open(self.image.path).save(self.image.path, quality=50, optimize=True)
