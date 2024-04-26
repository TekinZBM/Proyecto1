from ScrapeJobOffers import scrapeWeb3Offers

country ="Dubai"
print(f"Ofertas en {country} {"Page 1"}: ")
offers_page1 = scrapeWeb3Offers(country)
for offer in offers_page1:
    print(offer)
    print()

print(f"Offers in {country} {"Page 2"}: ")
offers_page2=scrapeWeb3Offers(country)
for offer in offers_page2:
    print(offer)
    print()
