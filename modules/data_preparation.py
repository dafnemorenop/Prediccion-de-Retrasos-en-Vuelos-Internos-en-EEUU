# En el archivo modules/data_preparation.py

import pandas as pd
from .load_data import cargar_y_combinar_df  # Asegúrate de que la ruta de importación sea correcta según la estructura de tu proyecto

def prepare_aeropuertos_unicos(num_trozos, ruta_base_pickle='df/pickle/df_aviones_trozo_'):
    """
    Prepara un DataFrame único de aeropuertos a partir de trozos de DataFrame guardados como archivos pickle.

    :param num_trozos: Número de trozos en los que se dividió el DataFrame original.
    :param ruta_base_pickle: Ruta base de los archivos pickle, sin el número de trozo ni la extensión.
    :return: DataFrame de aeropuertos únicos.
    """

    # Cargar y combinar los DataFrame desde los trozos de pickle
    df_aviones = cargar_y_combinar_df(num_trozos, ruta_base_pickle)

    # Extraer y renombrar columnas de interés
    cols_origen = ['aeropuerto_origen', 'ciudad_origen', 'estado_origen', 'latitude_origen', 'longitude_origen']
    cols_destino = ['aeropuerto_destino', 'ciudad_destino', 'estado_destino', 'latitude_destino', 'longitude_destino']

    df_origen = df_aviones[cols_origen].rename(columns={'aeropuerto_origen': 'nombre_aeropuerto', 'ciudad_origen': 'ciudad', 'estado_origen': 'estado', 'latitude_origen': 'latitude', 'longitude_origen': 'longitude'})
    df_destino = df_aviones[cols_destino].rename(columns={'aeropuerto_destino': 'nombre_aeropuerto', 'ciudad_destino': 'ciudad', 'estado_destino': 'estado', 'latitude_destino': 'latitude', 'longitude_destino': 'longitude'})

    # Combinar y eliminar duplicados para obtener aeropuertos únicos
    df_combinado = pd.concat([df_origen, df_destino]).drop_duplicates().reset_index(drop=True)

    return df_combinado

