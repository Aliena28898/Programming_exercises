def esCuadrada(matriz):
    return len(matriz) == len(matriz[0])

def esVacia(matriz):
    return matriz == []

def enteros(matriz):
    for fila in matriz:
        for numero in fila:
            if (numero * 10) % 10 == 0:
                pass
            else:
                return False
    return True

def numeros_en_rango(matriz):
    for fila in matriz:
        for numero in fila:
            if numero in range (1, len(matriz)):
                pass
            else:
                return False
    return True

def check_filas(matriz):
    for fila in matriz:
        apariciones = [ ]
        for i in range(0, len(fila) - 1):
            apariciones.append(0)

        for numero in fila:
            apariciones[ numero - 1 ] = + 1

        for posicion in apariciones:
            if posicion == 1:
                pass
            else:
                return False

    return True

def check_columnas(matriz):
    for columna in range (0, len(matriz)-1):
        apariciones = [ ]
        for i in range(0, len(fila) - 1):
            apariciones.append(0)

        for fila in matriz:
            numero = fila[columna]
            apariciones[ numero - 1 ] = + 1

        for posicion in apariciones:
            if posicion == 1:
                pass
            else:
                return False
    return True


def check_sudoku(matriz):
    if not esVacia(matriz):
        return esCuadrada(matriz) and enteros(matriz) and numeros_en_rango(matriz) and check_filas(matriz) and check_columnas(matriz)

    else:
        return False

correcto = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]

incorrecto = [[1, 2, 3],
              [2, 3, 1],
              [2, 3, 1]]

incorrecto1 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 2, 3],
               [4, 4, 4, 4]]

incorrecto2 = [[1, 2, 3, 4],
               [2, 3, 1, 4],
               [4, 1, 2, 3],
               [3, 4, 1, 2]]

incorrecto3 = [[1, 2, 3, 4, 5],
               [2, 3, 1, 5, 6],
               [4, 5, 2, 1, 3],
               [3, 4, 5, 2, 1],
               [5, 6, 4, 3, 2]]

incorrecto4 = [['a', 'b', 'c'],
               ['b', 'c', 'a'],
               ['c', 'a', 'b']]

incorrecto5 = [[1, 1.5],
               [1.5, 1]]

incorrecto6 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]


print(check_sudoku(correcto))
# >>> True

print(check_sudoku(incorrecto))
# >>> False

print(check_sudoku(incorrecto1))
# >>> False

print(check_sudoku(incorrecto2))
# >>> False

print(check_sudoku(incorrecto3))
# >>> False

print(check_sudoku(incorrecto4))
# >>> False

print(check_sudoku(incorrecto5))
# >>> False

print(check_sudoku(incorrecto6))
# >>> False





