import requests
from twilio.rest import Client



# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
data = response.json()
print(data)
news_parameter = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "language": "en",
    "sortBy": "publishedAt",
}
news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameter)
news_data = news_response.json()
articles = news_data["articles"][:3]


times = data["Time Series (Daily)"]
dates_list = list(times.keys())
latest_day = dates_list[0]
previous_day = dates_list[1]

latest_day_price = float(times[latest_day]["4. close"])
previous_day_price = float(times[previous_day]["4. close"])

price_differnce = abs(latest_day_price - previous_day_price)
price_percentage = (price_differnce / previous_day_price) * 100


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if price_percentage >= 5:
    client = Client(account_sid, auth_token)
    for news in articles:
        ## STEP 3: Use https://www.twilio.com
        # Send a seperate message with the percentage change and each article's title and description to your phone number.
        message = client.messages.create(
            body=articles["title"]&articles["description"],
            from_="+18643516254",
            to="+2349037256466"
        )
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"No significant change. Price change: {price_percentage:.2f}%",
        from_="+18643516254",
        to="+2349037256466"
    )





#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

