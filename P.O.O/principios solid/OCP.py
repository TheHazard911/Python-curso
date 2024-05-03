# las entidades del software se pueden ampliar mas no modificar

class Notificador:
    def __init__(self,usuario,mensaje) -> None:
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"enviando email a {self.usuario.email}")
    

class NotificadorSms(Notificador):
    def Notificar(self):
        print(f"enviando mensaje a {self.usuario.sms}")
        

class NotificadorWhatssapp(Notificador):
    def Notificar(self):
        print(f"enviando whatssapp a {self.usuario.WS}")
    
        