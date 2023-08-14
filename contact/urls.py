from django.urls import path
from .import views

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'), # страница контакт
    path('feedback/', views.CreateContact.as_view(), name='feedback'), # для формы контакт

    path('about/', views.AboutView.as_view(), name='about') # страница о нас
]