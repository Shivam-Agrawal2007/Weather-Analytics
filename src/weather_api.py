import requests

def get_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: API returned status code {response.status_code}")
            return None

        data = response.json()

        if "results" not in data:
            print("City not found.")
            return None

        latitude = data["results"][0]["latitude"]
        longitude = data["results"][0]["longitude"]

        return latitude, longitude

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None
    
def get_current_weather(latitude, longitude):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m,"
        f"apparent_temperature,wind_speed_10m,weather_code"
    )

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: API returned status code {response.status_code}")
            return None

        data = response.json()

        return data["current"]

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None