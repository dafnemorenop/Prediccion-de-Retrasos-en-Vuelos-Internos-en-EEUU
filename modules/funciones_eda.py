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



def mostrar_info_df(df):
    st.subheader('Información básica del dataset')
    st.write("Primeras filas del DataFrame")
    st.dataframe(df.head())

    st.write("Número de filas:", df.shape[0], "Número de columnas:", df.shape[1])

    with st.expander(label = 'Info del DataFrame', expanded = False):
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

def mostrar_columnas_df(df):
    # Mostrar las columnas del DataFrame 
    with st.expander(label = "Columnas del DataFrame", expanded = False):
        st.write(df.columns)

    st.write("Explicación de las columnas")
    st.markdown("""
        <div style="text-align: justify">
                    
        - **aerolinea**: Nombre de la aerolínea.
        - **fecha**: La fecha del vuelo en formato día/mes/año.
        - **numero_vuelo**: El número de vuelo.
        - **numero_cola**: El número de cola del vuelo.
        - **aeropuerto_destino**: El aeropuerto de destino del vuelo. 
        - **hora_salida_programada**: La hora programada de salida del vuelo.
        - **hora_salida_real**: La hora real de salida del vuelo.
        - **duracion_programada_vuelo**: La duración programada del vuelo.
        - **duracion_real**: La duración real del vuelo.
        - **retraso_salida**: El retraso en la salida del vuelo.
        - **hora_despegue**: La hora de despegue del vuelo.
        - **tiempo_pista_salida**: El tiempo en pista antes del despegue.
        - **tiempo_retraso_aerolinea**: Tiempo de retraso atribuido a la aerolínea.
        - **tiempo_retraso_clima**: Tiempo de retraso atribuido al clima.
        - **tiempo_retraso_sistema_aviacion**: Tiempo de retraso atribuido al sistema de aviación.
        - **tiempo_retraso_seguridad**: Tiempo de retraso atribuido a cuestiones de seguridad.
        - **retraso_llegada**: Retraso en la llegada de la aeronave.
        - **ciudad_origen**: La ciudad de origen del vuelo.
        - **estado_origen**: El estado de origen del vuelo.
        - **aeropuerto_origen**: El aeropuerto de origen del vuelo.
        - **dia_semana**: El día de la semana en que tuvo lugar el vuelo.
        - **anio**: El año en que tuvo lugar el vuelo.
        - **fin_de_semana**: Indicador de si el vuelo tuvo lugar durante el fin de semana o no.
        - **festivos**: Indicador de si el vuelo tuvo lugar en un día festivo o no.
        - **distancia_millas**: La distancia del vuelo en millas.
        - **ciudad_destino**: La ciudad de destino del vuelo.
        - **estado_destino**: El estado de destino del vuelo.
        - **codigo_aeropuerto_origen**: El código del aeropuerto de origen.
        - **codigo_aeropuerto_destino**: El código del aeropuerto de destino.
        - **direccion_destino**: Dirección del aeropuerto de destino.
        - **latitude_destino**: Latitud del aeropuerto de destino.
        - **longitude_destino**: Longitud del aeropuerto de destino.
        - **direccion_origen**: Dirección del aeropuerto de origen.
        - **latitude_origen**: Latitud del aeropuerto de origen.
        - **longitude_origen**: Longitud del aeropuerto de origen.
        - **mes**: Mes del vuelo.
        - **hora_llegada_real**: Hora real de llegada.
                    </div>""", unsafe_allow_html=True)
    

    with st.expander("Valores Únicos", expanded=False):
        st.write(df.nunique())


def mostrar_analisis_descriptivo(df, df_2021, df_2022, df_2023):

    st.subheader('Estadísticas descriptivas')
    st.markdown("""
                <div style="text-align: justify">
    
    - <strong>fecha</strong>: El rango de fechas va desde el 1 de diciembre de 2021 hasta el 31 de diciembre de 2023. 
                
    - <strong>numero_vuelo</strong>: El número promedio de vuelo es aproximadamente 2425, con un mínimo de 1 y un máximo de 9683.
                
    - <strong>duracion_programada_vuelo</strong>: La duración promedio de vuelo programada es de aproximadamente 147 minutos, con una desviación estándar de aproximadamente 74 minutos. 
    
    - <strong>duracion_real</strong>: La duración promedio de vuelo real es de aproximadamente 137 minutos, con una desviación estándar de aproximadamente 76 minutos. 
    
    - <strong>retraso_salida</strong>: El tiempo promedio de retraso en la salida es de aproximadamente 13 minutos, con un mínimo de -99 minutos (lo que sugiere que algunos vuelos salieron antes de la hora programada) y un máximo de 3786 minutos (aproximadamente 63 horas de retraso).

    - <strong>tiempo_pista_salida</strong>: El tiempo promedio en pista antes de la salida es de aproximadamente 17 minutos.
    
    - <strong>tiempo_retraso_aerolinea, tiempo_retraso_clima, tiempo_retraso_sistema_aviacion, tiempo_retraso_seguridad</strong>: Los tiempos promedio de retraso atribuidos a la aerolínea, clima, sistema de aviación y seguridad son relativamente bajos, con la mayoría de los registros mostrando 0 minutos de retraso.
    
    - <strong>retraso_llegada</strong>: El tiempo promedio de retraso en la llegada es de aproximadamente 5 minutos.
    
    - <strong>distancia_millas</strong>: La distancia promedio de vuelo es de aproximadamente 834 millas, con un mínimo de 32 millas y un máximo de 5082 millas.
                </div>""", unsafe_allow_html=True)
    with st.expander("Resumen estadístico del DataFrame", expanded=False):
        st.write(df.describe())

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.expander("2021", expanded=False):
            st.write(df_2021.describe())

    with col2:
        with st.expander("2022", expanded=False):
            st.write(df_2022.describe())

    with col3:
        with st.expander("2023", expanded=False):
            st.write(df_2023.describe())
    st.markdown("""
    <div style="text-align: justify">
    En 2021, la duración real promedio de los vuelos fue de aproximadamente 137 minutos, con el 75% de los vuelos teniendo una duración real de 170 minutos o menos. Además, se registró un retraso promedio en la salida de alrededor de 13 minutos, mientras que la mediana del retraso en la llegada fue de 3 minutos, lo que indica que la mitad de los vuelos experimentaron retrasos en la llegada iguales o menores a este valor, con un retraso promedio en la llegada de aproximadamente 5 minutos.

    En 2022, observamos que los vuelos en promedio fueron un poco más cortos que en 2021. Aunque la duración real promedio fue similar, se registró un retraso promedio en la salida ligeramente más alto, mientras que el retraso promedio en la llegada fue ligeramente más bajo en comparación con el año anterior.

    Finalmente, en 2023, los vuelos en promedio fueron un poco más cortos que en los años anteriores. Se observaron retrasos en la salida y llegada más bajos en comparación con los años anteriores, lo que indica una mejora en la puntualidad de los vuelos en este año.

    El análisis del dataset revela un amplio espectro de información sobre vuelos realizados entre diciembre de 2021 y diciembre de 2023, destacando una variabilidad significativa en el número de vuelos registrados, desde un mínimo de 1 hasta un máximo de 9683. Además, se observa que, aunque la duración promedio de los vuelos programados es de aproximadamente 147 minutos, existen diferencias notables entre la duración programada y la real, así como una amplia gama de tiempos de retraso en la salida, con algunos vuelos incluso adelantándose a la hora programada.
                    </div>""", unsafe_allow_html=True)


def mostrar_grafico_vuelos_anuales(df):
    st.subheader('Vuelos anuales registrados')
    st.markdown("""
    <div style="text-align: justify">
    En el gráfico de barras podemos observar que en el año 2021, se registraron un total de 551,821 vuelos internos en Estados Unidos. Esta cifra aumentó ligeramente en el año 2022, alcanzando un total de 556,976 vuelos. Finalmente, para el año 2023, el número de vuelos registrados aumentó aún más, llegando a 583,679.
                </div>""", unsafe_allow_html=True)

    df["anio"] = df["anio"].astype(str)

    vuelos_anuales = df.groupby(['anio']).size().reset_index(name ='cantidad_vuelos_anuales')

    fig = px.bar(data_frame = vuelos_anuales,
                 x          = 'anio',
                 y          = 'cantidad_vuelos_anuales',
                 opacity                 = 0.8,
                 title      = "Cantidad de Vuelos Anuales",
                 color      = 'anio')
    fig.update_layout(title_x=0.3, xaxis_title='Año', yaxis_title='Cantidad de Vuelos', xaxis={'type': 'category', 'categoryorder': 'total descending'})
    st.plotly_chart(fig)

    st.markdown("""
    <div style="text-align: justify">
    Estos datos muestran una tendencia de crecimiento en el número de vuelos internos en Estados Unidos a lo largo de los años.
                </div>""", unsafe_allow_html=True)


