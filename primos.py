


def esPrimo(numero):
    """
    Devuelve "True" si su argumento es primo    
    Al ejecutar `[ numero for numero in range(2, 50) if esPrimo(numero) ]`, la salida debe ser
    `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]`
    """
    for prueba in range (2, int(numero**0.5)+1):
        if numero % prueba == 0: return False

    return True

def primos(numero):

    """
    Devuelve una **tupla** con todos los números primos menores
    
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    return tuple([prueba for prueba in range(2, numero) if esPrimo(prueba)])


def descompon(numero):

    """
    Devuelve una tupla con la descomposición en factores
    >>> descompon (36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    factores = []

    for factor in primos(numero):
        while numero%factor == 0:
            factores.append(factor)
            numero //= factor
    return tuple(factores)


def dicFact(numero1, numero2):

    """
    """

    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores = set(factores1 + factores2)
    dicFact1 = {factor:0 for factor in factores}
    dicFact2 = {factor:0 for factor in factores}
    for factor in factores1: dicFact1[factor] += 1
    for factor in factores2: dicFact2[factor] += 1
    return dicFact1, dicFact2


def mcm(numero1, numero2):
    """
    >>> mcm(36, 30) 
    180
    """
    mcm = 1
    dicFact1, dicFact2 = dicFact(numero1, numero2)
    for factor in dicFact1 | dicFact2:
        mcm *= factor ** max(dicFact1[factor], dicFact2[factor])
    return mcm

import doctest
doctest.testmod()