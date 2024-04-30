# sistema para una escuela

# ejercicio 2 falta terminar (me dio sueño 10:43 PM)
class persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad 
        
    def mostrar_datos(self):
        print(f"Nombre {self.nombre}")
        print(f"edad {self.edad}")
        

class Estudiante(persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad )
        self.grado = grado
        
    def mostrar_grado(self):
        print(f"Nombre {self.grado}")


estudiante =Estudiante("juan",14,"10mo")

estudiante.mostrar_datos()
estudiante.mostrar_grado()

