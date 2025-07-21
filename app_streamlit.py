import streamlit as st
import pandas as pd
from sqlalchemy import create_engine


# conexion a la base de datos
engine = create_engine('postgresql://admin:admin123@localhost:5432/weatherdb')

#visualizacion de datos
st.title("🌦️ Visualización de Datos del Clima")

@st.cache_data
def cargar_datos():
    query = "SELECT * FROM weather_log"
    df = pd.read_sql(query, engine)
    return df

df= cargar_datos()

#mostrar la tabla
st.subheader("Tabla de Datos del Clima")
st.dataframe(df)

#Filtros por ciudad
ciudades= df['ciudad'].unique()
ciudad= st.selectbox("Selecciona una ciudad: ", ciudades)

#mostrar data
df_ciudad= df[df["ciudad"]== ciudad]
st.line_chart(df_ciudad.set_index('timestamp')[['temperatura', 'humedad', 'presion']])