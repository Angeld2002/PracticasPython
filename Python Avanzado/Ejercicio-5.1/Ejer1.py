"""
Explica y pon un ejemplo sencillo de una función lambda en Python 3.
"""
"""
La Expresion lambda que se plantea abajo llamada sumar es en sí como agregar una funcion a una variable
los valores a la izquierda de los dos puntos marcan la cantidad de parámetros que se le deben de pasar a la funcion.
los que hay a la derecha de los dos puntos marcan lo que hace la función en sí con los parámetros dados anteriormente
"""
# Definimos como ejemplo una función lambda llamada 'sumar' que toma dos argumentos 'num1' e 'num2' y devuelve su suma.
sumar = lambda num1, num2: num1 + num2
# Llamamos a la función lambda y mostramos el resultado.
print(sumar(5, 3))

"""
Después, pon un ejemplo que utilice las funciones de Python:
Utilizando "map()" (i "list()" e "int()" como apoyo para convertir a lista y a números enteros) debe leer de teclado una cadena de texto 
formada por números separados con espacio y transformarla en una lista formada por números enteros.
Utilizando "filter()", elimina de la cadena anterior los números menores que 10.
Con la cadena resultante y utilizando "reduce()", devuelve la multiplicación de los elementos de la lista.
"""

from functools import reduce


numInsertados = input("Ingrese números separados por espacios: ")
listaCadena = numInsertados.split()  # Dividir la cadena en una lista de cadenas
# Utilizamos "map()" para convertir la cadena de texto a una lista de enteros
listaNum = list(map(int, listaCadena))

print("Lista de números enteros:", listaNum)

# Usamos "filter()" para eliminar números menores que 10 con una funcion lambda
listaNumMayor = list(filter(lambda num: num >= 10, listaNum))

print("Números mayores o iguales a 10:", listaNumMayor)

# Usamos"reduce()" para multiplicar los elementos de la lista resultante
resultadoMultiplicacion = reduce(lambda num1, num2: num1 * num2, listaNumMayor, 1)

print("Resultado total:", resultadoMultiplicacion)