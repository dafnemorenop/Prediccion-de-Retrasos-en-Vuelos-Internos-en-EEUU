import streamlit as st
from modules.create_sidebar import create_sidebar

# Configuraciones globales de la app, como el título y la configuración de la página
# Configuración de la página, incluyendo el favicon
st.set_page_config(
    page_title="Análisis de Puntualidad en Aeropuertos",  # Título de la pestaña del navegador
    page_icon="✈️",  # Emoji de avión como favicon
    layout="wide"  # Opcional: Configura el layout de la página a "wide"
)
# Puedes llamar aquí a cualquier configuración global adicional si es necesario

# Llama a la función de la barra lateral que crea el menú
create_sidebar()
