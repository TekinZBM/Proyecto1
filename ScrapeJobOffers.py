import requests
from bs4 import BeautifulSoup
import json
#Esta funcion tiene que utilizar beautifulSoup .
#Para leer la siguiente pagina : https://web3.career/
#Paso 1 => Hacer un print con el contenido de esa web .xxxx
#Paso 2 => Investigar como funciona la pagina web , averiguar como filtra por pais , y modifica mi funcion para
#leer las ofertas de españa . xxxx
#Paso 3 => Conseguir en una variable / Extraer de la pagina solo la lista de las ofertas sin los demas elementos. Y hacerle
#un print xxxx
#Paso 4 => Utiliza la lista de ofertas para crear una array que contenga las ofertas formateadas con : Titulo , Empresa , Salario , Ubicacion 
#y hacer un print a la array xxx
#Paso 5 => Crea una variable Country en la funcion y asignale el valor Spain , y utilizala cuando lees la pagina con beautifulSoup
#y luego testea la variable con otros paises . xxxx
#Paso 6 => Haz que esa variable que sea un argumento para la funcion scrapeWeb3Offers .xxxx
#Paso 7 => En mi main printea la lista de los paises
#Paso 8 => Coger la segunda pagina tambien de ofertas 
import requests
from bs4 import BeautifulSoup
import json

def scrapeWeb3Offers(country):
    # Crear una lista para almacenar todas las ofertas
    all_offers = []

    # Iterar sobre las páginas
    for page_number in range(1, 3):  # Cambiar a (1, 3) para obtener las páginas 1 y 2
        # URL de la página web
        url = f"https://web3.career/web3-jobs-{country.lower()}?page={page_number}"

        # Realizar la solicitud GET a la página web
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Parsear el contenido HTML
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Encontrar todas las instancias de "@type": "JobPosting"
            job_postings = soup.find_all("script", {"type": "application/ld+json"})
            
            # Crear una lista para almacenar las ofertas formateadas de esta página
            page_offers = []
            
            # Iterar sobre las ofertas de trabajo y agregarlas a la lista formateada
            for job_posting in job_postings:
                job_data = json.loads(job_posting.text)
                if job_data.get("@type") == "JobPosting":
                    title = job_data.get("title", "No title")
                    company = job_data.get("hiringOrganization", {}).get("name", "No company")
                    salary = job_data.get("baseSalary", {}).get("value", {}).get("minValue", "No salary")
                    location = job_data.get("jobLocation", {}).get("address", {}).get("addressLocality", "No location")
                    formatted_offer = {
                        "Title": title,
                        "Company": company,
                        "Salary": salary,
                        "Location": location
                    }
                    page_offers.append(formatted_offer)
            
            # Agregar las ofertas de esta página a la lista de todas las ofertas
            all_offers.extend(page_offers)
        else:
            # Imprimir un mensaje de error si la solicitud falla
            print(f"Error al obtener la página {page_number}:", response.status_code)

    # Devolver la lista de todas las ofertas
    return all_offers