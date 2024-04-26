import requests
from bs4 import BeautifulSoup
#Esta funcion tiene que utilizar beautifulSoup .
#Para leer la siguiente pagina : https://web3.career/
#Paso 1 => Hacer un print con el contenido de esa web .xxxx
#Paso 2 => Investigar como funciona la pagina web , averiguar como filtra por pais , y modifica mi funcion para
#leer las ofertas de españa .
#Paso 3 => Conseguir en una variable / Extraer de la pagina solo la lista de las ofertas sin los demas elementos. Y hacerle
#un print



def scrapeWeb3Offers():
    # URL de la página web
    url = "https://web3.career/"

    # Realizar la solicitud GET a la página web
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Parsear el contenido HTML
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Imprimir el contenido de la página web
        print(soup.prettify())
    else:
        # Imprimir un mensaje de error si la solicitud falla
        print("Error al obtener la página:", response.status_code)

# Llamar a la función para raspar la página web

