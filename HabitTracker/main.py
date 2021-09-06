'''Habit tracker using Pixela API'''

import requests
from datetime import datetime

USERNAME = 'kritij19'
TOKEN = #######
GRAPH_NAME = 'Calorie Intake'
GRAPH_ID = #######

pixela_endpoint = 'https://pixe.la/v1/users'

pixela_params = {
    'token': TOKEN,   # Acts as a form of API key
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

######## Setting up the account
# response = requests.post(url = pixela_endpoint, json = pixela_params)
# print(response.text)

####### Create a new pixelation graph definition.
# Output: # https://pixe.la/v1/users/kritij19/graphs/dvcdfvfd434hj.html

# graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

# # Hidden not shown in the url entered
# graph_header = {
#     'X-USER-TOKEN': TOKEN
# }

# graph_config = {
#     'id': GRAPH_ID,
#     'name': GRAPH_NAME,
#     'unit': 'calory',
#     'type': 'int',
#     'color': 'ajisai'
# }

# graph_response = requests.post(url = graph_endpoint, json = graph_config, headers = graph_header)
# print(graph_response.text)

###### Posting a pixel

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_header = {
    'X-USER-TOKEN': TOKEN
}

current_date = datetime.now()

pixel_params = {

    'date': current_date.strftime("%Y%m%d"),
    'quantity': input("What was your calorie input today?")
}

pixel_response = requests.post(url = pixel_endpoint, json = pixel_params, headers = pixel_header)
print(pixel_response.text)

####### Updating a Pixel
# Once created comment the code and update

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210902"

# update_header = {
#     'X-USER-TOKEN': TOKEN
# }

# update_params = {
#        'quantity': '1500000' 
# }

# update_response = requests.put(url = update_endpoint, headers = update_header, json = update_params)
# print(update_response.text)

####### Similar to update we can delete
