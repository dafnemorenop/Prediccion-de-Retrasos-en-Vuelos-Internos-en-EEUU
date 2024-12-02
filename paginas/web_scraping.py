import streamlit as st
import requests
from bs4 import BeautifulSoup
from PIL import Image

def display():
    # Título de la página web
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
            <h1>Extracción de datos</h1>
        </div>
        """, unsafe_allow_html=True
    )

    # Descripción explicativa de cómo se realizó la extracción
    st.markdown("""
        <div style="text-align: justify">
        <h3>Automatización de extracción de datos de DOT de USA</h3>
        
        El proceso de extracción de datos de vuelos se realiza a través de un script automatizado que accede directamente al sitio web del **[Departamento de Estadísticas de Transporte de EE. UU.](https://www.transtats.bts.gov/ONTIME/Departures.aspx)**. Este script emplea librerías como BeautifulSoup y requests para extraer la información sobre vuelos internos, retrasos y otros datos relevantes para el análisis de la puntualidad aérea en los Estados Unidos.

        <h3>Flujo de trabajo</h3>
        1. **Obtención de opciones de aeropuertos y aerolíneas**:
        - Se hace una solicitud HTTP a la página y se extraen los datos de los menús desplegables (aeropuertos y aerolíneas) utilizando la librería `BeautifulSoup`.

        2. **Iteración para extraer los datos**:
        - Se recorren todas las combinaciones de aeropuertos y aerolíneas para extraer los datos deseados de manera eficiente.

        3. **Manejo de errores y estado de los datos**:
        - Se implementa un manejo de excepciones para casos donde no se encuentran datos o el proceso falla, notificando al usuario de manera apropiada.
        </div>""", unsafe_allow_html=True)

    st.markdown("""
        <div style="padding: 10px; border: 1px solid #f5c6cb; background-color: #721c24; border-radius: 5px;">
            <strong style="color: white;">Advertencia:</strong> Al pulsar el siguiente botón, se iniciará el proceso de extracción de datos de forma automatizada. Este proceso puede tomar un tiempo, dependiendo de la cantidad de datos.
        </div>
    """, unsafe_allow_html=True)

    # CSS para centrar y estilizar el botón
    st.markdown("""
        <style>
            .center-button {
                display: flex;
                justify-content: center;
                margin-top: 40px;
            }
            .custom-button {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 15px 30px;
                font-size: 22px;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            .custom-button:hover {
                background-color: #45a049;
            }
        </style>
    """, unsafe_allow_html=True)

    # Botón estilizado y centrado
    if st.button('Iniciar extracción', use_container_width=True, type="primary"):
        st.write("Iniciando el proceso de extracción de datos...")

        url = "https://www.transtats.bts.gov/ONTIME/Departures.aspx"

        def obtener_opciones(url, aeropuertos_aerolineas):
            """Con esta función se seleccionan los aeropuertos o las aerolíneas que están en un desplegable"""
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            seleccionar_aeropuerto_aerolinea = soup.find("select", attrs={"name": aeropuertos_aerolineas})
            if seleccionar_aeropuerto_aerolinea:
                opciones = seleccionar_aeropuerto_aerolinea.find_all("option")
                listado_opciones = [opcion.text for opcion in opciones]
                return listado_opciones
            else:
                return []

        # Obtener listado de aeropuertos y aerolíneas
        listado_aeropuertos = obtener_opciones(url, "cboAirport")
        listado_aerolineas = obtener_opciones(url, "cboAirline")

        # Comprobar si se encontraron los datos necesarios
        if not listado_aeropuertos or not listado_aerolineas:
            st.error("No se pudieron obtener los aeropuertos o las aerolíneas de la página.")
        else:
            st.write(f"Se han encontrado {len(listado_aeropuertos)} aeropuertos y {len(listado_aerolineas)} aerolíneas.")

            # Aquí puedes realizar cualquier procesamiento adicional que desees
            st.write("Ahora puedes utilizar estos datos para realizar análisis adicionales.")

            # Ejemplo de cómo podrías procesar o mostrar los datos
            st.write("Listado de aeropuertos:", listado_aeropuertos[:10])  # Muestra los primeros 10 aeropuertos
            st.write("Listado de aerolíneas:", listado_aerolineas[:10])  # Muestra las primeras 10 aerolíneas

    image = Image.open('images/avion.jpg')
    st.image(image, use_container_width=True)

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

