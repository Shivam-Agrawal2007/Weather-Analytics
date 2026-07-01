from src.weather_api import get_coordinates, get_current_weather
from src.weather_utils import get_weather_description
from src.storage import save_weather
from src.analysis import summary_report
from src.visualization import generate_all_charts
from src.analysis import (summary_report, search_city, compare_cities)
from src.report import generate_report
from src.forecast import get_forecast
from src.alerts import generate_alert
from src.logger import log_info


def current_weather():

    city = input("\nEnter city name: ")

    coordinates = get_coordinates(city)

    if coordinates is None:
        return

    latitude, longitude = coordinates

    weather = get_current_weather(latitude, longitude)

    if weather is None:
        return

    weather_description = get_weather_description(weather["weather_code"])
    weather["description"] = weather_description
    alerts = generate_alert(weather)

    save_weather(city, weather)
    log_info(f"Weather searched for {city}")

    print("\n========== CURRENT WEATHER ==========\n")

    print(f"City             : {city}")
    print(f"Temperature      : {weather['temperature_2m']} °C")
    print(f"Feels Like       : {weather['apparent_temperature']} °C")
    print(f"Humidity         : {weather['relative_humidity_2m']} %")
    print(f"Wind Speed       : {weather['wind_speed_10m']} km/h")
    print(f"Weather          : {weather_description}")
    print("\n========== ALERTS ==========\n")
    for alert in alerts:
        print(alert)


def weather_forecast():

    city = input("\nEnter city : ")

    coordinates = get_coordinates(city)

    if coordinates is None:
        return

    latitude, longitude = coordinates

    forecast = get_forecast(latitude, longitude)

    if forecast is None:
        return

    print("\n========== 7 DAY FORECAST ==========\n")

    for i in range(len(forecast["time"])):

        weather = get_weather_description(
            forecast["weather_code"][i]
        )

        print(f"Date        : {forecast['time'][i]}")
        print(f"Maximum Temp: {forecast['temperature_2m_max'][i]} °C")
        print(f"Minimum Temp: {forecast['temperature_2m_min'][i]} °C")
        print(f"Weather     : {weather}")
        print("-" * 35)
        
        log_info(f"Forecast generated for {city}")


def main():

    while True:

        print("\n==============================")
        print(" WEATHER ANALYTICS SYSTEM ")
        print("==============================")
        print("1. Current Weather")
        print("2. 7-day Forecast")
        print("3. View Analytics")
        print("4. Search City History")
        print("5. Compare Cities")
        print("6. Generate Charts")
        print("7. Generate Report")
        print("8. Exit")
        print("==============================")

        choice = input("Enter Choice : ")

        if choice == "1":
            current_weather()

        elif choice == "2":
            weather_forecast()

        elif choice == "3":
            summary_report()

        elif choice == "4":
            city = input("Enter city : ")
            search_city(city)

        elif choice == "5":
            city1 = input("First City : ")
            city2 = input("Second City : ")

            compare_cities(city1, city2)

        elif choice == "6":
            generate_all_charts()

        elif choice == "7":
            generate_report()

        elif choice == "8":
            break
        else:
            print("\nInvalid Choice!")


if __name__ == "__main__":
    main()