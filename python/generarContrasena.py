
import random

def generate_pass():
    mayus = ['A','B','C','D','E','F','G','H','I','J','K']
    minus = ['o','p','q','r','s','t']
    numbers = [1,2,3,4,5,6,7,8,9,0]
    simbols = ['-','/','_','@',',']

    caracteres = mayus + minus + numbers + simbols
    password = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(str(caracter_random))

    final_pass = "".join(password)
    return final_pass

def run():
    password = generate_pass()
    print(f'tu nueva contraseña es : {password}')


if __name__ == '__main__':
    run()


