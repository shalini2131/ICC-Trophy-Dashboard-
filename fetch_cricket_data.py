import requests
import json

# Free Cricket API (Replace with actual API Key)
API_URL = "https://api.cricapi.com/v1/currentMatches?apikey=49ee9f9f-18b3-44e0-864a-ea9ea0325aad"

def fetch_match_data():
    response = requests.get(API_URL)
    data = response.json()

    with open("match_data.json", "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    fetch_match_data()
