import requests, datetime

MY_LAT =-31.950527
MY_LNG=115.860458

parameters ={
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0,
    "tzid": "Australia/Perth"
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
print(datetime.datetime.now().hour)