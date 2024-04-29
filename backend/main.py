from ScrapeJobOffers import scrapeWeb3Offers, get_job_ids
from scrapeOfferacontent import scrape_offer_content
from IA.writeCompanyLetter import writeCompanyLetter
from curriculum import dummyCV
# Obtener las ofertas de trabajo

#ofertas = scrapeWeb3Offers("Spain")
offerDescription = "Blackwing is looking for a Senior Go Engineer to join a small team on the quest to transform the future of finance. Our ideal candidate thrives on having complete ownership over meaningful areas of the stack, solving complex engineering problems, and shipping products that users will love."

airesponse = writeCompanyLetter(dummyCV,offerDescription)

print(airesponse)









   







