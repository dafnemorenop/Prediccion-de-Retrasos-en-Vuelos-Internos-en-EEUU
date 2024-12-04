import streamlit as st
from PIL import Image
import os
import sys
from streamlit_option_menu import option_menu
import base64

from paginas import web_scraping
from paginas import data_cleaning
from paginas import eda
from paginas import modeling


# Configuración inicial de la página
st.set_page_config(
    page_title="FlyPredict",
    page_icon=":airplane:",
    layout="wide",
    initial_sidebar_state="expanded",  # Aseguramos que la barra lateral esté expandida
)





def set_background(image_path):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}");
            background-size: cover;
            background-position: center;
            height: 100vh;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Función principal para la página "Main"
def main():





    # ruta relativa de la imagen
    image_path = 'images/nieve.jpg'  # cambia esto a la ruta de tu imagen
    set_background(image_path)



    
    st.markdown(
        """
        <style>
            .title-section h1 {
                color: #90caf9; /* Color azul claro */
                font-size: 3rem;
                font-weight: bold;
                text-align: center;
                margin-top: 30px;
            }
        </style>
        <div class="title-section">
            <h1>FlyPredict</h1>
        </div>
        """, unsafe_allow_html=True
    )
    st.write("")  


    st.markdown(
        """
        <h2 style="text-align: center">
            Predicción de Retrasos en Vuelos Internos en EEUU: Desarrollo de un Modelo Predictivo con Streamlit para la Visualización de Datos</h2>
        """,
        unsafe_allow_html=True
    )
    st.write("")  
    st.write("")  
    st.write("")  
    # Crear las columnas para los contenedores
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="container">
                <h3>Descripción</h3>
                <p style="text-align: justify">FlyPredict es una aplicación para la predicción de vuelos internos en EE.UU. para el mes de diciembre entre los años 2021 y 2023.</p>
                <p style="text-align: justify">Puedes visitar la página del Departamento de Estadísticas de Transporte de EE. UU., de donde se obtuvieron los datos para el estudio mediante web scraping, en el siguiente enlace:</p>
                <p>👉<a href="https://www.transtats.bts.gov/ONTIME/Departures.aspx" target="_blank">Departamento de Estadísticas de Transporte de EE. UU.</a></p>
            </div>
            """, 
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="container">
                <h3>Objetivo</h3>
                <p style="text-align: justify">Este proyecto se centró en desarrollar un modelo predictivo para estimar retrasos en vuelos internos en EE. UU., utilizando técnicas de análisis de datos y aprendizaje automático.</p>
                <p style="text-align: justify">Este estudio proporciona una visión sobre las causas, el rendimiento y los factores que influyen en la puntualidad aérea, presentando un modelo predictivo que permite anticipar la puntualidad de las aerolíneas y contribuir así a la mejora de la satisfacción de los pasajeros.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="container">
                <h3>Tecnologías</h3>
                <p style="text-align: justify">El proyecto fue desarrollado con herramientas tecnológicas que facilitaron el análisis eficiente de grandes volúmenes de datos y la visualización clara e interactiva de resultados, destacando patrones y tendencias relevantes.</p>
                <ul>
                    <li>Lenguaje de programación: Python</li>
                    <li>Bibliotecas para manipulación y análisis de datos: Pandas y Numpy</li>
                    <li>Visualización de datos: Plotly y Matplotlib</li>
                    <li>Modelado predictivo: Keras</li>
                </ul>
            </div>
            """, 
            unsafe_allow_html=True
        )



    # # Ruta del archivo GIF
    # image_path = os.path.join(os.path.dirname(__file__), 'images', 'gif_avion.gif')
    
    # # Leer el GIF y convertirlo a base64
    # with open(image_path, "rb") as gif_file:
    #     gif_data = gif_file.read()
    #     gif_base64 = base64.b64encode(gif_data).decode("utf-8")
    
    # # Mostrar el GIF usando HTML
    # gif_html = f"""
    # <img src="data:image/gif;base64,{gif_base64}" alt="gif animado" style="width:100%; height:auto;">
    # """
    # st.markdown(gif_html, unsafe_allow_html=True)


    # Ruta del archivo GIF
    image_path = os.path.join(os.path.dirname(__file__), 'images', 'gif_avion.gif')
    
    # Leer el GIF y convertirlo a base64
    with open(image_path, "rb") as gif_file:
        gif_data = gif_file.read()
        gif_base64 = base64.b64encode(gif_data).decode("utf-8")
    
    # Mostrar el GIF con tamaño reducido usando HTML
    gif_html = f"""
    <img src="data:image/gif;base64,{gif_base64}" alt="gif animado" style="width:50%; height:auto; display:block; margin:auto;">
    """
    st.markdown(gif_html, unsafe_allow_html=True)


