import os
from dotenv import load_dotenv
from twilio.rest import Client
import smtplib
load_dotenv()

class NotificationManager:
    def __init__(self) -> None:
        self.client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
        self.email = os.getenv("MY_EMAIL")
        self._app_password = os.getenv("EMAIL_APP_PASSWORD")
    
    def send_sms(self, message_body):
        message = self.client.messages.create(
                body=message_body,
                from_=os.getenv("TWILIO_PHONE_NUMBER"),
                to=os.getenv("MY_PHONE_NUMBER"), # type: ignore
        )
        print(message.sid)
    
    def send_emails(self,email_list, email_body):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email, # type: ignore
                             password=self._app_password) # type: ignore
            for email in email_list:
                connection.sendmail(
                    from_addr=self.email, # type: ignore
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight: \n\n{email_body}"
                )