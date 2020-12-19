
# assert <expresion booleana>, <mensaje de error>


def primera_letra(lista):
    primeras_letras = []

    for palabra in lista:
        assert type(palabra) == str, f'{palabra } no es string'
        assert type(palabra) > 0, 'No se permiten strings vacios'


        primeras_letras.append(palabra[0])


    return primeras_letras



