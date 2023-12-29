from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request
# Create your views here.
def index(request):
        if request.method == 'POST':
            city=request.POST['city']
            res=urllib.request.urlopen('http://api.weatherapi.com/v1/current.json?key=bf98021869e14a81af5152618230609&q='+city).read()
            json_data=json.loads(res)
            data={
                  "temprature":str(json_data['current']['temp_c'])+'C',
                  "pressure":str(json_data['current']['pressure_in']),
                  "humidity":str(json_data['current']['humidity']), 
                  "coordinates":str(json_data['location']['lat'])+' '+str(json_data['location']['lon']),
                  "icon":str(json_data['current']['condition']['icon']),
                  "time":str(json_data['location']['localtime']),
                  "country":str(json_data['location']['country']), 
                  "feels_like":str(json_data['current']['feelslike_c']),  
                  "wind":str(json_data['current']['wind_kph']),
                      
                  }
            
            day_night=int(json_data['current']['is_day'])
            if day_night==0:
                  day_night='NIGHT'
            else:
                  day_night='DAY'
        else:
              city=''
              data=''
              day_night=''

        print(data)
      
        return render(request, 'index.html', {'city': city, 'data': data,'day_night':day_night})
