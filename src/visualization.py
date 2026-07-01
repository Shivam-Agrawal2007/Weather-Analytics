import os
import pandas as pd
import matplotlib.pyplot as plt
from src.logger import log_info

DATA_FILE = "data/weather_history.csv"
CHART_DIR = "charts"

os.makedirs(CHART_DIR, exist_ok=True)


def load_data():
    try:
        df = pd.read_csv(DATA_FILE)
        df["Date"] = pd.to_datetime(df["Date"])
        return df
    except FileNotFoundError:
        print("No weather history found.")
        return None


def temperature_trend(df):
    plt.figure(figsize=(8, 5))

    plt.plot(df["Date"], df["Temperature"], marker="o")

    plt.title("Temperature Trend")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(f"{CHART_DIR}/temperature_trend.png")
    plt.close()


def humidity_trend(df):
    plt.figure(figsize=(8, 5))

    plt.plot(df["Date"], df["Humidity"], marker="o")

    plt.title("Humidity Trend")
    plt.xlabel("Date")
    plt.ylabel("Humidity (%)")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(f"{CHART_DIR}/humidity_trend.png")
    plt.close()


def weather_distribution(df):
    weather = df["Weather"].value_counts()

    plt.figure(figsize=(8, 5))

    plt.bar(weather.index, weather.values)

    plt.title("Weather Distribution")
    plt.xlabel("Weather")
    plt.ylabel("Count")

    plt.xticks(rotation=30)

    plt.tight_layout()
    plt.savefig(f"{CHART_DIR}/weather_distribution.png")
    plt.close()


def city_average_temperature(df):
    city = df.groupby("City")["Temperature"].mean()

    plt.figure(figsize=(8, 5))

    plt.bar(city.index, city.values)

    plt.title("Average Temperature by City")
    plt.xlabel("City")
    plt.ylabel("Temperature (°C)")

    plt.tight_layout()
    plt.savefig(f"{CHART_DIR}/city_temperature.png")
    plt.close()


def dashboard(df):

    fig, ax = plt.subplots(2, 2, figsize=(14, 10))

    ax[0, 0].plot(df["Date"], df["Temperature"])
    ax[0, 0].set_title("Temperature Trend")

    ax[0, 1].plot(df["Date"], df["Humidity"])
    ax[0, 1].set_title("Humidity Trend")

    weather = df["Weather"].value_counts()

    ax[1, 0].bar(weather.index, weather.values)
    ax[1, 0].set_title("Weather Distribution")

    city = df.groupby("City")["Temperature"].mean()

    ax[1, 1].bar(city.index, city.values)
    ax[1, 1].set_title("Average Temperature")

    plt.tight_layout()

    plt.savefig(f"{CHART_DIR}/dashboard.png")

    plt.close()


def generate_all_charts():

    df = load_data()

    if df is None:
        return

    temperature_trend(df)
    humidity_trend(df)
    weather_distribution(df)
    city_average_temperature(df)
    dashboard(df)

    print("\nCharts Generated Successfully!")
    log_info("Charts generated")