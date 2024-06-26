from openai import OpenAI






client = OpenAI()

def writeCompanyLetter(CV , offerDescription):






    # Crea el prompt concatenando el CV y la descripción de la oferta
    prompt = f"""
    Tu trabajo es crear una carta para esa empresa, que de buena imagen sobre la persona que está buscando trabajo.\n
    Crea esta carta para que sea un email que convenza a la persona que está buscando trabajo por que el candidato es adecuado para el trabajo.\n
    Tienes que ser persuasivo pero profesional, y tiene que recalcar las habilidades del candidato en relación a los requisitos de la oferta y que exprese los intereses del candidato por el producto y empresa.\n
    No lo hagas muy largo.\n
    Este es el Curriculum Vitae del candidato:\n{CV}.\n
    Esta es la oferta de trabajo:\n{offerDescription}.\n
    """
  

    
    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "content": prompt}

            ],
            max_tokens=500,  # Ajustamos el máximo de tokens para cumplir con las métricas
            
        )

    return response


   

  


