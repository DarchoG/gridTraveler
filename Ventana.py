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

    Resultados = Laberinto.generarMatriz(N,M);
    Laberinto.imprimirArreglo(Resultados);

# Crear la ventana
ventana = tk.Tk()
ventana.title("Laberinto")

# Crear el botón
boton = tk.Button(ventana, text="Habilitar Espacios", command=habilitar_espacios)
boton.pack()

ventana.mainloop()
