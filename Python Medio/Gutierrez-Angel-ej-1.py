#1. Prepara con un ejemplo donde explicas cómo hacer en Python 3:

#Clonar una lista.
listaPrincipal = [1, 2, 3, 4, 5]
listaClon = listaPrincipal.copy()
print("Lista Original:", listaPrincipal)
print("Clon de la Lista:", listaClon)

#¿Cuál es la diferencia en Python entre "shallow copy" y "deep copy"?

# En "shallow copy", se crea una nueva lista, pero los elementos internos se mantienen como referencias.
# En "deep copy" o Copia Profunda, se crea una nueva lista y se copian también los elementos internos de manera independiente.

#Seguir por aqui
import copy

lista_anidada = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(lista_anidada)
deep_copy = copy.deepcopy(lista_anidada)
#Añadir un elemento a una lista.
nuevo_elemento = 6
listaPrincipal.append(nuevo_elemento)
print("Lista con Nuevo Elemento:", listaPrincipal)
#Eliminar un elemento de la lista.
elemento_a_eliminar = 3
listaPrincipal.remove(elemento_a_eliminar)
print("Lista sin el Elemento", elemento_a_eliminar, ":", listaPrincipal)
#Crear una nueva lista con los 4 últimos elementos de una lista.
ultimos_cuatro = listaPrincipal[-4:]
print("Últimos Cuatro Elementos:", ultimos_cuatro)
#Convertir las palabras de una cadena (separadas por espacio) a una lista.
cadena = "Esto es una cadena de ejemplo"
lista_palabras = cadena.split()
print("Lista de Palabras:", lista_palabras)
#Comentarios con una línea.
# Este es un comentario de una línea
#Comentarios multilínea.
"""
Este es
un comentario
multilínea.
"""