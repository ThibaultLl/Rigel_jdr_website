from django.shortcuts import render


def univers(request):
    return render(request, 'univers/univers.html')
