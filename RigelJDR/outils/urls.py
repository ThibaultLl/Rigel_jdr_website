from django.urls import path

from . import views

app_name = 'outils'
urlpatterns = [
    path('', views.outils, name='outils'),
]