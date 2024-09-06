import streamlit as st
import pandas as pd
import re
from textblob import TextBlob
import plotly.express as px
from PIL import Image
from modules.vuelos import *
import io

# TÍTULO DE LA PESTAÑA

st.set_page_config(
    page_title="Vuelos EEUU",
    page_icon="✈️",
    layout="centered")



# TÍTULO DE LA PÁGINA

st.markdown("<h1 style='text-align: center; color: red'>🛫 Predicción de retrasos de vuelos 🛬</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>🦅 Datos de vuelos en Estados Unidos para los meses de enero de 2019 y enero de 2020 🦅</h2>", unsafe_allow_html=True)


st.markdown("<h2 style='text-align: center;'>🧹 Data Cleaning 🧹</h2>", unsafe_allow_html=True)



st.markdown("<h2 style='text-align: center;'>📊 Data Visualization 📊</h2>", unsafe_allow_html=True)


# IMAGEN PRINCIPAL

image = Image.open( r"C:\Users\Dafne\OneDrive\Escritorio\hack a boss\3 PROYECTO AVIONES\sources\mapa.jpg")
st.image(image = image, use_column_width = True)

# LECTURA DEL DF, lee excel no csv. Crea un expandible en la pantalla para poder leerlo

with st.expander(label = "DataFrame - Fuel", expanded = False):
        df = pd.read_excel(r"C:\Users\Dafne\OneDrive\Escritorio\hack a boss\mod7-streamlit-main\machine_learning\Co2FuelConsumption_all.xlsx")
        st.dataframe(df)

