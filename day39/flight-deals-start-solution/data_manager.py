import requests, os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()


class DataManager:
    def __init__(self) -> None:
        self._user = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._authorisation = HTTPBasicAuth(self._user, self._password) # type: ignore
        self.price_endpoint = os.getenv("SHEETY_BASE_URL")
        self.user_endpoint = os.getenv("SHEET_USER_URL")
        self.destination_data={}
        self.customer_data ={}

    def get_destination_data(self):
        response=requests.get(url=self.price_endpoint,auth=self._authorisation) # type: ignore
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_code(self,row_id, **kwargs):
        body = {
            "price": kwargs
        }
        response=requests.put(url=f"{self.price_endpoint}/{row_id}", json=body, auth=self._authorisation)
        response.raise_for_status()
        print(response.text)
        
    def get_customer_emails(self):
        response = requests.get(url=self.user_endpoint, auth=self._authorisation) # type: ignore
        data = response.json()
        self.customer_data=data["users"]
        return self.customer_data

