#nombre="Angel"
#apellido="David"
#nombreCompleto= nombre + " " + apellido
#print ("hola " + nombreCompleto)
# Listas almacena secuencias
lista = [0,1,2,3,4,5]
# Puedes empezar con una lista prellenada
#otra_lista = [4, 5, 6]
# Añadir cosas al final de una lista con 'append'
#lista.append(1) #lista ahora es [1]
#lista.append(2) #lista ahora es [1, 2]
#lista.append(4) #lista ahora es [1, 2, 4]
#lista.append(3) #lista ahora es [1, 2, 4, 3]
# Accede a una lista como lo harías con cualquier arreglo
print(lista[0])  # => 1
# Mira el último elemento
print(lista[-1]) # => 3
# Mirar fuera de los límites es un error 'IndexError'
print(lista[4]) # Levanta la excepción IndexError
# Puedes mirar por rango con la sintáxis de trozo.
# (Es un rango cerrado/abierto para los matemáticos.)
print(lista[1:3]) # => [2, 4]
# Omite el inicio
print(lista[2:]) # => [4, 3]
# Omite el final
print(lista[:3]) # => [1, 2, 4]
# Selecciona cada dos elementos
print(lista[::2]) # =>[1, 4]
# Invierte la lista
print(lista[::-1]) # => [3, 4, 2, 1]
# Usa cualquier combinación de estos para crear trozos avanzados
# lista[inicio:final:pasos]