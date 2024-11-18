#clase Persona
class Persona:
    def __init__(self, nombre, edad, sexo):
        #atributos de la clase Persona
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo

    def __str__(self):
        #presenta cadena de texto persona
        return(f'Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}')
    
    



        