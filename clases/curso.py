from .profesor import Profesor

class Curso(Profesor):
    def __init__(self, nombre, codigo, profesor):
        self.nombre=nombre
        self.codigo=codigo
        self.profesor=profesor

    def __str__(self):
        return(f'Curso: {self.nombre}, \nCodigo: {self.codigo} , \nProfesor: {self.profesor}')