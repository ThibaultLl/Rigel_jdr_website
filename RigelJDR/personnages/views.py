from django.shortcuts import render


def personnages(request):
    return render(request, 'personnages/personnages.html')
