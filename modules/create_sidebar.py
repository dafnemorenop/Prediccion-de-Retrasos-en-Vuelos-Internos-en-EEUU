# modules/create_sidebar.py
import streamlit as st
from streamlit_option_menu import option_menu
from paginas import inicio, eda, vuelos, modelo, sobre_nosotros, sobre_proyecto

def create_sidebar():
    # Añadir texto personalizado en el sidebar con markdown y HTML
    st.sidebar.markdown(
        f'<div style="text-align: center; font-size: 18px; margin-bottom: 30px;">'
        f'Proyecto realizado por<br>'
        f'José Núñez, Rubén Maestre, Dafne Moreno y Nahuel Núñez'
        f'</div>',
        unsafe_allow_html=True
    )

    # Crear el menú de opciones en el sidebar con option_menu
    with st.sidebar:
        selected = option_menu("Menú del proyecto", ["Inicio", "EDA", "Vuelos en USA", "Modelo machine learning", "Sobre el proyecto", "Sobre nosotros"],
            icons=["house", "bar-chart-line", "airplane", "cpu", "book", "people"],
            menu_icon="cast", default_index=0, orientation="vertical")

    # Llama a la función de la página correspondiente en función de la selección
    if selected == "Inicio":
        inicio.display()
    elif selected == "EDA":
        eda.display()
    elif selected == "Vuelos en USA":
        vuelos.display()
    elif selected == "Modelo machine learning":
        modelo.display()
    elif selected == "Sobre el proyecto":
        sobre_proyecto.display()
    elif selected == "Sobre nosotros":
        sobre_nosotros.display()

