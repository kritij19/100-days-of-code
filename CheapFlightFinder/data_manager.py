import requests

sheety_endpoint = #####

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):        
        # Getting all data from spreadsheet
        self.response = requests.get(url = sheety_endpoint)
        self.data = self.response.json()

    def update_iatacode(self, row_id: int, row: dict):
        '''Updates value of IATA code in rows where value is empty. '''      
        
        put_endpoint = f'{sheety_endpoint}/{row_id}'
        put_body = {'price': row}
        put_response = requests.put(url = put_endpoint, json = put_body)
        
