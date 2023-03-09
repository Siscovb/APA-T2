""""
PAU PERÁLVAREZ CASASAMPERE

"""


def esPrimo(numero):
    """
    Devuelve **True** si su argumento es primo, 
    y False si no lo es.

    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    """
    for prueba in range(2, int(numero ** 0.5) + 1):                             
        if numero % prueba == 0: return False

    return True 


def primos(numero):
    """
    Devuelve una **tupla** con todos los números primos 
    menores que su argumento.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

    """
    return tuple([ prueba for prueba in range(2, 50) if esPrimo(prueba) ])


def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores 
    primos de su argumento.

    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)

    """
    resultado = []

    for i in primos(numero):
        while numero % i == 0:
            resultado.append(i)
            numero //= i

    return tuple(resultado)


from collections import Counter as C  


def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.

    >>> mcm(90, 14)
    630

    """
    numero1D = C(descompon(numero1))
    numero2D = C(descompon(numero2))

    #Combinamos las descomposiciones factoriales en un solo 'diccionario' (contador). 
    #En caso de igualdad nos quedamos con el exponente más grande
    factoritzacion = numero1D | numero2D  

    mcm = 1 
    for factor, exp in factoritzacion.items():
        mcm *= (factor**exp)

    return mcm


def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.

    >>> mcd(924, 780)
    12

    """
    numero1D = C(descompon(numero1))
    numero2D = C(descompon(numero2))

    #Combinamos las descomposiciones factoriales en un solo contador. 
    #En caso de igualdad nos quedamos con el exponente más pequeño
    factoritzacion = numero1D & numero2D  

    mcd = 1 
    for factor, exp in factoritzacion.items():
        mcd *= (factor**exp)

    return mcd


import doctest
doctest.testmod()

