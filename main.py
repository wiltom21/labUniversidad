#desde carpeta clases y el fichero "x" importa clase "x"
from clases.universidad import Universidad
from clases.profesor import Profesor
from clases.curso import Curso
from clases.estudiante import Estudiante
#no se manda a llamar persona porque no es necesario

#crear universidad
universidad=Universidad('Universidad de El Salvador')

#crear Profesores
profesor_juan= Profesor('Juan Perez', 30, 'masculino',20201212, 'matematicas')
profesor_maria= Profesor('Maria Lopez', 35, 'femenino', 20230815, 'fisica')
profesor_pedro= Profesor('Pedro Ramirez', 40, 'masculino', 20241117, 'quimica')

#crear cursos con profesores respectivos
curso_matematicas=Curso('matematicas',"MAT101",profesor_juan )
curso_fisica=Curso('fisica',"FIS101",profesor_maria )
curso_quimica=Curso('quimica',"QUI101",profesor_pedro )

#agregar cursos a universidad
universidad.agregar_curso(curso_matematicas)
universidad.agregar_curso(curso_fisica)
universidad.agregar_curso(curso_quimica)

#crear estudiante
estudiante_Carlos=Estudiante('Carlos Perez', 20, 'masculino', 202010101, 'Ingenieria en sistemas')

#imprimir informacion de universidad, estudiante, profesor y curso
print(universidad)
print('---------------------------------------')
print(estudiante_Carlos)
print('---------------------------------------')
print(profesor_juan)
print('---------------------------------------')
print(curso_matematicas)

#crear nuevo curso de fisica y agregarlo a la Universidad
curso_nuevo_fisica=Curso('Fisica', "FIS102", profesor_maria)
universidad.agregar_curso(curso_nuevo_fisica)

print('---------------------------------------')
print(curso_nuevo_fisica)

