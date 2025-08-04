from dotenv import load_dotenv
import requests, os
from datetime import datetime

class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date) -> None:
        """
        Constructor for initalising a new flight data instance with specific travel details.

        Parameters:
        - price: The cost of the flight
        - origin_airport: The IATA code for the flight's origin airport
        - destination_airport: The IATA code for the flight's destination airport.
        - out_date: The departure date for the flight
        - return_date: The return date for the flight
        """
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

def find_cheapest_flight(data): # type: ignore
    """
    Parses flight data received from the Amadues API to identify the cheapest flight
    option among multiple entries.

    Args:
        data (dict): The JSON data containing flight information returned by the API.
    
    Returns:
        FlightData: An instance of the FlightData class representing the cheapest flight found,
        or a FlightData instance where all fields are 'NA' if no valid flight data is available.

    This function initally checks if the data contains valid flight entries. If no valid data is found,
    it returns a FlightData object containing "N/A" for all fields. Otherwise, it starts by assumming the first
    flight in the list is the cheapest. It then iterates through all available flights in the data, updating
    the cheapest flight details whenever a lower-priced flight is encountered. The result is a populated
    FlightData object with the details of the most affordable flight.
    """
    if data is None or not data['data']: # type: ignore
        print("No flight data")
        return FlightData("N/A","N/A","N/A","N/A","N/A")
    
    first_flight = data['data'][0] # type: ignore
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight['itineraries'][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight['itineraries'][0]["segments"][0]["arrival"]["iataCode"]
    out_date= first_flight['itineraries'][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date= first_flight['itineraries'][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(lowest_price, origin, destination,out_date,return_date)

    for flight in data['data']: # type: ignore
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight['itineraries'][0]["segments"][0]["departure"]["iataCode"]
            destination = flight['itineraries'][0]["segments"][0]["arrival"]["iataCode"]
            out_date= flight['itineraries'][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date= flight['itineraries'][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination,out_date,return_date)
            print(f"Lowest price to {destination} is £{lowest_price}")

    return cheapest_flight


