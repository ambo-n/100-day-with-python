#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from datetime import datetime, timedelta
from notification_manager import NotificationManager
from pprint import pprint


# ==================== Set up the Flight Search ====================
dm = DataManager()
flight_search = FlightSearch()
sheet_data = dm.get_destination_data()
notification_manager = NotificationManager()

ORIGIN_CITY_DATA = "LON"

# ==================== Retrieve Customer emails ====================
users_data = dm.get_customer_emails()
email_list =[row["whatIsYourEmail?"] for row in users_data]
# ==================== Update the Airport Codes in Google Sheet ====================
for row in sheet_data:
    if not row['iataCode']:
        iataCode = flight_search.get_destination_code(row['city'], row['countryCode'])
        dm.update_destination_code(row_id=row['id'],iataCode=iataCode)

# ==================== Search for Flights ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=180)
for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_DATA,
        destination_city_code=destination['iataCode'],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price} with {cheapest_flight.stops} stop")

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights....")
        stopover_flights = flight_search.check_flights(
            origin_city_code=ORIGIN_CITY_DATA,
            destination_city_code=destination['iataCode'],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight to {destination['city']}: £{cheapest_flight.price} with {cheapest_flight.stops} stop/s")
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        notification_manager.send_sms(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                          f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                          f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )
        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly direct "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly "\
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                      f"with {cheapest_flight.stops} stop(s) "\
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."
        notification_manager.send_emails(email_list=email_list, email_body=message)





