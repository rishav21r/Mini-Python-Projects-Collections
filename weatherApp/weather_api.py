import requests

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
        return None
