# Generated by Django 3.0.2 on 2020-01-19 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_product_date_modified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-date_created']},
        ),
    ]
