import requests
from bs4 import BeautifulSoup

def scrapeOfferContent(link):
    try:
        # Realizar la solicitud GET al enlace proporcionado
        response = requests.get(link)
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Obtener el contenido HTML de la página
            html_content = response.text
            
            # Analizar el contenido HTML de la página
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Buscar todos los elementos que contienen la clase 'section'
            sections = soup.find_all('div', class_='section')
            
            # Extraer el texto de todas las secciones encontradas
            content = ''
            for section in sections:
                content += section.get_text(separator='\n').strip() + '\n\n'
                
            # Devolver el contenido de todas las secciones
            return content
            
        else:
            return f"Error al obtener la página: Código de estado {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

# Ejemplo de uso
link = "https://web3.career/product-lead-moonsong-labs/57085"
contenido_oferta = scrapeOfferContent(link)
print(contenido_oferta)
