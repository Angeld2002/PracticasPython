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