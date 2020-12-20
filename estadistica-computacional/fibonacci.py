import sys

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_dinamico(n,memo = {}):
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n-1,memo)+fibonacci_dinamico(n-2,memo)
    memo[n]=resultado

    return resultado


#Entry point
if __name__ == '__main__':
    sys.setrecursionlimit(10002)
    n = int(input('Escoge un numero \n >'))
    result = fibonacci_dinamico(n)
    print(result)
