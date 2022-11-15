from django.shortcuts import render


def index(request):
    return render(request, 'weather_1/index.html')
