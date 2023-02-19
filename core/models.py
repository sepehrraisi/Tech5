from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class Activity(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام فعالیت')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='توضیحات')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'فعالیت'
        verbose_name_plural = 'فعالیت ها'

    def __str__(self):
        return self.name


GENDER_CHOICES = (
    ('m', 'مرد'),
    ('fm', 'زن'),
    ('other', 'غیره')
)


class TeammateRequest(models.Model):
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name='جنسیت')
    location = models.CharField(max_length=255, verbose_name='موقعیت جغرافیایی')
    activities = models.ManyToManyField(Activity, related_name='teammates', verbose_name='فعالیت های انتخاب شده')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='teammate_requests', verbose_name='کاربر')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'درخواست هم تیمی'
        verbose_name_plural = 'درخواست های هم تیمی'

    def __str__(self):
        return f"{self.user.get_full_name()} | {self.location} | {self.activities.count()} فعالیت"


class GymRequest(models.Model):
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name='جنسیت')
    location = models.CharField(max_length=255, verbose_name='موقعیت جغرافیایی')
    activities = models.ManyToManyField(Activity, related_name='gyms', verbose_name='فعالیت های انتخاب شده')
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='gym_requests', verbose_name='کاربر'
    )
    files = models.FileField(
        upload_to='gym-request/', null=True, blank=True, verbose_name='اطلاعات مجموعه'
    )
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'درخواست باشگاه'
        verbose_name_plural = 'درخواست های باشگاه'

    def __str__(self):
        return f"{self.user.get_full_name()} | {self.location} | {self.activities.count()} فعالیت"


class CoachRequest(models.Model):
    TYPE_OF_TRAINING_CHOICES = (
        ('a', 'حضوری'),
        ('b', 'مجازی')
    )
    type_of_training = models.CharField(max_length=5, choices=TYPE_OF_TRAINING_CHOICES, verbose_name='نوع آموزش')
    location = models.CharField(max_length=255, verbose_name='موقعیت جغرافیایی')
    activities = models.ManyToManyField(Activity, related_name='coaches', verbose_name='فعالیت های انتخاب شده')
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='coach_requests', verbose_name='کاربر'
    )
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'درخواست مربی'
        verbose_name_plural = 'درخواست های مربی'

    def __str__(self):
        return f"{self.user.get_full_name()} | {self.location} | {self.activities.count()} فعالیت"
