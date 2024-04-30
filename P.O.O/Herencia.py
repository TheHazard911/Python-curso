class persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad        
    
    def hablar(self):
        print("hola estoy hablando un poco")

class empleado(persona):
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

class Estudiante(persona):
    def __init__(self, nombre, edad, nacionalidad,notas,universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universiadad = universidad
    

    
    def hablar(self):
        print("NO")
                
roberto = Estudiante("roberto",44,"argentino",20,"catolica")

roberto.hablar()