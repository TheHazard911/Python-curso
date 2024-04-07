                            # Ejercicios practicos
                            
# 1 alumno profesor 
# 1 aistente 

# A) pedir la edad de los compañeros que vinieron hoy a clases y ordenar los datos de mayor a menor 

# b) el mayor es el profesor y el menor es el asistente:
#     ¿quien es quien?

personas = int(input("ingrese la cantidad de alumnos que quiere registrar: "))

def datos(cantidad):
    compañeros = []
    for i in range (cantidad):
        nombre = input("ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor

asistente,profesor = datos(personas)

print(f"el asistente es {asistente}")
print(f"el profesor es {profesor}")