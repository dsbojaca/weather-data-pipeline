import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
#from src.config import DB_URL

def save_to_db(data):
    
    engine = create_engine("postgresql://admin:admin123@localhost:5432/weatherdb")
    df= pd.DataFrame([data])
    print("Data a insertar en DB:")
    print(df)
    df.to_sql("weather_log",engine, if_exists="append", index=False)