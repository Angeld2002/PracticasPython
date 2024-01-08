def esPalindromo(numero):
    """
    Comprueba si un número es palíndromo.
    y devuelve true si lo es
    """
    return str(numero) == str(numero)[::-1]

def esPrimo(numero):
    """
    Comprueba si un número es primo.
    y devuelve true si lo es
    """
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def main(archivo_entrada, archivo_salida):
    
    # Leer números del archivo de entrada
    with open(archivo_entrada, 'r') as file:
        numeros = [int(line.strip()) for line in file]

    # Calcular palíndromos y primos
    palindromos = [num for num in numeros if esPalindromo(num)]
    primos = [num for num in numeros if esPrimo(num)]
    palindromos_y_primos = [num for num in numeros if esPalindromo(num) and esPrimo(num)]

    # Escribir informe en el archivo de salida
    with open(archivo_salida, 'w') as file:
        file.write(f"Hay {len(palindromos)} numeros palindromos.\n")
        file.write(f"Hay {len(primos)} numeros primos.\n")
        for num in palindromos_y_primos:
            file.write(f"{num}\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: programa.py <archivo_entrada> <archivo_salida>")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]

    main(archivo_entrada, archivo_salida)
