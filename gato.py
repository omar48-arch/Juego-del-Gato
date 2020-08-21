import os
import random


#   Definción de Clases.
class Gato:
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    caracteres = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']] 
    ganador = [False, 0]

    def modificarJugadorMatriz(self, vector):
        x = vector[0]
        y = vector[1]
        self.matriz[x][y] = 1

    def modificarComputadoraMatriz(self):
        x = random.randint(0, 2)
        y = random.randint(0, 2)        
        while self.matriz[x][y] != 0:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
        self.matriz[x][y] = 2

    def modificarCaracteres(self):
        for i in range(3):
            for j in range(3):
                if self.matriz[i][j] == 1:
                    self.caracteres[i][j] = '\u001b[36mX\u001b[37m'
                elif self.matriz[i][j] == 2:
                    self.caracteres[i][j] = '\u001b[32mO\u001b[37m'

    def mostrarEstado(self):
        print('\n' + "{0}".format(' ' * 15) + '1   2   3')
        print('\n' + "{0}".format(' ' * 11) + '1   ' + self.caracteres[0][0] + '   ' + self.caracteres[0][1] + '   ' + self.caracteres[0][2])
        print('\n' + "{0}".format(' ' * 11) + '2   ' + self.caracteres[1][0] + '   ' + self.caracteres[1][1] + '   ' + self.caracteres[1][2])
        print('\n' + "{0}".format(' ' * 11) + '3   ' + self.caracteres[2][0] + '   ' + self.caracteres[2][1] + '   ' + self.caracteres[2][2])

    def comprobarPartida(self):
        for i in range(3):
            if ((self.matriz[i][0] == self.matriz[i][1]) and (self.matriz[i][0] == self.matriz[i][2])) and self.matriz[i][0] != 0:
                self.ganador[0] = True
                self.ganador[1] = self.matriz[i][0]
        for i in range(3):
            if ((self.matriz[0][i] == self.matriz[1][i]) and (self.matriz[0][i] == self.matriz[2][i])) and self.matriz[0][i] != 0:
                self.ganador[0] = True
                self.ganador[1] = self.matriz[0][i]
        if ((self.matriz[0][0] == self.matriz[1][1]) and (self.matriz[0][0] == self.matriz[2][2])) and self.matriz[0][0] != 0:
            self.ganador[0] = True
            self.ganador[1] = self.matriz[0][0]
        if ((self.matriz[0][2] == self.matriz[1][1]) and (self.matriz[1][1] == self.matriz[2][0])) and self.matriz[1][1] != 0:
            self.ganador[0] = True
            self.ganador[1] = self.matriz[1][1]

#   Definición de Funciones.
def codificar_jugada(dato):
    #   Esta función toma un dato con el formato 'numero_uno,numero_dos' y regresa 
    #   un vector [numero_uno,numero_dos] de enteros.
    a = int(dato[0]) - 1
    b = int(dato[2]) - 1
    return [a, b]

def introducir_jugada():
    jugada = input(mensaje_entrada)
    while len(jugada) != 3:
        print(mensaje_error)
        jugada = input(mensaje_entrada)
    while jugada[1] != ',':
        print(mensaje_error)
        jugada = input(mensaje_entrada)
    while (jugada[0].isdigit() != True) or (jugada[len(jugada) - 1].isdigit() != True):
        print(mensaje_error)
        jugada = input(mensaje_entrada)
    jugada_vector = codificar_jugada(jugada)
    return jugada_vector

def revisar_lugares():
    revision = False
    contador = 0
    for i in range(3):
        for j in range(3):
            if partida.matriz[i][j] != 0:
                contador = contador + 1
    if contador == 9:
        revision = True
    return revision


#   Inicio del Programa.
os.system('clear')

mensaje_entrada = '\n    \u001b[33mSelecciona una posición (por ejemplo 2,1): \u001b[37m'
mensaje_error = "\n    \u001b[31mIntroduce dos números separados por una coma.\u001b[37m"
mensaje_posicion = "\n    \u001b[31mEsa posición ya está ocupada. \u001b[37mIntenta de nuevo."
lugares_llenos = False

print("\n              \u001b[36mJUEGO DE GATO\u001b[37m\n")

partida = Gato()
tablas = False

partida.mostrarEstado()

while partida.ganador[0] != True:
    
    jugada_usuario = introducir_jugada()

    while partida.matriz[jugada_usuario[0]][jugada_usuario[1]] != 0:
        print(mensaje_posicion)
        partida.mostrarEstado()
        jugada_usuario = introducir_jugada()

    partida.modificarJugadorMatriz(jugada_usuario)
    partida.modificarCaracteres()
    partida.comprobarPartida()

    if partida.ganador[0] == True:
        break

    lugares_llenos = revisar_lugares()
    if lugares_llenos == True:
        tablas = True
        break

    partida.modificarComputadoraMatriz()
    partida.modificarCaracteres()
    partida.comprobarPartida()
    
    partida.mostrarEstado()
    

if tablas == True:
    partida.mostrarEstado()
    print("\n    \u001b[36mTABLAS.\u001b[37m")

if partida.ganador[1] == 1:
    partida.mostrarEstado()
    print("\n    \u001b[32mHAS GANADO EL JUEGO.\u001b[37m")
elif partida.ganador[1] == 2:
    print("\n    \u001b[31mHAS PERDIDO LA PARTIDA.\u001b[37m")