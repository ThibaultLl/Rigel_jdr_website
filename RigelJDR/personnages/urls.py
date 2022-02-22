from django.urls import path

from . import views

app_name = 'personnages'
urlpatterns = [
    path('', views.personnages, name='personnages'),
]