import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="FlyPredict",
    page_icon=":airplane:",
    layout="wide",
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
            margin-left: 1000px; 


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




# Definición de la función principal para la página
def main():
  

    # Agregar un estilo CSS personalizado para la página
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

    # CSS para estilizar los contenedores
    st.markdown(
        """
        <style>
            .container {
                padding: 10px; /* Espaciado interno */
                margin: 10px; /* Separación entre contenedores */
                text-align: justify; /* Justificar texto */
            }
            .container h3 {
                color: #90caf9; /* Azul claro para los títulos */
                margin-bottom: 10px; /* Separación del título */
            }
        </style>
        """, 
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: justify">
            <h2><strong>Predicción de Retrasos en Vuelos Internos en EEUU:</strong> 
            Desarrollo de un Modelo Predictivo con Streamlit para la Visualización de Datos</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    
    # Crear las columnas para los contenedores
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="container">
                <h3>Descripción</h3>
                <p>FlyPredict es una aplicación para la predicción de vuelos internos en EE.UU. para el mes de diciembre entre los años 2021 y 2023.</p>
                <p>Puedes visitar la página del Departamento de Estadísticas de Transporte de EE. UU., de donde se obtuvieron los datos para el estudio mediante web scraping, en el siguiente enlace:</p>
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
                <p>Este proyecto se centró en desarrollar un modelo predictivo para estimar retrasos en vuelos internos en EE. UU., utilizando técnicas de análisis de datos y aprendizaje automático.</p>
                <p>Este estudio proporciona una visión sobre las causas, el rendimiento y los factores que influyen en la puntualidad aérea, presentando un modelo predictivo que permite anticipar la puntualidad de las aerolíneas y contribuir así a la mejora de la satisfacción de los pasajeros.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="container">
                <h3>Tecnologías</h3>
                <p>El proyecto fue desarrollado con herramientas tecnológicas que facilitaron el análisis eficiente de grandes volúmenes de datos y la visualización clara e interactiva de resultados, destacando patrones y tendencias relevantes.</p>
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
        

    image = Image.open('images/vista-aerea.png')

    # Usar un contenedor y tres columnas
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])  # Aquí las columnas tienen proporciones 1:2:1

        # Centrar la imagen en la columna central (col2)
        with col2:
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


# Llama a la función main para que se ejecute cuando se corra este archivo
if __name__ == "__main__":
    main()
