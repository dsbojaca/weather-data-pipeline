import requests
from src.config import API_KEY

def parse_weather_data(city):
    url =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=es"
    response = requests.get(url)
    return response.json()

