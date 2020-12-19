

my_tuple = ()
type(my_tuple)

my_tuple = (1,'dos',True)
my_tuple[0] #-> 1 

"""

Si nosotros queremos reasignar un valor a la tupla, el programa tiraria error


"""


my_tuple = (1)

type(my_tuple)
#output : int

"""
Para que una variable sea una tupla debe contener una coma
"""

my_tuple = (1,)
type(my_tuple)
#output -> tuple

my_other_tuple = (2,3,4,5)
my_tuple+=my_other_tuple
print(my_tuple)
#output -> (1,2,3,4,5)



"""
podemos desempaquetarlas

"""

x,y,z = my_other_tuple
print(z,y,z)


def coordenadas():
    return (5,4)

coordenada = coordenadas()
print(coordenada)

x,y = coordenadas()































