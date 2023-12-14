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