"""
Paula Puigdevall Tornero

Funciones para la gestion de Numeros primos.

Ejemplos:

>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12
"""

def esPrimo(numero):
    """
    Funció que retorna True si l'argument es primer i False si no ho es.
    """
    for prova in range(2, int(numero**0.5)+1):
        if numero % prova == 0:
            return False
    return True

def primos(numero):
    """
    Funció que retorna una tupla amb tots els nombres primers menors que el seu argument
    
    """
    return tuple([prova for prova in range(2, numero) if esPrimo(prova)])

def descompon(numero):
    """
    Funcio que retorna una tupla amb la descomposicio en factors primers del seu argument
    """
    factors = tuple()
    for num in primos(numero + 1):
        while numero % num == 0:
            numero = numero // num
            factors = factors + (num,)
    return factors

def fact2dic(numero1, numero2):
    factors1 = descompon(numero1)
    factors2 = descompon(numero2)
    factors = set(factors1 + factors2)
    #inicialitzem els diccionaris a 0 i anirem afegint en funció de quants cops aparegui
    dicFact1 = {factor: 0 for factor in factors}
    dicFact2 = {factor: 0 for factor in factors}
    for factor in factors1:
        dicFact1[factor] += 1
    for factor in factors2:
        dicFact2[factor] += 1
    return dicFact1, dicFact2

def mcm(numero1, numero2):
    """
    Retorna el mcm
    """
    dicFact1, dicFact2 = fact2dic(numero1, numero2)
    mcm = 1
    #el for ens recorre totes les claus en factor1
    for factor in dicFact1:
        #Agafem el màxim exponent (factor en el diccionari de factors) de cada numero
        mcm *= factor**max(dicFact1[factor], dicFact2[factor])
    return mcm

def mcd(numero1, numero2):
    """
    Retorna el mcd
    """
    dicFact1, dicFact2 = fact2dic(numero1, numero2)
    mcd = 1
    #el for ens recorre totes les claus en factor1
    for factor in dicFact1:
        #Agafem el màxim exponent (factor en el diccionari de factors) de cada numero
        mcd *= factor**min(dicFact1[factor], dicFact2[factor])
    return mcd

import doctest
doctest.testmod()
