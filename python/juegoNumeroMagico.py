
import random

#numero_random = random.randrange(0,100)
#print(numero_random)


def run():
    numero_maquina = random.randrange(1,100)
    print(numero_maquina)
    intentos = 0
    puntos = 0
    while intentos<3:
        n_user = int(input('Ingrese numero : '))
        intentos+=1
        if n_user > numero_maquina:
            print('El numero ingreso es mayor al numero megico ')
        elif n_user < numero_maquina:
            print('El numero ingresado es menor al numero magico')
        elif n_user == numero_maquina:
            print('Adivinaste el numero magico! ')
            break

        if intentos == 3:
            print('Perdiste por maximo de intentos')
run()







