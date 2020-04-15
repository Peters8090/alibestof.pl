from django import forms

from base.models import UserProfileConfiguration


class UserProfileConfigurationForm(forms.ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    class Meta:
        model = UserProfileConfiguration
        fields = '__all__'
