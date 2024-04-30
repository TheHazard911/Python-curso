# class Celular():
#     marca = "samsung"
#     modelo = "s23"
#     camara = "38MP"
    
# celular1 = Celular()

class celular:
    def __init__(self, marca, modelo, camara) :
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"estas haciendo un llamada desde un {self.modelo}")
    
    def cortar(self):
        print(f"cortaste la llamada desde un {self.modelo}")
        
celular1 = celular("samsung","s23","48MP")

celular1.llamar()
celular1.cortar()