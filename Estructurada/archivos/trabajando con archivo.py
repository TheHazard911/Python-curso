#2 listas: una con nombre otra con apellidos 

nombres = ["lucas","matias","pedro","roberto"]
apellidos = ["dalto","zing","azuca","coco"]

# registrar esa info en un txt de forma optima con un bucle for 

with open("nombrearchivo.txt","w") as arch:
    arch.writelines("los datos son: \n")
    [arch.writelines(f"Nombre: {n}\n apellido: {a} \n-----------------") for n,a in zip(nombres,apellidos)]