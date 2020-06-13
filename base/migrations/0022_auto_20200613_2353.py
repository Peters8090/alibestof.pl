# Generated by Django 3.0.3 on 2020-06-13 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_configuration_how_to_buy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='how_to_buy',
            field=models.URLField(blank=True, help_text="Link to the instructions, it is only visible on the homepage user's page."),
        ),
    ]
