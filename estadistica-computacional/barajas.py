import random
import collections

PALOS = ["corazon","trebol","diamante","pica"]
VALORES = ['as','1','2','3','4','5','6','7','8','9','10','J','Q','K']

def formar_baraja():

    cartas = []

    for palo in PALOS:
        for valores in VALORES:
            cartas.append((palo,valores))

    
    return cartas


def obtener_mano(barajas,tamano_mano):

    mano = random.sample(barajas,tamano_mano)

    return mano

def main(tamano_mano,intentos):

    baraja = formar_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(baraja,tamano_mano)
        manos.append(mano)

        pares = 0 
        for mano in manos:
            valores = []
            for carta in mano:
                valores.append(carta[1])

            counter = dict(collections.Counter(valores))
            print(counter)        

            for valor in counter.values():
                if valor == 2:
                    pares+=1
                    #solamente encontrara un par dentro de la mano
                    break

        probabilidad = pares/intentos
        print(f'La probabilidad de encontrar pares en {tamano_mano} es de {probabilidad}')
    

 




if __name__ == '__main__':
    #tamano_mano = int(input('Tamaño de la mano\n>'))
    #intentos = int(input('Cantidad de intentos\n>'))
    
    main(5,100)