from twilio.rest import Client
import os

accountSID = 'AC655ae9465ff0091029df7814713ebfed'
authToken = '4057bc8293baeffdb27de178e9dd3128'
trialNum = '+14159513966'


class NotificationManager:

    def __init__(self):
        self.client = Client(accountSID, authToken)

    def send_text(self, arrive_city, arrive_iata, out_date, in_date, price, depart_city="London", depart_iata="LON"):
        msg = f"Low price alert! Only £{price} to fly from {depart_city}-{depart_iata} to {arrive_city}-{arrive_iata}" \
              f" from {out_date} to {in_date}"
        message = self.client.messages \
            .create(
            body=msg,
            from_=trialNum,
            to='+19294242480'
        )
        print(message.status)
