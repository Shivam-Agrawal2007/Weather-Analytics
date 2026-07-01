import os
import csv
from datetime import datetime


FILE_PATH = "data/weather_history.csv"


def save_weather(city, weather):
    file_exists = os.path.isfile(FILE_PATH)

    with open(FILE_PATH, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date",
                "Time",
                "City",
                "Temperature",
                "Feels Like",
                "Humidity",
                "Wind Speed",
                "Weather"
            ])

        now = datetime.now()

        writer.writerow([
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S"),
            city,
            weather["temperature_2m"],
            weather["apparent_temperature"],
            weather["relative_humidity_2m"],
            weather["wind_speed_10m"],
            weather["description"]
        ])