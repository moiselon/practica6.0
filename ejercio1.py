print('1. Crear una clase Persona que tenga como atributos el "cedula, nombre, apellido y la edad (definir las propiedades para poder acceder a dichos atributos)". Definir como responsabilidad una cuncion para mostrar ó imprimir. Crear una segunda clase Profesor que herede de la clase Persona. Añadir un atributo sueldo ( y su propiedad) y en la función para imprimir su sueldo. Definir un objeto de la clase Persona y llamar a sus funciones y propiedades. También crear un objeto de la clase Profesor y llamar a sus funciones y propiedades.\n')

class persona ():

    def __init__(self, cedu,nom, ape, ed):
        self.cedula = cedu
        self.nombre = nom
        self.apellido = ape
        self.edad = ed

    def mostrar (self):
        txt = 'cedula : {0} / nombre : {1} / apellido: {2} / edad : {3} '
        return txt.format(self.cedula, self.nombre, self.apellido, self.edad)

class profesor(persona):

    def __init__(self, cedu,  nom, ape, ed , suld):
        super().__init__(cedu, nom, ape, ed )
        self.sueldo = suld

profe = profesor('001-1285166-2', 'ramon' , 'caceres mendoza' , '37' , ' / sueldo: 20000$ pesos dominicanos')
print(profe.mostrar() , profe.sueldo)

