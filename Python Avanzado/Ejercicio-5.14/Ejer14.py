def es_seguro(tablero, fila, columna):
    # Verificar si hay una reina en la misma columna
    for i in range(fila):
        if tablero[i] == columna or \
           tablero[i] - i == columna - fila or \
           tablero[i] + i == columna + fila:
            return False
    return True

def colocar_reinas_util(tablero, fila, n, soluciones):
    if fila == n:
        # Se ha alcanzado una solución completa
        soluciones.append(tablero[:])
        return

    for columna in range(n):
        if es_seguro(tablero, fila, columna):
            tablero[fila] = columna
            colocar_reinas_util(tablero, fila + 1, n, soluciones)

def calcular_soluciones_totales(n):
    tablero = [0] * n
    soluciones = []
    colocar_reinas_util(tablero, 0, n, soluciones)
    return len(soluciones)

if __name__ == "__main__":
    # Probar para diferentes valores de N
    for N in range(4, 13):
        soluciones_totales = calcular_soluciones_totales(N)
        print(f"Tamaño N: {N}, Soluciones totales: {soluciones_totales}")
