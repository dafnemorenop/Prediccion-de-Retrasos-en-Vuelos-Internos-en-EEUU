import pandas as pd
import re
from textblob import TextBlob
import plotly.express as px
from PIL import Image
import io
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from datetime import datetime, timedelta
import itertools
import streamlit as st
import sys

def main():
    st.title("EDA")
    
st.set_page_config(
    page_title="EDA",  # Título en mayúsculas
    page_icon="📊",
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



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.funciones_eda import (mostrar_info_df, mostrar_columnas_df,
                                    mostrar_analisis_descriptivo, 
                                    mostrar_grafico_vuelos_anuales,
                                    mostrar_vuelos_semanales,
                                    mostrar_vuelos_diarios_anuales,
                                    mostrar_grafico_vuelos_por_aerolinea,
                                    mostrar_diagrama_caja,
                                    mostrar_mapa_calor,
                                    años_retrasos,
                                    mostrar_correlacion_pearson,
                                    mostrar_grafico_pastel_retrasos_salida_llegada,
                                    mostrar_grafico_pastel_festivos,
                                    mostrar_grafico_barras_retraso_aerolineas,
                                    mostrar_grafico_barras_retraso_aeropuertos,
                                    mostrar_grafico_lineas_diciembre,
                                    mostrar_grafico_lineas_acumulado_diciembre,
                                    mostrar_grafico_rango_horario_salidas_llegadas,
                                    mostrar_grafico_rango_horario_retrasos,
                                    mostrar_grafico_vuelos_semanales_retraso,
                                    mostrar_barras_retrasos_mas_comunes,
                                    mostrar_pastel_retrasos_mas_comunes,
                                    mostrar_estados_origen_retraso,
                                    mostrar_diagrama_caja_millas,
                                    mostrar_histograma_millas,
                                    mostrar_barras_millas,
                                    mostrar_diagrama_caja_retraso_llegada,
                                    mostrar_grafico_barras_intervalos_tiempo,
                                    mostrar_aerolineas_costo,
                                    mostrar_grafico_barras_retraso_aerolineas_costo,
                                    mostrar_conclusiones_finales)

def main():
    df = pd.read_pickle(r"C:\Users\Dafne\OneDrive\Escritorio\FlyPredict\data\vuelos_limpio.pkl") 
    df_copia= df.copy()
    df_2021 = df[df['anio'] == 2021]
    df_2022 = df[df['anio'] == 2022]
    df_2023 = df[df['anio'] == 2023]


    # Título
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
            <h1>Visualización de Datos</h1>
        </div>
        """, unsafe_allow_html=True
    )

    pagina_graficos = st.sidebar.selectbox("Seleccionar página de gráficos", [
        "Información básica del Dataset",
        "Exploración Temporal de Vuelos",
        "Gráficos lineales de Diciembre",
        "Mapa de Calor y Correlación",
        "Distribución horas",
        "Tipos de retrasos",
        "Retrasos por Fecha",
        "Porcentaje de Retrasos",
        "Retrasos por intervalo tiempo",
        "Retrasos por rango horario",

        "Gráfico Vuelos por Aerolínea y Retrasos",
        "Gráfico Vuelos por Aeropuerto y Estado de Origen",
        "Diagrama de Caja de Millas e Histograma",
        "Costo Aerolíneas",
        "Conclusiones Finales"
    ])

    # Mostrar gráfico seleccionado
    if pagina_graficos == "Información básica del Dataset":
        mostrar_info_df(df)
        mostrar_columnas_df(df)
        mostrar_analisis_descriptivo(df, df_2021, df_2022, df_2023)

    elif pagina_graficos == "Exploración Temporal de Vuelos":
        mostrar_grafico_vuelos_anuales(df_copia)
        mostrar_vuelos_semanales(df_copia, df_2021, df_2022, df_2023)
        mostrar_vuelos_diarios_anuales(df_copia)


    elif pagina_graficos == "Gráficos lineales de Diciembre":
        mostrar_grafico_lineas_diciembre(df)
        mostrar_grafico_lineas_acumulado_diciembre(df)

    elif pagina_graficos == "Mapa de Calor y Correlación":
        mostrar_mapa_calor(df)
        mostrar_correlacion_pearson(df)

    elif pagina_graficos == "Distribución horas":
        mostrar_diagrama_caja(df, df_2021, df_2022, df_2023)

    elif pagina_graficos == "Tipos de retrasos":
        mostrar_barras_retrasos_mas_comunes(df)
        mostrar_pastel_retrasos_mas_comunes(df)

    elif pagina_graficos == "Retrasos por Fecha":
        años_retrasos(df_copia)
        mostrar_grafico_vuelos_semanales_retraso(df, df_2021, df_2022, df_2023)

    elif pagina_graficos == "Porcentaje de Retrasos":
        mostrar_grafico_pastel_retrasos_salida_llegada(df, df_2021, df_2022, df_2023)
        mostrar_grafico_pastel_festivos(df, df_2021, df_2022, df_2023)

    elif pagina_graficos == "Retrasos por intervalo tiempo":
        mostrar_diagrama_caja_retraso_llegada(df)
        mostrar_grafico_barras_intervalos_tiempo(df)

    elif pagina_graficos == "Retrasos por rango horario":
        mostrar_grafico_rango_horario_salidas_llegadas(df)
        mostrar_grafico_rango_horario_retrasos(df)


    elif pagina_graficos == "Gráfico Vuelos por Aerolínea y Retrasos":
        mostrar_grafico_vuelos_por_aerolinea(df, df_2021, df_2022, df_2023)
        mostrar_grafico_barras_retraso_aerolineas(df, df_2021, df_2022, df_2023)

    elif pagina_graficos == "Gráfico Vuelos por Aeropuerto y Estado de Origen":
        mostrar_grafico_barras_retraso_aeropuertos(df, df_2021, df_2022, df_2023)
        mostrar_estados_origen_retraso(df)


    elif pagina_graficos == "Diagrama de Caja de Millas e Histograma":
        mostrar_diagrama_caja_millas(df)
        mostrar_histograma_millas(df)
        mostrar_barras_millas(df)

    elif pagina_graficos == "Costo Aerolíneas":
        mostrar_aerolineas_costo(df_copia)
        mostrar_grafico_barras_retraso_aerolineas_costo(df_copia)

    elif pagina_graficos == "Conclusiones Finales":
        mostrar_conclusiones_finales()

 

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
