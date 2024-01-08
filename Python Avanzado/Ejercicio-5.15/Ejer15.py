import pyperclip

def cargar_palabras_prohibidas(archivo):
    with open(archivo, 'r') as file:
        return [line.strip().lower() for line in file]

def sustituir_palabras_prohibidas(texto, palabras_prohibidas):
    for palabra in palabras_prohibidas:
        texto = texto.replace(palabra, '*' * len(palabra))
    return texto

def main():
    archivo_prohibidas = "lista.txt"
    palabras_prohibidas = cargar_palabras_prohibidas(archivo_prohibidas)

    while True:
        input("Copia algo al portapapeles y presiona Enter...")
        texto_original = pyperclip.paste()
        texto_modificado = sustituir_palabras_prohibidas(texto_original.lower(), palabras_prohibidas)
        
        # Copiar el texto modificado de vuelta al portapapeles
        pyperclip.copy(texto_modificado)

        print(f"Texto original: {texto_original}")
        print(f"Texto modificado: {texto_modificado}")
        print("¡Texto modificado copiado al portapapeles!\n")

if __name__ == "__main__":
    main()
