import requests
from twilio.rest import Client
import os
from decouple import config

# from https://www.latlong.net/
my_lat = 28.632429
my_long = 77.218788
receivers_num = '99999999999'     # Should be in twilio's verified contacts

# Twilio- To send text msgs
account_sid = 'AC81a9c9ff58b4a393d20bd56f4ef16a69'
auth_token = os.environ.get('auth_token')


# Weather data from Open Weather map
# url: http://api.openweathermap.org/data/2.5/onecall?lat=28.632429&lon=77.218788&exclude=current,minutely,daily&appid=fcee7e2c896cf8caa1ec3037a2b0b1b5

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"        
OWM_APIKEY = os.environ.get('api_key')     # API key set as env variable
parameters = {
    'lat': my_lat,
    'lon': my_long, 
    'exclude': 'current,minutely,daily',
    'appid': OWM_APIKEY
}

response = requests.get(url = OWM_endpoint, params = parameters)
response.raise_for_status()
# Hourly forecast for the next 48 hours
data = response.json()


# Checking if expected rain in the next 12 hrs
for hour in range(12):
    
    weather_code = data["hourly"][hour]["weather"][0]["id"]
    
    # If weather code less than 700 = rain
    if weather_code < 700:
        # Sending msg using twilio
        client = Client(account_sid, auth_token)
        message = client.messages \
                .create(
                     body="It is goin to rain today. Carry an umbrella.",
                     from_='+14694143615',
                     to = receivers_num
                 )
        print(message.status)
        break

# Host on pythonanywhere to run everyday at a given time
