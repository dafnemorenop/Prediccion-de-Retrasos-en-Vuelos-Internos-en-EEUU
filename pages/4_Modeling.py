import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import plotly.express as px 

st.set_page_config(
    page_title="Modelo",  # Título en mayúsculas
    page_icon="🤖",
)

def main():
    

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
            <h1>Modelo de clasificación</h1>
        </div>
        """, unsafe_allow_html=True
    )


    # Descripción del modelo
    st.header("Descripción del Modelo de Clasificación")

    st.write("""
    <div style="text-align: justify;">
        Este modelo tiene como objetivo predecir si un vuelo llegará tarde en función de diversas características.
        A continuación se detallan los pasos y decisiones clave en el proceso de construcción de este modelo:
        </div> """, unsafe_allow_html=True)
    
    st.write("""
 
        ### Creación de la Columna `target`
        La columna `llega_tarde` se binariza:
        - `1`: Si el retraso en la llegada es igual o superior a 15 minutos (llega tarde).
        - `0`: Si el retraso es menor a 15 minutos (llega a tiempo).
        
        ### Eliminación de Columnas Innecesarias
        Se eliminaron columnas que no aportan información útil para la predicción, como la columna `retraso_llegada` y `mes`, que solo contenía el valor "diciembre".
        
        ### Asignación de Costo a las Aerolíneas
        Se definió un diccionario `diccionario_costo` que clasifica las aerolíneas según su costo.
        
        ### Transformaciones y Balanceo de Datos
        - Se utilizó `target_encoding` para las columnas categóricas.
        - La variable `distancia_millas` fue transformada a su logaritmo natural.
        - Se aplicaron estrategias de balanceo de clases utilizando **undersampling** y **oversampling** con la técnica SMOTE para lograr un balance adecuado entre las clases.
        
        ### Modelos de Clasificación Evaluados
        - Random Forest
        - Naive Bayes
        - KNN
        - Gradient Boosting
        - Nearest Centroid
        - Decision Tree
        - AdaBoost Classifier
        
    """)

    # Mostrar resultados del balanceo de clases
    st.header("Distribución de Clases y Balanceo de Datos")
    st.write("""
        Tras aplicar las estrategias de balanceo con **undersampling** y **oversampling**, se logró un balance más adecuado entre las clases.
        A continuación, se presenta la distribución de clases tras el balanceo:
    """)

    # Resultados del balanceo de clases
    balanceado = Counter({0: 1052080, 1: 631248})
    st.write(f"Distribución de clases en el conjunto balanceado:")
    st.write(balanceado)
    st.write(f"Porcentaje de clase '0' (a tiempo): {round((balanceado[0] / sum(balanceado.values())) * 100, 2)}%")
    st.write(f"Porcentaje de clase '1' (tarde): {round((balanceado[1] / sum(balanceado.values())) * 100, 2)}%")

    # Resultados de Evaluación de Modelos
    st.header("Evaluación de Modelos de Clasificación")
    st.write("""
        A continuación se presentan los resultados de los modelos evaluados con las métricas de rendimiento:
      
    """)

    # Crear un dataframe con los resultados de los modelos
    results = {
        "Model": ["Random Forest", "Naive Bayes", "KNN", "Gradient Boosting", "Nearest Centroid", "Decision Tree", "AdaBoost Classifier"],
        "Jaccard Index": [0.889988, 0.492686, 0.743817, 0.833966, 0.299281, 0.890983, 0.790969],
        "Accuracy": [0.981861, 0.798630, 0.943072, 0.968475, 0.526110, 0.982083, 0.957429],
        "Precision": [0.922004, 0.592960, 0.789327, 0.860888, 0.525651, 0.923466, 0.827657],
        "Recall": [0.958588, 0.724478, 0.919280, 0.962611, 0.589481, 0.958133, 0.942174],
        "F1-score": [0.939363, 0.605496, 0.838564, 0.903790, 0.422933, 0.939963, 0.873940],
        "ROC AUC": [0.939363, 0.724478, 0.919280, 0.962611, 0.589481, 0.958133, 0.942174],
        "Specificity": [0.986143, 0.812274, 0.947449, 0.969554, 0.514449, 0.986489, 0.960236]
    }

    df_results = pd.DataFrame(results)

    # Mostrar la tabla de resultados
    st.write(df_results)

    # Análisis de los mejores modelos
    st.header("Análisis de Métricas")
    st.write("""
        Los modelos **Random Forest** y **Decision Tree** mostraron un rendimiento sobresaliente en las métricas clave, especialmente en el **Jaccard Index** y el **F1-score**. Sin embargo, **Decision Tree** fue elegido como modelo final por su simplicidad y la facilidad con la que se puede interpretar.
              """)


    # Transformar los resultados a formato largo para Plotly
    df_resultados = df_results.melt(id_vars=["Model"], value_vars=["Jaccard Index", "Accuracy", "Precision", "Recall", "F1-score", "ROC AUC", "Specificity"], 
                                    var_name="Métrica", value_name="Valor")

    # Crear la gráfica de barras
    fig = px.bar(df_resultados, x="Model", y="Valor", color="Métrica", 
                title="Métricas de Evaluación de los Modelos de Aprendizaje Automático",
                labels={"Valor": "Valor de la Métrica", "Métrica": "Métrica"},
                barmode="group")

    # Actualizar la distribución de las barras y el título
    fig.update_layout(title_x=0.1, xaxis={'categoryorder': 'total descending'})

    # Mostrar la gráfica con Streamlit
    st.plotly_chart(fig)



    # Conclusiones
    st.header("Conclusión Final")
    st.write("""
        <div style="text-align: justify;">
            Tras evaluar múltiples modelos, se optó por el <strong>Decision Tree</strong> debido a su rendimiento competitivo y a su simplicidad.
            Este modelo no solo cumple con los requisitos de rendimiento, sino que también permite una interpretación clara de cómo se toman las decisiones, lo cual es vital en el contexto de la predicción de vuelos retrasados.
        </div>
    """, unsafe_allow_html=True)




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
