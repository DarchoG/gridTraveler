import tkinter as tk
from tkinter import messagebox
import random
from collections import deque
import time

class Laberinto:
    def __init__(self, num_filas, num_columnas):
        self.num_filas = num_filas
        self.num_columnas = num_columnas
        self.lab = self.generar_laberinto()
        self.pos_jugador = (0, 0)
        self.pos_salida = (num_filas - 1, num_columnas - 1)
        self.pos_teletransporte = self.generar_teletransporte()
        self.pos_pregunta = self.generar_pregunta()

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
    
    def generar_teletransporte(self):
        while True:
            fila = random.randint(0, self.num_filas - 1)
            columna = random.randint(0, self.num_columnas - 1)
            if (fila, columna) != (0, 0) and (fila, columna) != self.pos_salida:
                return fila, columna
    
    def generar_pregunta(self):
        while True:
            fila = random.randint(0, self.num_filas - 1)
            columna = random.randint(0, self.num_columnas - 1)
            if (fila, columna) != (0, 0) and (fila, columna) != self.pos_salida and (fila, columna) != self.pos_teletransporte:
                return fila, columna
            
    def mostrar_pregunta(self):
        self.ventana_pregunta = tk.Toplevel()
        self.ventana_pregunta.title("Pregunta ¿?")
        pregunta_label = tk.Label(self.ventana_pregunta, text=" ¿Quien es mas humilde? \n ¿El Bicho o Messi?")
        pregunta_label.pack()

        def respuesta_si():
            messagebox.showinfo("Nada se compara al bicho :)", "¡SIIIIIIUUU! Puedes continuar:D")
            self.ventana_pregunta.destroy()

        def respuesta_no():
            messagebox.showinfo("Pista: Es la persona mas humilde del mundo", "Incorrecto :( Vuelve a intentarlo.")
            self.ventana_pregunta.lift()

        boton_si = tk.Button(self.ventana_pregunta, text="El bicho ", command=respuesta_si)
        boton_si.pack()

        boton_no = tk.Button(self.ventana_pregunta, text="Messi", command=respuesta_no)
        boton_no.pack()
    
    def mejor_ruta(self):
        # Algoritmo de búsqueda en anchura (BFS)
        visitado = set()
        cola = deque([(0, 0, [])])  # (fila, columna, ruta)
        
        while cola:
            fila, columna, ruta = cola.popleft()
            
            if (fila, columna) == self.pos_salida:
                return ruta
            
            if (fila, columna) not in visitado:
                visitado.add((fila, columna))
                
                for df, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nf, nc = fila + df, columna + dc
                    if 0 <= nf < self.num_filas and 0 <= nc < self.num_columnas and self.lab[nf][nc] != 1:
                        cola.append((nf, nc, ruta + [(nf, nc)]))


    def dibujar_laberinto(self, lienzo, mejor_ruta=None):
        ancho_celda = 20
        alto_celda = 20
        for i in range(self.num_filas):
            for j in range(self.num_columnas):
                x1, y1 = j * ancho_celda, i * alto_celda
                x2, y2 = x1 + ancho_celda, y1 + alto_celda
                if self.lab[i][j] == 1:  # Pared
                    lienzo.create_rectangle(x1, y1, x2, y2, fill="black")
                elif (i, j) in mejor_ruta and (i, j) not in [self.pos_jugador, self.pos_teletransporte, self.pos_pregunta,self.pos_salida]: # Mejor ruta (naranja)
                    lienzo.create_rectangle(x1, y1, x2, y2, fill="orange")
                elif self.pos_jugador == (i, j):  # Jugador
                    lienzo.create_rectangle(x1, y1, x2, y2, fill="red")
                elif self.pos_salida == (i, j):  # Salida
                    lienzo.create_rectangle(x1, y1, x2, y2, fill="cyan")
                elif self.pos_teletransporte == (i, j):  # Teletransporte
                    lienzo.create_rectangle(x1, y1, x2, y2, fill="yellow")
                elif self.pos_pregunta == (i, j):  # Pregunta
                    lienzo.create_rectangle(x1, y1, x2, y2, fill="green")
                else:  # Camino
                    lienzo.create_rectangle(x1, y1, x2, y2, fill="white")

    def mover_jugador_auto(self, lienzo, mejor_ruta):
        for i, (fila, columna) in enumerate(mejor_ruta):
        # Mover el jugador
            self.pos_jugador = (fila, columna)

        # Verificar si el jugador está en la posición de teletransporte
        if self.pos_jugador == self.pos_teletransporte:
            # Si el jugador está en la posición de teletransporte, elige una casilla aleatoria de la mejor ruta
            # Evitando la posición actual del jugador
            nuevas_posiciones = [pos for pos in mejor_ruta if pos != self.pos_jugador]
            nueva_posicion = random.choice(nuevas_posiciones)
            self.pos_jugador = nueva_posicion

        # Dibujar el laberinto con la nueva posición del jugador
        self.dibujar_laberinto(lienzo, mejor_ruta)

        # Mostrar la pregunta si el jugador está en la posición de pregunta
        if self.pos_jugador == self.pos_pregunta:
            self.mostrar_pregunta()
            while self.pos_jugador == self.pos_pregunta:
                time.sleep(1)
                
        # Esperar 1 segundo entre movimientos
        time.sleep(0.3)
