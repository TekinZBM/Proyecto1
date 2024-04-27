from ScrapeJobOffers import scrapeWeb3Offers, get_job_ids
from scrapeOfferacontent import scrape_offer_content
# Obtener las ofertas de trabajo
country = "Spain"
print(f"Ofertas en {country}: ")
offers_page1 = scrapeWeb3Offers(country)

# Iterar sobre cada oferta y obtener su descripción
for offer in offers_page1:
    print(offer)  # Imprimir la oferta para verificar su estructura
    offer_link = offer.get('Link')  # Utilizar get() para evitar errores de clave faltante
    if offer_link:
        description = scrape_offer_content(offer_link)
        print(description)
        print()
    else:
        print("No se encontró el enlace para la oferta.")