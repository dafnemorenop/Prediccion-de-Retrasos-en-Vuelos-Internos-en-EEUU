import streamlit as st
import pandas as pd
import sys
import os
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
            <h1>Análisis Exploratorio de Datos</h1>
        </div>
        """, unsafe_allow_html=True
    )

    # Cargar el dataset
    df = pd.read_pickle(r"vuelos_limpio.pkl") 
    df_copia = df.copy()
    df_2021 = df[df['anio'] == 2021]
    df_2022 = df[df['anio'] == 2022]
    df_2023 = df[df['anio'] == 2023]

    # Sidebar para la selección de gráficos
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

    # Copos de nieve para efectos visuales
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

# Llamar a la función display cuando se ejecute este archivo
if __name__ == "__main__":
    display()
