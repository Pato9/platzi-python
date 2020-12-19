# deficion de la clase


"""

class <nombre_de_la_clase>(<super_clase>):

    def __init__(self,<params>):
        <expresion>

    def nombre_del_metodo(self,<params>):
        <expresion>


"""


class Persona():
    
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def saludo(self,otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}'


#Uso
patricio = Persona('Patricio',23)
javiera = Persona('Javiera',22)


print(patricio.saludo(javiera))
