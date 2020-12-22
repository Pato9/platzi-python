import random
import math

#media
def media(n):
    return (sum(n)/len(n))

#desviacion estandar calculando directamente la varianza
def desviacion_estandar(lista):

    x = media(lista)
    var = 0
    for i in lista:
        var = var + (i - x )**2/len(lista)
    
    sigma = math.sqrt(var)
    return sigma


def tirar_agujas(numero_agujas):
    
    adentro_circulo = 0
    
    for _ in range(numero_agujas):
        x = random.random() * random.choice([-1,1])
        y = random.random() * random.choice([-1,1])
        #teorema de pitagora
        distancia_centro = math.sqrt(x**2 + y**2)

        if distancia_centro <= 1 :
            adentro_circulo+=1 

    return ( 4 * adentro_circulo) / numero_agujas
    
def estimacion(numero_agujas,numero_intentos):
    estimados = []

    for _ in range(numero_intentos):
        estimacion_pi = tirar_agujas(numero_agujas)
        estimados.append(estimacion_pi)

    media_estimados = media(estimados)
    sigma = desviacion_estandar(estimados)

    print(f'esti={round(media_estimados,5)}, sigma = {round(sigma,5)}')

    return (media_estimados,sigma)

def estimar_pi(precision,numero_intentos):

    numero_agujas = 1000
    sigma = precision

    while sigma >= precision / 1.96:
        media,sigma = estimacion(numero_agujas,numero_intentos)
        numero_agujas *= 2

    return media
if __name__ == '__main__':
    print(estimar_pi(0.01,1000))