def mostrar_vuelos_semanales(df_copia, df_2021, df_2022, df_2023):
    st.subheader('Vuelos semanales')
    st.markdown("""
    <div style="text-align: justify">
    Se puede observar en el conjunto de datos que los viernes presentan la mayor cantidad de vuelos, seguidos de cerca por los jueves. Sin embargo, al analizar los datos por año, se observa que el día de la semana con el mayor número de vuelos varía.                
                </div>""", unsafe_allow_html=True)
    diccionario_dias = {'0': 'Lunes', '1': 'Martes', '2': 'Miércoles', '3': 'Jueves', '4': 'Viernes', '5': 'Sábado', '6': 'Domingo'}
    df_copia['dia_semana'] = df_copia['dia_semana'].astype(str)
    df_copia['dia_semana'] = df_copia['dia_semana'].replace(diccionario_dias)

    vuelos_semanales = df_copia.groupby(['dia_semana']).size().reset_index(name='cantidad_vuelos_dia_semana')
    fig = px.bar(data_frame=vuelos_semanales,
                x='dia_semana',
                y='cantidad_vuelos_dia_semana',
                opacity=0.8,
                title="Cantidad de Vuelos Semanales",
                color='dia_semana')
    fig.update_layout(title_x=0.3, xaxis_title='Día de la semana', yaxis_title='Cantidad de Vuelos', xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(fig)

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.expander("2021", expanded=False):
                df_2021['dia_semana'] = df_2021['dia_semana'].astype(str)
                df_2021['dia_semana'] = df_2021['dia_semana'].replace(diccionario_dias)

                vuelos_semanales = df_2021.groupby(['dia_semana']).size().reset_index(name='cantidad_vuelos_dia_semana')
                fig = px.bar(data_frame=vuelos_semanales,
                            x='dia_semana',
                            y='cantidad_vuelos_dia_semana',
                            opacity=0.8,
                            title="Cantidad de Vuelos Semanales 2021",
                            color='dia_semana')
                fig.update_layout(title_x=0.3, xaxis_title='Día de la semana', yaxis_title='Cantidad de Vuelos', xaxis={'categoryorder': 'total descending'})
                st.plotly_chart(fig)

    with col2:
        with st.expander("2022", expanded=False):
                df_2022['dia_semana'] = df_2022['dia_semana'].astype(str)
                df_2022['dia_semana'] = df_2022['dia_semana'].replace(diccionario_dias)

                vuelos_semanales = df_2022.groupby(['dia_semana']).size().reset_index(name='cantidad_vuelos_dia_semana')
                fig = px.bar(data_frame=vuelos_semanales,
                            x='dia_semana',
                            y='cantidad_vuelos_dia_semana',
                            opacity=0.8,
                            title="Cantidad de Vuelos Semanales 2022",
                            color='dia_semana')
                fig.update_layout(title_x=0.3, xaxis_title='Día de la semana', yaxis_title='Cantidad de Vuelos', xaxis={'categoryorder': 'total descending'})
                st.plotly_chart(fig)

    with col3:
        with st.expander("2023", expanded=False):
                df_2023['dia_semana'] = df_2023['dia_semana'].astype(str)
                df_2023['dia_semana'] = df_2023['dia_semana'].replace(diccionario_dias)

                vuelos_semanales = df_2023.groupby(['dia_semana']).size().reset_index(name='cantidad_vuelos_dia_semana')
                fig = px.bar(data_frame=vuelos_semanales,
                            x='dia_semana',
                            y='cantidad_vuelos_dia_semana',
                            opacity=0.8,
                            title="Cantidad de Vuelos Semanales 2023",
                            color='dia_semana')
                fig.update_layout(title_x=0.3, xaxis_title='Día de la semana', yaxis_title='Cantidad de Vuelos', xaxis={'categoryorder': 'total descending'})
                st.plotly_chart(fig)

    st.markdown("""
    <div style="text-align: justify">
        La variación en los días de la semana con mayor cantidad de vuelos puede ser el resultado de una combinación de varios factores que afectan la industria de la aviación y los comportamientos de viaje de las personas.
                </div>""", unsafe_allow_html=True)

def mostrar_vuelos_diarios_anuales(df_copia):
    st.subheader('Vuelos anuales por día de mes')
    st.markdown("""
    <div style="text-align: justify">
    El gráfico de barras revela que los días con mayor cantidad de vuelos en el conjunto de datos son el 22 y el 21, mientras que los días con menor cantidad son el 25, 24 y 31 de diciembre.
        </div>""", unsafe_allow_html=True)
    df_copia['fecha'] = pd.to_datetime(df_copia['fecha'])
    df_copia['dia_mes'] = df_copia['fecha'].dt.day.astype(str)
    df_copia['anio'] = df_copia['anio'].astype(str)

    vuelos_por_dia_mes_anio = df_copia.groupby(['anio', 'dia_mes']).size().reset_index(name='cantidad_vuelos_dia_mes_anio')

    fig = px.bar(data_frame=vuelos_por_dia_mes_anio,
                x='dia_mes',
                y='cantidad_vuelos_dia_mes_anio',
                opacity=0.8,
                title="Cantidad de Vuelos por Día del Mes y Año",
                color='anio')

    fig.update_layout(title_x=0.3, xaxis_title='Día del mes', yaxis_title='Cantidad de Vuelos', xaxis={'type': 'category', 'categoryorder': 'total descending'})

    st.plotly_chart(fig)
    st.markdown("""
    <div style="text-align: justify">
    Los días con más vuelos probablemente se relacionan con un aumento en los viajes durante la temporada navideña, cuando las personas viajan para reunirse con sus familias o disfrutar de unas vacaciones durante este período festivo. Por otro lado, los días con menos vuelos coinciden típicamente con los días festivos más importantes.
                </div>""", unsafe_allow_html=True)

def mostrar_grafico_vuelos_por_aerolinea(df, df_2021, df_2022, df_2023):
    st.subheader('Gráfico de barras de la cantidad de vuelos realizados por cada compañía aérea entre 2021-2023')
    st.markdown(""" <div style="text-align: justify">
    En todos los años, Southwest Airlines lidera con 341292 vuelos y Horizon Air con la menor cantidad, con 18839 vuelos. 
                </div>""", unsafe_allow_html=True)

    vuelos_aerolinea = df.groupby(['aerolinea']).size().reset_index(name='numero_vuelos')

    fig = px.bar(data_frame=vuelos_aerolinea,
                 x='aerolinea',
                 y='numero_vuelos',
                 opacity=0.8,
                 title="Cantidad de Vuelos por Compañía Aérea",
                 color='aerolinea')

    fig.update_layout(title_x=0.2, xaxis_title='Compañía Aérea', yaxis_title='Cantidad de Vuelos',
                      xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(fig)

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.expander("2021", expanded=False):
            vuelos_aerolinea_2021 = df_2021.groupby(['aerolinea']).size().reset_index(name='numero_vuelos')

            fig = px.bar(data_frame=vuelos_aerolinea_2021,
                         x='aerolinea',
                         y='numero_vuelos',
                         opacity=0.8,
                         title="Cantidad de Vuelos por Compañía Aérea - 2021",
                         color='aerolinea')
            fig.update_layout(title_x=0.2, xaxis_title='Compañía Aérea', yaxis_title='Cantidad de Vuelos',
                              xaxis={'categoryorder': 'total descending'})
            st.plotly_chart(fig)

    with col2:
        with st.expander("2022", expanded=False):
            vuelos_aerolinea_2022 = df_2022.groupby(['aerolinea']).size().reset_index(name='numero_vuelos')

            fig = px.bar(data_frame=vuelos_aerolinea_2022,
                         x='aerolinea',
                         y='numero_vuelos',
                         opacity=0.8,
                         title="Cantidad de Vuelos por Compañía Aérea - 2022",
                         color='aerolinea')
            fig.update_layout(title_x=0.2, xaxis_title='Compañía Aérea', yaxis_title='Cantidad de Vuelos',
                              xaxis={'categoryorder': 'total descending'})
            st.plotly_chart(fig)

    with col3:
        with st.expander("2023", expanded=False):
            vuelos_aerolinea_2023 = df_2023.groupby(['aerolinea']).size().reset_index(name='numero_vuelos')

            fig = px.bar(data_frame=vuelos_aerolinea_2023,
                         x='aerolinea',
                         y='numero_vuelos',
                         opacity=0.8,
                         title="Cantidad de Vuelos por Compañía Aérea - 2023",
                         color='aerolinea')
            fig.update_layout(title_x=0.2, xaxis_title='Compañía Aérea', yaxis_title='Cantidad de Vuelos',
                              xaxis={'categoryorder': 'total descending'})
            st.plotly_chart(fig)

    st.markdown("""
    <div style="text-align: justify">
    Se nota una variabilidad considerable en la cantidad de vuelos por aerolínea, con las grandes compañías como Southwest Airlines, American Airlines o Delta Air Lines concentrando cientos de miles de vuelos registrados.

    Tanto en 2021 como en 2022, las tres principales aerolíneas, en orden descendente, fueron Southwest Airlines, American Airlines y Delta Air Lines. Sin embargo, en 2023, Delta Air Lines avanzó un puesto en esta clasificación, colocándose en la segunda posición por delante de American Airlines.
                </div>""", unsafe_allow_html=True)



def mostrar_diagrama_caja(df, df_2021, df_2022, df_2023):
    df_copia= df.copy()
    st.subheader('Distribución de las horas de salida y llegada')
    st.markdown("""<div style="text-align: justify">
    Convertimos las horas a minutos desde la medianoche para ordenarlas. En el conjunto de los datos, la mediana de las horas de salida es de 792 minutos, mientras que la mediana de las horas de llegada es de 880 minutos, la hora mediana de salida se sitúa aproximadamente a las 13:12, mientras que para la llegada, se estima alrededor de las 14:40.
                </div>""", unsafe_allow_html=True)


    df_copia["hora_salida_minutos"] = df_copia["hora_salida_real"].apply(lambda x: x.hour * 60 + x.minute)
    df_copia["hora_llegada_minutos"] = df_copia["hora_llegada_real"].apply(lambda x: x.hour * 60 + x.minute)

    minutos = list(range(0, 1441, 60))  

    fig = go.Figure()

    fig.add_trace(go.Box(x=df_copia["hora_salida_minutos"], name="Salida"))
    fig.add_trace(go.Box(x=df_copia["hora_llegada_minutos"], name="Llegada"))

    fig.update_layout(
        title="Diagrama de caja para las horas de salida y llegada de los vuelos",
        title_x=0.1,
        xaxis_title="Minutos")

    st.plotly_chart(fig)

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.expander("2021", expanded=False):
            df_2021["hora_salida_minutos"] = df_2021["hora_salida_real"].apply(lambda x: x.hour * 60 + x.minute)
            df_2021["hora_llegada_minutos"] = df_2021["hora_llegada_real"].apply(lambda x: x.hour * 60 + x.minute)

            minutos = list(range(0, 1441, 60))  

            fig = go.Figure()

            fig.add_trace(go.Box(x=df_2021["hora_salida_minutos"], name="Salida"))
            fig.add_trace(go.Box(x=df_2021["hora_llegada_minutos"], name="Llegada"))

            fig.update_layout(
                title="Diagrama de caja para las horas de salida y llegada de los vuelos en 2021",
                title_x=0.1,
                xaxis_title="Minutos")

            st.plotly_chart(fig)

    with col2:
        with st.expander("2022", expanded=False):
            df_2022["hora_salida_minutos"] = df_2022["hora_salida_real"].apply(lambda x: x.hour * 60 + x.minute)
            df_2022["hora_llegada_minutos"] = df_2022["hora_llegada_real"].apply(lambda x: x.hour * 60 + x.minute)

            minutos = list(range(0, 1441, 60))  

            fig = go.Figure()

            fig.add_trace(go.Box(x=df_2022["hora_salida_minutos"], name="Salida"))
            fig.add_trace(go.Box(x=df_2022["hora_llegada_minutos"], name="Llegada"))

            fig.update_layout(
                title="Diagrama de caja para las horas de salida y llegada de los vuelos en 2022",
                title_x=0.1,
                xaxis_title="Minutos")

            st.plotly_chart(fig)

    with col3:
        with st.expander("2023", expanded=False):
            df_2023["hora_salida_minutos"] = df_2023["hora_salida_real"].apply(lambda x: x.hour * 60 + x.minute)
            df_2023["hora_llegada_minutos"] = df_2023["hora_llegada_real"].apply(lambda x: x.hour * 60 + x.minute)

            minutos = list(range(0, 1441, 60))  

            fig = go.Figure()

            fig.add_trace(go.Box(x=df_2023["hora_salida_minutos"], name="Salida"))
            fig.add_trace(go.Box(x=df_2023["hora_llegada_minutos"], name="Llegada"))

            fig.update_layout(
                title="Diagrama de caja para las horas de salida y llegada de los vuelos en 2023",
                title_x=0.1,
                xaxis_title="Minutos")

            st.plotly_chart(fig)
                
    st.markdown("""<div style="text-align: justify">
    En promedio, salen y llegan más tarde. La mediana de las horas de salida se mantiene por encima de las 777 minutos en todos los años, con un ligero aumento en 2023 a 804 minutos. Por otro lado, la mediana de las horas de llegada tiende a ser aún mayor, con un aumento progresivo de 794 minutos en 2021 a 890 minutos en 2023.             
                </div>""", unsafe_allow_html=True)


def mostrar_mapa_calor(df):

    st.subheader('Mapa de calor')
    st.markdown("""<div style="text-align: justify">
    Generamos un mapa de calor que visualiza las correlaciones de Pearson entre las variables numéricas.
        </div>""", unsafe_allow_html=True)
    fig = px.imshow(
        img = round(df[['numero_vuelo', 'duracion_programada_vuelo', 'duracion_real', 'retraso_salida', 'tiempo_pista_salida', 
                            'tiempo_retraso_aerolinea', 'tiempo_retraso_clima', 'tiempo_retraso_sistema_aviacion',
                            'tiempo_retraso_seguridad', 'retraso_llegada', 'dia_semana', 'fin_de_semana',
                            'festivos']].corr(), 1),
        text_auto = True, title = "Correlaciones Lineales de las Variables Numéricas")

    fig.update_layout(title_x = 0.2, width = 800, height = 600 )
    st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify">
    La única correlación significativa relevante mediante el coeficiente de Pearson es entre el Retraso en la Salida y en la Llegada de Vuelos.
    </div>""", unsafe_allow_html=True)

def mostrar_correlacion_pearson(df):
    st.subheader('Gráfico de dispersión')
    st.markdown("""<div style="text-align: justify">
    Creamos un gráfico de dispersión para representar la correlación entre retraso en la salida y en la llegada de los vuelos. Hay una relación positiva moderadamente fuerte entre las dos variables. 
    </div>""", unsafe_allow_html=True)
    

    fig= px.scatter(data_frame  = df,
                    x           = "retraso_salida",
                    y           = "retraso_llegada",
                    title       = "Correlación Lineal entre los Indicadores de Retraso en la Salida y en la Llegada de Vuelos",
                    opacity     = 0.5,
                    trendline   = 'ols')

    st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify">
    Cuando un vuelo se retrasa en la salida, tiende a experimentar un retraso similar en la llegada. 
                </div>""", unsafe_allow_html=True)


def mostrar_grafico_pastel_retrasos_salida_llegada(df, df_2021, df_2022, df_2023):
    st.subheader('Vuelos con retraso')

    st.markdown("""<div style="text-align: justify; margin-bottom: 10px;">
        Calculando el porcentaje de vuelos con retraso superior a 15 minutos observamos que en los tres años, las salidas de los aviones experimentaron un retraso promedio del 20,7%, mientras que las llegadas tuvieron un retraso promedio del 7,77%. 
    </div>
    <div style="text-align: justify;">
        En 2021, las salidas sufrieron un retraso del 21,7%, mientras que las llegadas tuvieron un retraso del 7,61%. En 2022, los retrasos en las salidas aumentaron a 24,7%, y en las llegadas alcanzaron el 10,1%. Finalmente, en 2023, los retrasos en las salidas disminuyeron a 15,9%, y en las llegadas descendieron a 5,7%.
    </div>""", unsafe_allow_html=True)


    sin_retraso_salida = df[df['retraso_salida'] <= 15].shape[0]
    con_retraso_salida = df[df['retraso_salida'] > 15].shape[0]

    sin_retraso_llegada = df[df['retraso_llegada'] <= 15].shape[0]
    con_retraso_llegada = df[df['retraso_llegada'] > 15].shape[0]

    fig = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]], subplot_titles=('Salidas', 'Llegadas'))

    fig.add_trace(go.Pie(labels=['Sin retraso', 'Con retraso'], values=[sin_retraso_salida, con_retraso_salida]), 1, 1)
    fig.add_trace(go.Pie(labels=['Sin retraso', 'Con retraso'], values=[sin_retraso_llegada, con_retraso_llegada]), 1, 2)

    fig.update_layout(title_text = "Porcentaje de Retrasos Superiores a 15 Minutos en los Vuelos", title_x = 0.2)

    fig.update_traces(pull = [0.05, 0.05], marker = dict(colors = px.colors.qualitative.Set2))
    st.plotly_chart(fig)

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.expander("2021", expanded=False):
            sin_retraso_salida = df_2021[df_2021['retraso_salida'] <= 15].shape[0]
            con_retraso_salida = df_2021[df_2021['retraso_salida'] > 15].shape[0]

            sin_retraso_llegada = df_2021[df_2021['retraso_llegada'] <= 15].shape[0]
            con_retraso_llegada = df_2021[df_2021['retraso_llegada'] > 15].shape[0]

            fig = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]], subplot_titles=('Salidas', 'Llegadas'))

            fig.add_trace(go.Pie(labels=['Sin retraso', 'Con retraso'], values=[sin_retraso_salida, con_retraso_salida]), 1, 1)
            fig.add_trace(go.Pie(labels=['Sin retraso', 'Con retraso'], values=[sin_retraso_llegada, con_retraso_llegada]), 1, 2)

            fig.update_layout(title_text = "Porcentaje de Retrasos Superiores a 15 Minutos en los Vuelos de 2021", title_x = 0.2)

            fig.update_traces(pull = [0.05, 0.05], marker = dict(colors = px.colors.qualitative.Set2))
            st.plotly_chart(fig)

    with col2:
        with st.expander("2022", expanded=False):
            sin_retraso_salida = df_2022[df_2022['retraso_salida'] <= 15].shape[0]
            con_retraso_salida = df_2022[df_2022['retraso_salida'] > 15].shape[0]

            sin_retraso_llegada = df_2022[df_2022['retraso_llegada'] <= 15].shape[0]
            con_retraso_llegada = df_2022[df_2022['retraso_llegada'] > 15].shape[0]

            fig = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]], subplot_titles=('Salidas', 'Llegadas'))

            fig.add_trace(go.Pie(labels=['Sin retraso', 'Con retraso'], values=[sin_retraso_salida, con_retraso_salida]), 1, 1)
            fig.add_trace(go.Pie(labels=['Sin retraso', 'Con retraso'], values=[sin_retraso_llegada, con_retraso_llegada]), 1, 2)

            fig.update_layout(title_text = "Porcentaje de Retrasos Superiores a 15 Minutos en los Vuelos de 2022", title_x = 0.2)

            fig.update_traces(pull = [0.05, 0.05], marker = dict(colors = px.colors.qualitative.Set2))
            st.plotly_chart(fig)

    with col3:
        with st.expander("2023", expanded=False):
            sin_retraso_salida = df_2023[df_2023['retraso_salida'] <= 15].shape[0]
            con_retraso_salida = df_2023[df_2023['retraso_salida'] > 15].shape[0]

            sin_retraso_llegada = df_2023[df_2023['retraso_llegada'] <= 15].shape[0]
            con_retraso_llegada = df_2023[df_2023['retraso_llegada'] > 15].shape[0]

            fig = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]], subplot_titles=('Salidas', 'Llegadas'))

            fig.add_trace(go.Pie(labels=['Sin retraso', 'Con retraso'], values=[sin_retraso_salida, con_retraso_salida]), 1, 1)
            fig.add_trace(go.Pie(labels=['Sin retraso', 'Con retraso'], values=[sin_retraso_llegada, con_retraso_llegada]), 1, 2)

            fig.update_layout(title_text = "Porcentaje de Retrasos Superiores a 15 Minutos en los Vuelos de 2023", title_x = 0.2)

            fig.update_traces(pull = [0.05, 0.05], marker = dict(colors = px.colors.qualitative.Set2))
            st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify; margin-bottom: 10px;">
        Se puede apreciar una tendencia de aumento en los retrasos de 2021 a 2022, seguida de una mejora en la puntualidad en 2023 al analizar los datos por años.
    </div>
    <div style="text-align: justify;">
        Un porcentaje significativamente mayor de vuelos experimentan retrasos en la salida en comparación con los retrasos en la llegada. Esto sugiere que los retrasos en la salida pueden ser más comunes o tener un impacto más notable en la puntualidad de los vuelos en comparación con los retrasos en la llegada.
    </div>""", unsafe_allow_html=True)


def mostrar_grafico_pastel_festivos(df, df_2021, df_2022, df_2023):
    st.subheader('Vuelos con retraso en días festivos')
    st.markdown("""<div style="text-align: justify; margin-bottom: 10px;">
        En el conjunto de datos, durante los días laborables, el 22.8% de los vuelos experimentan retrasos en la salida, mientras que el 10.3% tienen retrasos en la llegada. Por otro lado, durante los días festivos, el 97.8% de los vuelos presentan retrasos en la salida, y el 97.5% experimentan retrasos en la llegada. 
    </div>
    <div style="text-align: justify;">
        En 2021, durante los días laborables, el 23.9% de los vuelos sufrieron retrasos en la salida y el 10.2% en la llegada. En días festivos, estos porcentajes fueron del 97.7% y 97.4% respectivamente.
    </div>
    <div style="text-align: justify;">
        En 2022, durante los días laborables, el 26.4% de los vuelos experimentaron retrasos en la salida y el 12.4% en la llegada. En días festivos, estos valores fueron del 98.2% y 97.7% respectivamente.
    </div>
    <div style="text-align: justify;">
        En 2023, durante los días laborables, el 18.3% de los vuelos presentaron retrasos en la salida y el 8.43% en la llegada. En días festivos, estos porcentajes fueron del 97.5% y 97.3% respectivamente.
    </div>""", unsafe_allow_html=True)

    salidas_laborables  = df[(df['retraso_salida'] <= 15) & (df['festivos'] == 0)].shape[0]
    salidas_festivos    = df[(df['retraso_salida'] <= 15) & (df['festivos'] == 1)].shape[0]
    llegadas_laborables = df[(df['retraso_llegada'] <= 15) & (df['festivos'] == 0)].shape[0]
    llegadas_festivos   = df[(df['retraso_llegada'] <= 15) & (df['festivos'] == 1)].shape[0]

    fig = make_subplots(rows  = 2, cols = 2, subplot_titles = ("Salidas en días laborables", "Salidas en días festivos", "Llegadas en días laborables", "Llegadas en días festivos"), 
                        specs = [[{'type':'domain'}, {'type':'domain'}], [{'type':'domain'}, {'type':'domain'}]])

    fig.add_trace(go.Pie(labels =['Sin retraso', 'Con retraso'], values = [salidas_laborables, df.shape[0] - salidas_laborables]), 1, 1)
    fig.add_trace(go.Pie(labels = ['Sin retraso', 'Con retraso'], values = [salidas_festivos, df.shape[0] - salidas_festivos]), 1, 2)
    fig.add_trace(go.Pie(labels = ['Sin retraso', 'Con retraso'], values = [llegadas_laborables, df.shape[0] - llegadas_laborables]), 2, 1)
    fig.add_trace(go.Pie(labels = ['Sin retraso', 'Con retraso'], values = [llegadas_festivos, df.shape[0] - llegadas_festivos]), 2, 2)

    fig.update_layout(title_text = "Comparación del Porcentaje de Retrasos en Salidas y Llegadas de Vuelos en días festivos", 
                    width      = 800, 
                    height     = 600)

    fig.update_traces(pull = [0.05, 0.05], marker = dict(colors=px.colors.qualitative.Set3), rotation = 60)

    st.plotly_chart(fig)

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.expander("2021", expanded=False):
                salidas_laborables  = df_2021[(df_2021['retraso_salida'] <= 15) & (df_2021['festivos'] == 0)].shape[0]
                salidas_festivos    = df_2021[(df_2021['retraso_salida'] <= 15) & (df_2021['festivos'] == 1)].shape[0]
                llegadas_laborables = df_2021[(df_2021['retraso_llegada'] <= 15) & (df_2021['festivos'] == 0)].shape[0]
                llegadas_festivos   = df_2021[(df_2021['retraso_llegada'] <= 15) & (df_2021['festivos'] == 1)].shape[0]

                fig = make_subplots(rows  = 2, cols = 2, subplot_titles = ("Salidas en días laborables", "Salidas en días festivos", "Llegadas en días laborables", "Llegadas en días festivos"), 
                                    specs = [[{'type':'domain'}, {'type':'domain'}], [{'type':'domain'}, {'type':'domain'}]])

                fig.add_trace(go.Pie(labels =['Sin retraso', 'Con retraso'], values = [salidas_laborables, df.shape[0] - salidas_laborables]), 1, 1)
                fig.add_trace(go.Pie(labels = ['Sin retraso', 'Con retraso'], values = [salidas_festivos, df.shape[0] - salidas_festivos]), 1, 2)
                fig.add_trace(go.Pie(labels = ['Sin retraso', 'Con retraso'], values = [llegadas_laborables, df.shape[0] - llegadas_laborables]), 2, 1)
                fig.add_trace(go.Pie(labels = ['Sin retraso', 'Con retraso'], values = [llegadas_festivos, df.shape[0] - llegadas_festivos]), 2, 2)

                fig.update_layout(title_text = "Comparación del Porcentaje de Retrasos en Salidas y Llegadas de Vuelos en días festivos en 2021", 
                                width      = 800, 
                                height     = 600)

                fig.update_traces(pull = [0.05, 0.05], marker = dict(colors=px.colors.qualitative.Set3), rotation = 60)

                st.plotly_chart(fig)

    with col2:
        with st.expander("2022", expanded=False):
                           salidas_laborables  = df_2022[(df_2022['retraso_salida'] <= 15) & (df_2022['festivos'] == 0)].shape[0]
                           salidas_festivos    = df_2022[(df_2022['retraso_salida'] <= 15) & (df_2022['festivos'] == 1)].shape[0]
                           llegadas_laborables = df_2022[(df_2022['retraso_llegada'] <= 15) & (df_2022['festivos'] == 0)].shape[0]
                           llegadas_festivos   = df_2022[(df_2022['retraso_llegada'] <= 15) & (df_2022['festivos'] == 1)].shape[0]

                           fig = make_subplots(rows  = 2, cols = 2, subplot_titles = ("Salidas en días laborables", "Salidas en días festivos", "Llegadas en días laborables", "Llegadas en días festivos"), 
                                            specs = [[{'type':'domain'}, {'type':'domain'}], [{'type':'domain'}, {'type':'domain'}]])

                           fig.add_trace(go.Pie(labels =['Sin retraso', 'Con retraso'], values = [salidas_laborables, df.shape[0] - salidas_laborables]), 1, 1)
                           fig.add_trace(go.Pie(labels = ['Sin retraso', 'Con retraso'], values = [salidas_festivos, df.shape[0] - salidas_festivos]), 1, 2)
                           fig.add_trace(go.Pie(labels = ['Sin retraso', 'Con retraso'], values = [llegadas_laborables, df.shape[0] - llegadas_laborables]), 2, 1)
                           fig.add_trace(go.Pie(labels = ['Sin retraso', 'Con retraso'], values = [llegadas_festivos, df.shape[0] - llegadas_festivos]), 2, 2)

                           fig.update_layout(title_text = "Comparación del Porcentaje de Retrasos en Salidas y Llegadas de Vuelos en días festivos en 2022", 
                                        width      = 800, 
                                        height     = 600)

                           fig.update_traces(pull = [0.05, 0.05], marker = dict(colors=px.colors.qualitative.Set3), rotation = 60)

                           st.plotly_chart(fig)

    with col3:
        with st.expander("2023", expanded=False):
                           salidas_laborables  = df_2023[(df_2023['retraso_salida'] <= 15) & (df_2023['festivos'] == 0)].shape[0]
                           salidas_festivos    = df_2023[(df_2023['retraso_salida'] <= 15) & (df_2023['festivos'] == 1)].shape[0]
                           llegadas_laborables = df_2023[(df_2023['retraso_llegada'] <= 15) & (df_2023['festivos'] == 0)].shape[0]
                           llegadas_festivos   = df_2023[(df_2023['retraso_llegada'] <= 15) & (df_2023['festivos'] == 1)].shape[0]

                           fig = make_subplots(rows  = 2, cols = 2, subplot_titles = ("Salidas en días laborables", "Salidas en días festivos", "Llegadas en días laborables", "Llegadas en días festivos"), 
                                            specs = [[{'type':'domain'}, {'type':'domain'}], [{'type':'domain'}, {'type':'domain'}]])

                           fig.add_trace(go.Pie(labels =['Sin retraso', 'Con retraso'], values = [salidas_laborables, df.shape[0] - salidas_laborables]), 1, 1)
                           fig.add_trace(go.Pie(labels = ['Sin retraso', 'Con retraso'], values = [salidas_festivos, df.shape[0] - salidas_festivos]), 1, 2)
                           fig.add_trace(go.Pie(labels = ['Sin retraso', 'Con retraso'], values = [llegadas_laborables, df.shape[0] - llegadas_laborables]), 2, 1)
                           fig.add_trace(go.Pie(labels = ['Sin retraso', 'Con retraso'], values = [llegadas_festivos, df.shape[0] - llegadas_festivos]), 2, 2)

                           fig.update_layout(title_text = "Comparación del Porcentaje de Retrasos en Salidas y Llegadas de Vuelos en días festivos en 2023", 
                                        width      = 800, 
                                        height     = 600)

                           fig.update_traces(pull = [0.05, 0.05], marker = dict(colors=px.colors.qualitative.Set3), rotation = 60)

                           st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify; margin-bottom: 10px;">
        En cada año, los porcentajes de retraso fueron más altos en las salidas que en las llegadas, tanto en días laborables como festivos. 
    </div>
    <div style="text-align: justify; margin-bottom: 10px;">
        En todos los años, los días festivos presentaron un alto porcentaje de vuelos con retraso tanto en la salida como en la llegada, en comparación con los días laborables. Este incremento tan notorio puede deberse a una combinación de varios factores, algunas interpretaciones que le damos son la reducción en el número de trabajadores durante los días festivos o un mayor volumen de viajes y por consiguiente mayor congestión en los aeropuertos...
    </div>
    <div style="text-align: justify;">
        En general, hubo una mejora en la puntualidad de los vuelos durante los días laborables de 2021 a 2023, con una disminución en los porcentajes de retraso tanto en la salida como en la llegada. Sin embargo, esta tendencia no se observa de manera consistente en los días festivos, donde los porcentajes de retraso se mantuvieron altos en todos los años.
    </div>""", unsafe_allow_html=True)

    

