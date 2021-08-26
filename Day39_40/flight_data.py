import requests, datetime as dt
from pprint import pprint


class FlightData:

    # https://tequila.kiwi.com/portal/docs/tequila_api/search_api

    def __init__(self):
        self.price = 0
        self.depart_airport_code = "ROC"
        self.depart_city = "Rochester"
        self.date_from = (dt.datetime.now() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
        self.date_to = (dt.datetime.now() + dt.timedelta(days=181)).strftime("%d/%m/%Y")

    def get_flight_data(self, iataCode):
        kiwi_APIKEY = '0W9Qto_T826kcQlmFVNjR__0511cpU9x'
        kiwi_search_endpoint = 'https://tequila-api.kiwi.com/v2/search'
        headers = {
            'apikey': kiwi_APIKEY
        }
        parameters = {
            'fly_from': self.depart_airport_code,
            'fly_to': iataCode,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'flight_type': 'round',
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'curr':'USD'
        }
        response = requests.get(url=kiwi_search_endpoint, params=parameters, headers=headers)
        price, arrive_city, arrive_iata = response.json()['data'][0]['price'], response.json()['data'][0]['cityTo'], \
                                          response.json()['data'][0]['cityCodeTo']
        out_date, in_date = response.json()['data'][0]['utc_departure'].split('T')[0], \
                            response.json()['data'][0]['utc_arrival'].split('T')[0]
        print(price, arrive_city, arrive_iata, out_date, in_date)
        return price, arrive_city, arrive_iata, out_date, in_date
