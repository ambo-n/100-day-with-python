import requests, os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

GET_TOKEN_URL ="https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT ="https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_OFFER_ENDPOINT="https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    def __init__(self) -> None:
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()
    
    def _get_new_token(self):
        headers = {
            "Content-Type":"application/x-www-form-urlencoded"
        }
        data = {
            "grant_type":"client_credentials",
            "client_id":self._api_key,
            "client_secret":self._api_secret

        }
        response = requests.post(url=GET_TOKEN_URL, headers=headers, data=data)
        print(f"Your token expires in {response.json()["expires_in"]} seconds")
        return response.json()['access_token']

    def get_destination_code(self, city_name, country_code):
        """        
        Retrieves the IATA code for a specified city using Amadeus Location API.

        Parameters:
        city_name (str): The name of the city for which to find the IATA code.

        Returns:
        str: The IATA code of the first matching city if found; "N/A" if no match is found
        due to an IndexError, or "Not Found" if no match is found due to a KeyError.

        The function sends a GET request to the IATA_ENDPOINT with a query that specifies the city
        name and other parameters to refine the search (e.g. "max":"2","include":"AIRPORTS"). It then 
        attempts to extract the IATA code from the JSON response.

        - If the city is not found in the response data (i.e., the data array is empty, leading to
        an IndexError), it logs a message indicating that no airport code was found for the city and
        returns "N/A"
        """
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        query = {
            "countryCode": country_code,
            "keyword": city_name,
            "max":2
        }
        response = requests.get(url=IATA_ENDPOINT, params=query,headers=headers)
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}")
            return "Not Found"
        else:
            return code
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        """
        Searches for flight options between two cities on specified departure and return dated using
        the Amadues API.

        Parameters:
            origin_city_code(str): The IATA code of the departure city
            destination_code(str): The IATA code of the destination city
            from_time(datetime): The departure date
            to_time (datetime): The return date
        
        Returns:
            dict or None: A dictionary containing flight offer data if the query
            is successful; None if there is an error.
        
        The function contructs a query with the flight search paramters and sends a GET
        request to the API. It handles the response, checking the status code and parsing the JSON
        data if the request is successful. If the response status code is not 200, it logs an error
        message and provides a link to the API documentation for status code details.
        """
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        query = {
                "originLocationCode": origin_city_code,
                "destinationLocationCode": destination_city_code,
                "departureDate": from_time.strftime("%Y-%m-%d"),
                "returnDate": to_time.strftime("%Y-%m-%d"),
                "adults": 1,
                "nonStop": "true" if is_direct else "false",
                "currencyCode": "GBP",
                "max": "10",
            }
        response = requests.get(url=FLIGHT_OFFER_ENDPOINT, headers=headers, params=query)
        if response.status_code !=200:
            print(f"check_flight() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None
        return response.json()
    