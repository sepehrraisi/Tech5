from django.urls import path
from .views import (
    home_view,
    TeammateRequestFormView,
    GymRequestFormView,
    CoachRequestFormView
)

app_name = 'core'
urlpatterns = [
    path('', home_view, name='home'),
    path('teammate-request/', TeammateRequestFormView.as_view(), name='teammate-request'),
    path('gym-request/', GymRequestFormView.as_view(), name='gym-request'),
    path('coach-request/', CoachRequestFormView.as_view(), name='coach-request'),
]
