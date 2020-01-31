# Generated by Django 3.0.2 on 2020-01-30 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='home_page_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_page_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='product_duplication_superuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_duplication_superuser', to=settings.AUTH_USER_MODEL, verbose_name='Product Duplication Superuser'),
        ),
    ]