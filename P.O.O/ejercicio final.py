# chat bot analizador de sentimientos
# sin chatgpt
# from textblob import TextBlob


# class AnalizadorDeSentimientos:
#     def analizar_sentimientos(self,texto):
#         analisis = TextBlob(texto)
#         if analisis.sentiment.polarity > 0:
#             return  "positivo"
#         elif analisis.sentiment.polarity == 0:
#             return "neutral"
#         else:
#             return "negativo"

# analizador = AnalizadorDeSentimientos()
# resultado = analizador.analizar_sentimientos("hello im bad")
# print(resultado)        

            # chat bot utilizando chatgpt 

import openai

openai.api_key = "sk-proj-Q4TE5i0uum6aSHuQNuUYT3BlbkFJ2iIXpJIviL4IGTs5VNR9"

system_rol = '''eres un analizador de sentimientos, yo te paso sentimientos y tu los analizas
                 el sentimiento de los mensajes y me das una repuesta o almenos un caracter 
                 y como maximo 4 caracteres, solo respuestas numericas donde -1 es negatividad maxima 
                 0 es neutral y 1 es positividad maxima (puedes responder solo con int o float)'''
                 

mensajes = [{"role": "system", "content": system_rol}]



class AnalizadorDeSentimientos:
     def analizar_sentimientos(self,polaridad):
        if polaridad > -0.8 and polaridad <= -0.3:
             return "\x1b[1;31m" + "Negativo" + "\x1b[0;37m"
        elif polaridad > -0.3 and polaridad <= -0.1:
             return "\x1b[1;31m" + "Algo negativo" + "\x1b[0;37m"
        elif polaridad >= -0.1 and polaridad <= 0.1:
             return "\x1b[1;33m" + "Neutral" + "\x1b[0;37m"
        elif polaridad >= 0.1 and polaridad <= 0.4:
             return "\x1b[1;32m" + "algo positivo" + "\x1b[0;37m"
        elif polaridad >= 0.4 and polaridad <= 0.9:
             return "\x1b[1;32m" + "positivo" + "\x1b[0;37m"
        elif polaridad >= 0.9:
             return "\x1b[1;32m" + "muy positivo" + "\x1b[0;37m"
        else:
            return "\x1b[1;31m" + "muy negativo" + "\x1b[0;37m"
        
analizador = AnalizadorDeSentimientos()

while True:
          user_prompt = input("\x1b[1;32m" + "\nDime algo: " + "\x1b[0;37m")
          mensajes.append({"role": "user","content": user_prompt})
    
          completion = openai.ChatCompletion.create(
         model = "gpt-3.5",
         menssages = mensajes,
         max_tokkens = 8
     )
          respuesta = completion.choices[0].messages["content"]
          mensajes.append({"role","assistant", "content", respuesta })

          resultado = analizador.analizar_sentimiento(respuesta)  

          print(resultado)
