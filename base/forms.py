from django import forms

from base.models import UserProfileConfiguration


class UserProfileConfigurationForm(forms.ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=False,
                               help_text='Leave it blank if you don\'t want to use the password protection for your products')

    class Meta:
        model = UserProfileConfiguration
        fields = '__all__'
        help_texts = '__all__'