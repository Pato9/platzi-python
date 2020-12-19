
"""
recursividad 

ejemplo fibonacci

"""

def fibonacci(n):
    """
    Este metodo es demasiado ineficiente
    """
   
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)




n = int(input('Ingrese un numero mayor a 0:'))
if n>0:
    print(f'En el mes {n} habra un total de {fibonacci(n)}')


