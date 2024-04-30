class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad
    
    # obtener (getters)
    def get_nombre(self):    
        return self._nombre
    
    # (setters lo mismo que getter pero los defino )
    def set_nombre(self,new_nombre):    
        self._nombre = new_nombre
    


    
dato = Persona("eber",18)

nombre = dato.get_nombre()
print(nombre)

nombre = dato.set_nombre("pepito")

nombre = dato.get_nombre()
print(nombre)

# con los decoradores se minimiza el uso de get y set