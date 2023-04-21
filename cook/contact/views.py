from django.shortcuts import render
from .forms import ContactForm
from .models import *
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy

class ContactView(View):
    """Выводит контакты, форму"""
    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForm()
        context = {
            'contacts': contacts,
            'form': form
        }
        return render(request, 'contact/contact.html', context)


class CreateContact(CreateView):
    """Обработка формы для связи с поваром"""
    form_class = ContactForm
    success_url = reverse_lazy('home')


class AboutView(View):
    """Выводит контакты, форму"""
    def get(self, request):
        about = About.objects.last() # что бы выводилась одна последняя запись
        context = {
            'about': about,
        }
        return render(request, 'contact/about.html', context)