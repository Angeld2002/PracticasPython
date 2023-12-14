#5. Depuración. Corregir los errores sintácticos del siguiente programa:

"""
pwd= input('Introduce la contraseña: ")
if pwd in ['curso2324'):
  print('Inicio de sesión realizado')
else
  print('Error en inicio de sesión')
"""

# Solución:
pwd= input("Introduce la contraseña: ")
if pwd in ["curso2324"]:
  print('Inicio de sesión realizado')
else:
  print('Error en inicio de sesión')