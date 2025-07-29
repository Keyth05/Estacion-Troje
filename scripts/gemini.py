from google.generativeai import configure, GenerativeModel

def formatear_respuesta(texto):
    return f"""
        <div style='background-color: #ffffff; color: #000000; padding: 20px; border-radius: 10px;
                    border: 1px solid #ccc; font-size: 18px; line-height: 1.8; text-align: justify;'>
            {texto.replace("**", "<strong>").replace(chr(10), "<br>")}
        </div>
    """

def configurar_gemini(api_key):
    configure(api_key=api_key)
    modelo = GenerativeModel(model_name="models/gemini-1.5-flash")
  # O usa 'models/gemini-1.5-flash'
    return modelo

def consultar_gemini(modelo, pregunta):
    respuesta = modelo.generate_content(pregunta)
    return respuesta.text
