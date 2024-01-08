from PIL import Image
import pytesseract
import os
# Ruta a la instalación de Tesseract en tu sistema
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'

def image_to_text(image_path):
    # Abrir la imagen desde el archivo
    img = Image.open(image_path)

    # Hacer el reconocimiento de texto utilizando pytesseract
    text = pytesseract.image_to_string(img)

    # Imprimir el texto reconocido
    print("Texto reconocido:")
    print(text)

script_dir = os.path.dirname(os.path.realpath(__file__))

image_filename = 'imagenTexto.jpg'

image_path = os.path.join(script_dir, image_filename)

image_to_text(image_path)