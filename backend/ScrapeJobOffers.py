import requests
from bs4 import BeautifulSoup
import json
from generatelink import generate_offer_link

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
#Paso 7 => En mi main printea la lista de los paises xxxxx
#Paso 8 => Coger la segunda pagina tambien de ofertas xxxxxx
#Paso 9 => Agregar nuevo key al objeto de cada oferta , el link hacia la oferta xxxxxx
#Paso 10 => Funcion nueva "scrapeOfferacontnet" que tenga como argumento : link. Tiene que devolver la descripcion de la 
#oferta que le pases por el link  xxxxxxxxxxxxx

#Paso 11 => Crea una array nueva que contenga lo mismo que la array de las ofertas iniciales pero cada oferta tiene extra la
#descipcion de la oferta

#Paso 12 => Haz la funcion principal de main . Esa funcion toma un argumento (el pais) y te devuelve por ese pais,
#50 ofertas ( o las que salgan en las primeras 2 paginas ) y cada oferta alli , tiene titulo , empresa , salario
#ubicacion , link de la oferta y descripcionxxxxx

#Paso 13 => CUANDO NO LE PASE NINGUN PAIS , ME TIENE QUE DEVOLVER LAS OFERTAS DE LA PAGINA PRINCIPAL.

#Section 2
#Paso 1 : Dentro de la carpeta backend crea una carpeta llamada IA , haz un archivo que se llame writeCompanyLetter
#En ese archivo crea una funcion que tome 2 parametros :CV Y OfferDescription
#Paso 2 : En writteCompanyLetter , crea una variable , que tenga un promt(string ) para la IA , que utilize
#datos de tu CV , y la descripcion de la oferta , para crear una carta para esa empresa , que de buena imagen sobre la persona
#que este buscando trabajo .
#Paso 3 : Lee la documentacion y invesitga el API de openAI para ver como funciona en python
#Paso 4 : Crea una variable que se llame aiResponse  y que tenga el resultado creado por la IA
#Printea aiResponse , si funciona printea el resultado en main
#Paso 5 : Asegurate de poder pasarle el cv y la descripcion de la oferta a la funcion de AI desde main .

#Section 3 : FLASK APi
#Paso 1 : Con flask , crea un endpoint /job-offers que cuando le hagas get con un pais como parametro , te devueva 
#las ofertas de ese pais . Por ejemplo get("/job-offers/spain") el server me tiene que devolver las ofertas de España .
#Paso 2 : Crea un endpoint que acepte 2 parametros , descripcion oferta y CV y que te devuelva la respuesta el GPT 
#Hay que pasarle un CV y una descripcion de trabajo desde postman .







def get_job_ids(response, url):
    # Realizar la solicitud GET a la página web
    

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Parsear el contenido HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar todas las etiquetas <tr> con el atributo data-jobid
        tr_tags = soup.find_all('tr', {'data-jobid': True})

        # Extraer los IDs de las ofertas
        job_ids = [tr['data-jobid'] for tr in tr_tags]

        return job_ids
    else:
        # Si la solicitud falla, imprimir un mensaje de error y devolver una lista vacía
        print(f"Error al obtener la página {url}: {response.status_code}")
        return []

def scrapeWeb3Offers(country="default"):
    # Crear una lista para almacenar todas las ofertas
    all_offers = []
    
    # Iterar sobre las páginas
    for page_number in [1, 2]:


        if country != "default" :
        # URL de la página web
            url = f"https://web3.career/web3-jobs-{country.lower()}?page={page_number}"


          # Realizar la solicitud GET a la página web
        else :
            url = "https://web3.career/"


        response = requests.get(url)
        # Obtener las IDs de las ofertas en la página actual
        job_ids = get_job_ids(response, url)
        # Aquí puedes usar las IDs de las ofertas para realizar las operaciones necesarias            

       

        

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Parsear el contenido HTML
            soup = BeautifulSoup(response.content, "html.parser")

           
            # Encontrar todas las instancias de "@type": "JobPosting"
            job_postings = soup.find_all("script", {"type": "application/ld+json"})
            
            # Crear una lista para almacenar las ofertas formateadas de esta página
            page_offers = []
            
            # Iterar sobre las ofertas de trabajo y agregarlas a la lista formateada
            for i, job_posting in enumerate(job_postings):
                job_data = json.loads(job_posting.text)
                if job_data.get("@type") == "JobPosting":
                    # Obtener la ID de la oferta
                    offer_id = job_ids[i]

                    title = job_data.get("title", "No title")
                    company = job_data.get("hiringOrganization", {}).get("name", "No company")
                    salary = job_data.get("baseSalary", {}).get("value", {}).get("minValue", "No salary")
                    location = job_data.get("jobLocation", {}).get("address", {}).get("addressLocality", "No location")
                    link = job_data.get("url", "No link")  # Obtener el enlace de la oferta
                    offer_link = generate_offer_link(title, company, offer_id)

                    formatted_offer = {
                        "Title": title,
                        "Company": company,
                        "Salary": salary,
                        "Location": location,
                        "Link" : offer_link
                        
                    }
                    page_offers.append(formatted_offer)
            
            # Agregar las ofertas de esta página a la lista de todas las ofertas
            all_offers.extend(page_offers)
        else:
            # Imprimir un mensaje de error si la solicitud falla
            print(f"Error al obtener la página {page_number}:", response.status_code)

    # Devolver la lista de todas las ofertas
    return all_offers
