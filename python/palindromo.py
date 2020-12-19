

def palindromo(string):
    """
    eliminamos los espacios y pasamos el string a minuscula
    """
    palabra = string.strip().replace(' ','').lower()
    """
    creamos una funcion lambda en donde preguntamos si x va ser igual a
    x al reves, vamos a retornar true o false dependiendo del caso
    """
    verificar = lambda x : True if x == x[::-1] else False
    """
    aca dependiendo de la variable verificar podremos saber si
    verificar es verdadero o falso
    """
    return(f'es palindromo ' if verificar(palabra) else 'No lo es :( ')


# validamos el ingreso
palabra = "Luz azul"
print(palindromo(palabra))






