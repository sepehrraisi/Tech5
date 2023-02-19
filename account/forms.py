from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django import forms
from account.models import User


class RegisterForm(UserCreationForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=17)

    social_media = forms.CharField(max_length=32, help_text='First name')
    age = forms.CharField(max_length=32, help_text='First name')
    education = forms.CharField(max_length=32, help_text='First name')
    favorite = forms.CharField(max_length=32, help_text='First name')
    experience = forms.CharField(max_length=32, help_text='First name')
    aims = forms.CharField(max_length=32, help_text='First name')

    class Meta:
        model = User
        fields = (
        'username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'social_media', 'age',
        'education', 'favorite', 'experience', 'aims')
