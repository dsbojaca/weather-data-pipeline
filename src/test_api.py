import requests
import os 
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

url= f"https://api.openweathermap.org/data/2.5/weather?q=Bogota&appid={API_KEY}&units=metric&lang=es"
res =requests.get(url)

print("Codigo fr respuesta: ", res.status_code)
print(res.json())


