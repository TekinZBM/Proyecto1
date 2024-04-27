from ScrapeJobOffers import scrapeWeb3Offers, get_job_ids
from scrapeOfferacontent import scrape_offer_content


# Obtener las ofertas de trabajo
country = "Spain"
print(f"Ofertas en {country}: ")
offers_page1 = scrapeWeb3Offers(country)

# Iterar sobre cada oferta y obtener su descripción
for offer in offers_page1:
    offer_link = offer['link']
    description = scrape_offer_content(offer_link)
    offer['description'] = description

    # Imprimir la oferta con su descripción
    print(offer)
    print()
