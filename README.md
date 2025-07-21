# Weather Data Pipeline 🌦️

Este Proyecto Implementa un pipeline de Datos para recolectar, almacenar, analizar y visualizar informacion climatica en tiempo real de diferentes ciudades usando tecnologias de Python, PostgreSQL y Streamlit.
---

## 🚀 Funcionalidad general

1. **Recolección de datos**: Se obtienen datos en tiempo real de la API de OpenWeather.
2. **Almacenamiento**: Los datos se almacenan en una base de datos PostgreSQL alojada en un contenedor Docker.
3. **Análisis**: Se pueden leer los datos desde la base de datos para hacer análisis exploratorio.
4. **Visualización interactiva**: A través de una app en Streamlit que permite filtrar y graficar los datos por ciudad.

---

## 🧰 Tecnologías utilizadas

- Python 3.12
- Pandas
- SQLAlchemy
- Psycopg2
- Requests
- Schedule
- PostgreSQL (en Docker)
- Streamlit

---

## 📁 Estructura del proyecto

```bash
Pipeline_clima/
│
├── app/
│   ├── main.py             
│   ├── leer_datos.py       
│   ├── app_streamlit.py    
├── env_clima/              
├── .env                    
├── requirements.txt        
└── README.md             
```
---

## 📝 Scripts y su funcionalidad

### `main.py`
- Se ejecuta automáticamente con un scheduler.
- Toma datos de la API del clima y los inserta en la tabla `weather_log`.

### `leer_datos.py`
- Conecta a la base de datos y devuelve un DataFrame con los datos.
- Útil para análisis exploratorios con Pandas o visualizaciones en Jupyter.

### `app_streamlit.py`
- Visualización interactiva.
- Puedes elegir una ciudad y graficar su temperatura, humedad y presión a lo largo del tiempo.
- Accedes ejecutando:
  ```bash
  streamlit run app/app_streamlit.py
    ```

---

# 🐳 Uso de Docker para la base de datos

  Este proyecto utiliza PostgreSQL dentro de un contenedor Docker para almacenar los datos del clima. A continuación se describen los pasos para levantar y usar la base de datos con Docker.

### ✅ Requisitos

    Tener Docker instalado en tu máquina.

### 🚀 Levantar la base de datos

Ejecuta el siguiente comando para iniciar un contenedor con PostgreSQL:
```bash
docker run --name weather-postgres \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin123 \
  -e POSTGRES_DB=weatherdb \
  -p 5432:5432 \
  -d postgres
```

### 📦 Parámetros explicados

- `--name weather-postgres`: le da un nombre al contenedor.
- `-e POSTGRES_USER=admin`: define el usuario administrador.
- `-e POSTGRES_PASSWORD=admin123`: define la contraseña.
- `-e POSTGRES_DB=weatherdb`: crea automáticamente una base de datos con ese nombre.
- `-p 5432:5432`: expone el puerto de PostgreSQL para que puedas conectarte desde tu aplicación local.
- `-d postgres`: usa la última versión oficial de la imagen `postgres`.
---


# 🐛 Problemas comunes con entornos virtuales e instalaciones

Durante el desarrollo del proyecto, se presentaron algunos errores frecuentes relacionados con la instalación de dependencias, entornos virtuales y conexión con servicios. A continuación, se listan los más relevantes y sus soluciones.

---

## 1. `This environment is externally managed` al usar pip

Este error ocurre cuando se intenta instalar paquetes en una instalación de Python administrada por el sistema operativo, como suele pasar en distribuciones Linux.


#### ✅ Solución

Crear y activar un entorno virtual antes de instalar paquetes:

```bash
python3 -m venv env_clima
source env_clima/bin/activate
```
Despues ejecutar

```bash
pip install -r requirements.txt
```

## 2. `ModuleNotFoundError`: No module named 'streamlit' (u otro paquete)

Este error indica que estás tratando de usar un paquete que no está instalado en el entorno virtual actual.
✅ Solución

Asegúrate de haber activado el entorno virtual y luego instala el paquete faltante:

```bash
pip install streamlit
```

## 3.`Restricciones por PEP 668` y --break-system-packages

En algunos sistemas, instalar paquetes con pip directamente genera advertencias o errores debido a restricciones impuestas para proteger el entorno del sistema.
✅ Solución recomendada

Usar siempre entornos virtuales para evitar estos conflictos:

```bash
python3 -m venv env_clima
source env_clima/bin/activate
```

### ✅ Solución alternativa (no recomendada)

En casos donde no se puede usar entorno virtual, puedes forzar la instalación con:


```bash
pip install <paquete> --break-system-packages
```


