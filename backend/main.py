from ScrapeJobOffers import scrapeWeb3Offers, get_job_ids

country ="Spain"
print(f"Ofertas en {country} {"Page 1 and 2"}: ")
offers_page1 = scrapeWeb3Offers(country)
for offer in offers_page1:
    print(offer)
    print()


