import random

def tirar_dado(cantidad_tiros):
    """

    dado que hay que tirar una x cantidad de veces y que la suma salga
    12

    """
    secuencia = []
    count_12 = 0 
    for _ in range(cantidad_tiros):
        dado1 = random.choice([1,2,3,4,5,6])
        dado2 = random.choice([1,2,3,4,5,6])
        suma = dado1 + dado2 
        secuencia.append(suma)
        if suma == 12:
            count_12+=1
    return secuencia


def tirar_dado2(cantidad_tiros):
    secuencia = []

    for _ in range(cantidad_tiros):
        dado = random.choice([1,2,3,4,5,6])
        secuencia.append(dado)
    return secuencia


def main(cantidad_tiro,cantidad_repeticiones):
    n_tiros = []
    
    for _ in range(cantidad_repeticiones):
        sec = tirar_dado2(cantidad_tiro)
        n_tiros.append(sec)

    cantidad_1 = 0
    for tiro in n_tiros:
        if 1 not in tiro:
            cantidad_1+=1

    print(n_tiros)

    probabilidad = cantidad_1 / cantidad_repeticiones
    print(probabilidad) 


main(70,10000)
    
