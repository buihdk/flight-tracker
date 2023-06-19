import requests
import os
import dotenv

dotenv.load_dotenv()
SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # pprint(data) Print formatted data using pretty print
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)

    def update_destination_lowest_price(self, row_id, new_price):
        new_data = {"price": {"lowestPrice": new_price}}
        requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}", json=new_data)
