import schedule
import time
from main import leer_ciudades, run_pipeline
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, "cities.txt")

def job():
    cities= leer_ciudades(path)
    run_pipeline(cities)

schedule.every(1).minute.do(job)

print("Sheduler is runing with job funcion every hour -----> CTL+C to Stop it")

while True:
    schedule.run_pending()
    time.sleep(1)