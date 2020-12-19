


def factorial(n):
    """
    calcula el factorial de n
    n -> entero > 0 
    return n!
    """
    print(n)
    if n == 1:
        return 1
    return n * factorial(n-1)


n = int(input('Ingrese un entero : '))

print(f'El factorial de {n} es de : {factorial(n)}')

