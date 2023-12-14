#1. Escribir un programa que pregunte al usuario por el número de horas trabajadas (valor entero sólo) y 
#el coste por hora. Después debe mostrar por pantalla el importe total que le corresponde seguido de €. Opcional que incluya dos decimales, separando la parte entera de la decimal con coma (,)

#Pedimos las horas
horas= int(input ("Pon el numero de horas trabajadas: "))
#Pedimos la cantidad por hora
cantidad= float(input ("Pon el coste por hora: "))
#mostramos por pantalla el resultado de multiplicar las horas por cantidad
#el round lo redondea con el ,2 a 2 decimales para dejarlo como se pedía opcionalmente
print(round(horas*cantidad, 2))