def mostrar_grafico_barras_retraso_aerolineas(df, df_2021, df_2022, df_2023):
    st.subheader('Gráfico de barras que muestra la cantidad de vuelos con y sin retraso en la llegada, desglosado por aerolínea')
    st.markdown("""<div style="text-align: justify; margin-bottom: 10px;">
        Está puesto con total descending para que cuando se seleccione uno salga el que más tiene retrasos o puntualidad. En el conjunto de los datos Southwest Airlines tiene la mayor cantidad de vuelos con retraso en la llegada, con un total de 36799 vuelos. Es el que menos vuelos con retraso tiene también, porque es el que más número total de vuelos realiza.
    </div>
    <div style="text-align: justify;">
        Cuando examinamos los datos por año, como hemos visto en gráficos previos, Southwest Airlines se mantiene como líder, mientras que American Airlines y Delta Air Lines compiten por el segundo lugar.
    </div>""", unsafe_allow_html=True)


    retrasos_llegada = df[df['retraso_llegada'] > 15]
    sin_retraso_llegada = df[df['retraso_llegada'] <= 15]

    retrasos_aerolinea_llegada = retrasos_llegada.groupby(['aerolinea']).size().reset_index(name='con_retraso')

    sin_retraso_aerolinea = sin_retraso_llegada.groupby(['aerolinea']).size().reset_index()
    sin_retraso_aerolinea.columns = ['aerolinea', 'sin_retraso']

    retrasos_aerolinea = retrasos_aerolinea_llegada.merge(sin_retraso_aerolinea, on='aerolinea', how='left').fillna(0)

    fig = px.bar(retrasos_aerolinea, 
                x                  = 'aerolinea', 
                y                  = ['con_retraso', 'sin_retraso'], 
                title              = 'Cantidad de vuelos con y sin retraso en la llegada por aerolínea',
                labels             = {'aerolinea': 'Aerolínea', 'value': 'Cantidad de vuelos'},
                opacity            = 0.7, 
                color_discrete_map = {"con_retraso": "gray", "sin_retraso": "pink"})

    fig.update_layout(title_x = 0.2, xaxis = {'categoryorder': 'total descending'})

    st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify">
    Para Delta Air Lines y SkyWest Airlines, ambas aerolíneas muestran una proporción relativamente baja de vuelos con retraso en la llegada en comparación con el total de vuelos. Tienen un buen desempeño en términos de puntualidad en comparación con otras aerolíneas.
                </div>""", unsafe_allow_html=True)



def mostrar_grafico_barras_retraso_aeropuertos(df, df_2021, df_2022, df_2023):
    st.subheader('Aeropuertos de origen con más retrasos en vuelos')

    st.markdown("""<div style="text-align: justify">
    Creamos un gráfico de barras de los aeropuertos de origen con mayor cantidad de vuelos retrasados en la llegada. Dado que el aeropuerto de origen cuenta con 362 valores, hemos restringido la visualización a los 15 aeropuertos con el mayor número de vuelos retrasados. Estos aeropuertos son precisamente aquellos con la mayor afluencia de vuelos.
                </div>""", unsafe_allow_html=True)

    retrasos_llegada = df[df['retraso_llegada'] > 15]
    sin_retraso_llegada = df[df['retraso_llegada'] <= 15]

    retraso_aeropuerto_llegada = retrasos_llegada.groupby(['aeropuerto_origen']).size().reset_index(name='con_retraso')

    sin_retraso_aeropuerto = sin_retraso_llegada.groupby(['aeropuerto_origen']).size().reset_index()
    sin_retraso_aeropuerto.columns = ['aeropuerto_origen', 'sin_retraso']

    retrasos_aeropuerto = retraso_aeropuerto_llegada.merge(sin_retraso_aeropuerto, on='aeropuerto_origen', how='left').fillna(0)
    retrasos_aeropuerto_ordenado = retrasos_aeropuerto.sort_values(by='con_retraso', ascending=False)
    retrasos_aeropuerto_ordenado = retrasos_aeropuerto_ordenado[:15]
    fig = px.bar(retrasos_aeropuerto_ordenado, x='aeropuerto_origen', y=['con_retraso', 'sin_retraso'], 
                title='Top 15 aeropuertos de origen con mayor cantidad de vuelos con retraso en la llegada',
                labels={'aeropuerto_origen': 'Aeropuerto origen', 'value': 'Cantidad de vuelos'},
                opacity= 0.7, color_discrete_map= {"con_retraso": "turquoise", "sin_retraso": "tan"})

    fig.update_layout(xaxis={'categoryorder': 'total descending'})

    st.plotly_chart(fig)


    col1, col2, col3 = st.columns(3)

    with col1:
        with st.expander("2021", expanded=False):
            retrasos_llegada = df_2021[df_2021['retraso_llegada'] > 15]
            sin_retraso_llegada = df_2021[df_2021['retraso_llegada'] <= 15]

            retraso_aeropuerto_llegada = retrasos_llegada.groupby(['aeropuerto_origen']).size().reset_index(name='con_retraso')

            sin_retraso_aeropuerto = sin_retraso_llegada.groupby(['aeropuerto_origen']).size().reset_index()
            sin_retraso_aeropuerto.columns = ['aeropuerto_origen', 'sin_retraso']

            retrasos_aeropuerto = retraso_aeropuerto_llegada.merge(sin_retraso_aeropuerto, on='aeropuerto_origen', how='left').fillna(0)
            retrasos_aeropuerto_ordenado = retrasos_aeropuerto.sort_values(by='con_retraso', ascending=False)
            retrasos_aeropuerto_ordenado = retrasos_aeropuerto_ordenado[:15]
            fig = px.bar(retrasos_aeropuerto_ordenado, x='aeropuerto_origen', y=['con_retraso', 'sin_retraso'], 
                        title='Top 15 aeropuertos de origen con mayor cantidad de vuelos con retraso en la llegada en 2021',
                        labels={'aeropuerto_origen': 'Aeropuerto origen', 'value': 'Cantidad de vuelos'},
                        opacity= 0.7, color_discrete_map= {"con_retraso": "turquoise", "sin_retraso": "tan"})

            fig.update_layout(xaxis={'categoryorder': 'total descending'})

            st.plotly_chart(fig)

    with col2:
        with st.expander("2022", expanded=False):
            retrasos_llegada = df_2021[df_2021['retraso_llegada'] > 15]
            sin_retraso_llegada = df_2021[df_2021['retraso_llegada'] <= 15]

            retraso_aeropuerto_llegada = retrasos_llegada.groupby(['aeropuerto_origen']).size().reset_index(name='con_retraso')

            sin_retraso_aeropuerto = sin_retraso_llegada.groupby(['aeropuerto_origen']).size().reset_index()
            sin_retraso_aeropuerto.columns = ['aeropuerto_origen', 'sin_retraso']

            retrasos_aeropuerto = retraso_aeropuerto_llegada.merge(sin_retraso_aeropuerto, on='aeropuerto_origen', how='left').fillna(0)
            retrasos_aeropuerto_ordenado = retrasos_aeropuerto.sort_values(by='con_retraso', ascending=False)
            retrasos_aeropuerto_ordenado = retrasos_aeropuerto_ordenado[:15]
            fig = px.bar(retrasos_aeropuerto_ordenado, x='aeropuerto_origen', y=['con_retraso', 'sin_retraso'], 
                        title='Top 15 aeropuertos de origen con mayor cantidad de vuelos con retraso en la llegada en 2022',
                        labels={'aeropuerto_origen': 'Aeropuerto origen', 'value': 'Cantidad de vuelos'},
                        opacity= 0.7, color_discrete_map= {"con_retraso": "turquoise", "sin_retraso": "tan"})

            fig.update_layout(xaxis={'categoryorder': 'total descending'})

            st.plotly_chart(fig)

    with col3:
        with st.expander("2023", expanded=False):
            retrasos_llegada = df_2021[df_2021['retraso_llegada'] > 15]
            sin_retraso_llegada = df_2021[df_2021['retraso_llegada'] <= 15]

            retraso_aeropuerto_llegada = retrasos_llegada.groupby(['aeropuerto_origen']).size().reset_index(name='con_retraso')

            sin_retraso_aeropuerto = sin_retraso_llegada.groupby(['aeropuerto_origen']).size().reset_index()
            sin_retraso_aeropuerto.columns = ['aeropuerto_origen', 'sin_retraso']

            retrasos_aeropuerto = retraso_aeropuerto_llegada.merge(sin_retraso_aeropuerto, on='aeropuerto_origen', how='left').fillna(0)
            retrasos_aeropuerto_ordenado = retrasos_aeropuerto.sort_values(by='con_retraso', ascending=False)
            retrasos_aeropuerto_ordenado = retrasos_aeropuerto_ordenado[:15]
            fig = px.bar(retrasos_aeropuerto_ordenado, x='aeropuerto_origen', y=['con_retraso', 'sin_retraso'], 
                        title='Top 15 aeropuertos de origen con mayor cantidad de vuelos con retraso en la llegada en 2023',
                        labels={'aeropuerto_origen': 'Aeropuerto origen', 'value': 'Cantidad de vuelos'},
                        opacity= 0.7, color_discrete_map= {"con_retraso": "turquoise", "sin_retraso": "tan"})

            fig.update_layout(xaxis={'categoryorder': 'total descending'})

            st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify; margin-bottom: 10px;">
        Al analizar los tres años por separado, se destaca que el aeropuerto con el mayor número total de vuelos en todos los años es Hartsfield-Jackson Atlanta International. Sin embargo, en cuanto al número de retrasos, el primer puesto varía entre Dallas/Fort Worth International y Denver International. Es importante señalar que, aunque el número de retrasos aumentó considerablemente en 2022, en 2023 volvió a descender.
    </div>
    <div style="text-align: justify;">
        En todos los años, los aeropuertos de origen con mayor cantidad de vuelos los tienen Dallas/Fort Worth International, Denver International y Hartsfield-Jackson Atlanta International. Sin embargo, en cuanto a vuelos con retraso, Denver y Dallas ocupan los primeros lugares, seguidos por Harry Reid International, mientras que Hartsfield-Jackson se ubica en el octavo lugar en términos de retrasos.
    </div>""", unsafe_allow_html=True)



