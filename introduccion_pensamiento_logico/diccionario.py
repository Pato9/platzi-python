


my_dict = {
        'David' : 35,
        'Erika' : 32,
        'Jaime' : 50,

        }


my_dict['David']

print(my_dict.get('Juan',50))

my_dict['Jaime'] = 60
print(my_dict)

#agregar un nuevo valor al diccionario

my_dict['Juan'] = 20
print(my_dict)

#eliminar una llave
del my_dict['Jaime']

print(my_dict)

"""
Como iterar 

"""
print('llaves')
for llave in my_dict.keys():
    print(llave)


print('valores')
for valores in my_dict.values():
    print(valores)

print('items')
for items in my_dict.items():
    print(items)


#preguntar si hay una llave dentro del diccionario

if 'David' in my_dict:
    print('Si existe')








