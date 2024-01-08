import cv2
from pyzbar.pyzbar import decode

def leer_codigo_barras(imagen):
    codigo_barras = decode(imagen)
    if codigo_barras:
        codigo = codigo_barras[0].data.decode('utf-8')
        # Eliminar ceros a la izquierda y un número de la derecha
        codigo = str(int(codigo))
        codigo = codigo [:-1]
        return codigo
    return None

def obtener_info_desde_imagen(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)
    id_alumno = leer_codigo_barras(imagen)
    if id_alumno:
        return id_alumno
    return None

def obtener_info_desde_directorio(directorio):
    import os

    info_alumnos = []

    for archivo in os.listdir(directorio):
        if archivo.endswith(".png"):
            nombre_alumno = os.path.splitext(archivo)[0]
            ruta_imagen = os.path.join(directorio, archivo)
            id_alumno = obtener_info_desde_imagen(ruta_imagen)
            if id_alumno:
                info_alumnos.append([nombre_alumno, id_alumno])

    return info_alumnos

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso: python programa.py <directorio>")
        sys.exit(1)

    directorio = sys.argv[1]
    info_alumnos = obtener_info_desde_directorio(directorio)

    if not info_alumnos:
        print("No se encontraron archivos PNG en el directorio.")
    else:
        print("Información de los alumnos:")
        for nombre, id_alumno in info_alumnos:
            print(f"Nombre: {nombre}, ID: {id_alumno}")
