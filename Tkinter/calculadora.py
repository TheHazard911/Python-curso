# calculadora parte grafica

from tkinter import *
from tkinter.messagebox import *

# ventana
root = Tk()
root.title("calculadora")
root.iconbitmap("img/calculator.ico")
root.resizable(0,0)  #esto sirve para no cambiar el tamaño de la ventana
root.geometry("260x390") #definimos la ventana por defecto
#                   logica
def pulsar_boton(valor):
    anterior = display.get()
    display.delete(0,END)
    display.insert(0,str(anterior) + str(valor))

def borrar():
    display.delete(0,END)

def igual():
   try:
    global num2
    num2 = display.get()
    display.delete(0,END)
    if operacion == "+":
        display.insert(0, round(float(num1) + float(num2)))
    elif operacion == "-":
        display.insert(0, round(float(num1) - float(num2)))
    elif operacion == "*":
        display.insert(0, round(float(num1) * float(num2)))
    elif operacion == "/":
        display.insert(0, round(float(num1) / float(num2)))
   except NameError:
    display.insert(0,"error")
    
def suma():
    global num1
    global operacion
    num1 = display.get()
    num1 = float(num1)
    display.delete(0,END)
    operacion = "+"

def rest():
    global num1
    global operacion
    num1 = display.get()
    num1 = float(num1)
    display.delete(0,END)
    operacion = "-"
    
def mult():
    global num1
    global operacion
    num1 = display.get()
    num1 = float(num1)
    display.delete(0,END)
    operacion = "*"
    
def div():
    global num1
    global operacion
    num1 = display.get()
    num1 = float(num1)
    display.delete(0,END)
    operacion = "/"
    
# ---------calculadora-----------------------
#pantalla
display = Entry(root,
                width="20",
                background="white",
                fg="black",
                borderwidth=0,
                font=("arial",16,"bold"))# se puede agregar fuente
#los padx/y sirven para los margenes
# lo que es columspan es para definir cuantas columnas queremos ocupar
display.grid(row=0,padx=1,pady=1, columnspan=10) 
# botones

boton_1 = Button(root,
                 text="1",
                 height=4,
                 width=8,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=lambda: pulsar_boton(1)
                 ).grid(row=1,column=0,padx=1,pady=1)

boton_2 = Button(root,
                 text="2",
                 height=4,
                 width=8,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=lambda: pulsar_boton(2)
                 ).grid(row=1,column=1,padx=1,pady=1)

boton_3 = Button(root,
                 text="3",
                 height=4,
                 width=8,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=lambda: pulsar_boton(3)
                 ).grid(row=1,column=2,padx=1,pady=1)

boton_4 = Button(root,
                 text="4",
                 height=4,
                 width=8,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=lambda: pulsar_boton(4)
                 ).grid(row=2,column=0,padx=1,pady=1)

boton_5 = Button(root,
                 text="5",
                 height=4,
                 width=8,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=lambda: pulsar_boton(5)
                 ).grid(row=2,column=1,padx=1,pady=1)

boton_6 = Button(root,
                 text="6",
                 height=4,
                 width=8,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=lambda: pulsar_boton(6)
                 ).grid(row=2,column=2,padx=1,pady=1)

boton_7 = Button(root,
                 text="7",
                 height=4,
                 width=8,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=lambda: pulsar_boton(7)
                 ).grid(row=3,column=0,padx=1,pady=1)

boton_8 = Button(root,
                 text="8",
                 height=4,
                 width=8,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=lambda: pulsar_boton(8)
                 ).grid(row=3,column=1,padx=1,pady=1)

boton_9 = Button(root,
                 text="9",
                 height=4,
                 width=8,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=lambda: pulsar_boton(9)
                 ).grid(row=3,column=2,padx=1,pady=1)

boton_igualar = Button(root,
                 text="=",
                 height=4,
                 width=8,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=igual
                 ).grid(row=4,column=2,padx=1,pady=1)

boton_0 = Button(root,
                 text="0",
                 height=4,
                 width=8,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=lambda: pulsar_boton(0)
                 ).grid(row=4,column=1,padx=1,pady=1)

boton_punto = Button(root,
                 text=".",
                 height=4,
                 width=8,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=lambda: pulsar_boton(".")
                 ).grid(row=4,column=0,padx=1,pady=1)


boton_sum = Button(root,
                 text="+",
                 height=4,
                 width=8,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=suma
                 ).grid(row=1,column=4,padx=1,pady=1)

boton_res = Button(root,
                 text="-",
                 height=4,
                 width=8,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=rest
                 ).grid(row=2,column=4,padx=1,pady=1)

boton_div = Button(root,
                 text="/",
                 height=4,
                 width=8,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=div
                 ).grid(row=3,column=4,padx=1,pady=1)

boton_mult = Button(root,
                 text="*",
                 height=4,
                 width=8,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=mult
                 ).grid(row=4,column=4,padx=1,pady=1)
boton_delete = Button(root,
                 text="CE",
                 height=4,
                 width=36,
                 bg="black",
                 fg="white",
                 borderwidth=0,
                 cursor="hand2",  #esto es un hover de click
                 command=borrar
                 ).grid(row=5,column=0,columnspan=5,padx=1,pady=1)



root.mainloop()