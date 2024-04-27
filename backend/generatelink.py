def generate_offer_link(title, company, offer_id):
    # Reemplazar espacios y caracteres especiales por guiones
    title_company_str = f"{title.lower().replace(' ', '-').replace(',', '').replace('.', '').replace('/', '')}-{company.lower().replace(' ', '-').replace(',', '').replace('.', '').replace('/', '')}"
    # Combinar el título, la empresa y el ID de la oferta
    link = f"https://web3.career/{title_company_str}/{offer_id}"
    return link