# https://random-word-api.herokuapp.com/word?length=5&lang=en
import requests


def fetch_word(length):
    url = f"https://random-word-api.herokuapp.com/word?length={length}&lang=en"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()[0]
    else:
        print(f"Failed to retrieve data. HTTP status code: {
              response.status_code}")
        return None
