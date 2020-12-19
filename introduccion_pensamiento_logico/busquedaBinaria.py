


"""
Busqueda binaria 

cuando la respuesta se encuntra en un conjunto ordenado,
podemos utilizar busqueda binaria 



"""



objetivo = int(input('Ingrese un numero : \n >'))
epsilon= 0.001
bajo = 0.0
alto = max(1.0,objetivo)
respuesta = (alto+bajo)/2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo : {bajo}, algo : {alto},respuesta : {respuesta}')
    if respuesta**2 < objetivo: 
        bajo = respuesta
    else:
        alto = respuesta
        print(alto)

    respuesta = (alto+bajo)/2

print(f'La raiz cuadra de {objetivo} es {respuesta}')








