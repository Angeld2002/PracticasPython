def contandoMinas(miCampo):
    filas = len(miCampo)
    columnas = len(miCampo[0])
    
    # Crear un nuevo campo para almacenar la cantidad de minas adyacentes
    resultado = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            # Si la casilla actual no tiene una mina cerca el resultado es 0
            if miCampo[i][j] != -1:
                # Iterar sobre las casillas adyacentes
                for x in range(max(0, i - 1), min(filas, i + 2)):
                    for y in range(max(0, j - 1), min(columnas, j + 2)):
                        # Incrementar el contador sumando 1 si la casilla cercana es una mina si no sumamos 0
                        resultado[i][j] += 1 if miCampo[x][y] == -1 else 0

    return resultado

# Leer el campo escrito por teclado
miCampo = []
print("Ingrese el campo de Buscaminas. Use 0 para casillas vacías y -1 para minas.")
while True:
    fila = input("Ingrese una fila (o 'fin' para finalizar): ")
    if fila.lower() == 'fin':
        break
    miCampo.append(list(map(int, fila.split())))

# Llamar a la función y mostrar el resultado
resultado = contandoMinas(miCampo)
for i in range(len(miCampo)):
    for j in range(len(miCampo[0])):
        # Marcar las posiciones con minas como -1
        if miCampo[i][j] == -1:
            resultado[i][j] = -1

print("Resultado:")
for fila in resultado:
    print(" ".join(map(str, fila)))
