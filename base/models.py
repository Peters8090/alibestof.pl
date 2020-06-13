from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404


class Configuration(models.Model):
    home_page_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='home_page_user', blank=False,
                                       null=True)
    product_duplication_superuser = models.ForeignKey(User, on_delete=models.SET_NULL,
                                                      related_name='product_duplication_superuser', blank=False,
                                                      null=True)
    products_per_page = models.IntegerField(default=20)
    product_link_validator = models.TextField(max_length=1000, blank=True)
    photos_link_validator = models.TextField(max_length=1000, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and len(Profile.objects.all()) > 0:
            return
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return 'Configuration'


class SocialLink(models.Model):
    configuration = models.ForeignKey(Configuration, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='base/social-links/')
    link = models.URLField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    password = models.CharField(max_length=50, blank=True, null=True,
                                help_text='Leave it blank if you don\'t want to use the password protection for your products.')

    class Meta:
        permissions = [
            ('can_interact_with_all_profiles', 'Can interact with all profiles'),
            ('can_interact_with_his_own_profile',
             'Can interact with his own profile')]

    def __str__(self):
        return f'Profile [{self.user.username}]'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
