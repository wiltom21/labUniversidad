#desde fichero persona trae clase Persona
from .persona  import Persona

#clase estidiante hereda de Persona
class Estudiante(Persona):
    #inicializacion de atributos de persona y adicionales
    def __init__(self, nombre, edad, sexo, carnet, carrera):
        super().__init__(nombre, edad, sexo)
        self.carnet=carnet
        self.carrera=carrera

    def __str__(self):
        return (f'{super().__str__()}, Carnet: {self.carnet},Carrera: {self.carrera}')      
                
    
    

