import smtplib
import requests


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.smtp_address = "smtp.gmail.com"
        self.senders_email = ####
        self.password = ####
        self.get_endpoint = #####
        

    def send_mail(self, subject: str, body: str):

        # Member sign up using replit
        

        # Getting all emails IDs from spreadsheet using sheety API
        get_response = requests.get(url = self.get_endpoint)
        email_data = get_response.json()

        # Sending mail to each member
        for user in email_data['users']:

            with smtplib.SMTP(self.smtp_address) as connection:
                # Encrypts to make it secure. Sets up Transfer Layer Security (TLS)
                connection.starttls()
                connection.login(user = self.senders_email, password = self.password)
                connection.sendmail(
                    from_addr = self.senders_email, 
                    to_addrs = user['email'], 
                    msg = f"subject: {subject} \n\n{body}"
                )
        
