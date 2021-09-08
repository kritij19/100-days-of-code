# This file will uses the DataManager, FlightSearch and NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint

datamanager = DataManager()
flightsearch = FlightSearch()
notification_manager = NotificationManager()

# Accessing data from prices sheet
sheet_data = datamanager.data['prices']


for row in sheet_data:

    # Replaces all empty IATA codes with actual value in spreadsheet
    if len(row['iataCode']) == 0:
        
        row['iataCode'] = flightsearch.iata_updater(row['city'])    # Updates value of IATA code in dictionary
        datamanager.update_iatacode(row['id'], row)     # Updates in google sheet

    # If a flight cheaper than minimum set price found. Sends mail.
    if flightsearch.flightsearcher(row['iataCode'], row['lowestPrice']):

        mail_subject = F"{row['city'].title()} flight price drop alert!"

        mail_body = f"""We have found an amazing deal for you!

ONLY {flightsearch.price} {flightsearch.currency} to Travel from {flightsearch.departure_city} ({flightsearch.departure_airport_code}) to {flightsearch.destination_city} ({flightsearch.destination_airport_code}) at just  between {flightsearch.trip_starting_date} and {flightsearch.trip_end_date}

Book the flights using the following link:
https://www.ixigo.com/search/result/flight?sort-type=fare&return-sort-type=fare&from={flightsearch.departure_airport_code}&to={flightsearch.destination_airport_code}&date={flightsearch.departure_date}&returnDate={flightsearch.arrival_date}&adults=1&children=0&infants=0&class=e&source=Search%20Form

Get your hands on this steal ASAP! 

Regards,
Fly High Club"""
        
        notification_manager.send_mail(subject = mail_subject, body = mail_body)
        print(f"{row['city']} mail sent") 
    else:
        print(f"{row['city']} skipped")



## pprint() makes it easy to view data
# pprint(f"\n\nFrom main.py: {sheet_data}") 
