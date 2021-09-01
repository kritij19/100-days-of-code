import requests

questions_api = 'https://opentdb.com/api.php'

parameters = {
    'amount': 10,
    'type': 'boolean'
}

# Getting list of dicts from opentdb API
response = requests.get(url = questions_api, params = parameters)
response.raise_for_status()
questions_json = response.json()
question_data = questions_json['results']   # List of dicts

