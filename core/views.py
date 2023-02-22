from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
from core.forms import TeammateRequestForm, GymRequestForm, CoachRequestForm
from core.models import TeammateRequest, GymRequest, CoachRequest


def home_view(request):
    return render(request, 'core/home.html')


def about_view(request):
    return render(request, 'core/about.html')


def home_ex_view(request):
    return render(request, 'core/home_ex.html')


class TeammateRequestFormView(SuccessMessageMixin, CreateView):
    model = TeammateRequest
    template_name = 'core/teammate_request_form.html'
    form_class = TeammateRequestForm
    success_url = reverse_lazy('core:teammate-request')
    success_message = 'درخواست شما با موفقیت ارسال شد.'

    def form_valid(self, form):
        teammate_request_form = form.save(commit=False)
        teammate_request_form.user = self.request.user
        teammate_request_form.save()
        return super(TeammateRequestFormView, self).form_valid(form)


class GymRequestFormView(SuccessMessageMixin, CreateView):
    model = GymRequest
    template_name = 'core/gym_request_form.html'
    form_class = GymRequestForm
    success_url = reverse_lazy('core:gym-request')
    success_message = 'درخواست شما با موفقیت ارسال شد.'

    def form_valid(self, form):
        gym_request_form = form.save(commit=False)
        gym_request_form.user = self.request.user
        gym_request_form.save()
        return super(GymRequestFormView, self).form_valid(form)


class CoachRequestFormView(SuccessMessageMixin, CreateView):
    model = CoachRequest
    template_name = 'core/coach_request_form.html'
    form_class = CoachRequestForm
    success_url = reverse_lazy('core:coach-request')
    success_message = 'درخواست شما با موفقیت ارسال شد.'

    def form_valid(self, form):
        coach_request_form = form.save(commit=False)
        coach_request_form.user = self.request.user
        coach_request_form.save()
        return super(CoachRequestFormView, self).form_valid(form)
