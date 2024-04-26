import requests
from bs4 import BeautifulSoup
import json
#Esta funcion tiene que utilizar beautifulSoup .
#Para leer la siguiente pagina : https://web3.career/
#Paso 1 => Hacer un print con el contenido de esa web .xxxx
#Paso 2 => Investigar como funciona la pagina web , averiguar como filtra por pais , y modifica mi funcion para
#leer las ofertas de españa .
#Paso 3 => Conseguir en una variable / Extraer de la pagina solo la lista de las ofertas sin los demas elementos. Y hacerle
#un print
#Paso 4 => Utiliza la lista de ofertas para crear una array que contenga las ofertas formateadas con : Titulo , Empresa , Salario , Ubicacion 
#y hacer un print a la array
#Paso 5 => Crea una variable Country en la funcion y asignale el valor Spain , y utilizala cuando lees la pagina con beautifulSoup
#y luego testea la variable con otros paises .
#Paso 6 => Haz que esa variable que sea un argumento para la funcion scrapeWeb3Offers .
#Paso 7 => En mi main printea la lista de los paises
#Paso 8 => 
def scrapeWeb3Offers():
    # URL de la página web
    url = "https://web3.career/web3-jobs-spain"

    # Realizar la solicitud GET a la página web
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Parsear el contenido HTML
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrar todas las instancias de "@type": "JobPosting"
        job_postings = soup.find_all("script", {"type": "application/ld+json"})
        
        # Imprimir solo el contenido relevante de las ofertas de trabajo
        for job_posting in job_postings:
            job_data = json.loads(job_posting.text)
            if job_data.get("@type") == "JobPosting":
                job_data.pop("baseSalary", None)
                job_data.pop("employmentType", None)
                job_data.pop("industry", None)
                job_data.pop("jobLocationType", None)
                job_data.pop("applicantLocationRequirements", None)
                job_data.pop("jobLocation", None)
                job_data.pop("image", None)
                job_data.pop("occupationalCategory", None)
                job_data.pop("workHours", None)
                job_data.pop("validThrough", None)
                job_data.pop("hiringOrganization", None)
                job_data.pop("title", None)
                job_data.pop("@context", None)
                job_data.pop("@type", None)
                
                print(json.dumps(job_data, indent=2))
    else:
        # Imprimir un mensaje de error si la solicitud falla
        print("Error al obtener la página:", response.status_code)