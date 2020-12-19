

"""

iteraciones o loops


la mayorias de las tareas computaciones no se pueden lograr
con ramificaciones.

cuando queremos que un programa haga lo mismo varias veces
utilizamos iteraciones. T

podemos usar break para salir de la iteracion.


"""

#while loop

"""
primero debemos tener una condicion para que la iteracion
se detenga. 
"""

contador_externo = 0
contador_interno = 0

while contador_externo < 5:
    while contador_interno < 6: 
        print(contador_externo,contador_interno)
        contador_interno+=1
    contador_externo+=1
    contador_interno = 0

print(message)











