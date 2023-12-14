#2. Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
#imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

#Pedimos el nombre
nombre= input ("Pon tu nombre: ")
#Pedimos las veces de repeticion
nVeces= int(input ("Pon el numero de veces: "))
#hacemos un bucle que repita el proceso desde 0 a las veces que pusimos
for i in range(0, nVeces):
    print(nombre)