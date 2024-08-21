import html

import requests


class Data:

    def __init__(self) -> None:
        self.url = "https://opentdb.com//api.php?amount=10&category=20&type=boolean"
        self.questions = []

    def get_data(self):
        """Sends a GET requests to Opentdb API and fetches data"""
        try:
            response = requests.get(self.url, timeout=5)

            if response.status_code == 200:
                data = response.json()
                if "results" in data:
                    self.questions = [
                        {**item, "question": html.unescape(item["question"])}
                        for item in data["results"]
                    ]
                else:
                    print("No 'results' found in the response.")
            else:
                print(f"Error requesting data: {response.status_code}")

        except requests.exceptions.Timeout:
            print("The request timed out.")
        except requests.exceptions.RequestException as e:
            print(f"An error occured: {e}")
