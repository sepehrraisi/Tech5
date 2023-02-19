from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django import forms
from account.models import User


class ContactusForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, required=False, label='پیام')
    name = forms.CharField(max_length=25, required=True, label='نام و نام خانوادگی')
    email = forms.EmailField(required=True, label='ایمیل', max_length=30)
    subject = forms.CharField(required=True, max_length=25, label='موضوع')
    phone = forms.CharField(max_length=11, required=True, label='شماره تماس')
