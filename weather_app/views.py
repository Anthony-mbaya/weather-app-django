from django.shortcuts import render
import json #send request to api get res in json format
import urllib.request
# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = '4eab6aa3c70540a179497d3f41336576'
        res = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}').read()
        json_data = json.loads(res)
        data = {
            'country_code' : str(json_data['sys']['country']),
            'coordinate' : str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            'temp' : str(json_data['main']['temp']) + 'k',
            'pressure' : str(json_data['main']['pressure']),
            'humidity' : str(json_data['main']['humidity']),
        }

    else:
        data = {}
    return render(request, 'index.html', data)