import requests
from pprint import pprint

kiwi_APIKEY = '0W9Qto_T826kcQlmFVNjR__0511cpU9x'
kiwi_endpoint = 'https://tequila-api.kiwi.com/locations'


class FlightSearch:

    def getIATA(self, city):
        headers = {
            'apikey': kiwi_APIKEY
        }
        query = {
            'term': city,
            'locale': 'en-US',
            'location_types': 'city',
            'limit': 1,
            'active_only': True,

        }
        response = requests.get(url=f"{kiwi_endpoint}/query", params=query, headers=headers)
        iataCode = response.json()['locations'][0]['code']
        return iataCode
