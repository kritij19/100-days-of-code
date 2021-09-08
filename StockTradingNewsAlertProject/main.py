import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_API_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_API_KEY = ######
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/everything'
NEWS_API_KEY = #######
TWILIO_ACCOUNT_SID = #######
TWILIO_AUTH_TOKEN = #######
receivers_num = #######
threshold_percentage_change = 5
symbol = None

# Dates
current = dt.datetime.now()
current_date = current.date()
time_delta = dt.timedelta(days = 1)
yest_date = current_date - time_delta
dby_date = yest_date - time_delta    # day before yest


###### STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday it is considered significant.

stock_parameters= {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'TSLA',
    'outputsize': 'compact',
    'apikey': STOCK_API_KEY,
}

stock_response = requests.get(url = STOCK_API_ENDPOINT, params = stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

# Closing prices
yest_close = float(stock_data["Time Series (Daily)"][str(yest_date)]["4. close"])
dby_close = float(stock_data["Time Series (Daily)"][str(dby_date)]["4. close"])

percentage_change = (abs(yest_close - dby_close) / yest_close) * 100

def significant_change():
    global symbol
    if percentage_change >= threshold_percentage_change:
        if yest_close > dby_close:
            symbol = "🔺"
        else:
            symbol = "🔻"
        print("Get news!")
        return True
    else:
        print("No news")
        return False
    

####### STEP 2: Use https://newsapi.org
# Get the first 3 news pieces for the COMPANY_NAME. 

news_parameters = {
    'qInTitle': 'tesla',
    'sortBy': 'popularity',
    'pageSize': 3,
    'apiKey': NEWS_API_KEY
}

news_response = requests.get(url = NEWS_API_ENDPOINT, params = news_parameters)
news_response.raise_for_status()
news_data = news_response.json()

######## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

if significant_change():
   # Framing message
    message_body = f"{symbol} {round(percentage_change, 5)}%\n\n"
    for news in news_data['articles']:
        headline = news["title"]
        brief = news["description"]
        message_body += f"Headline: {headline}\nBrief: {brief}\n\n"
    
    # Sending msg
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
            .create(
                 body = message_body,
                 from_='+14694143615',
                 to = receivers_num
             )
    print(message.status)