def mostrar_grafico_lineas_diciembre(df):
    st.subheader('Vuelos diarios en Diciembre')

    st.markdown("""<div style="text-align: justify">
    Creamos subgráficos para visualizar el número de vuelos por día en diciembre, desglosado por años: 2021, 2022 y 2023. 
                </div>""", unsafe_allow_html=True)


    df_fechas = df.groupby(['anio', 'fecha']).size().reset_index(name ='numero_vuelos')

    fig1 = px.line(df_fechas[(df_fechas['anio'] == 2021)], x ='fecha', y = 'numero_vuelos', color_discrete_sequence = ['skyblue'])
    fig2 = px.line(df_fechas[(df_fechas['anio'] == 2022)], x ='fecha', y = 'numero_vuelos', color_discrete_sequence = ['violet'])
    fig3 = px.line(df_fechas[(df_fechas['anio'] == 2023)], x ='fecha', y = 'numero_vuelos', color_discrete_sequence = ['springgreen'])

    fig = make_subplots(rows=1, cols=3, subplot_titles=('2021', '2022', '2023'))
    fig.add_trace(fig1.data[0], row = 1, col = 1)
    fig.add_trace(fig2.data[0], row = 1, col = 2)
    fig.add_trace(fig3.data[0], row = 1, col = 3)

    for n in range(1,4):
        fig.update_xaxes(title_text = 'Fecha', row = 1, col = n)

    fig.update_yaxes(title_text  = 'Número de vuelos', row = 1, col = 1)
    fig.update_layout(title_text = 'Número de vuelos por días en Diciembre', title_x = 0.3)

    st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify">
    Es destacable que hay un comportamiento similar en los datos de los tres años, aunque se observa un claro aumento en el número de vuelos según pasan los años. El pico descendente del 24-25 de diciembre indica una disminución en el número de vuelos durante la víspera y el día de Navidad.
                </div>""", unsafe_allow_html=True)


def mostrar_grafico_lineas_acumulado_diciembre(df):
    st.subheader('Vuelos diarios acumulados')

    st.markdown("""<div style="text-align: justify">
    Este gráfico presenta el número acumulado de vuelos por día durante el mes de diciembre en diferentes años. Cada línea muestra la acumulación de vuelos a medida que transcurren los días del mes.
                </div>""", unsafe_allow_html=True)


    df_fechas = df.groupby(['anio', 'fecha']).size().reset_index(name='numero_vuelos')
    df_fechas['vuelos_acumulativo'] = df_fechas.groupby('anio')['numero_vuelos'].cumsum()

    fig1 = px.line(df_fechas[(df_fechas['anio'] == 2021)], x='fecha', y='vuelos_acumulativo', color_discrete_sequence=['skyblue'])
    fig2 = px.line(df_fechas[(df_fechas['anio'] == 2022)], x='fecha', y='vuelos_acumulativo', color_discrete_sequence=['violet'])
    fig3 = px.line(df_fechas[(df_fechas['anio'] == 2023)], x='fecha', y='vuelos_acumulativo', color_discrete_sequence=['springgreen'])

    fig = make_subplots(rows=1, cols=3, subplot_titles=('2021', '2022', '2023'))
    fig.add_trace(fig1.data[0], row=1, col=1)
    fig.add_trace(fig2.data[0], row=1, col=2)
    fig.add_trace(fig3.data[0], row=1, col=3)

    for n in range(1, 4):
        fig.update_xaxes(title_text='Fecha', row=1, col=n)

    fig.update_yaxes(title_text='Número de vuelos acumulados', row=1, col=1)
    fig.update_layout(title_text='Número de vuelos acumulados por día en diciembre', title_x=0.3)
    st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify">
    Se evidencia un crecimiento constante en el número acumulado de vuelos a lo largo de los años, destacando un incremento más marcado en el año 2023.
                </div>""", unsafe_allow_html=True)


