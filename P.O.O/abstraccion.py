                    # abstraccion general
class Auto():
    # funcion constructora
    def __init__(self):
        self._estado = "apagado"
        
    # demas metodos
    def encender(self):
        self._estado = "encendido"
        print("el auto esta encendido")
    
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("conduciendo el auto")
        
mi_auto = Auto()

mi_auto.conducir()
