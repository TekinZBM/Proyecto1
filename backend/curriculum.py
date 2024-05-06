
dummyCV= "Nombre :Tekin | Edad : 25  | Habilidaded : Python , JavaScript , Html , Css | Experiencia : 5 experiencia en web-based products "

def scrapeWeb3Offers(country="default"):
    # Crear una lista para almacenar todas las ofertas
    all_offers = []
    
    # Iterar sobre las páginas
    for page_number in [1, 2]:
        if country != "default":
            # URL de la página web
            url = f"https://web3.career/web3-jobs-{country.lower()}?page={page_number}"
        else:
            url = "https://web3.career/"

        # Realizar la solicitud GET a la página web
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Parsear el contenido HTML
            soup = BeautifulSoup(response.content, "html.parser")
           
            # Encontrar todas las instancias de "@type": "JobPosting"
            job_postings = soup.find_all("script", {"type": "application/ld+json"})
            
            # Iterar sobre las ofertas de trabajo y agregarlas a la lista formateada
            for job_posting in job_postings:
                job_data = json.loads(job_posting.text)
                if job_data.get("@type") == "JobPosting":
                    title = job_data.get("title", "No title")
                    company = job_data.get("hiringOrganization", {}).get("name", "No company")
                    salary = job_data.get("baseSalary", {}).get("value", {}).get("minValue", "No salary")
                    location = job_data.get("jobLocation", {}).get("address", {}).get("addressLocality", "No location")
                    link = job_data.get("url", "No link")  # Obtener el enlace de la oferta
                    
                    # Formatear la oferta y agregarla a la lista de todas las ofertas
                    formatted_offer = f"Title: {title}\nCompany: {company}\nSalary: {salary}\nLocation: {location}\nLink: {link}\n"
                    all_offers.append(formatted_offer)
        else:
            # Imprimir un mensaje de error si la solicitud falla
            print(f"Error al obtener la página {page_number}:", response.status_code)

    # Devolver la lista de todas las ofertas
    return all_offers