from ScrapeJobOffers import scrapeWeb3Offers, get_job_ids
from scrapeOfferacontent import scrape_offer_content
from curriculum import dummyCV
from flask import Flask, request, jsonify,render_template
from IA.writeCompanyLetter import writeCompanyLetter 
# Obtener las ofertas de trabajo


app = Flask(__name__, template_folder='../frontend/templates')
@app.route("/")
def index():
    return render_template("index.html")



@app.route('/job-offers')
def get_job_offers():
    # Obtener el parámetro del país de la solicitud
    country = request.args.get('country', 'default')

    # Obtener las ofertas de trabajo para el país dado
    job_offers = scrapeWeb3Offers(country)

    # Devolver las ofertas de trabajo como respuesta JSON
    return render_template("job_offers.html", job_offers=job_offers)



@app.route("/response")
def get_ia_response():
    # Obtener el parámetro del CV y Descripcion
    dummyCV = request.args.get("cv", "default")    
    description = request.args.get("description", "default")

    # Obtener la respuesta del IA  
    ia_response = writeCompanyLetter(dummyCV, description)
    
    # Convertir el objeto ChatCompletion a un diccionario
    ia_response_dict = ia_response.to_dict()
    carta_generada = ia_response_dict['choices'][0]['message']['content']
    
    # Renderizar la plantilla con la respuesta del IA
    return render_template("iaresponse.html", carta_generada=carta_generada)
if __name__ == '__main__':
    app.run(debug=True)












   







