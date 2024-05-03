class Persona:
    # metodo constructor
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    # este metodo nos devuelve una representacion del objeto en una cadena de texto
    
    def __str__(self):
        return f'Persona(nombre = {self.nombre}, edad ={self.edad})'
    
    def __repr__(self):
        return f'persona {self.nombre}, {self.edad}'

    def __add__(self,otro):
         nuevo_valor = self.edad + otro.edad
         return Persona(self.nombre+otro.nombre,nuevo_valor)



dalto = Persona("Lucas",21)
pedro = Persona("pedro",30)
maria = Persona("maria",19)

nueva_persona = dalto + pedro + maria

print(nueva_persona.nombre)
        
        




















               # Métodos de iniciación y constructores


# __init__ Inicializa un objeto

# Crea un nuevo objeto cuando se llama a la instancia de una clase.

# class Car(object):
#     def __init__(self):
#         ...
#     def __repr__(self):
#         ...
# __new__ Crea un objeto

# __del__ Elimina un objeto

# Métodos mágicos de comparación
# __lt__ a < b

# __gt__ a > b

# __le__ a <= b

# __ge__ a >= b

# __ne__ a != b

# __eq__ a == b

# Métodos mágicos para matemáticas
# __add__ obj + …

# __sub__ obj - …

# __mul__ obj * …

# __floordiv__ obj //

# __truediv__ obj /

# __mod__ obj %

# __pow__ obj ** …

# Otros Métodos mágicos
# __str__ Pretty print object. Devuelve una cadena de carácteres. Representación Legible para usuarios.

# __repr__ Devuelve una cadena de carácteres. Representación no ambigua útil para desarrolladores.

# __len__ Devuelve la cantidad de elementos que tiene una lista.