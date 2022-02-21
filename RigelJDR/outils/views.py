from django.shortcuts import render


def outils(request):
    return render(request, 'outils/outils.html')
