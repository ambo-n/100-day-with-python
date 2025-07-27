import requests
from datetime import datetime

USERNAME = "ambon"
YOUR_T = "sth"

pixela_endpoint ="https://pixe.la/v1/users"
user_params ={
    "token": YOUR_T,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id":"graph1",
    "name": "Physio Exercise Graph",
    "unit": "rep",
    "type": "int",
    "color":"shibafu"
}

headers ={
    "X-USER-TOKEN": YOUR_T
}

today = datetime(year=2025,month=7,day=26)
formatted_day =today.strftime("%Y%m%d")

pixel_endpoint = f"{pixela_endpoint}/ambon/graphs/graph1"
pixel_config ={
    "date": formatted_day,
    "quantity": "10",
}


response = requests.delete(url=f"{pixel_endpoint}/{formatted_day}", headers= headers)
print(response.text)