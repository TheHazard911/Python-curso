# leer un archivo completo
archivo = open("archivos\\archivo.txt",encoding="UTF=8")
# print(archivo.read())

# leer la linea por linea de un archivo

# linea = archivo.readlines()

# leer una sola linea
linea = archivo.readline()

# cerrar el archivo

archivo.close()

print(linea)