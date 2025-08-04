import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()

class NotificationManager:
    def __init__(self) -> None:
        self.client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    
    def send_sms(self, message_body):
        message = self.client.messages.create(
                body=message_body,
                from_=os.getenv("TWILIO_PHONE_NUMBER"),
                to=os.getenv("MY_PHONE_NUMBER"), # type: ignore
        )
        print(message.sid)