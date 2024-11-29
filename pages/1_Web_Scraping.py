import streamlit as st
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from PIL import Image

st.set_page_config(
    page_title="Web Scraping",  # Título que aparecerá en la barra lateral con la primera palabra en mayúsculas
    page_icon="🌐",
)


# Código HTML para la barra de navegación como encabezado
html_code = """
<head>
    <style>
        /* Barra de navegación como encabezado */
        #navigation {
            background-color: rgba(44, 62, 80, 0.9); /* Fondo oscuro y semi-transparente */
            padding: 2px 5px;
            border-radius: 100px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            margin-bottom: 10px;
            display: flex;

            display: flex;
            justify-content: flex-start;
            margin-left: 700px; 


            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
        }

        /* Estilo para la lista de enlaces */
        .menu {
            display: flex;
            justify-content: space-around;
            width: 100%;
            max-width: 500px;
            gap: 40px;
        }

        /* Estilo para los enlaces */
        .menu li {
            list-style-type: none;
            display: flex;
            align-items: center;
            font-size: 20px;
            transition: transform 0.3s ease;  /* Animación suave al pasar el cursor */
        }

        /* Estilo para los iconos y texto */
        .menu li a {
            text-decoration: none;
            color: #ECF0F1;  /* Color claro */
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 10px;  /* Espacio entre el icono y el texto */
        }

        /* Efecto de cambio de color y tamaño al pasar el cursor */
        .menu li:hover {
            transform: scale(1.2);  /* Efecto de zoom */
            color: #3498DB;  /* Cambiar el color al azul */
        }

        /* Estilo de los iconos */
        .menu li i {
            font-size: 28px;  /* Tamaño de los iconos */
        }

        /* Ajustar el contenido de la página para no quedar tapado por la barra */
        .content {
            margin-top: 100px;
        }
    </style>
</head>

<div id='navigation'>
    <div class='container'>
        <div class='section' id='navigation-wrapper'>
            <div class='widget HTML' data-version='1' id='HTML11'>
                <ul class='menu'>
                    <li style="margin-top: 50px;"><a href='https://www.linkedin.com/in/dafne-moreno-palomares-86a30526b/' target='_blank'>
                        <i class="fa fa-linkedin"></i> LinkedIn</a></li>
                    <li style="margin-top: 50px;"><a href='https://github.com/dafnemorenop' target='_blank'>
                        <i class="fa fa-github"></i> GitHub</a></li>
                     <li style="margin-top: 50px;"><a href='https://github.com/dafnemorenop/Prediccion-de-Retrasos-en-Vuelos-Internos-en-EEUU' target='_blank'>
                        <i class="fa fa-github"></i> FlyPredict Data</a></li>
                </ul>
            </div>
        </div>
    </div>
</div>

"""

# Añadir el HTML al principio de la aplicación (barra en la parte superior)
st.markdown(html_code, unsafe_allow_html=True)




# Título de la página web
st.markdown(
    """
    <style>
        .title-section h1 {
            color: #90caf9; /* Color azul claro */
            font-size: 3rem;
            font-weight: bold;
            text-align: justify; /* Justificar el texto */
            margin-top: 30px;
        }
    </style>
    <div class="title-section">
        <h1>Extracción de datos: DOT de USA</h1>
    </div>
    """, unsafe_allow_html=True
)


# Descripción explicativa de cómo se realizó la extracción



st.markdown("""
        <div style="text-align: justify">
     <h3>Automatización de extracción de datos de vuelos</h3>
    
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
        <strong style="color: white;">Advertencia:</strong> Al pulsar el siguiente botón, se iniciará el proceso de extracción de datos de forma automatizada, lo que descargará más de 2000 archivos CSV. Este proceso puede tomar varias horas y generar una gran cantidad de datos, lo que podría afectar el rendimiento de tu dispositivo o conexión. Asegúrate de tener suficiente espacio de almacenamiento y una conexión estable antes de proceder.
    </div>
""", unsafe_allow_html=True)
import streamlit as st
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

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
        # Configuración del navegador en modo headless
        options = Options()
        options.add_argument("--headless")  # Ejecutar sin interfaz gráfica
        driver = webdriver.Firefox(options=options)  # Cambia a Chrome si lo prefieres
        driver.get(url)

        def preselecciones(driver):
            """Preselecciona las casillas necesarias para la extracción"""
            try:
                driver.find_element(By.ID, "chkAllStatistics").click()
                driver.find_element(By.ID, "chkAllDays").click()
                driver.find_element(By.ID, "chkMonths_11").click()  # Selecciona diciembre
                driver.find_element(By.ID, "chkYears_34").click()   # Selecciona 2021
                driver.find_element(By.ID, "chkYears_35").click()   # Selecciona 2022
                driver.find_element(By.ID, "chkYears_36").click()   # Selecciona 2023
            except Exception:
                pass  # Si falla, no se imprime nada

        preselecciones(driver)

        # Iterar sobre todos los aeropuertos y aerolíneas para descargar los datos
        for aeropuerto in listado_aeropuertos:
            select_aeropuerto = Select(driver.find_element(By.NAME, "cboAirport"))
            select_aeropuerto.select_by_visible_text(aeropuerto)

            for aerolinea in listado_aerolineas:
                try:
                    select_aerolinea = Select(driver.find_element(By.NAME, "cboAirline"))
                    select_aerolinea.select_by_visible_text(aerolinea)

                    click_submit = driver.find_element(By.ID, "btnSubmit").click()

                    # Desplazar la página para mostrar el botón de descarga
                    driver.execute_script("window.scrollBy(0, 200);")

                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "DL_CSV"))
                    )
                    if element:
                        element.click()
                        st.write(f"Datos descargados para el aeropuerto {aeropuerto} y la aerolínea {aerolinea}.")
                except Exception as e:
                    st.error(f"Error con el aeropuerto {aeropuerto} y la aerolínea {aerolinea}: {e}")
                    pass  # Si falla, no se imprime nada

        driver.quit()


image = Image.open('images/avion.jpg')


st.image(image, use_column_width=True)


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
