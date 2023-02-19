from django.contrib import admin
from .models import Activity, TeammateRequest, GymRequest, CoachRequest


# Register your models here.
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass


@admin.register(TeammateRequest)
class TeammateRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(GymRequest)
class GymRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(CoachRequest)
class CoachRequestAdmin(admin.ModelAdmin):
    pass
