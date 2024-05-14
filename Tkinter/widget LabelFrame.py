from tkinter import *

root = Tk()
root.title("frames")

# gracias al Label frame podemos dividir los cuadros
# en secciones para con grid independientes

buscador = LabelFrame(root,
                      text="buscador",
                      padx=10,
                      pady=10,
                      ) #aca es margin
buscador.grid(column=0,
              row=0,
              padx=50,
              pady=0
              ) #aca es padding

# en vez de colocar root (pantalla principal) 
# podemos colocar el nuevo frame que seria buscador
barra = Entry(buscador, text="buscas algo?").pack()
boton = Button(buscador,text="buscar").pack()

# se puede trabajar con pack y grids siempre y cuando
# los frame sean distintos

mainloop()