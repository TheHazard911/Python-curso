# creando una funcion que muestre la serie fibonacci entre 0 y un numero dado
n1 = int(input("ingrese un numero desde donde quiere comenzar la serie: "))
n2 = int(input("ingrese otro numero donde quiere terminar la serie: "))

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [n1]
    for i in range(num):
        if b > num: return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            a,b = b,a+b
            
resultado = fibonacci(n2)
print(resultado)