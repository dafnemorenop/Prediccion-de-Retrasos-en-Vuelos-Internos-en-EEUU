from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd

# Primera función para descargar los csv's desde la web fuente.
def descargar_datos():
    url = "https://www.transtats.bts.gov/ONTIME/Departures.aspx"

    def obtener_opciones(url, aeropuertos_aerolineas):

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        seleccionar_aeropuerto_aerolinea = soup.find("select", attrs={"name": aeropuertos_aerolineas})
        opciones = seleccionar_aeropuerto_aerolinea.find_all("option")

        listado_opciones = [opcion.text for opcion in opciones]

        return listado_opciones

    listado_aeropuertos = obtener_opciones(url, "cboAirport")
    listado_aerolineas  = obtener_opciones(url, "cboAirline")

    def seleccionar_por_indice(url, nombre_seleccionado, lista_elementos):

        driver = webdriver.Firefox()
        driver.get(url)

        seleccion = Select(driver.find_element(By.NAME, nombre_seleccionado))
        
        for elemento in lista_elementos:
            seleccion.select_by_visible_text(elemento)
            sleep(1) 

    def preselecciones(driver):

        driver.find_element(By.ID, "chkAllStatistics").click() # click_all_statics
        driver.find_element(By.ID, "chkAllDays").click()       # click_all_days
        driver.find_element(By.ID, "chkMonths_11").click()     # click_mes_diciembre
        
        # Selecciona 2021, 2022 y 2023
        driver.find_element(By.ID, "chkYears_34").click()
        driver.find_element(By.ID, "chkYears_35").click() 
        driver.find_element(By.ID, "chkYears_36").click() 
    
    driver = webdriver.Firefox()
    driver.get(url)

    preselecciones(driver)

    for aeropuerto in listado_aeropuertos:

        select_aeropuerto = Select(driver.find_element(By.NAME, "cboAirport"))
        select_aeropuerto.select_by_visible_text(aeropuerto)

        # sleep(1)
        for aerolinea in listado_aerolineas:

            select_aerolinea = Select(driver.find_element(By.NAME, "cboAirline"))
            select_aerolinea.select_by_visible_text(aerolinea)
        
            click_submit = driver.find_element(By.ID, "btnSubmit").click()
            
            # sleep(1)
            #el codigo de abajo hace una flecha hacia abajo,
            driver.execute_script("window.scrollBy(0, 200);")

            try:
                element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.ID, "DL_CSV")))
                # sleep(1)
                element.click()
                
            except:
                pass

    driver.quit()

    return

descargar_datos()

# Segunda función para fechar los festivos en EEUU para esas fechas.

def fechar_festivos():

    dias_festivos = list()
    mes_festivos = list()  
    years = list()

    for year in range(2019, 2024):

        url = f'https://www.cuandoenelmundo.com/calendario/estados-unidos/{year}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Dia_rojo
        reddays = soup.find_all('td', class_ = 'day redday')


        for d in reddays:
            dias_festivos.append(d.text)    

        # Mes_rojo
        redmonths = soup.find_all('td', class_ = 'month redday')


        for m in redmonths:
            mes_festivos.append(m.text)

        #Año
        for y in reddays:
            years.append(year)

    df = pd.DataFrame()
    df['dia'] = dias_festivos
    df['mes'] = mes_festivos
    df['ano'] = years

    diccionario = {'enero'     : 1,
                   'febrero'   : 2,
                   'marzo'     : 3,
                   'abril'     : 4,
                   'mayo'      : 5,
                   'junio'     : 6,
                   'julio'     : 7,
                   'agosto'    : 8,
                   'septiembre': 9,
                   'octubre'   : 10,
                   'noviembre' : 11,
                   'diciembre' : 12}
    
    df['dia'] = df['dia'].astype(int)
    df['mes'] = df['mes'].map(diccionario)
    df["festivos"] = pd.to_datetime(df["ano"].astype(str) + '-' + df["mes"].astype(str) + '-' + df["dia"].astype(str))

    df.to_pickle('fecha_festivos.pkl')

    return

fechar_festivos()