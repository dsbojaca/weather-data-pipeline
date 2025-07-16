from src.extract import parse_weather_data
from src.transform import parse_weather
from src.load import save_to_db

def run_pipeline(city):

    print(f"obteniendo datos de {city}...")
    raw= parse_weather_data(city)
    parsed= parse_weather(raw)
    save_to_db(parsed)


if __name__== "__main__":
    city = input("Ingrese la ciudad: ")
    run_pipeline(city)
