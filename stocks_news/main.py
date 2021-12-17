import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = "983a0ef3be454413a8b047f079d93d53"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_VANTAGE_API_ENDPOINT = "https://www.alphavantage.co/query"
ALPHA_VANTAGE_API_KEY = "U8O8I0R6FGCX2V86"
account_sid = "AC1f213138843cb4f37b76972bc091a0ac"
auth_token = "131576ae3cf4c1c2bb924daf3b741ac4"
ALPHA_VANTAGE_API_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY
}

response = requests.get(url=ALPHA_VANTAGE_API_ENDPOINT, params=ALPHA_VANTAGE_API_PARAMS)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = '🔺'
else:
    up_down = '🔻'
diff_percent = round((difference / float(yesterday_closing_price))*100)
if abs(diff_percent) > 5:
    NEWS_API_PARAMS = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(url=NEWS_API_ENDPOINT, params=NEWS_API_PARAMS)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief:{article['description']}" for article in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+13156591922',
            to='+84849396669'
        )
        print(message.status)
