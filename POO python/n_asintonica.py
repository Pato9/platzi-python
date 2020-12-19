
#LEY DE LA SUMA


def f(n):

    for i in range(n):
        print(i)

    for i in range(n):
        print(i)



"""

O(n) + O(n) -> O(n + n) -> O(2n) ->O(n)

"""

def f(n):
    for i in range(n):
        print(i)

    for i in range(n * n):
        print(i)

"""
O(n) + O(n**2) -> O(n+n**2) -> O(n**2)

"""

# ley de la multiplicacion

def f(n):

    for i in range(n):

        for j in range(n):
            print(i,j)

"""

O(n*n) -> O(n^2)

"""

#Recursividad fibonacci

def fibonacci(n):
    if n == 0 or n ==1:
        return 1
    return fibonacci(n+1) + fibonacci(n-2)


"""
O(2**n)

por forme va creciendo fibonacci nosotros nos vamos demorando mas tiempo
si llamamos una tercera vez a fibonacci

O(3**n)

"""



