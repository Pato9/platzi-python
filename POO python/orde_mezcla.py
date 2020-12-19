lista = [6,5,3,1,8,7,2,4]

def ordenamiento_por_mezcla(lista):
    if len(lista)>1:
        medio = len(lista)//2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda,'***',derecha)
        #llamada recursiva en cada mida
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # iteradores para recorrer las 2 sublistas
        i = 0
        j = 0
        #iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i+=1
            else:
                lista[k] = derecha[j]
                j+=1
            k+=1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i+=1
            k+=1

        while j < len(derecha):
            lista[k] = derecha[j]
            j+=1
            k+=1

        print(f'izquierda {izquierda}, derecha{derecha}')
        print(lista)
        print('-'*30)
    return lista

print(ordenamiento_por_mezcla(lista))
