from django.contrib.auth.models import User
from django.db import models
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

    def __str__(self):
        return 'Site configuration'

    @staticmethod
    def get_configuration():
        return get_object_or_404(Configuration)


class SocialLink(models.Model):
    configuration = models.ForeignKey(Configuration, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='base/social-links/')
    link = models.URLField()


class UserProfileConfiguration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    password = models.CharField(max_length=50, blank=True, null=True,
                                help_text='Leave it blank if you don\'t want to use the password protection for your products')

    class Meta:
        permissions = [
            ('can_interact_with_all_user_profile_configurations', 'Can interact with all user profile configurations'),
            ('can_interact_with_his_own_user_profile_configuration',
             'Can interact with his own user profile configuration')]

    def __str__(self):
        return f'Profile Configuration [{self.user.username}]'

    @staticmethod
    def get_user_profile_configuration(username):
        return UserProfileConfiguration.objects.get(user__username__exact=username)
