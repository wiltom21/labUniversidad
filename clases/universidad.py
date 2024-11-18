from .curso import Curso

class Universidad(Curso):
    #atributos nombre de la Universidad y lista de cursos
    def __init__(self, nombre):
        self.nombre=nombre
        self.cursos=[]
    #metodo para agresar curssos a la Universidad
    def agregar_curso(self, curso):
        self.cursos.append(curso)

    #cadena de presentarion
    def __str__(self):
        cursos_str="\n".join([str(curso) for curso in self.cursos])
        return (f'Universidad: {self.nombre},  \nCursos: {cursos_str}\n')


