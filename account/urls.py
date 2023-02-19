from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import (
    RegisterView,
    Login, Account, AccountUserRequests, AboutUs, BashgahTech5
)

app_name = 'account'
urlpatterns = [
    path('', Account.as_view(), name='account-page'),
    path('requests/', AccountUserRequests.as_view(), name='account-user-requests'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('about-us/', AboutUs.as_view(), name='about-us'),
    path('bashgah-tech5/', BashgahTech5.as_view(), name='bashgah-tech5'),
]
