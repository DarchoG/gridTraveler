import tkinter as tk
from tkinter import messagebox
import random

class Laberinto:
    def __init__(self, num_filas, num_columnas):
        self.num_filas = num_filas
        self.num_columnas = num_columnas
        self.lab = self.generar_laberinto()
        self.pos_jugador = (0, 0)
        self.pos_salida = (num_filas - 1, num_columnas - 1)

    def generar_laberinto(self): #Generacion de la matriz del laberinto
        lab = [[1] * self.num_columnas for _ in range(self.num_filas)]
        pila = [(0, 0)]

        while pila:
            actual = pila[-1]
            lab[actual[0]][actual[1]] = 0
            vecinos = []

            for df, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                f, c = actual[0] + df, actual[1] + dc
                if 0 <= f < self.num_filas and 0 <= c < self.num_columnas and lab[f][c] == 1:
                    cuenta = sum(1 for df2, dc2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]
                                 if 0 <= f + df2 < self.num_filas and 0 <= c + dc2 < self.num_columnas and lab[f + df2][c + dc2] == 0)
                    if cuenta == 1:
                        vecinos.append((f, c))

            if vecinos:
                siguiente_celda = random.choice(vecinos)
                pila.append(siguiente_celda)
            else:
                pila.pop()

        lab[0][0] = 0  # Punto de inicio
        lab[self.num_filas - 1][self.num_columnas - 1] = 2  # Punto de salida

        return lab

    def mover_jugador(self, direccion):   #JUGABILIDAD   
        fila, columna = self.pos_jugador
        if direccion == "w" and fila > 0 and self.lab[fila - 1][columna] != 1:
            self.pos_jugador = fila - 1, columna
        elif direccion == "s" and fila < self.num_filas - 1 and self.lab[fila + 1][columna] != 1:
            self.pos_jugador = fila + 1, columna
        elif direccion == "a" and columna > 0 and self.lab[fila][columna - 1] != 1:
            self.pos_jugador = fila, columna - 1
        elif direccion == "d" and columna < self.num_columnas - 1 and self.lab[fila][columna + 1] != 1:
            self.pos_jugador = fila, columna + 1

    def verificar_estado_juego(self):  
        if self.pos_jugador == self.pos_salida:
            messagebox.showinfo("FEKICIDADES!!!", "Has encontrado la salida :D")
            root.destroy()

    def dibujar_laberinto(self, lienzo):
        ancho_celda = 20
        alto_celda = 20
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                x1, y1 = j * ancho_celda, i * alto_celda
                x2, y2 = x1 + ancho_celda, y1 + alto_celda
                if self.lab[i][j] == 1:  # Pared
                    lienzo.create_rectangle(x1, y1, x2, y2, fill="black")
                elif self.pos_jugador == (i, j):  # Jugador
                    lienzo.create_rectangle(x1, y1, x2, y2, fill="red")
                elif self.pos_salida == (i, j):  # Salida
                    lienzo.create_rectangle(x1, y1, x2, y2, fill="cyan")
                else:  # Camino
                    lienzo.create_rectangle(x1, y1, x2, y2, fill="white")

def comenzar_juego():
    num_filas = int(entrada_filas.get())
    num_columnas = int(entrada_columnas.get())

    if num_filas < 6 or num_columnas < 6:
        messagebox.showwarning("ADVERTENCIA", "El tamaño minimo del laberinto es de 6x6.")
        return

    juego = Laberinto(num_filas, num_columnas)

    ventana_juego = tk.Toplevel(root)
    ventana_juego.title("Laberinto")

    lienzo = tk.Canvas(ventana_juego, width=num_columnas * 20, height=num_filas * 20)
    lienzo.pack()

    juego.dibujar_laberinto(lienzo)

    def mover(evento):
        direccion = evento.char
        juego.mover_jugador(direccion)
        juego.verificar_estado_juego()
        lienzo.delete("all")
        juego.dibujar_laberinto(lienzo)

    ventana_juego.bind("<KeyPress>", mover)



#INTERFAZ GRAFICA
root = tk.Tk()
root.title("Configuracion del laberinto")

etiqueta_filas = tk.Label(root, text="Numero de filas:")
etiqueta_filas.grid(row=0, column=0)
entrada_filas = tk.Entry(root)
entrada_filas.grid(row=0, column=1)

etiqueta_columnas = tk.Label(root, text="Numero de columnas:")
etiqueta_columnas.grid(row=1, column=0)
entrada_columnas = tk.Entry(root)
entrada_columnas.grid(row=1, column=1)

boton_inicio = tk.Button(root, text="Comenzar juego", command=comenzar_juego)
boton_inicio.grid(row=2, columnspan=2)

root.mainloop()