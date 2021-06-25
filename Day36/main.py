import requests, datetime, os
from twilio.rest import Client

# getting dates
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
dbf_yesterday = yesterday - datetime.timedelta(days=1)

# sms details
accountSID = os.environ.get('SID_VAR')
authToken = os.environ.get('AUTH_VAR')
trialNum = os.environ.get('TRIAL_NUM')

# Portfolio
STOCK_NAMES = ["TSLA", "AAPL"]
COMPANY_NAMES = ["Tesla", "Apple"]

# setting up stock api
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_KEY = os.environ.get('STOCK_KEY')
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = os.environ.get('NEWS_KEY')

for (STOCK_NAME, COMPANY_NAME) in zip(STOCK_NAMES, COMPANY_NAMES):
    stock_API_parameters = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK_NAME,
        'apikey': STOCK_KEY
    }

    news_API_parameters = {
        'q': COMPANY_NAME,
        'from': str(dbf_yesterday),
        'to': str(today),
        'sortBy': 'relevancy',
        'apikey': NEWS_KEY
    }

    stock_resp = requests.get(STOCK_ENDPOINT, params=stock_API_parameters)
    stock_resp.raise_for_status()

    stock_data = stock_resp.json()['Time Series (Daily)']

    spyc = stock_data[str(yesterday)]['4. close']  # stock price yesterday at close - spyc
    spyyc = stock_data[str(dbf_yesterday)][
        '4. close']  # stock price yesterday yesterday (i.e. day before yesterday) at close - spyyc
    diff = (float(spyc) - float(spyyc))
    percent_diff = round(diff / float(spyyc) * 100, 2)

    if abs(percent_diff) > 5:
        if percent_diff < 0:
            symb = '🔻'
        elif percent_diff > 0:
            symb = '🔺'
        news_resp = requests.get(NEWS_ENDPOINT, params=news_API_parameters)
        news_resp.raise_for_status()

        news_data = news_resp.json()
        top_three_articles = news_data['articles'][:3]
        x = [{'Headline': top_three_articles[i]['title'], 'Brief': top_three_articles[article]['description']} for
             article in top_three_articles]

        msg = f"\n{STOCK_NAME}: {symb}{abs(percent_diff)}%\n\n"
        for i in range(3):
            msg += f"Headline {i + 1}: {x[i]['Headline']}\nBrief: {x[i]['Brief']}\n\n"
        client = Client(accountSID, authToken)
        message = client.messages \
            .create(
            body=msg,
            from_=trialNum,
            to=os.environ.get('MY_NUM')
        )
        print(message.status)
