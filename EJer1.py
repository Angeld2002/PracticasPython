nombre= input ("Pon tu nombre: ")
apellido= input ("Pon tu apellido: ")
siglas= input ("Pon las siglas de tu modulo: ")

alumno = [nombre,apellido,siglas]

print(alumno)
alumno = alumno[::-1]
print(alumno)

listaModulos =("PSP","AD","EIE","DI","PMYDM","HLC")
alumno.extend(listaModulos)

print(alumno)

alumno.pop(1)
alumno.pop(1)
alumno.append(nombre)
alumno.append(apellido)

print(alumno)
