

"""

Enumeracion Exhautiva

llamado adivina y verifica

las computadores actuales son muy muy rapidas

uno de los primeros algoritmos que debes tratar


"""


objetivo = int(input('Ingrese un entero'))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta+=1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada del {objetivo} es :{respuesta}')
else:
    print(f'{objetivo} no tiene una raiz cuadrada exacta')




