# paginas/inicio.py
import streamlit as st
#from PIL import Image

def display():
    # Asegúrate de que la ruta a la imagen esté correcta y sea accesible
    st.image('sources/cabecera.jpg', use_column_width=True)

    #img = Image.open('sources/cabecera.jpg')
    #img.show()

    # Título de bienvenida
    st.title("Bienvenidos al análisis de puntualidad en aeropuertos")

    # Texto introductorio
    st.markdown("""
        ### Proyecto final para Hack a Boss

        Este proyecto representa el culmen de nuestro aprendizaje en el Bootcamp de Data Science & Inteligencia Artificial de Hack a Boss. Como nuestro tercer y último proyecto, hemos querido abordar un tema de gran relevancia y aplicabilidad práctica: el estudio de la puntualidad y los retrasos en los vuelos de diversos aeropuertos.

        ---
    """)

    # Creación de dos columnas para los textos
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            #### El Equipo

            Este estudio ha sido llevado a cabo por José Núñez, Rubén Maestre, Dafne Moreno y Nahuel Núñez. Juntos, hemos fusionado nuestros conocimientos y habilidades para sumergirnos en el fascinante mundo de la aviación, analizando grandes volúmenes de datos para extraer conclusiones significativas y patrones reveladores sobre los retrasos en los vuelos.
        """)
    
    with col2:
        st.markdown("""
            #### Metodología y Objetivos

            A través de un minucioso Análisis Exploratorio de Datos (EDA), hemos explorado las diferentes variables que pueden influir en la puntualidad de los vuelos. El objetivo final es desarrollar un modelo de Machine Learning capaz de predecir la probabilidad de retraso de un vuelo, basándose en una serie de factores determinantes.
        """)

    st.markdown("""
        ---
        #### Herramientas y Tecnologías

        Para llevar a cabo este proyecto, hemos utilizado una amplia gama de herramientas que hemos ido dominando a lo largo del curso, incluyendo Python, Pandas, Numpy, Plotly, Matplotlib y Keras, entre otras. Estas herramientas nos han permitido no solo procesar y analizar los datos de manera eficiente, sino también visualizar los resultados de forma clara e interactiva, facilitando la comprensión de los patrones y tendencias subyacentes.

        Gracias a Streamlit, hemos podido ilustrar y compartir nuestros hallazgos de una manera dinámica y accesible, permitiendo a cualquier interesado explorar los diferentes aspectos de nuestro análisis y las conclusiones a las que hemos llegado.

        Este proyecto es un testimonio de nuestro viaje de aprendizaje en Hack a Boss y de nuestro compromiso por aplicar la ciencia de datos para resolver problemas reales. Esperamos que encuentres los insights y visualizaciones proporcionados tanto informativos como estimulantes.
    """)

    # Aquí puedes añadir más contenido si lo deseas, como imágenes, gráficos interactivos, etc.