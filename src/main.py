from src.weather_api import get_coordinates, get_current_weather
from src.weather_utils import get_weather_description


def main():
    city = input("Enter city name: ")

    coordinates = get_coordinates(city)

    if coordinates is None:
        return

    latitude, longitude = coordinates

    weather = get_current_weather(latitude, longitude)
    weather_description = get_weather_description(weather["weather_code"])

    if weather is None:
        return

    print("\nCurrent Weather")
    print("-" * 30)
    print(f"Temperature      : {weather['temperature_2m']} °C")
    print(f"Feels Like       : {weather['apparent_temperature']} °C")
    print(f"Humidity         : {weather['relative_humidity_2m']} %")
    print(f"Wind Speed       : {weather['wind_speed_10m']} km/h")
    print(f"Weather          : {weather_description}")


if __name__ == "__main__":
    main()