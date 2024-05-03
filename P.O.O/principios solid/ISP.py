from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador,Durmiente,Comedor):
    def comer(self):
        print("El humano esta comiendo")
    
    def trabajar(self):
        print("el humano esta trabajando")
        
    def dormir(self):
        print("el humano esta durmiendo")


class Robot(Trabajador):
    def trabajar(self):
        print("el humano esta trabajando")
        
robot =Robot()
humano = Humano()

robot.trabajar()
humano.trabajar()
