import tkinter as tk
from tkinter import ttk
import Laberinto

def Inicio(ventana): #1° Screen

    # Crear la ventana
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

def proporcionAncho(X, Ventana):

    Ancho = Ventana.winfo_screenwidth(); #Brinda el ancho de la pantalla actual, a fin de calcular proporciones

    return int((Ancho * X)/100);

def proporcionLargo(X, Ventana):

    Largo = Ventana.winfo_screenheight(); #Brinda el largo de la pantalla actual, a fin de calcular proporciones

    return int((Largo * X)/100);

def habilitar_espacios(ventana, boton): #2° Screen

    global entrada1, entrada2, boton2

    Main = tk.Frame(ventana, background= "#19191a");
    Main.pack(expand=True);

    boton.destroy(); #Eliminar el boton previo

    entrada1 = tk.Entry(Main, font = "helvetica", foreground="gray") #Agregar un place holder con focus in y focus out con la ayuda de dos funciones
    entrada1.insert(0, "Ancho: ")
    entrada1.bind("<FocusIn>", lambda event: Entrada(event, entrada1))
    entrada1.bind("<FocusOut>", lambda event: Salida(event, entrada1, 0))
    entrada1.pack(pady=(0, proporcionLargo(2, ventana))) 
    
    entrada2 = tk.Entry(Main, font = "Helvetica", foreground="gray")
    entrada2.insert(0, "Largo: ")
    entrada2.bind("<FocusIn>", lambda event : Entrada(event, entrada2,))
    entrada2.bind("<FocusOut>", lambda event : Salida(event, entrada2, 1))
    entrada2.pack(pady=(0, proporcionLargo(2, ventana))) 

    boton2 = tk.Button(

        Main, #Pertenencia
        text="Generar Laberinto", #Texto 
        background="#373739", #Fondo
        foreground="white", # Color de la letra
        state=tk.DISABLED,
        font=("Helvetica", 12, "bold"),
        width = proporcionAncho(1.95, ventana), #Obtener Proporciones
        height = proporcionLargo(0.3, ventana), #Obtener Proporciones
        border = 0,
        cursor = "hand2",
        command= lambda : guardar_variables(ventana)
        
    )

    boton2.pack()

    def verificar_contenido(event=None): #En cualquier evento
        if entrada1.get() != "Ancho: " and entrada2.get() != "Largo: ":
            boton2.config(state=tk.NORMAL)  # Habilitar el segundo botón
        else:
            boton2.config(state=tk.DISABLED)  # Deshabilitar el segundo botón

    entrada1.bind("<KeyRelease>", verificar_contenido)
    entrada2.bind("<KeyRelease>", verificar_contenido)

def Entrada(event, Entry):

    if Entry.get() == "Ancho: " or Entry.get() == 'Largo: ':
        
        Entry.delete(0, 'end')
        Entry.config(foreground="black") 

def Salida(event, Entry, ID):

    if Entry.get() == "":

        if(ID == 0):
            Entry.insert(0, "Ancho: ")
        
        elif(ID == 1):
            Entry.insert(0, "Largo: ")

        Entry.config(foreground="gray") 

def guardar_variables(ventana): #3°Screen,
    global entrada1, entrada2

    N = int(entrada1.get())
    M = int(entrada2.get())

    Resultados = Laberinto.generarMatriz(N, M)
    # Eliminar todos los widgets en la ventana actual
    for widget in ventana.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(ventana, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True) # Hacer que el canvas se ajuste al tamaño de la ventana

    dibujar_cuadrados(ventana, Resultados, canvas)

    # Crear un nuevo botón "Cambiar"
    boton_cambiar = tk.Button(ventana, text="Cambiar",  command=lambda: recrear_elementos(ventana))
    boton_cambiar.pack()

def recrear_elementos(ventana):

    # Llamamos a la función habilitar_espacios para recrear los elementos
    for widget in ventana.winfo_children():
        widget.destroy() 

    Inicio(ventana)         
        
def dibujar_cuadrados(ventana, matriz, canvas):

    filas = len(matriz)
    columnas = len(matriz[0])

    ventana.update_idletasks() # Permite que la ventana se cargue completamente
    ancho_canvas = canvas.winfo_width()
    alto_canvas = canvas.winfo_height()

    ancho_cuadrado = ancho_canvas / columnas
    alto_cuadrado = alto_canvas / filas

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

ventana = tk.Tk()
Inicio(ventana);
