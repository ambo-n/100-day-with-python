import requests,os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("AMADEUS_API_KEY")
API_SECRET = os.getenv("AMADEUS_API_SECRET")
ORIGINAL_LOCATION ="LON"
CITY_SEARCH_URL ="https://test.api.amadeus.com/v1//reference-data/locations/cities"
FLIGHT_OFFER_SEARCH_URL ="https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    def __init__(self):
        self.token =self.get_token()
        self.headers = {
        'Authorization': f'Bearer {self.token}'
        }
        
    def get_token(self):
        get_token_headers = {
            "Content-Type":"application/x-www-form-urlencoded"
        }
        data ={
            "grant_type":"client_credentials",
            "client_id":API_KEY,
            "client_secret": API_SECRET
        }
        response= requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=get_token_headers, data=data)
        response.raise_for_status()
        return response.json()['access_token']
    
    def get_city_iata_code(self, city, country):
        parameters = {
            "countryCode":country,
            "keyword":city,
            "max":5
        }
        response = requests.get(url=CITY_SEARCH_URL, headers=self.headers, params=parameters)
        response.raise_for_status()
        data = response.json()["data"]
        iata_code = data[0]["iataCode"]
        return iata_code
    
    def get_flight_offers(self,destination,departure_date):
        parameters ={
            "originLocationCode": ORIGINAL_LOCATION,
            "destinationLocationCode": destination,
            "departureDate": departure_date,
            "adults":1,
            "nonStop": "true",
            "max":1,
            "currencyCode": "GBP"
        }
        response = requests.get(url=FLIGHT_OFFER_SEARCH_URL, params=parameters, headers=self.headers)
        response.raise_for_status()
        return response.json()


