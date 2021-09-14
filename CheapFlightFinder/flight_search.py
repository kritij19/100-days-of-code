# import json
import requests
from datetime import datetime, timedelta

# Can be changed
DEPARTURE_CITY = 'London'
DEPARTURE_CITY_CODE = 'LON'
CURRENCY = "GBP"

# Credentials for KIWI api.
location_endpoint = 'https://tequila-api.location.com/locations/query'
kiwi_api_key =  ####

search_endpoint = 'https://tequila-api.kiwi.com/v2/search'


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    
    def __init__(self):

        self.departure_city = DEPARTURE_CITY
        self.departure_city_code = DEPARTURE_CITY_CODE
        self.destination_city = ""
        self.destination_city_code = ""
        self.currency = CURRENCY

        # Used to display and use results
        ## Big cities can have multiple airports each having diff codes.
        self.destination_airport_code = ""
        self.departure_airport_code = ""
        self.price = 0
        self.trip_starting_date = None
        self.trip_end_date = None

        # Search dates from tommorow's date to 6 months from now
        current_date = datetime.now().date()

        tomm_date = current_date + timedelta(days = 1)
        tomm_date_formatted = tomm_date.strftime("%d/%m/%Y")    # DD/MM/YYYY
        self.search_starting_date = tomm_date_formatted

        date_after_6mo = current_date + timedelta(days = 180)
        date_after_6mo_formatted = date_after_6mo.strftime("%d/%m/%Y")  
        self.search_end_date = date_after_6mo_formatted
        
        # Formatted dates for flight link
        tomm_date_for_url = tomm_date.strftime("%d%m%Y")    # DDMMYYYY
        self.departure_date = tomm_date_for_url

        date_after_6mo_url = tomm_date.strftime("%d%m%Y")
        self.arrival_date = date_after_6mo_url

        # Common header for location and search api
        self.api_header = {'apikey': kiwi_api_key}

    def iata_updater(self, city_name: str):
        '''Returns IATA codes with the city name as input'''
        
        location_header = self.api_header
        location_body = {
            'term': city_name,
            # We want the city code (Since most of the cities have multiple airports)
            'location_types': 'city'    
        }
        
        location_reponse = requests.get(url = location_endpoint, headers = location_header, params = location_body)
        location_data = location_reponse.json()
        return location_data["locations"][0]['code']

    def flightsearcher(self, destination_city_code: str, minimum_price: int):
        '''Returns True if flight cheaper than minimum threshold available. Also sets attributes to values according to proposed flight details.
          Else returns False.'''
        
        search_body = {
            'fly_from': self.departure_city_code,
            'fly_to': destination_city_code,
            'date_from': self.search_starting_date,
            'date_to': self.search_end_date,
            'nights_in_dst_from': 7,    # Stay between 7 - 28 nights
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'adults': 1,
            'curr': self.currency,
            'max_stopovers': 0,     # Direct flight - No stopovers
            'one_for_city':  1
        }

        # Getting flight data from KIWI api
        search_response = requests.get(url = search_endpoint, params = search_body, headers = self.api_header)
        search_data = search_response.json()

        # Returns price for the cheapest flight
        try:
            self.price = search_data['data'][0]['price']
            print()

        except IndexError:
            # If no flights available. (Closed due to some reason)
            return False

        else:
            self.price = search_data['data'][0]['price']    # Trip expense
            
            # If flight price is less than threshold set by user returns True
            if self.price < minimum_price:
                              
                # Setting all attributes according to journey details
                self.destination_airport_code = search_data['data'][0]["flyTo"]
                self.departure_airport_code = search_data['data'][0]["flyFrom"]
                self.destination_city = search_data['data'][0]["cityTo"]
                self.trip_starting_date = search_data['data'][0]['route'][0]['local_departure'].split('T')[0]
                self.trip_end_date = search_data['data'][0]['route'][1]['local_departure'].split('T')[0]
                
                return True           
            
            else:
                return False
