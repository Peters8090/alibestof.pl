# Generated by Django 3.0.3 on 2020-04-15 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0036_auto_20200211_1340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-date_modified', '-pk'], 'permissions': [('can_interact_with_all_products', 'Can interact with all products'), ('can_interact_with_his_own_products', 'Can interact with his own products')]},
        ),
    ]