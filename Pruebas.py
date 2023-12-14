ListaNumeros = [2,50,0,1,10]
ListaNumeros.sort(reverse=True)
print(ListaNumeros)
def divide(lista):
    resultado = lista[0] / lista[1]
    print(f"division numero 0  :  {resultado}")
    for i in range(len(lista)):
            if i != 0:
                if lista[i] != 0:
                    resultado /= lista[i]
                    print(f"división número {i}: {resultado}")
                else:
                    print(f"división número {i}: No se puede dividir por cero. Ignorando.")

    return resultado
print(f"Resultado Final: {divide(ListaNumeros)}")