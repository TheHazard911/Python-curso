class Persona:
    def __init__(self):
        self._nombre = ""
        self._edad = 0

    def set_datos(self):
        self._nombre = input("Introduce el nombre: ")
        self._edad = int(input("Introduce la edad: "))

    def imprimir_datos(self):
        print("Nombre:", self._nombre)
        print("Edad:", self._edad)


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self._sueldo = 0

    def set_datos(self):
        super().set_datos()
        self._sueldo = float(input("Introduce el sueldo: "))

    def pagar_impuestos(self):
        if self._sueldo > 3000:
            print("Este empleado debe pagar impuestos.")
        else:
            print("Este empleado no debe pagar impuestos.")

    def get_datos(self):
        return [self._nombre, self._edad, self._sueldo]


# Programa principal
empleado1 = Empleado()
empleado1.set_datos()
print("\nDatos del empleado:")
empleado1.imprimir_datos()
empleado1.pagar_impuestos()
print("\nDatos del empleado en formato de lista:")
print(empleado1.get_datos())