def mostrar_grafico_rango_horario_salidas_llegadas(df):
    st.subheader('Salidas y llegadas por rango horario')
    st.markdown("""<div style="text-align: justify">
    Asignamos un rango horario a los vuelos para representar la cantidad de vuelos que salen y llegan en la madrugada, en la mañana, tarde y noche.
    </div>""", unsafe_allow_html=True)


    def asignar_rango(hora):
        if hora.hour < 6:
            return "00:00 - 05:59"
        elif hora.hour < 12:
            return "06:00 - 11:59"
        elif hora.hour < 18:
            return "12:00 - 17:59"
        else:
            return "18:00 - 23:59"

    llegada_salida = df[['hora_salida_real', 'hora_llegada_real']]

    llegada_salida['rango_salida'] = llegada_salida['hora_salida_real'].apply(asignar_rango)
    llegada_salida['rango_llegada'] = llegada_salida['hora_llegada_real'].apply(asignar_rango)

    fig = px.histogram(llegada_salida, x=["rango_salida", "rango_llegada"], 
                    title="Cantidad de llegadas/salidas por rangos horarios",
                    labels={"value": "Rango horario", "count": "Cantidad"},
                    barmode="group",
                    opacity= 0.7, color_discrete_map= {"rango_salida": "royalblue", "rango_llegada": "crimson"})

    fig.update_layout(title_x=0.2)
    st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify">
    Predominantemente, los vuelos tienen lugar en la madrugada o por la mañana, mientras que la mayoría de las llegadas ocurren durante la mañana.
                </div>""", unsafe_allow_html=True)


def mostrar_grafico_rango_horario_retrasos(df):
    st.subheader('Retrasos por rango horario')
    st.markdown("""<div style="text-align: justify">
    Generamos un gráfico para investigar el número retrasos en salidas y llegadas por rango horario
        </div>""", unsafe_allow_html=True)
    def asignar_rango(hora):
        if hora.hour < 6:
            return "00:00 - 05:59"
        elif hora.hour < 12:
            return "06:00 - 11:59"
        elif hora.hour < 18:
            return "12:00 - 17:59"
        else:
            return "18:00 - 23:59"
        
    llegada_salida_retrasos = df[['hora_salida_real', 'hora_llegada_real', 'retraso_llegada']]

    llegada_salida_retrasos['rango_salida'] = llegada_salida_retrasos['hora_salida_real'].apply(asignar_rango)
    llegada_salida_retrasos['rango_llegada'] = llegada_salida_retrasos['hora_llegada_real'].apply(asignar_rango)
    llegada_salida_retrasos['retraso'] = llegada_salida_retrasos['retraso_llegada'].apply(lambda x: 1 if x > 15 else 0)

    salida_retrasos =  llegada_salida_retrasos.groupby(['rango_salida']).agg({'retraso' : 'sum'}).reset_index()
    llegada_retrasos =  llegada_salida_retrasos.groupby(['rango_llegada']).agg({'retraso' : 'sum'}).reset_index()

    fig1 = px.bar(salida_retrasos, x='rango_salida', y='retraso', title='Retrasos por Rango de Salida', opacity= 0.7)
    fig2 = px.bar(llegada_retrasos, x='rango_llegada', y='retraso', title='Retrasos por Rango de Llegada', opacity= 0.7)

    fig1.update_xaxes(title_text='Rango de Salida')
    fig1.update_yaxes(title_text='Cantidad de Retrasos')
    fig2.update_xaxes(title_text='Rango de Llegada')
    fig2.update_yaxes(title_text='Cantidad de Retrasos')

    fig = make_subplots(rows=1, cols=2, subplot_titles=('Retrasos por Rango de Salida', 'Retrasos por Rango de Llegada'))
    fig.add_trace(fig1['data'][0], row=1, col=1)
    fig.add_trace(fig2['data'][0], row=1, col=2)
    st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify">
    Se evidencia que tanto en las salidas como en las llegadas, la mayoría de los retrasos se concentran en el rango horario de la tarde-noche. Esta observación resulta sorprendente dado que este no es el período de mayor tráfico aéreo. Una posible explicación podría estar relacionada con la congestión del tráfico aéreo en estos horarios.
                </div>""", unsafe_allow_html=True)


