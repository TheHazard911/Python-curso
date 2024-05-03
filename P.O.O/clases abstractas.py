from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"hola , me llamo {self.nombre} y tengo {self.edad} años")
        

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
       print(f"Estoy estudiando: {self.actividad}")
    
        
class Trabajador(Persona):
     def __init__(self,nombre,edad,sexo,actividad):
         super().__init__(nombre,edad,sexo,actividad)
        
     def hacer_actividad(self):
         print(f"actualmente estoy trabajando en el rubro de programador {self.actividad}")
        

pedrito = Estudiante("pedro",18,"masculino","programacion")
dalto = Estudiante("lucas",21,"masculino","programacion")

dalto.presentarse()
dalto.hacer_actividad()
pedrito.presentarse()
pedrito.hacer_actividad()