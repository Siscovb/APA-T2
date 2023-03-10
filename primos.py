"""
Joan Marc Fuentes Soler 

Modulo de gestión de numeros primos

"""

def esPrimo(numero):
    """
    Devuelve True si su argumento es primo y False si no lo es.
    >>> [numero for numero in range(2,50) if esPrimo(numero)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    for prueba in range(2,int(numero**0.5+1)):
        if numero % prueba == 0:
            return False
    return True

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    return tuple([prueba for prueba in range(2,numero) if esPrimo(prueba)])

def descompon(numero): 
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    >>> descompon(36 * 175 * 143) 
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    factores = tuple()
    for factor in primos(numero+1):
        while numero % factor == 0 :
            numero = numero / factor
            factores = factores + (factor,)
    return factores

def fact2dic(numero1,numero2):

    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores = set(factores1) | set(factores2)
    dic1 = {factor:0 for factor in factores}
    dic2 = {factor:0 for factor in factores}
    for factor in factores1:
        dic1[factor] += 1
    for factor in factores2:
        dic2[factor] += 1
    return dic1,dic2

import doctest
doctest.testmod()