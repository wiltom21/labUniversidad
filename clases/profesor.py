from .persona import Persona
  #clase profesor que hereda de persona

class Profesor(Persona):
    def __init__(self, nombre, edad, sexo, codigo, especialidad):
        super().__init__(nombre, edad, sexo)
        self.codigo = codigo
        self.especialidad = especialidad

    def __str__(self):
        return (f'{super().__str__()}, Codigo: {self.codigo}, Especialidad: {self.especialidad}')	


  
