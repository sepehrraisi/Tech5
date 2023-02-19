from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from account.forms import RegisterForm
from core.mixins import AuthenticatedUserMixin

# Create your views here.
from core.models import TeammateRequest, GymRequest, CoachRequest


class RegisterView(SuccessMessageMixin, AuthenticatedUserMixin, CreateView):
    model = User
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('account:login')
    success_message = 'حساب شما با موفقیت ساخته شد، لطفا وارد حساب خود شوید.'


class Login(AuthenticatedUserMixin, LoginView):
    template_name = 'account/login.html'


class Account(LoginRequiredMixin, TemplateView):
    template_name = 'account/account.html'


class AccountUserRequests(LoginRequiredMixin, ListView):
    template_name = 'account/account_user_request.html'

    def get_queryset(self):
        type_param = self.request.GET.get('type')
        if type_param == 'gym':
            return GymRequest.objects.filter(user=self.request.user)
        elif type_param == 'teammate':
            return TeammateRequest.objects.filter(user=self.request.user)
        elif type_param == 'coach':
            return CoachRequest.objects.filter(user=self.request.user)
        raise Http404


class AboutUs(TemplateView):
    template_name = 'account/about-us.html'


class BashgahTech5(TemplateView):
    template_name = 'account/bashgah-tech5.html'
