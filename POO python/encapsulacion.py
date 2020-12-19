

class Employee:

    def __init__(self,nombre,apellido):
        self._nombre = nombre
        self._apellido = apellido


    @property
    def correo(self):
        return '{}.{}@correo.com'.format(self._nombre,self._apellido)

    
    @property
    def nombre_completo(self):
        return '{} {}'.format(self._nombre,self._apellido)

    @nombre_completo.setter
    def nombre_completo(self,name):
        nombre,apellido = name.split(' ')
        self._nombre = nombre
        self._apellido = apellido

    
    @nombre_completo.deleter
    def nombre_completo(self):
        print('Se elimino el nombre')
        self._nombre = None
        self._apellido = None



emp_1 = Employee('Patricio','Soto')

print(emp_1.correo)
nombre = emp_1.nombre_completo
emp_1.nombre_completo('Patricio Soto')
       



