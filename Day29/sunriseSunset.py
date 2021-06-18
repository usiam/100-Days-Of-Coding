import requests
from datetime import datetime

ROC_LAT = 43.161030
ROC_LONG = -77.610924

# API Parameters
parameters = {
    'lat': ROC_LAT,
    'lng': ROC_LONG,
    'formatted': 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

sunriseHour = sunrise.split('T')[1].split(":")[0]
sunsetHour = sunset.split('T')[1].split(":")[0]

now = datetime.now()
nowHour = now.hour