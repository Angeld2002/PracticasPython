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