import re
var = input("ingresa un texto a buscar")

texto = '''hola maestro, esta es la cadena 1
            esta es la segunda linea
            esta es la final'''

# haciendo una busqueda simple

resultado = re.findall(var ,texto)

print(resultado)