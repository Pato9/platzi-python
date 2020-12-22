import random


def mayor_a_numero(cantidad_tiros,numero):

    dado = [1,2,3,4,5,6]

    numeros = []
    for  i in dado:
        if i>numero:
            numeros.append(i)

    if numero>0 and numero<7:
        total_dados = len(dado)
        total_posibilidades = len(numeros)
        print(f'{total_posibilidades}-{total_dados}')
    
        posibilidad = (total_posibilidades/total_dados)**cantidad_tiros
    
        return posibilidad*100

def bolas(colores):
    """
    Ejercicio 1

    probabilidad de obtener uno de color azul y el segundo sea de color rojo 
    ya que uno depende de otra es un evento dependiente

    P(A y B) = P(A) * P(B|A)

    """
    color1,color2 = colores
    print(color1,'-',color2)


    bolas = {"verde":3,
             "rojo":5,
             "azul":2}

    cantidad_bolas = 0

    c_color_1 = 0
    c_color_2 = 0

    for color,valor in bolas.items():
        cantidad_bolas+=valor
        if color1 == color:
            c_color_1 = valor
        elif color2 == color:
            c_color_2 = valor
   


    p_a = (c_color_1/cantidad_bolas)
    p_b_a = (c_color_2/(cantidad_bolas-1))

    probabilidad = p_a * p_b_a
    return round(probabilidad*100,2)
    
    #print(p_a*100,'%')


    

#def cantidad_simulaciones(cantidad_simulaciones):

def dinero_helado():
    """
    Evendo independiente

    primer evento : el 8% de las personas de x lugar ganan mas de 1000usd
    segundo evento : el 60% le gustan los helados

    ¿si se selecciona una persona en este lugar cual es la posibilidad de que
    gane mas de 1000usd y le guste el helado 
    """

    p_a = 0.08
    p_b = 0.6 

    probabilidad = p_a*p_b
    print(probabilidad*100,'%')

#TODO: generar un sistema que tire dados de forma aleatoria en una cierta cantidad
#      de tiros y 


if __name__ == '__main__':
    #ejercicio 1
    #numeros_tiros = int(input('Cuantas veces tiramos los datos'))
    #numero_mayor = int(input('Ingrese cuandas posibiliodades tiene a partir del numero :'))
    #print(mayor_a_numero(numeros_tiros,numero_mayor))

    #ejercicio 2
    #print('Los colores a elegir son verdes,rojos,azules')
    #print('vea la probabilidad de que la primera sea del color 1 y la segunda color 2')
    #input_color_1 = input('Ingrese primer color \n>')
    #input_color_2 = input('Ingrese segundo color \n>')
    #input_colores = [input_color_1.lower(),input_color_2.lower()]
    #print(bolas(input_colores))

    #ejercicio 3
    #dinero_helado()

    