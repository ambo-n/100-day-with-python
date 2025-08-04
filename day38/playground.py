import os
from dotenv import load_dotenv
load_dotenv()

SHEETY_USERNAME=os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD=os.getenv("SHEETY_PASSWORD")

print(SHEETY_USERNAME)
print(SHEETY_PASSWORD)