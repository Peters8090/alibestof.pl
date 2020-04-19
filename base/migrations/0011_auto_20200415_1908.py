# Generated by Django 3.0.3 on 2020-04-15 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0010_auto_20200415_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileconfiguration',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]