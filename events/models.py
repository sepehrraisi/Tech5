from django.db import models
from django.core.validators import RegexValidator
from django import forms


# Create your models here.


class ContactUs(models.Model):
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    phone = models.CharField(max_length=11, default=None)

    class Meta:
        verbose_name = 'رویداد'
        verbose_name_plural = 'رویدادها'

    def __str__(self):
        return self.name
