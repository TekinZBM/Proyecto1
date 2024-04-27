import requests
from bs4 import BeautifulSoup

def scrapeOfferContent(link):
# Realizar la solicitud GET a la página web
        link = "https://web3.career/product-lead-moonsong-labs/57085"
        response = requests.get(url)