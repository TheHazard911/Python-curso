# decorador @property

class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad
    
# al agregar @property podemos convertir la funcion en una propiedad y podemos verla asi sea privada 
    @property
    # obtener (getters)
    def get_nombre(self):    
        return self.__nombre

dato = Persona("eber",18)


nombre = dato.get_nombre

print(nombre)

# con los decoradores se minimiza el uso de get y set