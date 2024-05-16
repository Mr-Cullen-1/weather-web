from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        try:
            source = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q='
                + city + '&appid=7348791f96293ee98a03fe3f46c30e22').read()
            list_of_data = json.loads(source)

            data = {
                "country_code": str(list_of_data.get('sys', {}).get('country', '')),
                "coordinate": str(list_of_data.get('coord', {}).get('lon', '')) + ' '
                              + str(list_of_data.get('coord', {}).get('lat', '')),
                "temp": str(list_of_data.get('main', {}).get('temp', '')) + 'k',
                "pressure": str(list_of_data.get('main', {}).get('pressure', '')),
                "humidity": str(list_of_data.get('main', {}).get('humidity', '')),
            }
        except Exception as e:
            print("An error occurred:", e)
            data = {}
    else:
        data = {}
    return render(request, "main/index.html", data)
