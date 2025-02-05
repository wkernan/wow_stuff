import os
from twilio.rest import Client


class TwilioClient:
    def __init__(self):
        self.client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

    # Send SMS Alert via Twilio
    def send_sms_alert(self, price, quantity):

        message = f"⚡ Bismuth price alert! ⚡\nPrice: {price} gold\nQuantity: {quantity}\nAct fast!"

        self.client.messages.create(
            body=message,
            from_=os.getenv("TWILIO_PHONE_NUMBER"),
            to=os.getenv("MY_PHONE_NUMBER"),
        )

        print(f"SMS Alert Sent: {message}")
