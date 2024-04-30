# es hacer un atributo de una clase privada

class Miclase:
    
    def __init__(self):
        # en los atributos privados los diferencia los _ al principio del nombre
        self._atributo_privado = "valor1"
    
        self.__atributo_super_privado = "valor2"
    
    def _hablar (self):
        print("hola como estas")
        
objeto = Miclase()
print(objeto._hablar())