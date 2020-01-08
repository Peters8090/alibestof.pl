# Generated by Django 3.0.2 on 2020-01-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200108_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='product',
            name='link',
            field=models.URLField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='reflink',
            field=models.URLField(blank=True, max_length=1000),
        ),
    ]
