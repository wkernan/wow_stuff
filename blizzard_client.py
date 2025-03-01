import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class BlizzardClient:
    def __init__(self):
        self.token = self._get_access_token()
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def _get_access_token(self):
        print(os.getenv("CLIENT_ID"))
        print(os.getenv("CLIENT_SECRET"))
        url = "https://oauth.battle.net/token"
        data = {"grant_type": "client_credentials"}
        auth = (os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))

        response = requests.post(url, data=data, auth=auth)
        return response.json().get("access_token")

    def get_realms(self):
        url = "https://us.api.blizzard.com/data/wow/realm/index"
        params = {"namespace": "dynamic-us"}

        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.json().get("realms", [])
        return []

    # Fetch Auction House Data
    def fetch_auction_data(self):
        url = "https://us.api.blizzard.com/data/wow/connected-realm/69/auctions"
        params = {"namespace": "dynamic-us"}
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print("Error fetching auction data:", response.status_code, response.text)
            return None

        # Fetch Auction House Data

    def fetch_commodities_data(self):
        url = "https://us.api.blizzard.com/data/wow/auctions/commodities"
        params = {"namespace": "dynamic-us"}
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(
                "Error fetching commodities data:", response.status_code, response.text
            )
            return None

    def get_item(self, item_id):
        url = f"https://us.api.blizzard.com/data/wow/item/{item_id}"
        params = {"namespace": "static-us"}

        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response.json()
        return "Unknown Item"
