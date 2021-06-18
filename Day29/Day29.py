import requests  # a way to interact with API
from datetime import datetime
import smtplib
import time

EMAIL = input("Enter your email: ")
PASSWORD = input("Enter your password: ")
ROC_LAT = float(input("Enter your latitude: ")) #43.161030
ROC_LONG = float(input("Enter your longitude: ")) #-77.610924

parameters = {
    'lat': ROC_LAT,
    'lng': ROC_LONG,
    'formatted': 0
}

print("\nProgram now running")

def issOverhead():
    '''
    :returns True if the difference in longitude and latitude between user longitude and lattitude is +/- 5
    and False otherwise
    '''
    response = requests.get(url="http://api.open-notify.org/iss-now.json")  # returns a response code
    response.raise_for_status()  # raises the appropriate error if any

    data = response.json()  # returns the json data

    issLong, issLat = float(data["iss_position"]["longitude"]), float(data["iss_position"]["latitude"])

    if abs(ROC_LAT - issLat) <= 5 and abs(ROC_LONG - issLong) <= 5:
        return True
    return False


# API Parameters


def isNight():
    '''
    Checks if the time right now is between sunrise and sunset time
    :returns True if the time right now is between sunrise and sunset and False otherwise
    '''
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']

    sunriseHour = int(sunrise.split('T')[1].split(":")[0])
    sunsetHour = int(sunset.split('T')[1].split(":")[0])

    now = datetime.now()
    nowHour = now.hour
    if nowHour >= sunsetHour or nowHour <= sunriseHour:
        return True
    return False


while True:
    time.sleep(60) # runs this every 60 seconds
    if isNight() and issOverhead():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs='usiam@u.rochester.edu',
                                msg="Subject: ISS Overhead\n\nLook outside!")
