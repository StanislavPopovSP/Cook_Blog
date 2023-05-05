from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('', cache_page(60 * 15)(views.HomeView.as_view()), name='home'), # путь ведущий на главную страницу, страница закеширована. Всремя в сек 60 * 15 = 15 мин.

    path('comment/<int:pk>/', views.CreateComment.as_view(), name='create_comment'), # связь комментария с постом
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'), # путь для какой-то категории
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_single'), # путь для просмотра отдельной статьи
]