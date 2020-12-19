

"""
Para modificar las lista podemos usar
append(),pop(),remove(),insert()....

"""


my_list = [1,2,3]

my_list[0]
#-> 1

my_list[1:]
#->2,3

my_list.append(4)

print(my_list)

#my_list[0] = 'Adam'
#print(my_list)

#Eliminar elementos de una lista
#pop elimina el ultimo elemento
my_list.pop()

for element in my_list:
    print(element)

a = [1,2,3]

"""
las lista 'my_list' y 'a' ocupan la misma direccion en memoria

"""

b = a

print(id(a))
print(id(b)) 

c = [a,b]
print(c)
a.append(5)
print(c)



"""
Clonacion
"""

a = [1,2,3]
print(id(a))

b = a

c = list(a)

print(id(a))
print(id(b))
print(id(c))


d = b[::]
print(id(d))


"""
List comprehension

"""

my_new_list = list(range(0,100))
print(my_new_list)

pares = [i for i in my_new_list if i % 2 == 0]
print(pares)

double = [i * 2 for i in my_new_list]
print(double )
































