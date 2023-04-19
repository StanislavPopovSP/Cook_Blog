from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    """Создание формы, для связи с поваром"""
    class Meta:
        model = ContactModel
        fields = '__all__'
