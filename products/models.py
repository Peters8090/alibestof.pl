from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/')
    link = models.URLField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_modified']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        def replace_url(text, text2):
            if text[:4] == text2:
                text = "." + text
            text = text.replace(f' {text2}', f'.{text2}')
            text = text.replace(f'\n{text2}', f'\n.{text2}')

            return text

        self.description = replace_url(self.description, 'http')
        self.description = replace_url(self.description, 'www')
        super(Product, self).save(*args, *kwargs)
