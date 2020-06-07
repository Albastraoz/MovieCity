from django.urls import path, include
from .views import index, add_movie, search_movie

urlpatterns = [
    path('', index, name='index'),
    path('add_movie/<str:id>', add_movie, name='add_movie'),
    path('search/', search_movie, name='search_movie'),
]