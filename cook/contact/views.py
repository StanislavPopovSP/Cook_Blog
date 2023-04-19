from .forms import ContactForm
from django.views.generic import CreateView
from django.urls import reverse_lazy




class CreateContact(CreateView):
    """Обработка формы для связи с поваром"""
    form_class = ContactForm
    template_name = 'blog/addpage.html'
    success_url = reverse_lazy('home')