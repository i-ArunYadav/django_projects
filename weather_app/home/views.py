from django.shortcuts import render
import requests

def index(request):

	city = request.GET.get('city',"lucknow")
	url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f3ac7848cc27d8d386d0ca1c19ab575d'
	data = requests.get(url).json()
	payload = {
		'city': data['name'], 
		'weather': data['weather'][0]['main'],
		'icon':data['weather'][0]['icon'],
		'kelvin_temperature': data['main']['temp'],
		'celsius_temperature': data['main']['temp']-273,
		'pressure': data['main']['pressure'],
		'humidity':data['main']['humidity'],
		'description':data['weather'][0]['main']
	}

	context ={'data':payload}
	print(data)
	return render(request,'home/home.html',context)


