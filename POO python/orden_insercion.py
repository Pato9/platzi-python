
lista = [7,3,1,2,4,6]

def orden_insercion(lista):
    for indice in range(1,len(lista)):
        valor_inicial = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual -1 ] > valor_inicial:
            lista[posicion_actual] = lista[posicion_actual - 1 ]
            posicion_actual-=1
        lista[posicion_actual] = valor_inicial
    return lista

print(orden_insercion(lista))




