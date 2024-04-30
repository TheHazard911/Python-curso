# a) pedirle al usuario que diga cualquier texto real y:
    # 1 segundo /2palabras  
    # cuantos segundos / x palabras

#     -calcular cuanto tardaria en decir esa frase 
#     -cuantas palabras dijo?
    
# b) si se tarda mas de 1 minuto 
#     -decirle: Para flaco tampoco te pedi un testamento 
    
# c) dalto habla un 30% mas rapido:
#     cuanto tardaria el en decirlo?

frase = input("dime algo y te calculo cuanto tardas diciendolo y te comparo con dalto:")

palabras_separadas = frase.split(" ")

cantidad_de_palabras = len(palabras_separadas)

print(f"(dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirlo")
print(f"Dalto lo diria en {cantidad_de_palabras/2*1.3} segundos en decirlo")

if cantidad_de_palabras > 5:
    print("para flaco, no te pedi un testamento")
else:
    print("mejor no digas nada ")