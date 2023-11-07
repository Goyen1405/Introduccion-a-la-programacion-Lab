
# Inicialización del tablero de juego
TamañoTablero = 10
TableroJ1 = [['~' for _ in range(TamañoTablero)] for _ in range(TamañoTablero)]
TableroJ2 = [['~' for _ in range(TamañoTablero)] for _ in range(TamañoTablero)]
TableroJ1VAC = [['~' for _ in range(TamañoTablero)] for _ in range(TamañoTablero)]
TableroJ2VAC = [['~' for _ in range(TamañoTablero)] for _ in range(TamañoTablero)]

fila_a_Numero = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}


# Función para colocar barcos en el tablero
def PosicionarBarcoJ1(TableroJ1, tam, NombreBarco, salir):
        while salir == False:
            try:
                posicion = input(f"Introduce la posición inicial del {NombreBarco} (por ejemplo, A2): ")
                orientacion = input(f"Introduce la dirección del {NombreBarco} (H para horizontal, V para vertical): ").upper()
                fila = fila_a_Numero[posicion[0]]
                columna = int(posicion[1]) - 1
                if orientacion == 'H':
                    if columna + tam <= TamañoTablero:
                        for i in range(columna, columna + tam):
                            if TableroJ1[fila][i] == '~':
                                TableroJ1[fila][i] = "B"
                                salir = True
                            else:
                                raise ValueError
                    else:
                        raise ValueError
                elif orientacion == 'V':
                    if fila + tam <= TamañoTablero:
                        for i in range(fila, fila + tam):
                            if TableroJ1[i][columna] == '~':
                                TableroJ1[i][columna] = "B"
                                salir = True
                            else:
                                raise ValueError
                    else:
                        raise ValueError
                else:
                    raise ValueError
            except (ValueError, IndexError):
                print("Posición inválida. Inténtalo de nuevo.")


# Función para colocar barcos en el tablero
def PosicionarBarcoJ2(TableroJ2, tam, NombreBarco, salir):
        while salir == False:
            try:
                posicion = input(f"Introduce la posición inicial del {NombreBarco} (por ejemplo, A2): ")
                orientacion = input(f"Introduce la dirección del {NombreBarco} (H para horizontal, V para vertical): ").upper()
                fila = fila_a_Numero[posicion[0]]
                columna = int(posicion[1]) - 1
                if orientacion == 'H':
                    if columna + tam <= TamañoTablero:
                        for i in range(columna, columna + tam):
                            if TableroJ2[fila][i] == '~':
                                TableroJ2[fila][i] = "B"
                                salir = True
                            else:
                                raise ValueError
                    else:
                        raise ValueError
                elif orientacion == 'V':
                    if fila + tam <= TamañoTablero:
                        for i in range(fila, fila + tam):
                            if TableroJ2[i][columna] == '~':
                                TableroJ2[i][columna] = "B"
                                salir = True
                            else:
                                raise ValueError
                    else:
                        raise ValueError
                else:
                    raise ValueError
            except (ValueError, IndexError):
                print("Posición inválida. Inténtalo de nuevo.")


# Colocar barcos para ambos jugadores
print("Jugador 1, coloca tus barcos:")
salir1=False
salir2=False
salir3=False
salir4=False
salir5=False
PosicionarBarcoJ1(TableroJ1, 3, 'Barco pequeño 1', salir1)
PosicionarBarcoJ1(TableroJ1, 3, 'Barco pequeño 2', salir2)
PosicionarBarcoJ1(TableroJ1, 3, 'Barco pequeño 3', salir3)
PosicionarBarcoJ1(TableroJ1, 5, 'Barco grande 1', salir4)
PosicionarBarcoJ1(TableroJ1, 5, 'Barco grande 2', salir5)

salir1=False
salir2=False
salir3=False
salir4=False
salir5=False
print("Jugador 2, coloca tus barcos:")
PosicionarBarcoJ2(TableroJ2, 3, 'Barco pequeño 1', salir1)
PosicionarBarcoJ2(TableroJ2, 3, 'Barco pequeño 2', salir2)
PosicionarBarcoJ2(TableroJ2, 3, 'Barco pequeño 3', salir3)
PosicionarBarcoJ2(TableroJ2, 5, 'Barco grande 1', salir4)
PosicionarBarcoJ2(TableroJ2, 5, 'Barco grande 2', salir5)


# Función para imprimir el tablero de un jugador
def ImprimirTableroJ1(TableroJ1):
    print("  1 2 3 4 5 6 7 8 9 10")
    for i in range(TamañoTablero):
        print(chr(65 + i), end=' ')
        for j in range(TamañoTablero):
            print(TableroJ1[i][j], end=' ')
        print()


# Función para imprimir el tablero de un jugador
def ImprimirTableroJ2(TableroJ2):
    print("  1 2 3 4 5 6 7 8 9 10")
    for i in range(TamañoTablero):
        print(chr(65 + i), end=' ')
        for j in range(TamañoTablero):
            print(TableroJ2[i][j], end=' ')
        print()