def mostrar_grafico_vuelos_semanales_retraso(df, df_2021, df_2022, df_2023):
    
    st.subheader('Gráfico para observar el número de vuelos por día de la semana, con y sin retrasos')
    st.markdown("""<div style="text-align: justify">
    Se aprecia que los viernes registran la mayor cantidad de vuelos, seguidos de cerca por los jueves. Sin embargo, al examinar los días con más retrasos, la situación cambia: primero se observa el jueves, seguido por el viernes.
                </div>""", unsafe_allow_html=True)

    retrasos_llegada = df[df['retraso_llegada'] > 15]
    sin_retraso_llegada = df[df['retraso_llegada'] <= 15]

    retraso_dia_semana = retrasos_llegada.groupby(['dia_semana']).size().reset_index(name='con_retraso')
    sin_retraso_semana = sin_retraso_llegada.groupby(['dia_semana']).size().reset_index()
    sin_retraso_semana.columns = ['dia_semana', 'sin_retraso']

    retrasos_dia_semana = retraso_dia_semana.merge(sin_retraso_semana, on='dia_semana', how='left').fillna(0)

    fig = px.bar(retrasos_dia_semana, 
                x       = "dia_semana",  
                y       = ["sin_retraso", "con_retraso"], 
                barmode = "stack", 
                labels  = {"value": "Cantidad de vuelos", "dia_semana": "Día de la semana"},  
                color_discrete_map = {"con_retraso": "lightsalmon", "sin_retraso": "pink"})

    fig.update_layout(
        title = "Cantidad de vuelos con y sin retraso por día de la semana",
        xaxis = dict(
            tickmode = "array",
            tickvals = list(range(7)),
            ticktext = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
            type = 'category',
            categoryorder = 'total descending'),
        title_x = 0.2)

    st.plotly_chart(fig)


    col1, col2, col3 = st.columns(3)

    with col1:
        with st.expander("2021", expanded=False):
            retrasos_llegada = df_2021[df_2021['retraso_llegada'] > 15]
            sin_retraso_llegada = df_2021[df_2021['retraso_llegada'] <= 15]

            retraso_dia_semana = retrasos_llegada.groupby(['dia_semana']).size().reset_index(name='con_retraso')
            sin_retraso_semana = sin_retraso_llegada.groupby(['dia_semana']).size().reset_index()
            sin_retraso_semana.columns = ['dia_semana', 'sin_retraso']

            retrasos_dia_semana = retraso_dia_semana.merge(sin_retraso_semana, on='dia_semana', how='left').fillna(0)

            fig = px.bar(retrasos_dia_semana, 
                        x       = "dia_semana",  
                        y       = ["sin_retraso", "con_retraso"], 
                        barmode = "stack", 
                        labels  = {"value": "Cantidad de vuelos", "dia_semana": "Día de la semana"},  
                        color_discrete_map = {"con_retraso": "lightsalmon", "sin_retraso": "pink"})

            fig.update_layout(
                title = "Cantidad de vuelos con y sin retraso por día de la semana",
                xaxis = dict(
                    tickmode = "array",
                    tickvals = list(range(7)),
                    ticktext = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
                    type = 'category',
                    categoryorder = 'total descending'),
                title_x = 0.2)

            st.plotly_chart(fig)

    with col2:
        with st.expander("2022", expanded=False):
            retrasos_llegada = df_2022[df_2022['retraso_llegada'] > 15]
            sin_retraso_llegada = df_2022[df_2022['retraso_llegada'] <= 15]

            retraso_dia_semana = retrasos_llegada.groupby(['dia_semana']).size().reset_index(name='con_retraso')
            sin_retraso_semana = sin_retraso_llegada.groupby(['dia_semana']).size().reset_index()
            sin_retraso_semana.columns = ['dia_semana', 'sin_retraso']

            retrasos_dia_semana = retraso_dia_semana.merge(sin_retraso_semana, on='dia_semana', how='left').fillna(0)

            fig = px.bar(retrasos_dia_semana, 
                        x       = "dia_semana",  
                        y       = ["sin_retraso", "con_retraso"], 
                        barmode = "stack", 
                        labels  = {"value": "Cantidad de vuelos", "dia_semana": "Día de la semana"},  
                        color_discrete_map = {"con_retraso": "lightsalmon", "sin_retraso": "pink"})

            fig.update_layout(
                title = "Cantidad de vuelos con y sin retraso por día de la semana",
                xaxis = dict(
                    tickmode = "array",
                    tickvals = list(range(7)),
                    ticktext = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
                    type = 'category',
                    categoryorder = 'total descending'),
                title_x = 0.2)

            st.plotly_chart(fig)

    with col3:
        with st.expander("2023", expanded=False):
            retrasos_llegada = df_2023[df_2023['retraso_llegada'] > 15]
            sin_retraso_llegada = df_2023[df_2023['retraso_llegada'] <= 15]

            retraso_dia_semana = retrasos_llegada.groupby(['dia_semana']).size().reset_index(name='con_retraso')
            sin_retraso_semana = sin_retraso_llegada.groupby(['dia_semana']).size().reset_index()
            sin_retraso_semana.columns = ['dia_semana', 'sin_retraso']

            retrasos_dia_semana = retraso_dia_semana.merge(sin_retraso_semana, on='dia_semana', how='left').fillna(0)

            fig = px.bar(retrasos_dia_semana, 
                        x       = "dia_semana",  
                        y       = ["sin_retraso", "con_retraso"], 
                        barmode = "stack", 
                        labels  = {"value": "Cantidad de vuelos", "dia_semana": "Día de la semana"},  
                        color_discrete_map = {"con_retraso": "lightsalmon", "sin_retraso": "pink"})

            fig.update_layout(
                title = "Cantidad de vuelos con y sin retraso por día de la semana",
                xaxis = dict(
                    tickmode = "array",
                    tickvals = list(range(7)),
                    ticktext = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
                    type = 'category',
                    categoryorder = 'total descending'),
                title_x = 0.2)

            st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify; margin-bottom: 10px;">
        Al analizar los datos por año, observamos una gran variabilidad en los días con mayor número de retrasos. En 2021, los jueves y los lunes destacaron con un mayor número de retrasos, mientras que en 2022 los viernes experimentaron más retrasos, seguidos de los jueves. En 2023, el domingo corona con un gran número de retrasos, seguido por el viernes.
    </div>
    <div style="text-align: justify;">
        Si consideramos todos los datos en conjunto, a pesar de que los viernes son los días con mayor cantidad de vuelos, posiblemente debido a la demanda de viajes de fin de semana, los jueves muestran una tendencia más alta a experimentar retrasos.
    </div>""", unsafe_allow_html=True)
    


def mostrar_barras_retrasos_mas_comunes(df):
    st.subheader('Tipos de retrasos más comunes')
    st.markdown("""<div style="text-align: justify">
    Es evidente que los retrasos relacionados con la seguridad prácticamente no tienen incidencia. El tipo de retraso más frecuente es el "tiempo de retraso por aerolínea", con más de de 9,000,000 minutos, seguido por "retraso por sistema de aviación" con más de 3,000,000 minutos.
    </div>""", unsafe_allow_html=True)

    tipos_retrasos = df[['tiempo_retraso_aerolinea', 'tiempo_retraso_clima', 'tiempo_retraso_sistema_aviacion', 'tiempo_retraso_seguridad']]
    total_tipo = tipos_retrasos.sum()

    fig = px.bar(x=total_tipo.index, y=total_tipo.values, labels={'x': 'Tipo de retraso', 'y': 'Total minutos'},
                title='Total de minutos por cada tipo de retraso', color_discrete_sequence=['skyblue'])
    fig.update_layout(title_x=0.3, xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify">
    Los retrasos relacionados con el tiempo de la aerolínea son significativamente más frecuentes y prolongados en comparación con el resto. Esto podría indicar que las aerolíneas tienen un papel importante en la gestión de sus horarios y operaciones para minimizar los retrasos y mejorar la puntualidad de los vuelos.
                </div>""", unsafe_allow_html=True)
    

