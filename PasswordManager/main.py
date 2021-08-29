from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
DEFAULT_EMAIL = 'abc@gmail.com'

# ------------------------------- PASSWORD GENERATOR ------------------------------------ #

def password_generator():
    """Generates a password of random number of random characters and automatically copies it to clipbaord."""

    password_list = []

    # Random number of random letters, symbols and numbers
    password_list_letters = [choice(letters) for char in range(randint(8, 10))]
    password_list_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_list_numbers = [choice(numbers) for char in range(randint(2, 4))]
    
    password_list = password_list_letters + password_list_numbers + password_list_symbols

    # Shuffles all characters
    shuffle(password_list)

    # List to string
    password = "".join(password_list)

    password_input.insert(0, password)
    # Copies to clipboard
    pyperclip.copy(password)

# ------------------------------------ SAVE PASSWORD ------------------------------------------- #

def save():
    """Writes to data file once Add button has been clicked"""
    
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    # Dictionary of data entry in json format
    data_entry = {
        website: {
            "email": email,
            "password": password
        }
    }

    # Warning fields empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title = "Warning", message = "Some fields are still empty!")   
    else:
        try:
            # If file exists  
            # Read data from file and update with existing data                         
            with open('data.json', mode = 'r') as datafile:
                data = json.load(datafile)
                data.update(data_entry)
        except FileNotFoundError:
            # Create and write new data into file
            with open('data.json', mode = 'w') as datafile:
                json.dump(data_entry, datafile, indent = 4)      
        else:
            # Write updated data               
            with open('data.json', mode = 'w') as datafile:
                json.dump(data, datafile, indent = 4)  
        finally:
            # Clear entries as soon as add button clicked
            website_input.delete(0, END)
            password_input.delete(0, END)

#---------------------------------SEARCH FOR PRE-EXISTING ENTRY---------------------------------#

def search():
    """Searches if data for website entered already exists. If exists displays password and email."""
    website = website_input.get()
    
    try:
        with open('data.json', 'r') as datafile:
            data = json.load(datafile)
    # If json file doesnt exist
    except FileNotFoundError:
        print("Data file not found")
    else:
        # Display email and password in a message box 
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message = f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showwarning(title = "Error", message = f"Data for {website} not found")

# -------------------------------------- UI SETUP ---------------------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = Canvas(width = 200, height = 200)
mypass_image = PhotoImage(file = 'logo.png')
canvas.create_image(100, 100, image = mypass_image )
canvas.grid(row = 0, column = 1)

# Website label
website_label = Label(text = "Website:")
website_label.grid(row = 1, column = 0)
website_label.config(padx = 2, pady = 2)

# Email label
email_label = Label(text = "Email/Username:")
email_label.grid(row = 2, column = 0)
email_label.config(padx = 2, pady = 2)

# Password label
password_label = Label(text = "Password:")
password_label.grid(row = 3, column = 0)
password_label.config(padx = 2, pady = 2)

# Website input
website_input = Entry(width = 35)
website_input.grid(row = 1, column = 1, columnspan = 2)
# Blinking cursor in the box
website_input.focus()

# Email input
email_input = Entry(width = 35)
email_input.grid(row = 2, column = 1, columnspan = 2)
# Input pre-populated with most used email
email_input.insert(0, DEFAULT_EMAIL)

# Password input
password_input = Entry(width = 35)
password_input.grid(row = 3, column = 1,columnspan = 2)

# Generate password button
password_button = Button(text = "Generate Password", command = password_generator)
password_button.grid(row = 3, column = 2, columnspan = 1)

# Add button
add_button = Button(text = "Add", width = 30, command = save)
add_button.grid(row = 4, column = 1, columnspan = 2)
add_button.config(padx = 2, pady = 2)

# Search button
search_button = Button(text = "Search", command = search)
search_button.grid(row = 1, column = 2, columnspan = 1)
search_button.config(padx = 32)

window.mainloop()
