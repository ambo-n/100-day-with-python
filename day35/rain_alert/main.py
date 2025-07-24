import requests, os
from twilio .rest import Client



OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("API_KEY")

account_sid = os.environ.get("ACCOUNT_ID")
auth_token = os.environ.get("AUTH_TOKEN")


paramaters ={
    "lat":10.440077,
    "lon":107.163086,
    "cnt":4,
    "appid": API_KEY
}

response = requests.get(url=OWM_ENDPOINT,params=paramaters)
response.raise_for_status()
weather_data = response.json()
weather_list = weather_data['list']

will_rain = False
weather_ids = [element['weather'][0]['id'] for element in weather_list]

for weather_id in weather_ids:
    if weather_id < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="twilio_phone_number",
        to="your_phone_number",
    )

print(message.status)
