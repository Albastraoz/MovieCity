from django.urls import path, include
from .views import index, add_movie

urlpatterns = [
    path('', index, name='index'),
    path('add_movie/', add_movie, name='add_movie'),
]