from django.db import migrations


def configuration_setup(apps, _):
    Configuration = apps.get_model('base', 'Configuration')

    Configuration().save()


class Migration(migrations.Migration):
    dependencies = [
        ('base', '0019_auto_20200613_2228'),
    ]

    operations = [
        migrations.RunPython(configuration_setup),
    ]
