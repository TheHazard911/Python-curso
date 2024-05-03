class Personaje:
    # creando la funcion constructora
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    # creando la representacion
    def __repr__(self):
        return f'{self.nombre}(Fuerza : {self.fuerza},velocidad: {self.velocidad})'
    
    def __add__(self,otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.34)
        nueva_velocidad = round(((self.velocidad + otro_pj.fuerza)/2)**1.34)
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)
    
        
    
goku = Personaje("goku",100,100)
vegetta = Personaje("vegetta",95,95)
giren = Personaje("giren ",130,140)
gogeta = goku+vegetta
gireta = gogeta + giren

print(gireta)