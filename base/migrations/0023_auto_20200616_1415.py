# Generated by Django 3.0.7 on 2020-06-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_auto_20200613_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuration',
            name='how_to_buy',
        ),
        migrations.AddField(
            model_name='profile',
            name='how_to_buy',
            field=models.URLField(blank=True, help_text="Link to the instructions, it is only visible on the homepage user's page."),
        ),
    ]
