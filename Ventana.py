import tkinter as tk
from tkinter import ttk
import Laberinto

def habilitar_espacios(ventana, boton):
    global entrada1, entrada2, boton2

    

    boton.destroy();

    entrada1 = tk.Entry(ventana)
    entrada1.pack()
    entrada2 = tk.Entry(ventana)
    entrada2.pack()

    boton2 = tk.Button(

        ventana, #Ventana pertenencia
        text="Generar Laberinto", #Texto 
        background="#373739", #Fondo
        foreground="white", # Color de la letra
        #state=tk.DISABLED,
        font=("Helvetica", 12, "bold"),
        width = proporcionAncho(1.95, ventana), #Obtener Proporciones
        height = proporcionLargo(0.3, ventana), #Obtener Proporciones
        borderwidth=0,
        cursor = "hand2",
        command= lambda : guardar_variables(ventana)
        
    )

    boton2.pack()

    def verificar_contenido(event=None):
        if entrada1.get() and entrada2.get():
            boton2.config(state=tk.NORMAL)  # Habilitar el segundo botón
        else:
            boton2.config(state=tk.DISABLED)  # Deshabilitar el segundo botón

    entrada1.bind("<KeyRelease>", verificar_contenido)
    entrada2.bind("<KeyRelease>", verificar_contenido)

def guardar_variables(ventana):
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

def recrear_elementos(ventana):
    # Llamamos a la función habilitar_espacios para recrear los elementos
    for widget in ventana.winfo_children():
        widget.destroy()    
        
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

def proporcionAncho(X, Ventana):

    Ancho = Ventana.winfo_screenwidth();

    return int((Ancho * X)/100);

def proporcionLargo(X, Ventana):

    Largo = Ventana.winfo_screenheight();

    return int((Largo * X)/100);


def Inicio():

    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Laberinto")

    Ancho = ventana.winfo_screenwidth()
    Largo = ventana.winfo_screenheight();
    ventana.geometry(str(int(Ancho * 40 / 100))+ "x" + str(int(Largo * 60 / 100)))

    gris = tk.Frame(ventana, bg = '#19191a')
    gris.place(relwidth = 1, relheight = 1)

    style = ttk.Style()
    style.configure('TButton', borderwidth=2, relief='solid', foreground="white", background="#373739", padding=10, anchor = "center")

    # Crear el botón

    boton = tk.Button(

        ventana, #Ventana pertenencia
        text="Habilitar Espacios", #Texto 
        background="#373739", #Fondo
        foreground="white", # Color de la letra
        font=("Helvetica", 12, "bold"),
        width = proporcionAncho(3.25, ventana), #Obtener Proporciones
        height = proporcionLargo(0.5, ventana), #Obtener Proporciones
        borderwidth=0,
        cursor = "hand2",
        relief = tk.RAISED, 
        command = lambda : habilitar_espacios(ventana, boton),
        
        )
    boton.pack(expand=True)

    ventana.mainloop()

Inicio();
