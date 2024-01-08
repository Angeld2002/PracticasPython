import csv
from barcode import EAN13
from barcode.writer import ImageWriter

def generar_codigo_barras(id_alumno, nombre_alumno):
    id_alumno_completo = id_alumno.zfill(12)  # Completa con ceros a la izquierda
    codigo = EAN13(id_alumno_completo, writer=ImageWriter())
    nombre_archivo = f"{nombre_alumno}"
    codigo.save(nombre_archivo)

def generar_codigos_barras_desde_csv(archivo_csv):
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        lector_csv = csv.reader(csvfile)

        for fila in lector_csv:
            nombre_alumno, id_alumno = fila
            generar_codigo_barras(id_alumno, nombre_alumno)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso: python programa.py <archivo_csv>")
        sys.exit(1)

    archivo_csv = sys.argv[1]
    generar_codigos_barras_desde_csv(archivo_csv)
