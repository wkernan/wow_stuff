import os
import requests

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send_simple_message(price, quantity):
        print(os.getenv("MAILGUN_API_KEY"))
        test = "$66"
        return requests.post(
  		"https://api.mailgun.net/v3/sandbox5cb2aa424c704ae18d344fff8dd0ac47.mailgun.org/messages",
            auth=("api", os.getenv('MAILGUN_API_KEY', 'MAILGUN_API_KEY')),
  		data={"from": "Mailgun Sandbox <postmaster@sandbox5cb2aa424c704ae18d344fff8dd0ac47.mailgun.org>",
                "to": "Bill Kernan <wkernan@gmail.com>",
                "subject": "Bismuth Rank 3 Price Alert",
                "text": f"Bismuth Rank 3 Price: {price} gold (Qty: {quantity}) - Below Threshold!"})