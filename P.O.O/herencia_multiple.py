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
    
# ejemplo de herencia multiple
class Artista:
    def __init__(self,habilidad) :
        self.habilidad = habilidad
    def mostrar_habilidad(self):
        print(f"Mi habilidad es : {self.habilidad   }")

class EmpleadoArtista(persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
       persona.__init__(self,nombre, edad, nacionalidad)
       Artista.__init__(self,habilidad)
       self.salario = salario
       self.empresa = empresa
       
# aca termina el ejemplo            
roberto = Estudiante("roberto",44,"argentino",20,"catolica")

herencia = issubclass(EmpleadoArtista,Artista)
instancia = isinstance(roberto,EmpleadoArtista)

print(instancia)