### Run in repl.it and share console with users.
# Link: https://replit.com/@kritij19/UserRegistration?outputonly=1&embed=1#main.py

import requests

print("Welcome to THE FLY HIGH club!\n")
print("At this club notify you about the best flight deals.")
print("Please enter the following details to sign up.")
details_incomplete = True

while details_incomplete:

    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email ID: ")
    confirmation_email = input("Re-enter Email ID: ")
    
    # User has to re-enter if details do not match 
    if email != confirmation_email:
        print(
            "The email IDs do not match. Please re-enter the details below: \n"
        )
    else:
        print("Congratulations! You are now a member")
        details_incomplete = False

sheety_endpoint = ######
sheety_header = {'Content-Type': "application/json"}
# User in in singular. Sheety expects singular sheet name in body
body = {
    'user': {
        'firstName': first_name,  # No spaces second word capitalized
        'lastName': last_name,
        'email': email
    }
}

response = requests.post(url=sheety_endpoint, json=body, headers=sheety_header)
