
my_var = 'Hello Platzi'
print(my_var)

my_var = 3
print(my_var)



"""
espacio en memoria
...
my_var -----> 0x00001 -> 'Hello Platzi'
              0x00002 -> 3
              ....

"""
"""
Variables

*pueden contener mayus,minus, numeros(sin comenzar con uno) y el simbolo

no pueden llamarse como palabras reservadas

-lista de palabras reservadas

False
None
True
and
as assert
async
await
break
class
continue
def
del
elif
else
except
finally
for
from
global
if
import
in as
lambda
nonlocal
not
or
pass
raise
return
try
while
with
yield

"""


# cadenas

my_str = 'Platzi'
largo = len(my_str)
print(largo)

#      1ra posicion
my_str[0]

#rebanadas

my_str[2:] # ->atzi
my_str[:3] # ->pla
my_str[:-2] # ->Plat
my_str[::-2] # talP
my_str[::2] # Paz -> va de 2 en 2


# inputs

nombre = input('Cual es tu nombre? : \n >')

print(f'Tu nombre es {nombre}') # tu nombre es patricio

numero = int(input('Escribe un numero : \n >'))

print(f'El doble del numero es {numero * 2}')









