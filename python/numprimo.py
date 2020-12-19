"""
mastrar los numeros primos hasta 100

se uso el teorema de wilson

"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def primo(n):
    wilson = factorial(n-1) + 1
    if wilson % n == 0:
        print('es primo')
    else:
        print('no es primo')

input_num = int(input("Ingrese un numero"))

primo(input_num)






