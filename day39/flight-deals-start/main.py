from flight_data import FlightData
from flight_search import FlightSearch

flight_data = FlightData()
flight_data.update_iata_codes()
deals = flight_data.deals_available()
print(deals)