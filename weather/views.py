"""
This is a Docstring
"""
import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(req):
    """
    No Errors
    """
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=68c1a68142b2624ec37472f31c8dca52'
    

    if req.method == 'POST':
        form = CityForm(req.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    
    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(req, 'weather/weather.html', context)
