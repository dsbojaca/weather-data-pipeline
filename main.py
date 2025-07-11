from src.extract import get_weather_data
from src.transform import parse_weather
from src.load import save_to_db

def run_pipeline():
    raw= get_weather_data("Bogota")
    parsed= parse_weather(raw)
    save_to_db(parsed)


if __name__== "__main__":
    run_pipeline()