def mostrar_pastel_retrasos_mas_comunes(df):
    st.subheader('Retrasos por tiempo y número')
    st.markdown("""<div style="text-align: justify">
    Este gráfico de pastel hace un análisis en porcentaje de los retrasos aéreos. Se divide en dos, la distribución del tiempo acumulado de retraso por tipo y la frecuencia de ocurrencia de cada tipo de retraso en relación con el total de retrasos.
                </div>""", unsafe_allow_html=True)
    tipos_retrasos = df[['tiempo_retraso_aerolinea', 'tiempo_retraso_clima', 'tiempo_retraso_sistema_aviacion', 'tiempo_retraso_seguridad']]

    porcentaje_por_columna = tipos_retrasos.sum() / tipos_retrasos.sum().sum() * 100 
    valores_no_cero = tipos_retrasos.astype(bool).sum(axis=0) 

    fig = make_subplots(rows=1, cols=2,
                        subplot_titles = ("Tiempo de retraso acumulados.", "Porcentaje de retrasos."),
                        specs=[[{'type':'domain'}, {'type':'domain'}]])

    fig.add_trace(go.Pie(labels=porcentaje_por_columna.index, values=porcentaje_por_columna.values), row = 1,col = 1)
    fig.add_trace(go.Pie(labels=valores_no_cero.index, values=valores_no_cero.values), row = 1,col =  2)

    fig.update_layout(title_text = 'Análisis de Retrasos Aéreos',
                    title_x    = 0.3, 
                    width      = 800, 
                    height     = 600)

    fig.update_traces(pull = [0.05, 0.05], marker = dict(colors=px.colors.qualitative.Set3))
    st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify">
    Como se evidenció en el gráfico anterior, la mayor cantidad de tiempo de retraso se concentra en el retraso por aerolínea, que es el más frecuente en términos de incidencia. Sin embargo, es notable que el retraso debido al sistema de aviación también es bastante recurrente.
    La cantidad frecuente de retrasos causados por problemas en el sistema de aviación resalta la necesidad de mejorar la eficiencia y confiabilidad de la gestión del tráfico aéreo y la infraestructura de los aeropuertos.
    </div>""", unsafe_allow_html=True)



def mostrar_estados_origen_retraso(df):
    st.subheader('Estados de origen y retrasos')
    st.markdown("""<div style="text-align: justify">
    El gráfico de barras muestra el número total de vuelos de llegada, revelando que los estados de Texas, California y Florida, además de ser los más concurridos, también experimentan más retrasos debido a su elevado número de vuelos.
    </div>""", unsafe_allow_html=True)

    retrasos_llegada = df[df['retraso_llegada'] > 15]
    sin_retraso_llegada = df[df['retraso_llegada'] <= 15]

    retrasos_estados_origen = retrasos_llegada.groupby(['estado_origen']).size().reset_index(name = 'con_retraso')
    sin_retraso_estados_origen = sin_retraso_llegada.groupby(['estado_origen']).size().reset_index(name = 'sin_retraso')

    estados = retrasos_estados_origen.merge(sin_retraso_estados_origen, on = 'estado_origen', how =  'left').fillna(0)
    estados_EEUU = {
        'TX': 'Texas',
        'OH': 'Ohio',
        'GA': 'Georgia',
        'MS': 'Mississippi',
        'FL': 'Florida',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'PA': 'Pennsylvania',
        'MO': 'Missouri',
        'AK': 'Alaska',
        'HI': 'Hawaii',
        'MI': 'Michigan',
        'MT': 'Montana',
        'NE': 'Nebraska',
        'NJ': 'New Jersey',
        'TN': 'Tennessee',
        'WI': 'Wisconsin',
        'LA': 'Louisiana',
        'WY': 'Wyoming',
        'NV': 'Nevada',
        'OK': 'Oklahoma',
        'WV': 'West Virginia',
        'ID': 'Idaho',
        'KY': 'Kentucky',
        'KS': 'Kansas',
        'AR': 'Arkansas',
        'CA': 'California',
        'CO': 'Colorado',
        'NH': 'New Hampshire',
        'IA': 'Iowa',
        'OR': 'Oregon',
        'MN': 'Minnesota',
        'UT': 'Utah',
        'AL': 'Alabama',
        'IL': 'Illinois',
        'SC': 'South Carolina',
        'NY': 'New York',
        'VA': 'Virginia',
        'MD': 'Maryland',
        'TT': 'Trust Territory',
        'WA': 'Washington',
        'AZ': 'Arizona',
        'SD': 'South Dakota',
        'PR': 'Puerto Rico',
        'ME': 'Maine',
        'RI': 'Rhode Island',
        'NM': 'New Mexico',
        'IN': 'Indiana',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'MA': 'Massachusetts',
        'VT': 'Vermont',
        'VI': 'Virgin Islands',
        'CT': 'Connecticut'
    }

    estados['estado_origen'] = estados['estado_origen'].map(estados_EEUU)

    fig = px.bar(estados, 
                x                  = 'estado_origen', 
                y                  = ['con_retraso', 'sin_retraso'], 
                title              = 'Cantidad de vuelos con y sin retraso en la llegada desde estado de origen',
                labels             = {'estado_origen': 'Estado', 'value': 'Cantidad de vuelos'},
                opacity            = 0.8, 
                color_discrete_map = {"con_retraso": "gray", "sin_retraso": "skyblue"})

    fig.update_layout(title_x = 0.1, xaxis = {'categoryorder': 'total descending'})
    st.plotly_chart(fig)
    st.markdown("""<div style="text-align: justify">
    Los estados de Texas, California y Florida tienen el mayor número de vuelos, en ese orden. Sin embargo, en términos de retrasos, Florida lidera, seguido de Texas y luego California.
    El hecho de que Florida experimente más retrasos sugiere que pueden existir desafíos adicionales en los aeropuertos de Florida que afectan la puntualidad de los vuelos. Esto podría deberse a una variedad de factores, como la congestión del tráfico aéreo, la capacidad de los aeropuertos, o problemas específicos de gestión de vuelos en esa región.
    </div>""", unsafe_allow_html=True)


def mostrar_diagrama_caja_millas(df):
    st.subheader('Distancia en Millas')
    st.markdown("""<div style="text-align: justify">
    Las millas mínimas registradas son 32.06 y las máximas alcanzan 5081.93. La mediana de las millas es de 692, y se observan valores atípicos a partir de 2087 millas.
    </div>""", unsafe_allow_html=True)

    fig = px.box(data_frame= df,
                    x = 'distancia_millas')

    fig.update_layout(title='Diagrama de Caja de la Distancia en Millas', title_x=0.2)
    st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify">
    La amplia gama de millas registradas sugiere una gran variabilidad en las distancias de los vuelos. La mediana de 692 indica que la mitad de los vuelos tienen una distancia menor a este valor, lo que sugiere que la mayoría de los vuelos son de corta o media distancia. 
    </div>""", unsafe_allow_html=True)


def mostrar_histograma_millas(df):
    st.subheader('Histograma de millas')
    st.markdown("""<div style="text-align: justify">
    Es interesante observar que la media está alrededor de 825-830 millas, mientras que la mediana está en un rango más bajo, aproximadamente entre 690 y 695 millas. 
    </div>""", unsafe_allow_html=True)

    fig = px.histogram(df, x="distancia_millas", title="Histograma de Distancia en Millas",
                        opacity                 = 0.4)
    media = np.mean(df['distancia_millas'])
    mediana = np.median(df['distancia_millas'])

    fig.add_vline(x=media, line_dash="dash", line_color="red", name="Media")
    fig.add_vline(x=mediana, line_dash="dash", line_color="green", name="Mediana")

    fig.update_layout(title_x=0.3)
    st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify">
    Parece que hay una discrepancia entre la media y la mediana en el histograma. Esta diferencia sugiere que hay algunos vuelos de larga distancia que están influyendo en la media y desplazándola hacia valores más altos, mientras que la mayoría de los vuelos se concentran en distancias más cortas, lo que se refleja en la mediana. Los vuelos internos en Estados Unidos tienden a cubrir distancias más cortas.
    </div>""", unsafe_allow_html=True)


def mostrar_barras_millas(df):
    st.subheader('Puntualidad según Ruta')
    st.markdown("""<div style="text-align: justify">
    Creamos un gráfico de barras para mostrar la distribución de vuelos en diferentes rangos de millas, junto con la cantidad de vuelos que experimentaron retrasos y los que no. 500 millas equivalen aproximadamente a 805 kilómetros.
    </div>""", unsafe_allow_html=True)

    retraso_millas = df[df['retraso_llegada'] > 15]
    sin_retraso_millas = df[df['retraso_llegada'] <= 15]

    def asignar_rango_millas(milla):
        if milla < 500:
            return 'menos de 500'
        elif 500 <= milla < 1000:
            return '500-1000'
        elif 1000 <= milla < 1500:
            return '1000-1500'
        elif 1500 <= milla < 2000:
            return '1500-2000'
        else:
            return 'más de 2000'

    retraso_millas['rango_millas'] = retraso_millas['distancia_millas'].apply(asignar_rango_millas)
    sin_retraso_millas['rango_millas'] = sin_retraso_millas['distancia_millas'].apply(asignar_rango_millas)

    retrasos_estados_origen = retraso_millas.groupby(['rango_millas']).size().reset_index(name='con_retraso')
    sin_retraso_estados_origen = sin_retraso_millas.groupby(['rango_millas']).size().reset_index(name='sin_retraso')

    millas = retrasos_estados_origen.merge(sin_retraso_estados_origen, on='rango_millas', how='left').fillna(0)

    fig = px.bar(millas, 
                x                  = 'rango_millas', 
                y                  = ['con_retraso', 'sin_retraso'], 
                title              = 'Cantidad de vuelos con y sin retraso en la llegada según el recorrido del vuelo.',
                labels             = {'rango_millas': 'Rango de millas', 'value': 'Cantidad de vuelos'},
                opacity            = 0.7, 
                color_discrete_map = {"con_retraso": "gray", "sin_retraso": "violet"})

    fig.update_layout(title_x = 0.1, xaxis = {'categoryorder': 'total descending'})

    st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify">
    Parece haber una tendencia a que los vuelos de mayor distancia (más de 2000 millas) tengan menos retrasos en comparación con los vuelos de distancias más cortas (menos de 500 millas y de 500 a 1000 millas). 
    </div>""", unsafe_allow_html=True)


def mostrar_diagrama_caja_retraso_llegada(df):
    st.subheader('Retraso en la llegada')
    st.markdown("""<div style="text-align: justify">
    Se marcan los outliers todos los valores de retraso en la llegada que exceden los cinco minutos, siendo especialmente destacado un valor extremadamente separado de 2586 minutos, que equivalen a aproximadamente 43 horas y 6 minutos. Esto se debe a que la gran mayoría sale a tiempo.
    </div>""", unsafe_allow_html=True)

    fig = px.box(data_frame= df,x = 'retraso_llegada')

    fig.update_layout(title='Diagrama de Caja del retraso en la llegada', title_x=0.3)
    st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify">
    La mayoría de los retrasos en la llegada están dentro de un rango de tiempo relativamente corto, con unos pocos casos excepcionales que presentan retrasos significativamente más largos. Este valor extremadamente alto de 2586 minutos destaca como un outlier extremo en comparación con la mayoría de los retrasos en la llegada.
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div style="text-align: justify; margin-bottom: 10px;">
        Observamos el día con mayor retraso, por si es un valor erróneo y descubrimos que durante ese día ocurrió un ciclón que causó grandes destrozos en diversas ciudades del estado de Tennessee, con especial impacto en la capital, Nashville.
    </div>
   """, unsafe_allow_html=True)
    st.markdown("""
        [Enlace al artículo sobre el ciclón](https://www.elperiodico.com/es/vida-y-estilo/20231211/tornado-estados-unidos-tennesse-videos-dv-95684507)
    """)
def mostrar_grafico_barras_intervalos_tiempo(df):
    st.subheader('Retrasos en la llegada por intervalos')
    st.markdown("""<div style="text-align: justify">
    Generamos un gráfico de barras agrupando los retrasos en la llegada en intervalos de 5 minutos hasta 200. Excluimos el intervalo de 0 a 5 minutos, ya que no lo consideramos un retraso significativo. La mediana se encuentra en el rango de 40 a 50 minutos. Observamos que la mayoría de los retrasos se concentran en la primera hora.
    </div>""", unsafe_allow_html=True)

    intervalos = list(range(0, df['retraso_llegada'].max() + 6, 5))

    df['intervalo'] = pd.cut(df['retraso_llegada'], bins=intervalos, right=False)

    tabla = df.groupby('intervalo').size().reset_index(name='numero_de_retrasos')
    tabla['intervalo'] = tabla['intervalo'].astype(str)

    tabla_filtrada = tabla[tabla['numero_de_retrasos'] >= 1]
    tabla_filtrada= tabla_filtrada[1:]
    mediana_retrasos = tabla_filtrada['numero_de_retrasos'].median()

    fig = px.bar(tabla_filtrada[:40], x='intervalo', y='numero_de_retrasos', opacity= 0.8)

    fig.update_layout(title='Número de Retrasos por Intervalo (Hasta 200 Minutos)',
                    xaxis_title='Intervalo de Retraso',
                    yaxis_title='Número de Retrasos', title_x=0.2)

    fig.add_vline(x=mediana_retrasos, line_dash="dash", line_color="green", name="Mediana")
    st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify">

Los retrasos son más comunes durante la primera hora después de la hora programada de llegada de los vuelos. Esta tendencia puede atribuirse a varios factores, como congestión del tráfico aéreo, problemas en la programación de vuelos o demoras en el proceso de desembarque y llegada de pasajeros.    </div>""", unsafe_allow_html=True)

