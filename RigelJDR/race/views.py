from django.shortcuts import render


def race(request):
    return render(request, 'race/race.html')
