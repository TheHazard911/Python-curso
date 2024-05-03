class Motocicleta:
    # atributo de clase
    es_nueva = True
    marcha_motor = False
    # metodo constructor
    def __init__(self, color, matricula, litros_combustible,num_ruedas, 
                 marca, modelo, fecha_fabricacion, velocidad_max, peso,capacidad_tanque,precio):
        self.color = color
        self.matricula = matricula
        self.litros_combustible = litros_combustible
        self.num_ruedas = num_ruedas 
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_max  = velocidad_max
        self.peso = peso
        self.capacidad_tanque = capacidad_tanque
        self.precio = precio
    # metodos
    def arrancar(self):
        if(self.marcha_motor == False):
            print("El motor a arrancado")
            self.marcha_motor = True
        elif(self.marcha_motor == True):
            print("El motor ya esta en marcha")
    
    def detener(self):
        if(self.marcha_motor == True):
            print("El motor se a detenido")
            self.marcha_motor = False
        elif(self.marcha_motor == False):
            print("El motor ya estaba detenido")
    
    def consultar_precio(self):
        try:
            print(f"El precio de la motocicleta marca {self.marca} y modelo {self.modelo} es de {self.precio} $.")
        except AttributeError:
             print("Esta motocicleta aún no tiene un precio asignado.")
    
    def cargar_combustible(self, litros):
        if self.litros_combustible+ litros > self.capacidad_tanque:
            print("No puedes cargar más combustible del que el tanque puede contener.")
        else:
            self.litros_combustible += litros
            print(f"Has cargado {litros} litros de combustible. Ahora tienes {self.litros_combustible} litros de combustible.")
            print(f"La capacidad máxima del tanque es de {self.capacidad_tanque} litros.")
            print(f"Faltan {self.capacidad_tanque - self.litros_combustible} litros para llenar el depósito.")
            print(f"Reporte del depósito de “{self.marca} {self.modelo} de motocicleta”.")
    
    def recargar_combustible(self):
        litros_a_recargar = float(input("Por favor, introduce la cantidad de litros a recargar: "))
        if self.litros_combustible + litros_a_recargar > self.capacidad_tanque:
            print("No puedes recargar más combustible del que el tanque puede contener. Inténtalo de nuevo.")
        else:
            self.litros_combustible += litros_a_recargar
            print(f"Has recargado {litros_a_recargar} litros de combustible. Ahora tienes {self.litros_combustible} litros de combustible.")
   
moto = Motocicleta(
     color="Rojo", 
     matricula="ABC123", 
     litros_combustible=10, 
     num_ruedas=2, 
     marca="Yamaha", 
     modelo="YZF-R1", 
     fecha_fabricacion="2024-01-01", 
     velocidad_max=299, 
     peso=200,
     capacidad_tanque = 15,
     precio= 15000
    )
otra_moto = Motocicleta(
    matricula="XYZ789", 
    color="Azul", 
    marca="Honda", 
    modelo="CBR600RR", 
    fecha_fabricacion="2024-02-01", 
    velocidad_max=252, 
    peso=194, 
    num_ruedas=2, 
    capacidad_tanque = 20,
    precio= 10000,
    litros_combustible= 10
)

moto.cargar_combustible(10)