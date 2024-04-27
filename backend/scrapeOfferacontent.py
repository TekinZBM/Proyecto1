import requests
from bs4 import BeautifulSoup
from ScrapeJobOffers import scrapeWeb3Offers

def scrape_offer_content(link):
    try:
        # Realizar la solicitud GET al enlace proporcionado
        response = requests.get(link)
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Obtener el contenido HTML de la página
            html_content = response.text
            
            # Analizar el contenido HTML de la página
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Buscar el elemento que contiene la clase 'text-dark-grey-text'
            main_div = soup.find('div', class_='text-dark-grey-text')
            
            # Extraer todo el texto contenido en el elemento principal
            content = main_div.get_text(separator='\n').strip()
                
            # Devolver el contenido de la oferta
            return content
            
        else:
            return f"Error al obtener la página: Código de estado {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"
