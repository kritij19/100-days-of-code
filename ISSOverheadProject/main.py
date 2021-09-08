
import requests
import datetime as dt
import smtplib

my_latitude = 28.644800
my_longitude = 77.216721

smtp_address = "smtp.gmail.com"     # for gmail
my_email = #####
pswd = ####
receivers_email = #####

# Getting longitude and latitude from ISS API
iss_response = requests.get(url = 'http://api.open-notify.org/iss-now.json')
iss_response.raise_for_status()
iss_data = iss_response.json()
latitude = float(iss_data['iss_position']['latitude'])
longitude = float(iss_data['iss_position']['longitude'])

parameters = {'lat': my_latitude, 
              'lng':  my_longitude,
              'formatted': 0}

# Determine time of sunset and sunrise
sunset_response = requests.get(url = 'https://api.sunrise-sunset.org/json?lat=28.644800&lng=77.216721', params = parameters)
sunset_response.raise_for_status()
data = sunset_response.json()
# Extracting hour from format
sunrise_hr = int(data['results']['sunrise'].split("T")[1].split(":")[0])
sunset_hr = int(data['results']['sunset'].split("T")[1].split(":")[0])

# Determine current time
time_now = dt.datetime.now()
current_hr = time_now.hour

# Determine if ISS near users location
def ISS_near():
    if latitude >= my_latitude - 5 and latitude <= my_latitude + 5 and longitude  >= my_longitude - 5 and longitude <= my_longitude + 5:
        return True
    else:
        return False

if current_hr > sunset_hr:
    if ISS_near():
        with smtplib.SMTP(smtp_address) as connection:
            connection.starttls()
            connection.login(user = my_email, password = pswd)
            connection.sendmail(
                from_addr = my_email,
                to_addrs = receivers_email,
                msg = "subject: LOOK UP!\n\n The ISS is near. LOOK UP!"
            )
