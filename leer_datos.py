import pandas as pd
from sqlalchemy import create_engine

#Cambia estos valores
usuario = 'admin'
contraseña = 'admin123'
host = 'localhost'
puerto = '5432'
base_de_datos = 'weatherdb'

#Conexion URL
url = f'postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{base_de_datos}'

#Crear el motor de conexion
engine= create_engine(url)

#Leer a tabla   
df= pd.read_sql_table("weather_log", con=engine)
print(df.head())