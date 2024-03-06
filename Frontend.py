import random

def imprimirArreglo(Contenido):

    for i in range(len(Contenido) - 1, -1, -1):
        
        for j in range(len(Contenido[i]) -1, -1, -1):

            print(Contenido[i][j], end = " ");

        print("");

def generarSalida(N,M): #Cambiar unicamente uno de los dos parametros de borde, a fin de que la salida este en un borde.

    Random = random.randint(1, 2);

    if(Random == 1):

        Temporal = random.randint(1, N);
        N -= Temporal;

    else:

        Temporal = random.randint(1,M);
        M -= Temporal;

    return [N, M];
    
def generarCamino(N,M): #Generar un camino valido, para posteriormente incorporar las paredes y garantizar al menos una solución.

    N -=1;
    M -=1;

    X = N;
    Y = M;
    Destino = generarSalida(N,M);  
    Camino = [[N,M]];
    Control = True;

    while(Control):

        Direccion = random.randint(1, 4); #Tengo 4 posiciones para moverme.

        if(Direccion == 1):
            X +=1;
        elif(Direccion == 2):
            Y +=1;
        elif(Direccion == 3):
            X -=1;
        elif(Direccion == 4):
            Y -=1;

        if(0 > X): #Evitar que se salga de los bordes, es necesario actualizar el valor.
            X += 1;
            continue;
        elif(0 > Y):
            Y += 1;
            continue;
        
        if(X > N):            
            X -= 1;
            continue;
        
        elif(Y > M):
            Y -= 1;
            continue;
        
        Auxiliar = [X,Y];

        if(not(Auxiliar in Camino)): #Evitar elementos repetidos;

            Camino.append(Auxiliar);
        
        if(Auxiliar == Destino): #Detener bucle;
            Control = False;
            continue;

    return Camino;

def generarMatriz(N,M):

    Laberinto = [];

    for i in range(N):

        Fila = [];

        for j in range(M):
            
            Fila.append(-1);

        Laberinto.append(Fila);

    Temporal = generarCamino(N,M);

    for i in (Temporal):

        j = i[0];
        k = i[1];
    
        Laberinto[j][k] = 0;

    Auxiliar =  Temporal[len(Temporal) - 1];
    X = Auxiliar[0];
    Y = Auxiliar[1];

    Laberinto[X][Y] = 2

    return Laberinto; 
