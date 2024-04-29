from slugify import slugify
def generate_offer_link(title, company, offer_id):
    if offer_id:
        # Crear una cadena slug para el título y la empresa
        title_slug = slugify(title)
        company_slug = slugify(company)

        # Combinar el título, la empresa y el ID de la oferta
        return f"https://web3.career/{title_slug}-{company_slug}/{offer_id}"
    else:
        # Si no se proporciona un ID de oferta, solo generar un enlace con el título y la empresa
        title_slug = slugify(title)
        company_slug = slugify(company)
        return f"https://web3.career/{title_slug}-{company_slug}"