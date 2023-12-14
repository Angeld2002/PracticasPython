#2. Explica con ejemplos cómo funcionan los operadores "is", "not", "in" en Python 3

ListaNombres = ["Pablo", "Juan","Pepe"]
OtroNombre = ("Pepe")
NombreCopia = OtroNombre
#Estos operadores sirven para buscar Strings o ints mediante por ejemplo usando ifs
Nombre = input("Pon un Nombre: ")
#Este da de salida true si ambos elementos que se van a comparar ocupan el mismo espacio en memoria es decir, es el mismo
if NombreCopia is OtroNombre:
    print("Este Nombre ya me lo sé")
#Este da de salida true si ambos elementos que se van a comparar no ocupan el mismo espacio en memoria es decir, no son el mismo
if Nombre is not OtroNombre:
    print("¡Este Nombre es Nuevo!")
#Este es para hacer lo mismo pero para saber si el String o int está dentro de alguno de los String/ints que hay contenidos en una lista
if Nombre in ListaNombres:
    print("Este Nombre ya está en mi lista")
#Este es para hacer lo mismo pero al contrario, para saber si el String o int no está dentro de alguno de los String/ints que hay contenidos en una lista
if Nombre not in ListaNombres:
    print("Este Nombre no estaba en mi lista")