from django.shortcuts import render
import requests

def index(request):
    appid = 'd6ed9b41d7205a064759ad98176b28ef'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = "Madrid"
    res = requests.get(url.format(city))

    print(res.text)
    return render(request, 'weather_1/index.html')
