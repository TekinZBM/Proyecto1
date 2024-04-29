import openai






def writeCompanyLetter(CV , offerDescription):
#OpenAIKey : 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

    openai.api_key = "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"
    

   
    # Crea el prompt concatenando el CV y la descripción de la oferta
    prompt = f"""

    Tu trabajo es crear una carta para esa empresa, que de buena imagen sobre la persona que esta buscando trabajo.\n
    Crea esta carta para que sea un email que convenzca a la persona que este buscando trabajo por que el candidato es adecuando para el trabajo\n
    Tienes que ser persuasivo pero profesinal, y tiene que recalcar las habilidades del candidato en relacion a los requisitos de la oferta y que exprime los intereses del candidato por el producto y empresa .\n
    No lo hagas muy largo . \n
    Este es el Curriculum Vitae del candidato : {CV}.\n
    Esta es la oferta de trabajo : {offerDescription}.\n

    
    """


    print(prompt)

    
   

  