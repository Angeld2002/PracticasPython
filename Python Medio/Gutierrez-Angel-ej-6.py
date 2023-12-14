#6. Diccionarios. Escribir un programa que guarde en una variable el 
#diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

#Creamos el diccionario de Divisas como se indicó
dicDivisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
#Pedimos la divisa
divisas= input ("Escriba una Divisa: ")
#Se pregunta si la divisa escrita está dentro (in) del diccionario creado
if divisas in dicDivisas:
    #Si está dentro del diccionario creado se ejecuta esto
    #la f antes de las comillas permite usar las llaves {} en medio de las comillas para poner variables
    print(f"Se encontró la clave {divisas} y su simbolo es {dicDivisas[divisas]}")
else:
    #Si no está dentro del diccionario creado se ejecuta esto
    #la f antes de las comillas permite usar las llaves {} en medio de las comillas para poner variables
    print(f"No se encontró la clave {divisas}")