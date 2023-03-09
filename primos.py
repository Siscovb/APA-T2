"""
Milene Granda
Módulo de gestión de numeros primos
Exemples:
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

    for proba in range(2, int(numero**0.5+1)):
        if numero % proba ==0:
            return False
    return True 

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento
    """
    return tuple([proba for proba in range(2,numero) if esPrimo(proba)])

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    """
    factores = tuple()
    for factor in primos(numero + 1):
        while numero%factor ==0:
            numero = numero//factor
            factores = factores + (factor,)

    return factores

def mcm (numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    """

def fact2dic(numero1, numero2):
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    

'esto es para hacer la prueba:'
import doctest
doctest.testmod()
