import requests, os
from twilio.rest import Client

OWMEndpoint = 'https://api.openweathermap.org/data/2.5/onecall'
APIKEY = os.environ.get('API_KEY')
parameters = {
    'lat': 43.156578,
    'lon': -77.608849,
    'appid': APIKEY,
    'exclude': 'current,minutely,daily'
}
accountSID = os.environ.get('SID_VAR')
authToken = os.environ.get('AUTH_VAR')
trialNum = os.environ.get('TRIAL_NUM')

response = requests.get(OWMEndpoint, params=parameters)
response.raise_for_status()

weatherData = response.json()

idList = [weatherData['hourly'][hour]['weather'][0]['id'] for hour in range (0,12)]

willRain = False

for id in idList:
    if int(id) < 700:
        willRain = True

if willRain:
    client = Client(accountSID, authToken)
    message = client.messages \
        .create(
        body="It will rain today while you are outside!",
        from_=trialNum,
        to='+19294242480'
    )
    print(message.status)
