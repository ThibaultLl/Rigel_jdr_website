from django.shortcuts import render


def jeu(request):
    return render(request, 'jeu/jeu.html')
