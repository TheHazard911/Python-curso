class Animal:
    def comer(self):
        print("el animal esta comiendo")
class Ave(Animal):
    def volar(self):
        print("el animal esta volando")
class Mamifero(Animal):
    def amamantar(self):
        print("el animal esta amamantando")

class Murcielago(Mamifero,Ave):
    pass

animal = Murcielago()

animal.amamantar()
animal.comer()
animal.volar()


print(Murcielago.mro())