def años_retrasos(df_copia):
    st.subheader('Vuelos con retraso anuales')
    st.markdown("""
    <div style="text-align: justify">
    En el gráfico se muestra el número total de vuelos por año, destacándose 2023 como el año con mayor cantidad de vuelos, seguido por 2022 y 2021. Sin embargo, al filtrar por vuelos con retraso en la llegada, se observa que 2023 fue el año con menos retrasos.                </div>""", unsafe_allow_html=True)
    sin_retraso_llegada = df_copia[df_copia['retraso_llegada'] <= 15].groupby('anio').size().reset_index(name='sin_retraso_llegada')
    con_retraso_llegada = df_copia[df_copia['retraso_llegada'] > 15].groupby('anio').size().reset_index(name='con_retraso_llegada')

    vuelos_anuales = df_copia.groupby('anio').size().reset_index(name='cantidad_vuelos_anuales')
    vuelos_anuales = vuelos_anuales.merge(sin_retraso_llegada, on='anio', how='left')
    vuelos_anuales = vuelos_anuales.merge(con_retraso_llegada, on='anio', how='left')

    fig = px.bar(vuelos_anuales, 
                x='anio', 
                y=['sin_retraso_llegada', 'con_retraso_llegada'], 
                labels={'value':'Cantidad de Vuelos', 'anio':'Año', 'variable':'Tipo de Vuelo'}, 
                title='Cantidad de Vuelos Anuales con y sin Retraso en la Llegada',
                opacity=0.8,
                color_discrete_map={'sin_retraso_llegada':'lightcoral', 'con_retraso_llegada':'mediumseagreen'})

    fig.update_layout(title_x=0.2,  xaxis={'type': 'category', 'categoryorder': 'total descending'})
    st.plotly_chart(fig)
    
    st.markdown("""
        <div style="text-align: justify">
        El análisis del gráfico revela una tendencia interesante en los vuelos de los últimos tres años. A pesar de que 2023 registró el mayor número total de vuelos, es también el año con menos retrasos en las llegadas, lo que podría indicar una mejora en la eficiencia operativa o en la gestión de los vuelos. Por el contrario, aunque 2021 y 2022 tuvieron menos vuelos, registraron más retrasos, sugiriendo posibles desafíos en la puntualidad durante esos años. Esta relación inversa entre el volumen de vuelos y los retrasos en 2023 destaca un avance positivo en la industria.
        </div>""", unsafe_allow_html=True)
def mostrar_aerolineas_costo(df_copia):
    st.subheader('Costo de Vuelos por Aerolínea')
    st.markdown("""<div style="text-align: justify">
    Separamos las aerolíneas según su categoría de costo: alto, medio y bajo. Observamos que hay más vuelos en la categoría de alto costo, seguida por la de bajo costo y luego la de medio costo.
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div style="text-align: justify; margin-bottom: 10px;">
        - <strong>Alto costo</strong>: Delta Air Lines, American Airlines, United Airlines, Alaska Airlines y Hawaiian Airlines. 
        </div>
        <div style="text-align: justify; margin-bottom: 10px;">
        - <strong>Medio costo</strong>: Southwest Airlines y JetBlue Airways.
            </div>
        <div style="text-align: justify; margin-bottom: 10px;">
        - <strong>Bajo costo</strong>: Allegiant Air, Frontier Airlines, Spirit Airlines, Envoy Air, SkyWest Airlines, PSA Airlines, Endeavor Air, Mesa Airlines, Republic Airways y Horizon Air.
        </div>""", unsafe_allow_html=True)

    diccionario_costo = {
        'alto_costo': ["Delta Air Lines", "American Airlines", "United Airlines", "Alaska Airlines", "Hawaiian Airlines"],
        'medio_costo': ["Southwest Airlines", "JetBlue Airways"],
        'bajo_costo': ['Allegiant Air', 'Frontier Airlines', 'Spirit Airlines', 'Envoy Air', 'SkyWest Airlines', 'PSA Airlines', 
                    'Endeavor Air', 'Mesa Airlines', 'Republic Airways', 'Horizon Air']}

    def asignar_costo(aerolinea):
        for costo, aerolineas in diccionario_costo.items():
            if aerolinea in aerolineas:
                return costo

    df_copia['costo_aerolinea'] = df_copia['aerolinea'].apply(asignar_costo)

    vuelos_aerolinea = df_copia.groupby(['costo_aerolinea']).size().reset_index(name ='numero_vuelos')

    fig = px.bar(data_frame = vuelos_aerolinea,
                x          = 'costo_aerolinea',
                y          = 'numero_vuelos',
                opacity                 = 0.8,
                title      = "Cantidad de Vuelos según el costo de la aerolínea",
                color      = 'costo_aerolinea')

    fig.update_layout(title_x=0.3, xaxis_title='Compañía Aérea', yaxis_title='Cantidad de Vuelos', xaxis = {'categoryorder' : 'total descending'})
    st.plotly_chart(fig)
    st.markdown("""<div style="text-align: justify">
    En términos de cantidad de vuelos, las aerolíneas de alto costo son las más frecuentes. Esto podría sugerir que hay una demanda significativa de vuelos de alto costo, lo que podría estar relacionado con factores como la preferencia de los pasajeros por comodidades adicionales, rutas específicas o frecuencia de vuelos. Por otro lado, las aerolíneas de bajo costo pueden ser preferidas por aquellos que buscan opciones más económicas.
    </div>""", unsafe_allow_html=True)


def mostrar_grafico_barras_retraso_aerolineas_costo(df_copia):
    st.subheader('Retrasos según Costo de Aerolíneas')
    st.markdown("""<div style="text-align: justify">
    Generamos un gráfico de barras para comparar los retrasos en las aerolíneas según su categoría de costo. Observamos que las aerolíneas de costo medio tienen un mayor número de retrasos en comparación con las de bajo costo, a pesar de tener más vuelos en total.
    </div>""", unsafe_allow_html=True)

    df_copia['sin_retraso_llegada'] = (df_copia['retraso_llegada'] <= 15).astype(int)
    df_copia['con_retraso_llegada'] = (df_copia['retraso_llegada'] > 15).astype(int)

    vuelos_aerolinea = df_copia.groupby('costo_aerolinea').agg({'sin_retraso_llegada': 'sum','con_retraso_llegada': 'sum'}).reset_index()

    fig = px.bar(vuelos_aerolinea, x='costo_aerolinea', y=['sin_retraso_llegada', 'con_retraso_llegada'],
                title='Número de Vuelos con y sin retraso por aerolínea',
                labels={'value': 'Número de Vuelos', 'costo_aerolinea': 'Aerolínea', 'variable': 'Tipo de Vuelo'},
                barmode='group', opacity = 0.8)
                
    fig.update_layout(title_x=0.2, xaxis = {'categoryorder': 'total descending'})
    st.plotly_chart(fig)

    st.markdown("""<div style="text-align: justify">
    Como se puede apreciar, el hecho de que una aerolínea en EEUU sea de costo medio no garantiza una mejor gestión operativa o logística en comparación con las aerolíneas de bajo costo. 
    </div>""", unsafe_allow_html=True)


def mostrar_conclusiones_finales():
    st.markdown("<h4 style='text-align: center;'>📈 Conclusiones finales del EDA 📈</h4>", unsafe_allow_html=True)
    st.markdown("""<div style="text-align: justify; margin-bottom: 10px;">
        - <strong>Tendencia de crecimiento en el número de vuelos</strong>: A lo largo de los años analizados, se observa un incremento en el número de vuelos. Esto puede indicar un aumento en la demanda de viajes aéreos internos en EEUU.
    </div>
    <div style="text-align: justify; margin-bottom: 10px;">
        - <strong>Variedad en el desempeño de las aerolíneas</strong>: Existe una variabilidad significativa en la cantidad de vuelos realizados por cada compañía aérea. Las aerolíneas más grandes, como Southwest Airlines y American Airlines, lideran en número de vuelos, mientras que las más pequeñas tienen una presencia más limitada.
    </div>
    <div style="text-align: justify; margin-bottom: 10px;">
        - <strong>Relación entre retrasos en la salida y llegada</strong>: Se observa una relación positiva moderadamente fuerte entre los retrasos en la salida y los retrasos en la llegada de los vuelos. Esto sugiere que los vuelos que experimentan retrasos en la salida tienden a experimentar retrasos similares en la llegada.
    </div>
    <div style="text-align: justify; margin-bottom: 10px;">
        - <strong>Impacto de los días festivos en los retrasos</strong>: Durante los días festivos, se registra un aumento significativo en la incidencia de retrasos tanto en la salida como en la llegada de los vuelos, en comparación con los días laborables. Esto puede deberse a una combinación de factores, como la mayor congestión en los aeropuertos y los cambios en las operaciones de las aerolíneas.
    </div>
    <div style="text-align: justify; margin-bottom: 10px;">
        - <strong>Desafíos en la puntualidad de los vuelos</strong>: Algunos estados, como Florida, experimentan más retrasos en comparación con otros, a pesar de tener un alto número de vuelos. Esto sugiere que pueden existir desafíos adicionales en los aeropuertos de esos estados que afectan la puntualidad de los vuelos.
    </div>
    <div style="text-align: justify; margin-bottom: 10px;">
        - <strong>Impacto de la distancia en los retrasos</strong>: Existe una tendencia a que los vuelos de mayor distancia tengan menos retrasos en comparación con los vuelos de distancias más cortas. Esto puede ser útil para las aerolíneas al planificar sus rutas y horarios para minimizar los retrasos.
    </div>
    <div style="text-align: justify;">
        - <strong>Desempeño operativo de las aerolíneas según su categoría de costo</strong>: Las aerolíneas de costo medio tienen un mayor número de retrasos en comparación con las aerolíneas de bajo costo, a pesar de tener más vuelos en total. Esto sugiere que el costo de los vuelos no necesariamente está relacionado con la puntualidad o la eficiencia operativa de las aerolíneas.
    </div>""", unsafe_allow_html=True)

