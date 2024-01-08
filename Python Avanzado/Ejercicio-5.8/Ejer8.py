import os
import shutil

def organizar_archivos(lista_extensiones):
    # Crear carpetas para cada extensión
    for extension in lista_extensiones:
        carpeta_destino = extension.lower()
        os.makedirs(carpeta_destino, exist_ok=True)

    # Mover archivos a las carpetas correspondientes
    for archivo in os.listdir():
        if os.path.isfile(archivo):
            nombre, extension = os.path.splitext(archivo)
            # Eliminamos el punto y convertimos a minúsculas
            extension = extension[1:].lower()  
            if extension in lista_extensiones:
                carpeta_destino = extension
                shutil.move(archivo, os.path.join(carpeta_destino, archivo))

if __name__ == "__main__":
    # Lista de extensiones que quieres organizar
    lista_extensiones = ["png", "mp4", "doc"]

    # Llamar a la función para organizar los archivos
    organizar_archivos(lista_extensiones)