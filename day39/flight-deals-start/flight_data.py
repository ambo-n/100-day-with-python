from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch

NUMBER_OF_DAYS = 180

class FlightData:
    def __init__(self):
        self.data_manager = DataManager()
        self.flight_search = FlightSearch()
        self.cheap_deals =[]
    
    @property
    def date_list(self):
        start = datetime.now()
        return [(start+timedelta(days=x)).strftime("%Y-%m-%d") for x in range(NUMBER_OF_DAYS)]
    
    def update_iata_codes(self):
        rows = self.data_manager.get().json()["prices"]
        for row in rows:
            if not row['iataCode']:
                iataCode = self.flight_search.get_city_iata_code(
                    city=row['city'],
                    country=row['countryCode'])
                self.data_manager.put(row_id=row['id'],iataCode=iataCode)
        print("Iata step ran")
                
    def deals_available(self):
        rows = self.data_manager.get().json()["prices"]
        for row in rows:
            for date in self.date_list:
                offer = self.flight_search.get_flight_offers(row['iataCode'],date)
                deal_price = float(offer["data"][0]["price"]["total"])
                if deal_price <= row['lowestPrice']:
                    self.cheap_deals.append(offer)
                print("Working through the dates")
        return self.cheap_deals


