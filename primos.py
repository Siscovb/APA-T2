"""
Albert Giménez Arnal

Módulo de gestión de números primos

Exemples:

>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(9856)
(2, 2, 2, 2, 2, 2, 2, 7, 11)

>>> mcm(90,14)
630
"""

def esPrimo(numero):
    """
    Devuelve `True` si su argumento es primo, y `False` si no lo es.
    """

    for proba in range(2,numero):
        if numero % proba == 0:
            return False
        
    return True

def primos(numero):
    """
    Devuelve una **tupla** con todos los números primos menores que su argumento.
    """
    return tuple([prova for prova in range(2,numero) if esPrimo(prova)])


def descompon(numero):
    """
    Devuelve una **tupla** con la descomposición en factores primos de su argumento.
    """
    num = numero+1
    listaPrimos = list(primos(num))
    salida = tuple()
    for proba in listaPrimos:
        while numero % proba == 0:
            numero = numero//proba
            salida=salida + (proba,)    
    return salida

def dicFact(numero1, numero2):

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
    Devuelve el minimo común múltiplo
    """
    mcm = 1
    dicFact1, dicFact2 = dicFact(numero1, numero2)
    for factor in dicFact1 | dicFact2:
        mcm *= factor ** max(dicFact1[factor], dicFact2[factor])
    return mcm
        
        
        
import doctest
doctest.testmod()


