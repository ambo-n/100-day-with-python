import requests, os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("SHEETY_BASE_URL")

class DataManager:
    def __init__(self) -> None:
        self._user = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._authorisation = HTTPBasicAuth(self._user, self._password) # type: ignore
        self.destination_data={}

    def get_destination_data(self):
        response=requests.get(url=BASE_URL,auth=self._authorisation) # type: ignore
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_code(self,row_id, **kwargs):
        body = {
            "price": kwargs
        }
        response=requests.put(url=f"{BASE_URL}/{row_id}", json=body, auth=self._authorisation)
        response.raise_for_status()
        print(response.text)
        
