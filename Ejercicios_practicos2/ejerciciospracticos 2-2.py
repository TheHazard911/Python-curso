# creando una funcion que nos devuelve los numeros primos entre 0 y el argumento que pasamos 
numero = int(input("ingresa un numero para saber si es primo: "))

def numeros_primos(num):
    for i in range(2,num-1):
        if num%i==0: return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(num+1):
        resultado = numeros_primos(i)
        if resultado == True: primos.append(i)
    return primos
        
resultado = primos_hasta(numero)
print(resultado)