# Función para crear la barra lateral personalizada con íconos
def create_sidebar():
    # CSS personalizado para mejorar la barra lateral y los botones
    st.markdown(
        """
        <style>
            /* Estilo para la barra lateral */
            .stSidebar {
                background-color: #212121; /* Fondo oscuro */
                color: white; /* Texto blanco */
                padding: 20px;
                font-size: 18px;
                font-family: "Arial", sans-serif;
            }

            /* Título de la barra lateral */
            .stSidebar h2 {
                color: #90caf9;
                text-align: center;
                font-size: 22px;
            }

            /* Estilo de los botones del menú */
            .stSidebar select {
                background-color: #90caf9;
                color: white;
                border: none;
                padding: 10px;
                font-size: 16px;
                width: 100%;
                border-radius: 8px;
                margin-bottom: 10px;
                cursor: pointer;
            }

            .stSidebar select:focus {
                background-color: #1976d2;
            }

            /* Estilo para los links en la barra lateral */
            .stSidebar a {
                color: white;
                text-decoration: none;
                font-size: 16px;
                display: block;
                padding: 8px;
                border-radius: 5px;
                margin: 5px 0;
            }

            .stSidebar a:hover {
                background-color: #1976d2;
            }
        </style>
        """, unsafe_allow_html=True
    )

    st.sidebar.markdown(
        f'<div style="text-align: center; font-size: 18px; margin-bottom: 30px;">'
        f'Proyecto realizado por<br>'
        f'Dafne Moreno Palomares'
        f'</div>',
        unsafe_allow_html=True
    )

    # Crear la barra lateral
def create_sidebar():
    st.sidebar.markdown(
        f'<div style="text-align: center; font-size: 18px; margin-bottom: 30px;">'
        f'Proyecto realizado por<br>'
        f'Dafne Moreno Palomares'
        f'</div>',
        unsafe_allow_html=True
    )

    with st.sidebar:
        selected = option_menu(
            "Menú",
            ["Inicio", "Web Scraping", "Limpieza", "EDA", "Modelo"],
            icons=["house", "globe", "trash", "bar-chart-line", "cpu"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical",
        )

    # Navegación de las páginas
    if selected == "Inicio":
        main()  # Llama a la función principal
    elif selected == "Web Scraping":
        web_scraping.display()
    elif selected == "Limpieza":
        data_cleaning.display()
    elif selected == "EDA":
        eda.display()
    elif selected == "Modelo":
        modeling.display()


    # Copos de nieve
st.markdown(
        """
        <style>
            .snowflakes {
                position: fixed;
                width: 100%;
                height: 100%;
                top: 0;
                left: 0;
                pointer-events: none;
                z-index: 1000; /* Siempre encima */
            }

            .snowflake {
                position: absolute;
                top: -10px;
                color: #fff; /* Color blanco */
                font-size: 1.5rem;
                user-select: none;
                animation: fall 8s linear infinite, sway 2s ease-in-out infinite;
            }

            .snowflake:nth-child(1) { left: 5%; animation-duration: 8s; font-size: 1.2rem; }
            .snowflake:nth-child(2) { left: 15%; animation-duration: 12s; font-size: 2rem; }
            .snowflake:nth-child(3) { left: 25%; animation-duration: 10s; font-size: 1.8rem; }
            .snowflake:nth-child(4) { left: 35%; animation-duration: 9s; font-size: 1.5rem; }
            .snowflake:nth-child(5) { left: 45%; animation-duration: 11s; font-size: 1.6rem; }
            .snowflake:nth-child(6) { left: 55%; animation-duration: 14s; font-size: 1.4rem; }
            .snowflake:nth-child(7) { left: 65%; animation-duration: 10s; font-size: 1.7rem; }
            .snowflake:nth-child(8) { left: 75%; animation-duration: 13s; font-size: 1.3rem; }
            .snowflake:nth-child(9) { left: 85%; animation-duration: 15s; font-size: 2.2rem; }
            .snowflake:nth-child(10) { left: 95%; animation-duration: 8s; font-size: 1.2rem; }

            @keyframes fall {
                0% { top: -10%; opacity: 1; }
                100% { top: 100%; opacity: 0; }
            }

            @keyframes sway {
                0%, 100% { transform: translateX(0); }
                25% { transform: translateX(-10px); }
                50% { transform: translateX(10px); }
                75% { transform: translateX(-5px); }
            }
        </style>

        <div class="snowflakes" aria-hidden="true">
            <div class="snowflake">❄</div>
            <div class="snowflake">❄</div>
            <div class="snowflake">❄</div>
            <div class="snowflake">❄</div>
            <div class="snowflake">❄</div>
            <div class="snowflake">❄</div>
            <div class="snowflake">❄</div>
            <div class="snowflake">❄</div>
            <div class="snowflake">❄</div>
            <div class="snowflake">❄</div>
        </div>
        """, unsafe_allow_html=True
    )

# Ejecutar la aplicación
if __name__ == "__main__":
    create_sidebar()


