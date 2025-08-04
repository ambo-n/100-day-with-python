import requests,os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("SHEETY_BASE_URL")
class DataManager:

    def get(self):
        response = requests.get(url=BASE_URL) # type: ignore
        response.raise_for_status()
        return response
    
    def put(self,row_id,**kwargs):
        json_body ={
            "price":kwargs
        }
        response = requests.put(url=f"{BASE_URL}/{row_id}", json=json_body)
        response.raise_for_status()
        return response


