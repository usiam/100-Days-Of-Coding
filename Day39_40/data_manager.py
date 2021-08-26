import requests

sheetly_endpoint = 'https://api.sheety.co/a96437876dce61755e1ca0bf709aa1fb/flightDeals/prices'


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheetly_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def put_IATA_code(self, id, iataCode):
        data = {
            'price': {
                'iataCode': iataCode
            }
        }
        sheet_input = requests.put(url=f"{sheetly_endpoint}/{id}", json=data)
