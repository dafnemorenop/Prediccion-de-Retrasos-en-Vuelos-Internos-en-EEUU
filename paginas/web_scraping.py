import streamlit as st
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
        
        El proceso de extracción de datos de vuelos se realiza a través de un script automatizado que accede directamente al sitio web del **[Departamento de Estadísticas de Transporte de EE. UU.](https://www.transtats.bts.gov/ONTIME/Departures.aspx)**. Este script emplea librerías como BeautifulSoup y Selenium para navegar en el sitio, seleccionar las opciones de aeropuertos y aerolíneas, y extraer la información sobre vuelos internos, retrasos y otros datos relevantes para el análisis de la puntualidad aérea en los Estados Unidos.

    
        <h3>Flujo de trabajo</h3>
        1. **Obtención de opciones de aeropuertos y aerolíneas**:
        - Se hace una solicitud HTTP a la página y se extraen los datos de los menús desplegables (aeropuertos y aerolíneas) utilizando la librería `BeautifulSoup`.

        2. **Automatización de la selección de datos con Selenium**:
        - Se emplea Selenium para iniciar un navegador y seleccionar las opciones de aeropuertos y aerolíneas de manera programada.

        3. **Preselección de estadísticas y configuraciones**:
        - Se marcan las opciones de estadísticas, días, meses y años para ajustar la búsqueda.

        4. **Iteración para extraer los datos**:
        - Se recorren todas las combinaciones de aeropuertos y aerolíneas para hacer clic en el botón de descarga y guardar los archivos CSV.

        5. **Manejo de errores y estado de los datos**:
        - Se implementa un manejo de excepciones para casos donde no se encuentran datos o el proceso falla, notificando al usuario de manera apropiada.
        
        </div>""", unsafe_allow_html=True)

    st.markdown("""
        <div style="padding: 10px; border: 1px solid #f5c6cb; background-color: #721c24; border-radius: 5px;">
            <strong style="color: white;">Advertencia:</strong> Si desea los datos para trabajar con ellos podrá extraerlos corriendo el notebook de notebooks -> 01.0_web_scraping.ipynb en GitHub. Tenga en cuenta que se iniciará el proceso de extracción de datos de forma automatizada, lo que descargará más de 2000 archivos CSV. Este proceso puede tomar varias horas y generar una gran cantidad de datos, lo que podría afectar el rendimiento de tu dispositivo o conexión. Asegúrate de tener suficiente espacio de almacenamiento y una conexión estable antes de proceder.
        </div>
    """, unsafe_allow_html=True)
     st.write("")  
    st.write("")  
    st.write("") 

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

