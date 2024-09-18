import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
from modules.data_preparation import prepare_aeropuertos_unicos
from modules.load_data import cargar_y_combinar_df


# Para cargar desde CSV
df_aeropuertos_unicos = pd.read_csv('df/aeropuertos_unicos.csv')

# Ajusta el número de trozos y la ruta base según cómo dividiste y guardaste el DataFrame original
num_trozos = 5
ruta_base_pickle = 'df/pickle/df_aviones_trozo_'
# Preparar y cargar el DataFrame de aeropuertos únicos
df_aeropuertos_unicos = prepare_aeropuertos_unicos(num_trozos, ruta_base_pickle)

def display():
    st.title('Vuelos en USA')

    # Crear el mapa base con Folium
    mapa = folium.Map(location=[40, -95], zoom_start=4)  # Ajusta según tus necesidades

    # Añadir marcadores para cada aeropuerto (este es solo un ejemplo, ajusta según tu DataFrame)
    for index, row in df_aeropuertos_unicos.iterrows():
        folium.Marker([row['latitude'], row['longitude']], popup=row['nombre_aeropuerto']).add_to(mapa)

    st_folium(mapa, width=1280, height=720)

def display_map(filtered_df):
    # Crear un mapa base con Folium
    mapa = folium.Map(location=[40, -95], zoom_start=4)

    # Añadir marcadores para cada aeropuerto en el DataFrame filtrado
    for index, row in filtered_df.iterrows():
        folium.Marker([row['latitude_origen'], row['longitude_origen']], 
                      popup=f"{row['aeropuerto_origen']} ({row['ciudad_origen']}, {row['estado_origen']})").add_to(mapa)

    # Mostrar el mapa en Streamlit
    st_folium(mapa, width=725, height=500)

def app():
    st.title('Vuelos en USA')

    # Llamar a display() para mostrar el primer mapa
    display()

    st.write("Seleccione un Estado para ver los aeropuertos correspondientes:")  # Solo para agregar claridad en la UI

    # Selección de Estado
    estados = df_aeropuertos_unicos['estado_origen'].unique()
    estado_seleccionado = st.selectbox('', estados)  # Eliminé el texto del selectbox para evitar repetición

    # Filtrar DataFrame basado en la selección de estado
    df_filtrado = df_aeropuertos_unicos[df_aeropuertos_unicos['estado_origen'] == estado_seleccionado]

    # Mostrar mapa basado en el DataFrame filtrado
    display_map(df_filtrado)

if __name__ == "__main__":
    app()