import requests


def get_forecast(latitude, longitude):
    """
    Fetch 7-day weather forecast.
    """

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        f"&daily=temperature_2m_max,temperature_2m_min,"
        f"weather_code"
        f"&timezone=auto"
    )

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print("Unable to fetch forecast.")
            return None

        data = response.json()

        return data["daily"]

    except requests.exceptions.RequestException as e:
        print(e)
        return None