from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
load_dotenv()
db_uri = os.getenv("DB_URI")
engine = create_engine(db_uri)

try: 
    with engine.connect() as connection:
        result = connection.execute(text("SELECT NOW()"))
        print("Database connection successful",result.fetchone())
except Exception as e:
    print("error de conexion", e)
