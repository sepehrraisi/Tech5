from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    # path('events/', views.events.as_view(), name='new-events'),
    path('events/', views.Contact_Us, name='new-events'),
]
