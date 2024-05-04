from flask import Flask, request, jsonify
from ScrapeJobOffers import scrapeWeb3Offers

app = Flask(__name__)

@app.route('/job-offers')
def get_job_offers():
    # Obtener el parámetro del país de la solicitud
    country = request.args.get('country', 'default')

    # Obtener las ofertas de trabajo para el país dado
    job_offers = scrapeWeb3Offers(country)

    # Devolver las ofertas de trabajo como respuesta JSON
    return jsonify(job_offers)

if __name__ == '__main__':
    app.run(debug=True)