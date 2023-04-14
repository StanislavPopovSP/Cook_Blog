from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # путь ведущий на главную страницу
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list') # путь для какой-то категории
]