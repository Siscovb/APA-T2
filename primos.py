""""
Gisela León Pipó

Modulo de gestión de números primos

Exemples d'utilització:

>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)
"""


def esPrimo(numero):
    """ 
     Devuelve True si su argumento es primo, y False si no lo es.
    """

    for prova in range(2, numero):
        if numero % prova == 0:
            return False  

    return True

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.
    """

    return tuple([prova for prova in range(2, numero) if esPrimo(prova)])

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    """

    return tuple([prova for prova in range (2, numero) if primos(numero)])

import doctest
doctest.testmod()
