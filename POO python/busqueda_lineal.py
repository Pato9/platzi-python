
import random

def busqueda_linea(lista,objetivo):
    match = False
    iteraciones = 0
    for elemento in lista:
        iteraciones+=1
        if objetivo == elemento:
            match = True
            break
    return match,iteraciones

"""
O(n)

"""



def main():
    tamano_lista = int(input('Que tamaño sera la lista :'))

    objetivo = int(input('Que numero quieres encontrar'))

    lista = [random.randint(0,100) for i in range(tamano_lista)]
    print(lista)

    encontrado,iteraciones = busqueda_linea(lista,objetivo)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"}')
    print(f'iteraciones : {iteraciones}')


if __name__ == '__main__':
    main()






