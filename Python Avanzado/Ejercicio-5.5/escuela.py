# escuela.py

class Profesor:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

class Alumno:
    def __init__(self, nombre, curso, profesor_responsable):
        self.nombre = nombre
        self.curso = curso
        self.profesor_responsable = profesor_responsable

class Escuela:
    def __init__(self, nombre, localidad, responsable):
        self.nombre = nombre
        self.localidad = localidad
        self.responsable = responsable
        self.profesores = []
        self.alumnos = []

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)

    def eliminar_profesor(self, profesor):
        self.profesores.remove(profesor)

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def eliminar_alumno(self, alumno):
        self.alumnos.remove(alumno)

    def mostrar_info_escuela(self):
        print(f"Escuela: {self.nombre}")
        print(f"Localidad: {self.localidad}")
        print(f"Responsable: {self.responsable}")
        print("\nProfesores:")
        for profesor in self.profesores:
            print(f"Nombre: {profesor.nombre}, Tipo: {profesor.tipo}")
        print("\nAlumnos:")
        for alumno in self.alumnos:
            print(f"Nombre: {alumno.nombre}, Curso: {alumno.curso}, Profesor Responsable: {alumno.profesor_responsable.nombre}")
