import unittest
from unittest.mock import patch
from weather_api import fetch_weather
from weather_display import display_weather

class TestWeatherFunctions(unittest.TestCase):

    @patch('weather_api.requests.get')
    def test_fetch_weather_success(self, mock_get):
        mock_response = {
            'name': 'London',
            'main': {'temp': 22.5, 'humidity': 44},
            'weather': [{'description': 'broken clouds'}],
            'wind': {'speed': 2.57}
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        city = 'London'
        result = fetch_weather(city)
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], 'London')
        self.assertEqual(result['main']['temp'], 22.5)
        self.assertEqual(result['weather'][0]['description'], 'broken clouds')
        self.assertEqual(result['main']['humidity'], 44)
        self.assertEqual(result['wind']['speed'], 2.57)

    @patch('weather_api.requests.get')
    def test_fetch_weather_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        city = 'InvalidCity'
        result = fetch_weather(city)
        self.assertIsNone(result)

    def test_display_weather_success(self):
        mock_data = {
            'name': 'London',
            'main': {'temp': 22.5, 'humidity': 44},
            'weather': [{'description': 'broken clouds'}],
            'wind': {'speed': 2.57}
        }
        expected_output = (
            "Weather in London:\n"
            "Temperature: 22.5°C\n"
            "Weather: broken clouds\n"
            "Humidity: 44%\n"
            "Wind Speed: 2.57 m/s"
        )
        result = display_weather(mock_data)
        self.assertEqual(result, expected_output)

    def test_display_weather_failure(self):
        result = display_weather(None)
        self.assertEqual(result, "Error: Could not fetch weather data.")

if __name__ == '__main__':
    unittest.main()
