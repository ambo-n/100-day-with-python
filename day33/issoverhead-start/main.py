import requests
from datetime import datetime
import smtplib

MY_LAT = -31.950527 
MY_LONG = 115.860458
MY_EMAIL = "sth@mail.com"
PASSWORD = "STH"


def iss_is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5<=iss_latitude<=MY_LAT+5 and MY_LONG-5<=iss_longitude<= MY_LONG+5:
        return True

def is_dark():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now <= sunrise or time_now >= sunset:
        return True

if is_dark() and iss_is_close():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=MY_EMAIL,
                            msg="Subject:ISS\n\n Look up")



