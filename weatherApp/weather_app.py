import requests

# Define your OpenWeatherMap API key
API_KEY = '6814838dda1e5b8b1cdd326a53f15d2b'

def fetch_weather(city):
    """
    Fetch weather data from OpenWeatherMap API for the given city.
    """
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def display_weather(data):
    """
    Display the weather information from the fetched data.
    """
    if data:
        city = data['name']
        temp = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Weather: {weather_description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("No data to display.")

def main():
    """
    Main function to run the weather app.
    """
    city = input("Enter city name: ")
    weather_data = fetch_weather(city)
    display_weather(weather_data)

if __name__ == '__main__':
    main()
