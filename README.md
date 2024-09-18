# Proyecto FlyPredict

Este repositorio contiene diversos scripts y datos relacionados con el proyecto FlyPredict.

Los datos para este estudio fueron extraídos del Departamento de Estadísticas de Transporte de EE. UU. (BTS), una entidad del Departamento de Transporte (DOT).

[Departamento de Estadísticas de Transporte de EE. UU.](https://www.transtats.bts.gov/ONTIME/Departures.aspx)

## Descripción 

Predicción de Retrasos en Vuelos Internos en EEUU: Desarrollo de un Modelo Predictivo con Streamlit para la Visualización de Datos.

Puedes acceder a la aplicación de Streamlit en el siguiente enlace:

[Aplicación de Streamlit](https://proyectoaviones.streamlit.app/)

## Objetivo

Este proyecto se centró en desarrollar un modelo predictivo para estimar retrasos en vuelos internos en EE. UU., utilizando técnicas de análisis de datos y aprendizaje automático. Además, se creó una interfaz interactiva con Streamlit, que permite a los usuarios explorar y visualizar de manera intuitiva las predicciones y los datos asociados con los retrasos de vuelos, facilitando una comprensión más clara y accesible de la información.

## Estructura del Proyecto

Este proyecto está organizado en diferentes carpetas para facilitar su uso y mantenimiento. A continuación, se detalla la organización de las carpetas y archivos:

- **`.git`**: Carpeta de control de versiones de Git que contiene los datos necesarios para el seguimiento de cambios y la gestión del repositorio.

- **`.venv`**: Entorno virtual de Python donde se encuentran las dependencias y librerías necesarias para el proyecto. Asegúrate de activar este entorno antes de ejecutar el proyecto.

- **`cuadernos`**: Carpeta que incluye los cuadernos de Jupyter utilizados para el desarrollo y análisis del proyecto:
  - **`web_scraping`**: Scripts y notebooks relacionados con la recolección de datos a través de web scraping.
  - **`limpieza`**: Scripts para la limpieza y preparación de datos.
  - **`eda`**: Análisis exploratorio de datos (Exploratory Data Analysis).
  - **`modelo`**: Modelos de machine learning y análisis predictivo.

- **`data`**: Carpeta que contiene todos los archivos `.csv` con datos de vuelos que se utilizan en el proyecto.

- **`modules`**: Contiene módulos de código reutilizables y funciones auxiliares que se utilizan en el proyecto.

- **`paginas`**: Carpeta con los archivos HTML para las diferentes páginas del sitio web:
  - **`eda`**: Página para el análisis exploratorio de datos.
  - **`inicio`**: Página de inicio del sitio web.
  - **`modelo`**: Página para mostrar los resultados del modelo.
  - **`sobre_nosotros`**: Página con información sobre el equipo o la organización.
  - **`sobre_proyecto`**: Página con detalles sobre el proyecto.
  - **`vuelos`**: Página que muestra información sobre los vuelos.

- **`proyecto_paginas`**: Carpeta con archivos adicionales relacionados con la estructura y funcionalidad de las páginas del proyecto.

- **`sources`**: Carpeta que incluye recursos adicionales, como bibliotecas externas, datos auxiliares o documentación relevante.

### Cómo Navegar por el Proyecto

1. **Revisa los cuadernos en la carpeta `cuadernos`**: Aquí encontrarás los scripts para scraping, limpieza, EDA y modelado.
2. **Consulta los datos en `data`**: Contiene los archivos `.csv` con la información de vuelos.
3. **Explora los módulos en `modules`**: Accede a las funciones y clases reutilizables.
4. **Examina las páginas en `paginas`**: Verifica el contenido y diseño de las páginas web.
5. **Revisa `proyecto_paginas` y `sources`**: Encuentra archivos adicionales que pueden ayudar en el desarrollo y documentación del proyecto.

Esta estructura facilita la navegación y el mantenimiento del proyecto, proporcionando una organización clara y eficiente.

## Librerías

- **beautifulsoup4 (BeautifulSoup)**: Herramienta para el web scraping y la extracción de datos de archivos HTML y XML.
- **requests**: Librería para realizar solicitudes HTTP y obtener datos de sitios web.
- **selenium**: Herramienta para la automatización de navegadores y la interacción con páginas web dinámicas.
- **pandas**: Biblioteca para la manipulación y análisis de datos en estructuras tabulares.
- **numpy**: Biblioteca para operaciones matemáticas y numéricas avanzadas.
- **seaborn**: Biblioteca para la visualización de datos estadísticos con gráficos atractivos.
- **matplotlib**: Biblioteca para la creación de gráficos estáticos en 2D.
- **folium**: Herramienta para la visualización de datos geoespaciales en mapas interactivos.
- **plotly**: Biblioteca para la creación de gráficos interactivos y visualizaciones avanzadas.
- **joblib**: Herramienta para la serialización de objetos de Python y la optimización de modelos.
- **scikit-learn**: Biblioteca para algoritmos de machine learning, validación de modelos y métricas de evaluación.
- **imbalanced-learn**: Herramienta para técnicas de muestreo y balanceo de clases en conjuntos de datos desequilibrados.
- **category_encoders**: Biblioteca para la codificación de variables categóricas en modelos de machine learning.
