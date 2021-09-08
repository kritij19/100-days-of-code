'''WORKOUT TRACKER:

User inputs their exercise in text format. 
"Ran x miles and swam for y minutes"
"Swam for x minutes"

Stats for each activity (duration, calories) stored in a google sheet. If duration is not mentioned by user, calculated using values of speed.
Results will be personalised according to age, weight and height. (Which can be changed in the body of the code)'''

import requests
import datetime as dt
import os

# Nutritionix API to Naturally Process text inputted by the user
NUTRITIONIX_API_ID = ######
NUTRITIONIX_API_KEY = os.environ.get('NUTRITIONIX_API_KEY')

#### Posting exercise information
nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': NUTRITIONIX_API_ID,
    'x-app-key': NUTRITIONIX_API_KEY,
}

body = {   
 "query": input("Describe your today's workout routine: \n"),
 "gender": "female",
 "weight_kg": 48,
 "height_cm": 155,
 "age": 19
}

response = requests.post(url = nutritionix_endpoint, headers = headers, json = body)
nutritionix_data = response.json()


##### Posting data into google sheets using Sheety
# No authentication rqrd

sheety_endpoint = os.environ.get('SHEETY_ENDPOINT')

sheety_header = {
    'Authorization': os.environ.get('SHEETY_BEARER_TKN')
}
current = dt.datetime.now()
current_date = current.strftime("%d/%m/%Y")
current_time = current.strftime("%X")

# Adding a new row for each of the activity

for exercise in nutritionix_data['exercises']:
    sheety_body = {
        'workoutTracker': {
            'date': current_date,
            'time': current_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheety_response = requests.post(url = sheety_endpoint, json = sheety_body, headers = sheety_header)
    sheety_data = sheety_response.json()
    # print(sheety_response.text)
    print(f"YOUR LOG: \nExercise: {exercise['name'].title()}\nDuration: {exercise['duration_min']} minutes\nCalories: {exercise['nf_calories']}\n")
