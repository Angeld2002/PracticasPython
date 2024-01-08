from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Escuela(Base):
    __tablename__ = 'escuelas'
    
    id = Column(String, primary_key=True)
    nombre = Column(String)
    localidad = Column(String)
    responsable = Column(String)

class Profesor(Base):
    __tablename__ = 'profesores'
    
    id = Column(String, primary_key=True)
    nombre = Column(String)
    tipo = Column(String)
    escuela_id = Column(String, ForeignKey('escuelas.id'))

class Alumno(Base):
    __tablename__ = 'alumnos'
    
    id = Column(String, primary_key=True)
    nombre = Column(String)
    curso = Column(String)
    profesorR_id = Column(String, ForeignKey('profesores.id'))
    escuela_id = Column(String, ForeignKey('escuelas.id'))

# Configuración de la conexión a la base de datos SQLite en memoria
engine = create_engine('sqlite:///:memory:')

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Registrar las clases en el registro
Base.registry.metadata.create_all(bind=engine)

# Crear instancias de escuela, profesores y alumnos 
escuela1 = Escuela(id='1', nombre="Politecnico", localidad="Málaga", responsable="Fran")
profesorProgramacion = Profesor(id='1', nombre="Juan", tipo="Programacion", escuela_id='1')
profesorFol = Profesor(id='2', nombre="Maria", tipo="Fol", escuela_id='1')
alumno1 = Alumno(id='1', nombre="Ali", curso="Primero", profesorR_id= 2 , escuela_id='1')
alumno2 = Alumno(id='2', nombre="Gonzalo", curso="Segundo", profesorR_id= 1, escuela_id='1')

# Agregar profesores y alumnos a la sesión y persistir en la base de datos
session.add_all([profesorProgramacion, profesorFol, alumno1, alumno2])
session.commit()


print("\nAlumnos en la base de datos:")
for alumno in session.query(Alumno).all():
    print("Nombre: " + alumno.nombre)
    print("ID: " + alumno.id)
    print("Curso: " + alumno.curso)
    print("ID Profesor Responsable: " + alumno.profesorR_id)
    print("ID Escuela: " + alumno.escuela_id)

