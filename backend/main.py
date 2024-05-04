from ScrapeJobOffers import scrapeWeb3Offers, get_job_ids
from scrapeOfferacontent import scrape_offer_content
from curriculum import dummyCV
from flask import Flask, request, jsonify
from IA.writeCompanyLetter import writeCompanyLetter
# Obtener las ofertas de trabajo

app = Flask(__name__)

@app.route('/job-offers')
def get_job_offers():
    # Obtener el parámetro del país de la solicitud
    country = request.args.get('country', 'default')

    # Obtener las ofertas de trabajo para el país dado
    job_offers = scrapeWeb3Offers(country)

    # Devolver las ofertas de trabajo como respuesta JSON
    return jsonify(job_offers)



@app.route ("/response")
def get_ia_response():
    #Obtener el parametro del CV y Descripcion
    dummyCV = request.args.get("cv", "default")    
    description = request.args.get("description", "default")

    #Obtener la respuesta del IA  
    ia_response = writeCompanyLetter(dummyCV, description)
    
    # Convertir el objeto ChatCompletion a un diccionario
    ia_response_dict = ia_response.to_dict()
    
    #Devolver la respuesta del IA como JSON 
    return jsonify(ia_response_dict)
    

if __name__ == '__main__':
    app.run(debug=True)













   







