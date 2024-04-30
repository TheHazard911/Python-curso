class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print("Estudiando...")
    
nombre = input("Ingrese su nombre: ")
edad = input("ingrese su edad: ")
grado = input("ingrese su grado: ")

estudiante = Estudiante(nombre,edad,grado)

print(f"""
      Datos del estudiante: \n\n
      Nombre: {estudiante.nombre} 
      edad: {estudiante.edad}     
      grado: {estudiante.grado}
      
      """ )

while True:
    estudiar = input()
    if (estudiar.lower == "estudiar"):
        estudiante.estudiar()