from django.urls import path, include
from .views import index, add_movie, search_movie, delete_movie

urlpatterns = [
    path('', index, name='index'),
    path('search/', search_movie, name='search_movie'),
    path('add_movie/<str:id>', add_movie, name='add_movie'),
    path('delete_movie/<int:id>', delete_movie, name='delete_movie'),
]