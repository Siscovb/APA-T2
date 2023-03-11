"""
Alexandr Ramos
"""

def es_primo(numero):
    """
    Devuelve True si su argumento es primo, y False si no lo es.

    >>> [ numero for numero in range(2, 50) if es_primo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    #Busca divisors amb residu 0 entre els valors 2 i nuermo*sqrt(2)
    for prueba in range(2, int(numero**0.5)+1):     
        if numero % prueba == 0: return False

    return True    


def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    # Aplico una "comprehension" per generar una tupla valorant es_primo(valor)
    return tuple([valor for valor in range(2, numero) if es_primo(valor)])


def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    factores = []

    #Sempre que sigui divisible amb residu 0, s'afegeix a la tupla
    for factor in primos(numero):
        while numero%factor == 0:
            factores.append(factor)
            numero //= factor
    return tuple(factores)


def __diccionari_de_factors_privat(numero1, numero2):
    """
    Clase privada que genera 2 diccionaris que relaciona quants factors n'hi ha de cada.
    """
    # Em paso tots els possibles factors en un sol conjunt factors
    factors_1 = descompon(numero1)
    factors_2 = descompon(numero2)
    factors = set(factors_1 + factors_2)

    # Genero 2 dicionaris amb cada possible factor com a clau i vegades a multiplicar com a valor
    diccionari_factors_1 = {factor:0 for factor in factors}
    diccionari_factors_2 = {factor:0 for factor in factors}
    for factor in factors_1: diccionari_factors_1[factor] += 1
    for factor in factors_2: diccionari_factors_2[factor] += 1
    return diccionari_factors_1, diccionari_factors_2


def mcm(numero1, numero2):
    """"
    Devuelve el mínimo común múltiplo de sus argumentos
    >>> mcm(90, 14)
    630
    """
    mcm = 1
    diccionari_factors_1, diccionari_factors_2 = __diccionari_de_factors_privat(numero1, numero2)
    
    # Multimplique els factors elevats al maxim de la seva aparició per factor.
    for factor in diccionari_factors_1 | diccionari_factors_2:
        mcm *= factor ** max(diccionari_factors_1[factor], diccionari_factors_2[factor])
    return mcm


def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    >>> mcd(924, 780)
    12
    """
    mcd = 1
    diccionari_factors_1, diccionari_factors_2 = __diccionari_de_factors_privat(numero1, numero2)

    # Multipliquem els factors elevats al minim de la seva aparició
    for factor in diccionari_factors_1 | diccionari_factors_2:
        mcd *= factor ** min(diccionari_factors_1[factor], diccionari_factors_2[factor])
    return mcd


import doctest
doctest.testmod()