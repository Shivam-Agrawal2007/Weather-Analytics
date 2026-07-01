def generate_alert(weather):

    alerts = []

    temperature = weather["temperature_2m"]
    humidity = weather["relative_humidity_2m"]
    wind = weather["wind_speed_10m"]
    condition = weather["description"]

    if temperature >= 40:
        alerts.append("🔥 Heatwave Alert: Stay hydrated and avoid direct sunlight.")

    elif temperature <= 5:
        alerts.append("🥶 Cold Weather Alert: Wear warm clothes.")

    if humidity >= 85:
        alerts.append("💧 High Humidity: It may feel hotter than the actual temperature.")

    if wind >= 30:
        alerts.append("🌪 Strong Wind Warning: Avoid unnecessary outdoor travel.")

    if "Rain" in condition:
        alerts.append("☔ Carry an umbrella.")

    if "Thunderstorm" in condition:
        alerts.append("⛈ Thunderstorm Warning: Stay indoors if possible.")

    if "Snow" in condition:
        alerts.append("❄ Snow Alert: Roads may become slippery.")

    if not alerts:
        alerts.append("✅ No weather alerts. Have a great day!")

    return alerts