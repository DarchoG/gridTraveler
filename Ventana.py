import tkinter as tk
import Laberinto

def habilitar_espacios():
    global entrada1, entrada2, boton2

    entrada1 = tk.Entry(ventana)
    entrada1.pack()
    entrada2 = tk.Entry(ventana)
    entrada2.pack()

    boton2 = tk.Button(ventana, text="Botón 2", state=tk.DISABLED, command=guardar_variables)
    boton2.pack()

    def verificar_contenido(event=None):
        if entrada1.get() and entrada2.get():
            boton2.config(state=tk.NORMAL)  # Habilitar el segundo botón
        else:
            boton2.config(state=tk.DISABLED)  # Deshabilitar el segundo botón

    entrada1.bind("<KeyRelease>", verificar_contenido)
    entrada2.bind("<KeyRelease>", verificar_contenido)

def guardar_variables():
    global entrada1, entrada2

    N = int(entrada1.get())
    M = int(entrada2.get())

    Resultados = Laberinto.generarMatriz(N, M)
    # Eliminar todos los widgets en la ventana actual
    for widget in ventana.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(ventana, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True) # Hacer que el canvas se ajuste al tamaño de la ventana

    dibujar_cuadrados(Resultados, canvas)

    # Crear un nuevo botón "Cambiar"
    boton_cambiar = tk.Button(ventana, text="Cambiar", command = recrear_elementos)
    boton_cambiar.pack()

def recrear_elementos():
    # Llamamos a la función habilitar_espacios para recrear los elementos
    for widget in ventana.winfo_children():
        widget.destroy()    

    boton = tk.Button(ventana, text="Habilitar Espacios", command=habilitar_espacios)
    boton.pack()

    habilitar_espacios()

def dibujar_cuadrados(matriz, canvas):

    filas = len(matriz)
    columnas = len(matriz[0])

    ventana.update_idletasks() # Permite que la ventana se cargue completamente
    ancho_canvas = canvas.winfo_width()
    alto_canvas = canvas.winfo_height()

    ancho_cuadrado = ancho_canvas / columnas
    alto_cuadrado = alto_canvas / filas

    print(ancho_cuadrado)
    print(alto_cuadrado)

    for i in range(filas):
        for j in range(columnas):

            if(matriz[i][j] == 0):
                color = "white"
            elif(matriz[i][j] == -1):
                color = "black"
            else:
                color = "blue"    

            x1 = j * ancho_cuadrado
            y1 = i * alto_cuadrado
            x2 = (j + 1) * ancho_cuadrado
            y2 = (i + 1) * alto_cuadrado
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Laberinto")
ventana.geometry("800x600")

# Crear el botón
boton = tk.Button(ventana, text="Habilitar Espacios", command=habilitar_espacios)
boton.pack()

#ventana.update_idletasks()
#Ancho = ventana.winfo_reqwidth();
#Altura = ventana.winfo_reqheight();
#x = (Ancho - boton.winfo_reqwidth()) / 2;
#y = (Altura - boton.winfo_reqwidth()) / 2;

boton.place();

ventana.mainloop()
