def display_weather(data):
    """
    Format the weather information from the fetched data.
    """
    if data:
        city = data['name']
        temp = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        weather_info = (
            f"Weather in {city}:\n"
            f"Temperature: {temp}°C\n"
            f"Weather: {weather_description}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
        return weather_info
    else:
        return "Error: Could not fetch weather data."
