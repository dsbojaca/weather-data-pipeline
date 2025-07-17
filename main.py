from src.extract import parse_weather_data
from src.transform import parse_weather
from src.load import save_to_db


def leer_ciudades(path="./env_clima/app/cities.txt"):
    with open(path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]
    
def run_pipeline(cities):
    for city in cities:
        try:
            print(f"obteniendo datos de {city}...")
            raw= parse_weather_data(city)
            parsed= parse_weather(raw)
            save_to_db(parsed)     
        except Exception as e:
            print(f"Error en el Pipeline: {e}")


if __name__== "__main__":
    cities= leer_ciudades()
    run_pipeline(cities)
