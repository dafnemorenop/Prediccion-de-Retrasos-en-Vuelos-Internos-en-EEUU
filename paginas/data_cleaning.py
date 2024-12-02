import streamlit as st


# st.set_page_config(
#     page_title="Limpieza",  # Título en mayúsculas
#     page_icon="🧹",
# )

def display():
    # Título principal de la página
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
            .subtitle-section h2 {
                color: #64b5f6; /* Color azul más oscuro */
                font-size: 2rem;
                font-weight: bold;
                margin-top: 20px;
                margin-bottom: 10px;
            }
        </style>
        <div class="title-section">
            <h1>Limpieza de los datos</h1>
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown(
    """
    <style>
        .subtitle-section, .result-section, p {
            text-align: justify;
        }
    </style>

    <div class="subtitle-section">
        <h2>Unificación de Datasets</h2>
    </div>
    <p>
        Se creó una función para leer y unir todos los datasets presentes en una carpeta. 
        Se eliminaron las primeras filas y la última fila de cada archivo mediante los parámetros 
        <span style="color: #007BFF;">`skiprows`</span> y <span style="color: #007BFF;">`skipfooter`</span>. 
        A partir de la segunda fila de cada archivo, se extrajo información adicional utilizando expresiones regulares, 
        incluyendo las columnas <code>ciudad-origen</code>, <code>estado-origen</code>, 
        <code>aeropuerto-origen</code> y <code>codigo-aeropuerto-origen</code>. 
        Los datasets procesados se concatenaron en un único DataFrame.
    </p>
    """,
    unsafe_allow_html=True
)
    

    # Código Python que se mostrará en la app
    codigo_python = """
    url = "https://www.transtats.bts.gov/ONTIME/Departures.aspx"

    # Función para leer y unir los datasets.
    def unir_datasets(ruta):
        dfs = []

        for nombre_archivo in os.listdir(ruta):
            if nombre_archivo.endswith('.csv'):
                ruta_archivo = os.path.join(ruta, nombre_archivo)
                df = pd.read_csv(ruta_archivo, skiprows=7, skipfooter=1, engine='python')  # Eliminamos las primeras filas y la última de cada dataset.

                with open(ruta_archivo, 'r') as archivo:
                    segunda_fila = archivo.readlines()[1].strip()  # Rescatamos información de la segunda fila de los csv's.
                    coincidencia = re.search(r'Origin Airport: (.+), (.+): (.+) \\((.+)\\)', segunda_fila)

                    if coincidencia:
                        ciudad_origen = coincidencia.group(1)
                        estado_origen = coincidencia.group(2)
                        aeropuerto_origen = coincidencia.group(3)
                        codigo_aeropuerto_origen = coincidencia.group(4)

                        df['ciudad_origen'] = ciudad_origen
                        df['estado_origen'] = estado_origen
                        df['aeropuerto_origen'] = aeropuerto_origen
                        df['codigo_aeropuerto_origen'] = codigo_aeropuerto_origen

                        dfs.append(df)
                    else:
                        print("La segunda fila no tiene el formato esperado en el archivo:", nombre_archivo)

        resultado_df = pd.concat(dfs, ignore_index=True)
        resultado_df.to_pickle('data/pickle/vuelos.pkl')


    ruta = r'data'  # Ruta en la que se encuentren todos los csv's.
    unir_datasets(ruta)
    """

    # Mostrar el código en la app
    st.code(codigo_python, language="python")


    st.markdown(
    """
    <div class="subtitle-section">
        <h2>Renombrado de Columnas</h2>
    </div>
    <p>
        Todas las columnas fueron traducidas al español para facilitar su comprensión y análisis.
    </p>
    """,
    unsafe_allow_html=True
)


    codigo_python = """
    df.rename(columns={ 
        'Carrier Code'                            : 'aerolinea',
        'Date (MM/DD/YYYY)'                       : 'fecha',
        'Flight Number'                           : 'numero_vuelo',
        'Tail Number'                             : 'numero_cola',
        'Destination Airport'                     : 'codigo_aeropuerto_destino',
        'Scheduled departure time'                : 'hora_salida_programada',
        'Actual departure time'                   : 'hora_salida_real',
        'Scheduled elapsed time (Minutes)'        : 'duracion_programada_vuelo',
        'Actual elapsed time (Minutes)'           : 'duracion_real',
        'Departure delay (Minutes)'               : 'retraso_salida',
        'Wheels-off time'                         : 'hora_despegue',
        'Taxi-Out time (Minutes)'                 : 'tiempo_pista_salida',
        'Delay Carrier (Minutes)'                 : 'tiempo_retraso_aerolinea',
        'Delay Weather (Minutes)'                 : 'tiempo_retraso_clima',
        'Delay National Aviation System (Minutes)': 'tiempo_retraso_sistema_aviacion',
        'Delay Security (Minutes)'                : 'tiempo_retraso_seguridad',
        'Delay Late Aircraft Arrival (Minutes)'   : 'retraso_llegada'
    }, inplace=True)
    """

    # Mostrar el código en la app
    st.code(codigo_python, language="python")


    st.markdown(
    """
    <div class="subtitle-section">
        <h2>Eliminación de Duplicados</h2>
    </div>
    <p>
        Se identificaron y eliminaron filas duplicadas en el DataFrame consolidado para garantizar la calidad de los datos.
    </p>
    """,
    unsafe_allow_html=True
)

    codigo_python = """
    duplicados = df.duplicated()

    if duplicados.any():
        print("El DataFrame tiene filas duplicadas.")
    else:
        print("El DataFrame no tiene filas duplicadas.")

    num_filas_duplicadas = df.duplicated().sum()

    print("Número de filas duplicadas:", num_filas_duplicadas)
    """

    # Mostrar el código en la app
    st.code(codigo_python, language="python")


    st.markdown(
    """
    <div class="subtitle-section">
        <h2>Asignación de Números de Cola</h2>
    </div>
    <p>
        Se estableció una relación entre los números de cola y los números de vuelo. 
        Para las filas donde el número de cola estaba ausente 
        (<span style="color: #FF5733;">`NaN`</span>), se buscó en un diccionario y se reemplazaron los valores faltantes.
    </p>
    """,
    unsafe_allow_html=True
)

    st.markdown(
    """
    <div class="subtitle-section">
        <h2>Procesamiento de Fechas y Horas</h2>
    </div>
    <p>
        Se agregaron y ajustaron columnas relacionadas con las fechas y horas para garantizar un formato uniforme en el dataset.
    </p>
    """,
    unsafe_allow_html=True
)

    codigo_python = """
    df['hora_llegada_real'] = pd.to_timedelta(df['hora_salida_real'].astype(str)) + pd.to_timedelta(df['duracion_real'], unit='m')
    df['dia_semana'] = df['fecha'].dt.dayofweek
    df['anio'] = df['fecha'].dt.year
    df['mes'] = df['fecha'].dt.month
    df['fin_de_semana'] = (df['fecha'].dt.dayofweek >= 5).astype(int)
        """

    # Mostrar el código en la app
    st.code(codigo_python, language="python")

    st.markdown(
    """
    <div class="subtitle-section">
        <h2>Corrección de Códigos de Aeropuerto</h2>
    </div>
    <p>
        Se corrigieron códigos de aeropuertos mal etiquetados para garantizar consistencia en los datos.
    </p>
    """,
    unsafe_allow_html=True
)
    codigo_python = """
    df.loc[df['aeropuerto_origen'] == 'Tri Cities', 'codigo_aeropuerto_origen'] = 'PSC'
    """

    # Mostrar el código en la app
    st.code(codigo_python, language="python")

    st.markdown(
    """
    <div class="subtitle-section">
        <h2>Agregado de Columnas de Destino</h2>
    </div>
    <p>
        Se añadieron las columnas <code>ciudad-destino</code> y <code>estado-destino</code> 
        para completar la información sobre los destinos de los vuelos.
    </p>
    """,
    unsafe_allow_html=True
)
    codigo_python = """
    df['aeropuerto_destino'] = df['codigo_aeropuerto_destino'].replace(diccionario_aeropuertos)
   """
    # Mostrar el código en la app
    st.code(codigo_python, language="python")

    st.markdown(
    """
    <div class="subtitle-section">
        <h2>Resultado Final</h2>
    </div>
    <p>
        El dataset limpio y procesado se guarda en un archivo <code>.pkl</code> listo para análisis o modelado.
    </p>
    """,
    unsafe_allow_html=True
)

    codigo_python = """
   df.to_pickle('data/vuelos_limpio.pkl')
   """
    # Mostrar el código en la app
    st.code(codigo_python, language="python")




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
