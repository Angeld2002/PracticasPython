def numeroPatrones(texto):
    # Inicializamos el contador de los patrones
    contadorPatron = 0

    # Hacemos una lista de los patrones a buscar
    patrones = ["00", "101", "ABC", "HO"]

    # Iteramos sobre cada patrón con un for
    for patron in patrones:
        # Convertimos tanto el texto como el patrón a minúsculas para hacer la búsqueda sin distinguir mayúsculas y minúsculas
        cadenaTexto = texto.lower()
        cadenaPatron = patron.lower()

        # Inicializamos el índice en 0
        inicio = 0

        # While para buscar en el texto
        while inicio < len(cadenaTexto):
            # Encontramos la próxima ocurrencia del patrón
            indiceOcurrencia = cadenaTexto.find(cadenaPatron, inicio)

            # Si no se encuentra ninguna otra ocurrencia, salimos del bucle
            if indiceOcurrencia == -1:
                break

            # Incrementamos el contador de patrones si se encuentra
            contadorPatron += 1

            # Actualizamos el índice de inicio 
            inicio = indiceOcurrencia + 1

    # Devolvemos el contador total de patrones
    return contadorPatron

# Solicitamos la cadena de texto al usuario
texto_usuario = input("Ingrese una cadena de texto: ")

# Llamamos a la función numeroPatrones y mostramos el resultado total
total_patrones = numeroPatrones(texto_usuario)
print(f'\nEn total, hay {total_patrones} patrones opuestos en el texto.')
