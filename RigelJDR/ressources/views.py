from django.shortcuts import render


def ressources(request):
    return render(request, 'ressources/ressources.html')