# Crear un botón de descarga del archivo
def download_excel(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # Convertir CSV a base64
    href = f'<a href="data:file/csv;base64,{b64}" download="co2_fuel_consumption.xlsx">Descargar archivo Excel</a>'
    return href

st.markdown(download_excel(df), unsafe_allow_html=True)


# MOSTRAR LA INFORMACIÓN BÁSICA
# Info
st.write("Número de filas:", df.shape[0], "Número de columnas:", df.shape[1])

with st.expander(label = 'Info del DataFrame', expanded = False):
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

# Tipos de datos de las columnas
with st.expander("Tipos de datos de las columnas", expanded=False):
    st.write(df.dtypes)

# Mostrar el resumen estadístico
with st.expander("Resumen estadístico del DataFrame", expanded=False):
    st.write(df.describe())

# Mostrar las columnas del DataFrame
with st.expander(label = "Columnas del DataFrame", expanded = False):
    st.write(df.columns)

# Mostrar los nulos
with st.expander("Nulos del DataFrame", expanded=False):

#st.write("Nulos del DataFrame:")
    st.write(df.isna().sum())


st.subheader('Gráfico de Nans del DataFrame')

fig = px.imshow(df.isna(), labels=dict(x="Columnas", y="Filas"), x=df.columns, y=df.index)
fig.update_layout(title='Visualización de NaNs', title_x=0.3)

st.plotly_chart(figure_or_data = fig)

# Analisis

st.markdown("<h2 style='text-align: center;'>📈 Fuel Análisis 📈</h2>", unsafe_allow_html=True)


#     df["season"] = df["episode"].apply(lambda x : int(x[:2]))
#     df["ep_number"] = df["episode"].apply(lambda x : int(x[3:5]))

#     df = df[df["ep_number"] != 99]

#     df["script"] = df["script"].apply(lambda x : list(eval(x)))

#     # with st.expander(label = "DataFrame", expanded = False):
#     #     st.dataframe(df)
#     #     st.write(f"DataFrame dimensions: {df.shape[0]}x{df.shape[1]}")
#     #     st.balloons()

#     st.sidebar.markdown("### Select an episode of this amazing series to have a look on the script's insights.")
#     season = st.sidebar.selectbox(label   = "Select season:",
#                                   options = df["season"].unique(),
#                                   index   = 0)
    
#     ep_number = st.sidebar.selectbox(label   = "Select episode:",
#                                      options = df[df["season"] == season]["episode"].values,
#                                      index   = 0)

#     # Filtra el dataframe
#     df_sidebar = df[df["episode"] == ep_number][["script"]]
#     df_sidebar = df_sidebar.explode(column = "script")

#     # Crea la columna "character"
#     df_sidebar["character"] = df_sidebar["script"].apply(lambda x : x.split(":")[0])

#     # Eliminar Publicidad
#     df_sidebar = df_sidebar[~df_sidebar["character"].isin(["(adsbygoogle = window.adsbygoogle || []).push({});",
#                                                            "\n\n(adsbygoogle = window.adsbygoogle || []).push({});"])]

#     # Elimina texto dentro de parentesis y corchetes
#     df_sidebar["script"] = df_sidebar["script"].apply(lambda x : re.sub("[\(\[].*?[\)\]]", "", x))

#     df_sidebar["character"] = df_sidebar["character"].apply(lambda x : re.sub("[\(\[].*?[\)\]]", "", x))
#     df_sidebar = df_sidebar[~df_sidebar["character"].isin(["", "All"])]

#     # Total Words
#     df_sidebar["total_words"] = df_sidebar["script"].apply(lambda x : len(x.split()))
#     df_sidebar["total_words"] = df_sidebar["total_words"] - df_sidebar["character"].apply(lambda x : len(x.split()))

#     # Texto
#     with st.expander(f"{ep_number} Script", expanded = False):

#         for row in df_sidebar["script"].values:
#             st.write(row)
#             st.write("-"*10)
#         st.balloons()

#     # Descargar Datos    
#     st.markdown(body = download_file(df = df_sidebar, ep_number = ep_number), unsafe_allow_html = True)

#     # Polaridad y Subjetividad
#     pol = lambda x: TextBlob(x).sentiment.polarity
#     sub = lambda x: TextBlob(x).sentiment.subjectivity

#     df_sidebar["polarity"] = df_sidebar["script"].apply(pol)
#     df_sidebar["subjectivity"] = df_sidebar["script"].apply(sub)

#     # Reset Index
#     df_sidebar.reset_index(drop = True, inplace = True)
    
#     # Aggregate Functions
#     agg_func = {"total_words" : ["count", "sum"],
#                 "polarity" : ["mean"],
#                 "subjectivity" : ["mean"]}

#     df_group = df_sidebar.groupby(by = "character", as_index = False).agg(agg_func)

#     df_group.columns = ["character", "total_lines", "total_words", "polarity", "subjectivity"]

#     # Words per Line
#     df_group["words_per_line"] = df_group["total_words"] / df_group["total_lines"]

#     # Bubble Chart
#     fig_scatter = px.scatter(data_frame = df_group,
#                              x          = "polarity",
#                              y          = "subjectivity",
#                              color      = "character",
#                              size       = "total_words",
#                              title      = "Polarity v Subjectivity")
    
#     # Bar Chart 1
#     fig_bar1 = px.bar(data_frame = df_group,
#                      y          = "total_words",
#                      x          = "character",
#                      color      = "character",
#                      title      = "Total Words - Character",
#                      text_auto  = True)
    
#     fig_bar1.update_xaxes(title_text = "Characters")
#     fig_bar1.update_yaxes(title_text = "Total Words")
#     fig_bar1.update_xaxes(categoryorder = "total descending")

#     # Bar Chart 2
#     fig_bar2 = px.bar(data_frame = df_group,
#                      y          = "total_lines",
#                      x          = "character",
#                      color      = "character",
#                      title      = "Total Lines - Character",
#                      text_auto  = True)
    
#     fig_bar2.update_xaxes(title_text = "Characters")
#     fig_bar2.update_yaxes(title_text = "Total Lines")
#     fig_bar2.update_xaxes(categoryorder = "total descending")

#     # Pie Chart
#     fig_pie = px.pie(data_frame = df_group,
#                      values     = "words_per_line",
#                      names      = "character",
#                      title      = "Words per Line - Character",
#                      labels     = "character")
    
#     fig_pie.update_traces(textposition = "inside", textinfo = "percent+label")

#     # Line Chart
#     fig_line = px.line(data_frame = df_sidebar,
#                        y          = "polarity",
#                        title      = "Episode's Polarity")
    
#     fig_line.update_xaxes(title_text = "", showticklabels = False)
    
#     # Plots
#     st.plotly_chart(figure_or_data = fig_scatter)
#     st.plotly_chart(figure_or_data = fig_bar1)
#     st.plotly_chart(figure_or_data = fig_bar2)
#     st.plotly_chart(figure_or_data = fig_pie)
#     st.plotly_chart(figure_or_data = fig_line)
 
# if __name__ == "__main__":
#     main()
