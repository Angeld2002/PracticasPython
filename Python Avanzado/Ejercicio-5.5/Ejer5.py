# programa_principal.py
from escuela import Profesor, Alumno, Escuela

# Crear instancias de profesores
profesorProgramacion = Profesor("Juan", "Programacion")
profesorFol = Profesor("Maria", "Fol")

# Crear instancias de alumnos
alumno1 = Alumno("Ali", "Primero", profesorProgramacion)
alumno2 = Alumno("Gonzalo", "Segundo", profesorFol)

# Crear instancia de la escuela
MiColegio = Escuela("Politecnico", "Málaga", "Fran")

# Agregar profesores y alumnos a la escuela
MiColegio.agregar_profesor(profesorProgramacion)
MiColegio.agregar_profesor(profesorFol)
MiColegio.agregar_alumno(alumno1)
MiColegio.agregar_alumno(alumno2)

# Mostrar información de la escuela
print("Información de la escuela:")
MiColegio.mostrar_info_escuela()

# Eliminar un profesor y mostrar información actualizada
MiColegio.eliminar_profesor(profesorProgramacion)
print("\nDespués de eliminar un profesor:")
MiColegio.mostrar_info_escuela()

# Agregar un nuevo alumno y mostrar información actualizada
alumno3 = Alumno("Angel", "Segundo", profesorFol)
MiColegio.agregar_alumno(alumno3)
print("\nDespués de agregar un nuevo alumno:")
MiColegio.mostrar_info_escuela()
