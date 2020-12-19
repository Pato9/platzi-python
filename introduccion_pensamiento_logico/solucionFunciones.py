

def raiz_cuadrada(numero):
    respuesta = 0
    while respuesta**2 < numero:
        respuesta+=1
    
    if respuesta**2 == numero:
        print(f'La raiz cuadrada de {numero} es {respuesta}')
    else:
        print(f'{numero} no posee una raiz cuadrada exacta')



def epsilon(numero):
    respuesta = 0.0
    epsilon = 0.001
    paso = epsilon**2
    while abs(respuesta**2-numero)>=epsilon and respuesta<=numero:
        respuesta+=paso
    
    if abs(respuesta**2-numero)>=epsilon:
        print(f'No se encontro la raiz cuadrada del objetivo {numero}')
    else:
        print(f'La raiz cuadrada de {numero} es {respuesta}')


def busqueda_binaria(numero):
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0,numero)
    respuesta = (alto+bajo)/2

    while abs(respuesta**2-numero) >= epsilon:
        print(f'bajo : {bajo}, alto : {alto}, respuesta : {respuesta}')
        if respuesta**2< numero:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto+bajo)/2

    print(f'La raiz cuadrada de {numero} es {respuesta}')



opcion = int(input(""" Bienvenido \n
Eliga una opcion > 
1)Raiz cuadrada
2)epsilon
3)Busqueda binaria
"""))

numero = int(input('Ingrese numero  :'))

while(opcion >0 and opcion<4):
    if opcion == 1:
       raiz_cuadrada(numero)
       break
    elif opcion == 2:
        epsilon(numero)
        break
    elif opcion == 3:
        busqueda_binaria(numero)
        break











