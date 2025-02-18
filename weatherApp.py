# Weather App
import requests

def get_weather(city):
    api_key = "your_api_key"  # Replace with a valid API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': api_key}

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if response.status_code == 200:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        return f"Weather in {city}: {temperature}°C, {description.capitalize()}."
    else:
        return f"Error: Unable to fetch weather data for {city}."

# Example usage
city_name = input("Enter city name: ")
weather_info = get_weather(city_name)
print(weather_info)