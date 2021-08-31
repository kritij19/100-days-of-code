import datetime as dt
import pandas as pd
import smtplib
import random

smtp_address = "smtp.gmail.com"     # for gmail
my_email = "hellotesting739@gmail.com" # Senders
pswd = "testing@123"
 # Receivers

letters_path_list = ['letter_templates\letter_1.txt', 'letter_templates\letter_2.txt', 'letter_templates\letter_3.txt'] 

# Today's date
current = dt.datetime.now()
current_date = current.date()

# Reading csv and converting df to nested list
birthday_data = pd.read_csv('birthdays.csv')
birthdays_list  = birthday_data.values.tolist()

for birthday in birthdays_list:
    # Making a date object for birthdays
    birthdate = dt.date(
        year = birthday[2],
        month = birthday[3],
        day = birthday[4])
    
    if current_date.day == birthdate.day and current_date.month == current_date.month:
        name = birthday[0]
        receivers_email = birthday[1]
        # Randomly choosing a birthday message
        chosen_letter_path = random.choice(letters_path_list)
        
        with open(chosen_letter_path) as letter:
            letter_content = letter.read()

        # Replacing placeholder with receiver's name
        letter_content = letter_content.replace("[NAME]", name)
        letter_content = letter_content.replace("Angela", "Kriti")

        # Sending the mail
        with smtplib.SMTP(smtp_address) as connection:
            connection.starttls()
            connection.login(user = my_email, password = pswd)
            connection.sendmail(
                from_addr = my_email,
                to_addrs = receivers_email,
                msg = f"subject: HAPPY BIRTHDAY!\n\n{letter_content}")

