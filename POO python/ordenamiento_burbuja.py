import random


def ordenamiento_de_burbuja(lista):

    n = len(lista)
    for i in range(n):
        for j in range(n - 1):
            if lista[j] > lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
    return lista

"""
O(n)* O(n) -> O(n*n) -> O(n^2)

"""



if __name__ == '__main__':
    lista = [random.randint(0,10) for i in range(0,15)]
    print(lista)
    orden = ordenamiento_de_burbuja(lista)
    print(orden)




