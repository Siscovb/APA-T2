"""
Gerard Piqueras Codina

Módulo de gestión de numeros primos

Exemples:
>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
"""

def esPrimo(numero):
    """
    Devuelve True si su argumento es primo, y False si no lo es
    """
    for prova in range(2, numero):
        if numero % prova == 0:
            return False
        
    return True

def primos(numero):
    """
    Devuelve...
    """

    return tuple([prova for prova in range(2,numero) if esPrimo(prova)])


import doctest
doctest.testmod()