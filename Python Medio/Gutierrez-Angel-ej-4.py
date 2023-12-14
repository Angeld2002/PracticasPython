#4. Escribir una función que reciba un número entero positivo y devuelva su factorial.
numero = 5
def calcularFactorial(num):
        if num == 0:
            return 1
        else:
            return num * calcularFactorial(num - 1)
print(f"El factorial de {numero} es {calcularFactorial(numero)}")
    