from django.shortcuts import render
# from django.http import HttpResponse
import requests
from .models import SearchedCity
# Create your views here.
def main(request):
    return render(request, 'index.html')


def weather(request):
    return render(request, 'weather.html')
def search(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        API_KEY = '6621546e1a94625a215c063e4320d66d'
        weather_API=f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}'
        res=requests.get(weather_API)
        data=res.json()
        temp = data['main']['temp']
        feels_like=data['main']['feels_like']
        temp_min=data['main']['temp_min']
        temp_max=data['main']['temp_max']
        sys = data['sys']['country']
        weather=f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
        clouds=data['clouds']['all']
        searchedCity = SearchedCity()
        searchedCity.city=request.POST.get('city').title()
        searchedCity.temperature=temp
        searchedCity.image=weather
        searchedCity.save()
        all_context={'data' :data, 'temp' :temp, 'city' :city.title(), 'feels_like' :feels_like, 'temp_min' :temp_min, 'temp_max' :temp_max, 'sys' :sys, 'weather1' :weather, 'clouds' :clouds}
        return render(request, 'weather.html', context=all_context)
def city(request): 
    cities = SearchedCity.objects.all()
    return render(request, 'index.html', {'cities' :cities})  
  