from blizzard_client import BlizzardClient
from twilio_client import TwilioClient

PRICE_THRESHOLD = 1000  # 1000 gold


# Main Function
def main():
    print("Fetching Blizzard OAuth token...")
    client = BlizzardClient()
    commodities_data = client.fetch_commodities_data()

    if commodities_data:
        print("\n=== Auction House Prices ===")
        for auction in commodities_data.get("auctions", []):
            if auction["item"]["id"] == 210932:
                price = (
                    auction.get("unit_price", auction.get("buyout", 0)) / 10000
                )  # Convert to gold
                quantity = auction["quantity"]
                if price < PRICE_THRESHOLD:
                    TwilioClient().send_sms_alert(price, quantity)
                print(f"Bismuth Rank 3 Price: {price} gold (Qty: {quantity})")
                return

        print("Bismuth not found in the Auction House.")


if __name__ == "__main__":
    main()
