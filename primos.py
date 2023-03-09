"""
Kirian Rodríguez Alonso

Módulo de gestión de números primos

Exemples: 
>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
La salida debe ser [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47].
"""

def esPrimo(numero):
    """
    Devuelve True si su argumento es primo, y False si no lo es.
    >>> [numero for numero in range(2,50) if esPrimo(numero)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    for prueba in range(2, numero):
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
    Devuelve una tupla con la descomposicion en factos primos de su argumento
    """

    factores=tuple()
    for factor in primos(numero+1):
        while numero%factor==0:
            numero=numero//factor
            factores=factores+(factor,)
    return factores

import doctest
doctest.testmod()