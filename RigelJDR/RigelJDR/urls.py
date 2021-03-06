from django.contrib import admin
from django.urls import include, path
from django.urls import re_path
from home import views
urlpatterns = [
    path('contact/', include('contact.urls')),
    path('home/', include('home.urls')),
    path('jeu/', include('jeu.urls')),
    path('outils/', include('outils.urls')),
    path('ressources/', include('ressources.urls')),
    path('team/', include('team.urls')),
    path('univers/', include('univers.urls')),
    re_path('^$',views.accueil,name='home'),
    path('admin/', admin.site.urls),
    path('race/', include('race.urls')),
    path('personnages/', include('personnages.urls')),
]