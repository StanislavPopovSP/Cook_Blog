from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'), # путь ведущий на главную страницу

    path('comment/<int:pk>/', views.CreateComment.as_view(), name='create_comment'), # связь комментария с постом
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'), # путь для какой-то категории
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_single'), # путь для просмотра отдельной статьи
]