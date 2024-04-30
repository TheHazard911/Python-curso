#
# systaxis
# nombre = lambda x : x*2
# la x es un parametro, se pueden incluir mas y a partir de los : es la operacion que se realiza
# luego se pasan valores a la funcion

# ejemplo

# Función lambda que suma dos números
n1 = int(input("ingresa un numero para sumar: "))
n2 = int(input("ingresa otro numero para sumar: "))

suma = lambda x, y: x + y
# Uso de la función lambda
# dentro de la suma se incluyen las variables o parametros para la operacion
resultado = suma(n1, n2)
print(f"El resultado de la suma es: {resultado}")