# Función para imprimir el tablero de un jugador
def ImprimirTableroJ1VAC(TableroJ1VAC):
    print("  1 2 3 4 5 6 7 8 9 10")
    for i in range(TamañoTablero):
        print(chr(65 + i), end=' ')
        for j in range(TamañoTablero):
            print(TableroJ1VAC[i][j], end=' ')
        print()

# Función para imprimir el tablero de un jugador
def ImprimirTableroJ2VAC(TableroJ2VAC):
    print("  1 2 3 4 5 6 7 8 9 10")
    for i in range(TamañoTablero):
        print(chr(65 + i), end=' ')
        for j in range(TamañoTablero):
            print(TableroJ2VAC[i][j], end=' ')
        print()

def ImpactoJugador2(TableroJ2,TableroJ2VAC, fila, columna):
    if TableroJ2[fila][columna] == '~':
        print("¡Agua!")
        TableroJ2[fila][columna] = 'O'
        TableroJ2VAC[fila][columna] = 'O'
        return False
    elif TableroJ2[fila][columna] == 'X' or TableroJ2[fila][columna] == 'O':
        print("Ya has disparado en esa casilla.")
        return False
    else:
        print("¡Impacto!")
        TableroJ2VAC[fila][columna] = 'X'
        TableroJ2[fila][columna] = 'X'
        print(" Le haz dado a un barco .")
        return True

def ImpactoJugador1(TableroJ1,TableroJ1VAC, fila, columna):
    if TableroJ1[fila][columna] == '~':
        print("¡Agua!")
        TableroJ1[fila][columna] = 'O'
        TableroJ1VAC[fila][columna] = 'O'
        return False
    elif TableroJ1[fila][columna] == 'X' or TableroJ1[fila][columna] == 'O':
        print("Ya has disparado en esa casilla.")
        return False
    else:
        print("¡Impacto!")
        TableroJ1VAC[fila][columna] = 'X'
        TableroJ1[fila][columna] = 'X'
        print(" Le haz dado a un barco .")
        return True

BarcorUndidosJ1 = 0
BarcorUndidosJ2 = 0

# Función para determinar si un jugador ha ganado
def validarGanadorJ1(TableroJ2):
    for fila in TableroJ2:
        for celda in fila:
            if celda == 'B':
                return False  # Se encontró al menos una 'B', el jugador 1 no ha ganado
    return True  # No se encontraron 'B' en ninguna celda, el jugador 1 ha ganado


def validarGanadorJ2(TableroJ1):
    for fila in TableroJ1:
        for celda in fila:
            if celda == 'B':
                return False  # Se encontró al menos una 'B', el jugador 1 no ha ganado
    return True  # No se encontraron 'B' en ninguna celda, el jugador 1 ha ganado


TurnoJugador = 1

contadorbarcos1 = 0;
barcos1 = 0;

contadorbarcos2 = 0;
barcos2 = 0;

while True:
    if TurnoJugador == 1:
        print("\nTurno del Jugador 1")
        ImprimirTableroJ2VAC(TableroJ2VAC)
        posicion = input("Selecciona una casilla para disparar (por ejemplo, A2): ")
        fila = fila_a_Numero[posicion[0]]
        columna = int(posicion[1]) - 1
        resultado = ImpactoJugador2(TableroJ2,TableroJ2VAC, fila, columna)
        if resultado:
            contadorbarcos1 = contadorbarcos1 + 1
            if contadorbarcos1 == 3:
                barcos1 = 1
            if contadorbarcos1 == 6:
                barcos1 = 2
            if contadorbarcos1 == 9:
                barcos1 = 3
            if contadorbarcos1 == 14:
                barcos1 = 4
            if contadorbarcos1 == 19:
                barcos1 = 5
            if validarGanadorJ1(TableroJ2):
                print("¡Jugador 1 ha ganado!")
                break
        print("-----------------------------------------")
        print("- Cantidad de Disparos Acertados: " + str(contadorbarcos1))
        print("- Cantidad de Barcos Destruidos: " + str(barcos1))
        print("-----------------------------------------")
        TurnoJugador = 2
    else:
        print("\nTurno del Jugador 2")
        ImprimirTableroJ1VAC(TableroJ1VAC)
        posicion = input("Selecciona una casilla para disparar (por ejemplo, A2): ")
        fila = fila_a_Numero[posicion[0]]
        columna = int(posicion[1]) - 1
        resultado = ImpactoJugador1(TableroJ1,TableroJ1VAC, fila, columna)

        if resultado:
            contadorbarcos2 = contadorbarcos2 + 1
            if contadorbarcos2 == 3:
                barcos2 = 1
            if contadorbarcos2 == 6:
                barcos2 = 2
            if contadorbarcos2 == 9:
                barcos2 = 3
            if contadorbarcos2 == 14:
                barcos2 = 4
            if contadorbarcos2 == 19:
                barcos2 = 5

            if validarGanadorJ2(TableroJ1):
                print("¡Jugador 2 ha ganado!")
                break

        TurnoJugador = 1
        print("-----------------------------------------")
        print("- Cantidad de Disparos Acertados: " + str(contadorbarcos2))
        print("- Cantidad de Barcos Destruidos: " + str(barcos2))
        print("-----------------------------------------")

print("Fin del juego")