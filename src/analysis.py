import pandas as pd

FILE_PATH = "data/weather_history.csv"


def load_history():
    """
    Load weather history from CSV.

    Returns:
        DataFrame or None
    """
    try:
        df = pd.read_csv(FILE_PATH)
        return df
    except FileNotFoundError:
        print("No weather history found.")
        return None


def total_records(df):
    return len(df)


def average_temperature(df):
    return round(df["Temperature"].mean(), 2)


def maximum_temperature(df):
    return round(df["Temperature"].max(), 2)


def minimum_temperature(df):
    return round(df["Temperature"].min(), 2)


def average_humidity(df):
    return round(df["Humidity"].mean(), 2)


def average_wind_speed(df):
    return round(df["Wind Speed"].mean(), 2)


def maximum_wind_speed(df):
    return round(df["Wind Speed"].max(), 2)


def most_common_weather(df):
    return df["Weather"].mode()[0]


def most_searched_city(df):
    return df["City"].mode()[0]


def city_statistics(df, city):
    city_df = df[df["City"].str.lower() == city.lower()]

    if city_df.empty:
        print("No records found.")
        return None

    stats = {
        "City": city,
        "Total Records": len(city_df),
        "Average Temperature": round(city_df["Temperature"].mean(), 2),
        "Maximum Temperature": round(city_df["Temperature"].max(), 2),
        "Minimum Temperature": round(city_df["Temperature"].min(), 2),
        "Average Humidity": round(city_df["Humidity"].mean(), 2),
        "Average Wind Speed": round(city_df["Wind Speed"].mean(), 2),
        "Most Common Weather": city_df["Weather"].mode()[0]
    }

    return stats


def weather_frequency(df):
    return df["Weather"].value_counts()


def monthly_average_temperature(df):
    df["Date"] = pd.to_datetime(df["Date"])
    return (
        df.groupby(df["Date"].dt.to_period("M"))["Temperature"]
        .mean()
        .round(2)
    )


def daily_average_temperature(df):
    df["Date"] = pd.to_datetime(df["Date"])
    return (
        df.groupby(df["Date"].dt.date)["Temperature"]
        .mean()
        .round(2)
    )


def summary_report():
    df = load_history()

    if df is None:
        return

    print("\n========== WEATHER ANALYTICS ==========\n")

    print(f"Total Records          : {total_records(df)}")
    print(f"Average Temperature    : {average_temperature(df)} °C")
    print(f"Maximum Temperature    : {maximum_temperature(df)} °C")
    print(f"Minimum Temperature    : {minimum_temperature(df)} °C")
    print(f"Average Humidity       : {average_humidity(df)} %")
    print(f"Average Wind Speed     : {average_wind_speed(df)} km/h")
    print(f"Maximum Wind Speed     : {maximum_wind_speed(df)} km/h")
    print(f"Most Common Weather    : {most_common_weather(df)}")
    print(f"Most Searched City     : {most_searched_city(df)}")


def search_city(city):
    df = load_history()

    if df is None:
        return

    city_df = df[df["City"].str.lower() == city.lower()]

    if city_df.empty:
        print("\nNo records found for this city.")
        return

    print(f"\n========== WEATHER HISTORY : {city.title()} ==========\n")

    print(city_df.to_string(index=False))


def compare_cities(city1, city2):
    df = load_history()

    if df is None:
        return

    city1_df = df[df["City"].str.lower() == city1.lower()]
    city2_df = df[df["City"].str.lower() == city2.lower()]

    if city1_df.empty:
        print(f"\nNo records found for {city1}.")
        return

    if city2_df.empty:
        print(f"\nNo records found for {city2}.")
        return

    print("\n========== CITY COMPARISON ==========\n")

    print(f"{city1.title()}")
    print("-" * 30)
    print(f"Records             : {len(city1_df)}")
    print(f"Average Temperature : {city1_df['Temperature'].mean():.2f} °C")
    print(f"Maximum Temperature : {city1_df['Temperature'].max():.2f} °C")
    print(f"Minimum Temperature : {city1_df['Temperature'].min():.2f} °C")
    print(f"Average Humidity    : {city1_df['Humidity'].mean():.2f} %")
    print(f"Average Wind Speed  : {city1_df['Wind Speed'].mean():.2f} km/h")
    print(f"Most Common Weather : {city1_df['Weather'].mode()[0]}")

    print("\n")

    print(f"{city2.title()}")
    print("-" * 30)
    print(f"Records             : {len(city2_df)}")
    print(f"Average Temperature : {city2_df['Temperature'].mean():.2f} °C")
    print(f"Maximum Temperature : {city2_df['Temperature'].max():.2f} °C")
    print(f"Minimum Temperature : {city2_df['Temperature'].min():.2f} °C")
    print(f"Average Humidity    : {city2_df['Humidity'].mean():.2f} %")
    print(f"Average Wind Speed  : {city2_df['Wind Speed'].mean():.2f} km/h")
    print(f"Most Common Weather : {city2_df['Weather'].mode()[0]}")


if __name__ == "__main__":
    summary_report()