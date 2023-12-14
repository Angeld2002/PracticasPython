#7. Diccionarios. Escribir un programa que pregunte al usuario su 
#nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> 
#tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

#Pedimos el Nombre
iNombre= input ("Pon tu Nombre: ")
#Pedimos la Edad
iEdad= input ("Pon tu Edad: ")
#Pedimos la Direccion
iDireccion= input ("Pon tu Direccion: ")
#Pedimos el Telefono
iTelefono= input ("Pon tu Telefono: ")
#Creamos el diccionario de Datos usando como valor las variables pedidas antes
dicDatos = {"nombre": iNombre, "edad":iEdad, "direccion":iDireccion, "telefono":iTelefono}
#Mostramos el mensaje indicado en la tarea usando el diccionario directamente
#la f antes de las comillas permite usar las llaves {} en medio de las comillas para poner variables
print(f"{dicDatos['nombre']} tiene {dicDatos['edad']} años, vive en {dicDatos['direccion']} y su número de teléfono es {dicDatos['telefono']}.")