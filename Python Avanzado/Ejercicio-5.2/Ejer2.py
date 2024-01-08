def leerArchivoConstruirMatriz(nombre_archivo):
    matriz = []
    
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            numeros = [int(numero) for numero in linea.strip().split()]
            matriz.append(numeros)
    return matriz

def esSudokuCorrecto(sudokuMatriz):
    for numInFila, fila in enumerate(sudokuMatriz):
        for columnaIndex, valor in enumerate(fila):
            # Verificar en la misma fila contando ese numero si sale mas de 1 vez da Falso
            if fila.count(valor) > 1:
                return False

            # Verificar en la misma Columna contando ese numero si sale mas de 1 vez da Falso
            for i in range(len(sudokuMatriz)):
                if i != numInFila and sudokuMatriz[i][columnaIndex] == valor:
                    return False
    return True

            

def main():
    nombreArchivo = "Sudoku.in"
    sudoku = leerArchivoConstruirMatriz(nombreArchivo)

    if sudoku:
        resultado = esSudokuCorrecto(sudoku)

        if resultado:
            print("Correcto")
        else:
            print("Incorrecto")


if __name__ == "__main__":
    main()