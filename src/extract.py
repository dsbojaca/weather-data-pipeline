import requests
from src.config import API_KEY

def parse_weather_data(city='Bogota'):
    url =f"http:"
    response = requests.get(url)
    return response.json()

