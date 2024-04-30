def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("despues de llamar a la funcion")
    return funcion_modificada

# def saludo():
#     print("hola mundo")
    
# saludo_modificado = decorador(saludo)

# saludo_modificado()

@decorador
def saludo():
     print("hola mundo")


saludo()    