import requests
import os
import dotenv

dotenv.load_dotenv()
SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")
SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")


class DataManager:
    def __init__(self):
        self.headers = {"Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"}
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        data = response.json()

        self.destination_data = data["prices"]
        # pprint.pprint(data) print data in clearer format
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                headers=self.headers,
                json=new_data,
            )

    def update_destination_lowest_price(self, row_id, new_price):
        new_data = {"price": {"lowestPrice": new_price}}
        requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
            headers=self.headers,
            json=new_data,
        )

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=self.headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
