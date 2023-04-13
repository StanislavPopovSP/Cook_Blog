from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home') # путь ведущий на главную страницу
]