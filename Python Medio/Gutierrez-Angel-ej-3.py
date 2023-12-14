#3. Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!., siendo <nombre> tu nombre obtenido del teclado.
Nombre = input("Pon un Nombre: ")
def saludo(nombre):
    return("¡Hola {}!.".format(nombre))
print(saludo(Nombre))