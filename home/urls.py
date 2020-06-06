from django.conf.urls import path, include
from .views import index

urlpatterns = [
    path('^$', index, name='index'),
]