#1. Escribir un programa que pregunte al usuario por el número de horas trabajadas (valor entero sólo) y 
#el coste por hora. Después debe mostrar por pantalla el importe total que le corresponde seguido de €. Opcional que incluya dos decimales, separando la parte entera de la decimal con coma (,)

#Pedimos las horas
horas= int(input ("Pon el numero de horas trabajadas: "))
#Pedimos la cantidad por hora
cantidad= float(input ("Pon el coste por hora: "))
#mostramos por pantalla el resultado de multiplicar las horas por cantidad
#el round lo redondea con el ,2 a 2 decimales para dejarlo como se pedía opcionalmente
print(round(horas*cantidad, 2))


#2. Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
#imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

#Pedimos el nombre
nombre= input ("Pon tu nombre: ")
#Pedimos las veces de repeticion
nVeces= int(input ("Pon el numero de veces: "))
#hacemos un bucle que repita el proceso desde 0 a las veces que pusimos
for i in range(0, nVeces):
    print(nombre)


#3. Escribir un programa que pregunte el nombre completo del usuario en la consola y 
#después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

#Pedimos el nombre Completo
nombreCompleto= input ("Pon tu nombre: ")
#Mostramos el nombre completo en minusculas
print(nombreCompleto.lower())
#Mostramos el nombre completo en mayusculas
print(nombreCompleto.upper())
#Mostramos el nombre completo poniendo la primera letra mayuscula de cada palabra
print(nombreCompleto.title()) 


#4. Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

#Pedimos la edad
edad= int(input ("¿Que edad tienes?: "))
#Revisamos si edad es mayor o igual a 18
if edad >= 18:
    #Si es mayor o igual se ejecuta esto
    print("Es mayor de edad")
else:
    #Si no es mayor o igual se ejecuta esto
    print("Es menor de edad")

    
#5. Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido 
#(desde 1 hasta su edad). Por ejemplo, si tiene 18 años: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18

#Pedimos la edad
edad= int(input ("¿Que edad tienes?: "))
#hacemos un bucle que repita el proceso desde 1 a las veces que tengamos según la edad que pusimos +1 
#hay que poner +1 por que si no cuando llega a la edad indicada se detiene es decir
#el bucle por defecto se efectúa mientras el primer numero en este caso 1 sea menor que edad no menor o igual asi que
#por eso sumamos 1 mas a edad para que llegue a la edad que pusimos
for i in range(1, edad+1):
    print(i)


#6. Diccionarios. Escribir un programa que guarde en una variable el 
#diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

#Creamos el diccionario de Divisas como se indicó
dicDivisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
#Pedimos la divisa
divisas= input ("Escriba una Divisa: ")
#Se pregunta si la divisa escrita está dentro (in) del diccionario creado
if divisas in dicDivisas:
    #Si está dentro del diccionario creado se ejecuta esto
    #la f antes de las comillas permite usar las llaves {} en medio de las comillas para poner variables
    print(f"Se encontró la clave {divisas} y su simbolo es {dicDivisas[divisas]}")
else:
    #Si no está dentro del diccionario creado se ejecuta esto
    #la f antes de las comillas permite usar las llaves {} en medio de las comillas para poner variables
    print(f"No se encontró la clave {divisas}")

    
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


#CREAR UNA FUNCION QUE RECIBA UNA LISTA DE NUMEROS. TENDRÁ QUE DIVIDIRLOS DE DOS EN DOS Y MOSTRAR CADA DIVISIÓN,
#PERO EL PRIMERO ES EL MÁS GRANDE Y EL ÚLTIMO EL MAS PEQUEÑO, CONTROLAR ERROR DIVISIÓN POR CERO

ListaNumeros = (5,8,23,3,10)
ListaNumerosOrdenada = ListaNumeros.sort(reverse=True)
print(ListaNumerosOrdenada)

#1. Prepara con un ejemplo donde explicas cómo hacer en Python 3:

#Clonar una lista.

#¿Cuál es la diferencia en Python entre "shallow copy" y "deep copy"?

#Añadir un elemento a una lista.

#Eliminar un elemento de la lista.

#Crear una nueva lista con los 4 últimos elementos de una lista.

#Convertir las palabras de una cadena (separadas por espacio) a una lista.

#Comentarios con una línea.

#Comentarios multilínea.

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


#3. Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!., siendo <nombre> tu nombre obtenido del teclado.
Nombre = input("Pon un Nombre: ")
def saludo(nombre):
    return("¡Hola {}!.".format(nombre))
print(saludo(Nombre))


#4. Escribir una función que reciba un número entero positivo y devuelva su factorial.
numero = 5
def calcularFactorial(num):
        if num == 0:
            return 1
        else:
            return num * calcularFactorial(num - 1)
print(f"El factorial de {numero} es {calcularFactorial(numero)}")


#5. Depuración. Corregir los errores sintácticos del siguiente programa:

"""
pwd= input('Introduce la contraseña: ")
if pwd in ['curso2324'):
  print('Inicio de sesión realizado')
else
  print('Error en inicio de sesión')
"""

# Solución:
pwd= input("Introduce la contraseña: ")
if pwd in ["curso2324"]:
  print('Inicio de sesión realizado')
else:
  print('Error en inicio de sesión')