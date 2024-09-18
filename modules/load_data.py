# En el archivo modules/load_data.py

import pandas as pd

def cargar_y_combinar_df(trozos, ruta='df/pickle/df_aviones_trozo_'):
    """
    Carga y combina trozos de DataFrame desde archivos pickle.

    :param trozos: Número de trozos en los que se dividió el DataFrame.
    :param ruta: Ruta base de los archivos pickle, sin el número de trozo ni la extensión.
    :return: DataFrame combinado.
    """

    # Lista para almacenar los trozos de DataFrame
    dfs_trozos = []

    # Cargar cada trozo y agregarlo a la lista
    for i in range(trozos):
        df_trozo = pd.read_pickle(f'{ruta}{i}.pkl')
        dfs_trozos.append(df_trozo)

    # Combinar todos los trozos para reconstruir el DataFrame original
    df_combinado = pd.concat(dfs_trozos).reset_index(drop=True)

    return df_combinado
