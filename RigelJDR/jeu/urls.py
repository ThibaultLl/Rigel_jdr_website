from django.urls import path

from . import views

app_name = 'jeu'
urlpatterns = [
    path('', views.jeu, name='jeu'),
]