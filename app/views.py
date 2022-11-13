from django.shortcuts import render
import requests

# Create your views here.



def home(request):
    # if 'city' in request.GET

    city = request.GET.get('city', 'Rapid City')

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=aaf4c1da5761e18d8d315fd10081d3e0'
    data = requests.get(url).json()

    if(data['cod']!='404' and city!=''):
        allData = {
            'city': data['name'],
            'weather': data['weather'][0]['main'],
            'icon': data['weather'][0]['icon'],
            'main': data['weather'][0]['main'],
            'K_temperature': data['main']['temp'],
            'c_temperature': int(data['main']['temp'] - 273),
            'f_temperature': int(int(data['main']['temp'] - 273) * 5 / 9 + 32),
            'c_temp_max': int(data['main']['temp_max'] - 273),
            'c_temp_min': int(data['main']['temp_min'] - 273),
            'f_temp_max': int(int(data['main']['temp_max'] - 273) * 5 / 9 + 32),
            'f_temp_min': int(int(data['main']['temp_min'] - 273) * 5 / 9 + 32),
            'description': data['weather'][0]['description'].capitalize(),
            'message': ''
        }
    else:
        city='Rapid City'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=aaf4c1da5761e18d8d315fd10081d3e0'
        data = requests.get(url).json()
        allData = {
            'city': data['name'],
            'weather': data['weather'][0]['main'],
            'icon': data['weather'][0]['icon'],
            'main': data['weather'][0]['main'],
            'K_temperature': data['main']['temp'],
            'c_temperature': int(data['main']['temp'] - 273),
            'f_temperature': int(int(data['main']['temp'] - 273) * 5 / 9 + 32),
            'c_temp_max': int(data['main']['temp_max'] - 273),
            'c_temp_min': int(data['main']['temp_min'] - 273),
            'f_temp_max': int(int(data['main']['temp_max'] - 273) * 5 / 9 + 32),
            'f_temp_min': int(int(data['main']['temp_min'] - 273) * 5 / 9 + 32),
            'description': data['weather'][0]['description'].capitalize(),
            'message':'Please enter a valid city'
            
        }

    context = {'data': allData}
    print(context)
    return render(request, 'app/home.html', context)