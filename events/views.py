from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from .forms import ContactusForm
from config import settings
from django.core.mail import send_mail
from .models import ContactUs

# Create your views here.


class events(ListView):
    template_name = 'events.html'


def Contact_Us(request):

    sent = False
    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():


            cd = form.cleaned_data
            subject = cd['subject']
            name = cd['name']
            email = cd['email']
            phone = cd['phone']
            message = cd['message']

            obj = ContactUs()
            obj.name = form.cleaned_data['name']
            obj.email = form.cleaned_data['email']
            obj.phone = form.cleaned_data['phone']
            obj.save()

            msg = "name: {0}\nphone: {1}\nemail: {2}\n".format(name, phone, email, message)
            # todo : show user a success message
            send_mail(subject, msg, 'sara.adibi20000@gmail.com', ['sara.adibi20000@gmail.com', 'tech5.ir.event@gmail.com'], fail_silently=False)
            sent = True
            return render(request, 'events.html', {'form': form, sent:sent})
    form = ContactusForm()
    return render(request, 'events.html', )
