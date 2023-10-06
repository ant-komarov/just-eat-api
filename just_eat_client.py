from typing import List

import requests

BASE_URL = "https://uk.api.just-eat.io/restaurants/bypostcode/"
POSTAL_CODE = "G31"  # Change postal code here


class JustEatClient:
    def __init__(self):
        self.base_url = BASE_URL

    def get_restaurants_by_postalcode(self, postcode: str) -> List[dict]:
        url = self.base_url + postcode
        headers = {
            "Content-Type": "application/json",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/117.0.0.0 Safari/537.36"
            )
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            restaurants = []

            for restaurant_data in data["Restaurants"]:
                restaurant = {
                    "Name": restaurant_data.get("Name"),
                    "Rating": restaurant_data.get("RatingStars"),
                    "Cuisines": [cuisine.get("Name") for cuisine in restaurant_data.get("Cuisines")]
                }
                restaurants.append(restaurant)

            return restaurants

        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to get results: {e}")


if __name__ == "__main__":
    client = JustEatClient()
    restaurants = client.get_restaurants_by_postalcode(POSTAL_CODE)
    print(restaurants)
