# este principio se basa en 1 clase 1 tarea

class Auto():
    def __init__(self,tanque) -> None:
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            return print("has movido el auto exitosamente ")
            
        else:
            print("no hay suficiente combustible")
            
    def obtenerPosicion(self):
        return self.posicion

class TanqueDeCombustible():            
    def __init__(self) -> None:
       self.combustible = 100
        
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad 
        
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self,cantidad):
        self.combustible -= cantidad
        
tanque = TanqueDeCombustible()
auto = Auto(tanque)
    
    
print(auto.obtenerPosicion())
print(auto.mover(10))
print(auto.obtenerPosicion())
print(auto.mover(20))
print(auto.obtenerPosicion())
print(auto.mover(60))
print(auto.obtenerPosicion())
print(auto.mover(100))
print(auto.obtenerPosicion())
print(auto.mover(100))
print(auto.obtenerPosicion())

