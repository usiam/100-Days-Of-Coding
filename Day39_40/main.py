from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

dataManager = DataManager()
sheet_data = dataManager.get_destination_data()  # fills with google sheets data here

for destination in sheet_data:
    if destination['iataCode'] == '':
        flightSearch = FlightSearch()
        iataCode = flightSearch.getIATA(destination['city'])
        dataManager.put_IATA_code(destination['id'], iataCode)
        sheet_data = dataManager.get_destination_data()

for destination in sheet_data:
    flightData = FlightData()
    price, arrive_city, arrive_iata, out_date, in_date = flightData.get_flight_data(destination['iataCode'])
    print(f"{destination['city']}: ${price}")
    if price < destination['lowestPrice']:
        notify = NotificationManager()
        notify.send_text(arrive_city=arrive_city, arrive_iata=arrive_iata, out_date=out_date, in_date=in_date,
                         price=price)
