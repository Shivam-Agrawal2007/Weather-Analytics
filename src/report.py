from datetime import datetime
import os
from src.logger import log_info

from src.analysis import (
    load_history,
    total_records,
    average_temperature,
    maximum_temperature,
    minimum_temperature,
    average_humidity,
    average_wind_speed,
    maximum_wind_speed,
    most_common_weather,
    most_searched_city,
)


REPORT_FOLDER = "reports"
REPORT_FILE = os.path.join(REPORT_FOLDER, "weather_report.txt")


def generate_report():

    df = load_history()

    if df is None:
        return

    os.makedirs(REPORT_FOLDER, exist_ok=True)

    with open(REPORT_FILE, "w", encoding="utf-8") as file:

        file.write("=" * 50 + "\n")
        file.write("        WEATHER ANALYTICS REPORT\n")
        file.write("=" * 50 + "\n\n")

        file.write(
            f"Generated On : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n"
        )

        file.write(f"Total Records       : {total_records(df)}\n")
        file.write(f"Average Temperature : {average_temperature(df)} °C\n")
        file.write(f"Maximum Temperature : {maximum_temperature(df)} °C\n")
        file.write(f"Minimum Temperature : {minimum_temperature(df)} °C\n")
        file.write(f"Average Humidity    : {average_humidity(df)} %\n")
        file.write(f"Average Wind Speed  : {average_wind_speed(df)} km/h\n")
        file.write(f"Maximum Wind Speed  : {maximum_wind_speed(df)} km/h\n")
        file.write(f"Most Common Weather : {most_common_weather(df)}\n")
        file.write(f"Most Searched City  : {most_searched_city(df)}\n")

    print("\nReport generated successfully!")

    log_info("Weather report generated")
    print(f"Saved at : {REPORT_FILE}")