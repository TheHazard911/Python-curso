# class Diccionario:
#     def verificar_palabra(self,palabra):
#         # logica para verificar palabras
#         pass
    
# class CorrectorOrtografico():
#     def __init__(self) -> None:
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self,texto):
#         # usamos el diccionario para corregir el texto
#         pass

from abc import ABC,abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
        # logica para verificar palabras
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # logica para verificar la palabra si esta en el diccionario
        pass
    
class ServicioOnline(VerificadorOrtografico):
     def verificar_palabra(self, palabra):
         # logica para verificar palabra desde el servicio online
         pass    
    
class correctorOrtografico():
    def __init__(self,verificador) -> None:
        self.verificador = verificador
    
    def corregir_texto(self,texto):
        # usamos el verificador para corregir texto
        pass

corrector = correctorOrtografico(ServicioOnline())