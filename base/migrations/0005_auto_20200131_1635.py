# Generated by Django 3.0.2 on 2020-01-31 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20200131_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sociallink',
            name='alt',
        ),
        migrations.AddField(
            model_name='sociallink',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
