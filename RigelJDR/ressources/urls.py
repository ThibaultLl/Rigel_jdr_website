from django.urls import path

from . import views

app_name = 'ressources'
urlpatterns = [
    path('', views.ressources, name='ressources'),
]