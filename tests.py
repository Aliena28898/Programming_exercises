def esCuadrada(matriz):
    return len(matriz) == len(matriz[0])

def esVacia(matriz):
    return matriz == []

def esAntisimetrica(matriz):
    if not esVacia(matriz):
        if esCuadrada(matriz):
            fila = 0

            while fila < len(matriz):
                columna = 0
                while columna < len(matriz[fila]):
                    if matriz[fila][columna] != -matriz[columna][fila]:
                        return False

                    else:
                        pass

                    columna += 1


                fila +=1

            return True

        else:
            return False

    else:
        return False

print(esAntisimetrica([ [ 0, 1, 2 ],
                      [ -1, 0, 3 ],
                      [ -2, -3, 0 ] ]))

print(esAntisimetrica([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])==True)

print(esAntisimetrica([[0, 1, 2],
                     [-1, 0, -2],
                     [2, 2,  3]]) == False)
#>>> False

print(esAntisimetrica([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]) == False)
#>>> False

# casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert)

matriz4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print(esAntisimetrica(matriz4) == False)
#>>>False

matriz5 = [[1,0,0,0,0,0,0,0,0]]

print(esAntisimetrica(matriz5)== False)
#>>>False

#caso test de matriz vacía
print(esAntisimetrica([]) == False)







