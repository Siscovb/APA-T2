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

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcmN(42, 60, 70, 63)
1260

>>> mcdN(840, 630, 1050, 1470)
210
"""


def esPrimo(numero):
    """ 
     Devuelve True si su argumento es primo, y False si no lo es.
    """

    for prova in range(2, int (numero**0.5) + 1):
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

    factores = tuple()
    for factor in primos(numero + 1):
        while numero % factor == 0:
            numero = numero // factor
            factores = factores + (factor,) 
    
    return factores

def fact2dic(numero1, numero2):
    fact1 = descompon(numero1)
    fact2 = descompon(numero2)
    factores = set(fact1) | set(fact2) #convertir a conjunto
    #inicialitzem el diccionari a 0 i anem afegint en funció de quants cops aparegui el mateix factor
    dic1 = {factor : 0 for factor in factores}
    dic2 = {factor : 0 for factor in factores}
    for factor in fact1:
        dic1[factor] += 1
    
    for factor in fact2:
        dic2[factor] += 1

    return dic1, dic2

def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    """

    mcm = 1
    #establim a les variables dicFact1 i dicFact2, la descomposició dels dos valors
    dicFact1, dicFact2 = fact2dic(numero1, numero2)
    for factor in dicFact1:
        mcm *= factor**max(dicFact1[factor], dicFact2[factor])
    
    return mcm

def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    """
    
    mcd = 1
    #establim a les variables dicFact1 i dicFact2, la descomposició dels dos valors
    dicFact1, dicFact2 = fact2dic(numero1, numero2)
    for factor in dicFact1:
        mcd *= factor**min(dicFact1[factor], dicFact2[factor])
    
    return mcd

def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos
    """
    
    # Si es pasa nomès un número, el mcm és el mateix número
    if len(numeros) == 1:
        return numeros[0]
    
    #Iterem sobre els parells de números i calculem el mcm
    #Per cada iteració, reemplaçem el primero número per el mcm parcial
    mcm_actual = numeros[0]
    for i in range(1, len(numeros)):
        mcm_actual = mcm(mcm_actual, numeros[i])
    return mcm_actual

def mcdN(*numeros):
    """
    Devuelve el máximo común divisor de sus argumentos.
    """
    
    # Si es pasa nomès un número, el mcd és el mateix número
    if len(numeros) == 1:
        return numeros[0]
    
    mcd_actual = numeros[0]
    for i in range(1, len(numeros)):
        mcd_actual = mcd(mcd_actual, numeros[i])
    return mcd_actual

import doctest
doctest.testmod()
