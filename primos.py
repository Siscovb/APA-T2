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

>>> mcd(924,780)
12

>>> mcmN(42, 60, 70, 63)
1260

>>> mcdN(840, 630, 1050, 1470)
210

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
    
    salida = tuple()
    for proba in primos(numero+1):
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


def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor
    """
    mcd = 1
    dicFact1, dicFact2 = dicFact(numero1, numero2)
    for factor in dicFact1 | dicFact2:
        mcd *= factor ** min(dicFact1[factor], dicFact2[factor])
    return mcd
        
        
def dicFactN(*numeros):
    """
    Devuelve una lista de diccionarios, con todos los posibles números primos descompuestos de todos los números pasados como argumento, y sus exponentes
    """

    i=0
    conjDesc = set()
    listaD = list()
    for num in numeros:
        conjDesc = conjDesc | set(descompon(num))
    while i < len(numeros):
        dicFact1 = {factor:0 for factor in list(conjDesc)} 
        for factor in descompon(numeros[i]): dicFact1[factor] += 1
        listaD.append(dicFact1)
        i += 1
    return listaD


def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    """
     
    listaDeDic = dicFactN(*numeros)
    mcmN = 1
    for factor in listaDeDic[0].keys():
        maxi = 0
        i=0
        while i < len(listaDeDic):
            if listaDeDic[i][factor] > maxi:
                maxi = listaDeDic[i][factor]
            i+=1
        mcmN *= factor ** maxi  
    return mcmN


def mcdN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    """

    listaDeDic = dicFactN(*numeros)
    mcdN = 1
    min = 999
    for factor in listaDeDic[0].keys():
        chek = False
        i=0
        while i < len(listaDeDic):
            if listaDeDic[i][factor] == 0:
                chek = True
                break
            if listaDeDic[i][factor] < min:
                min = listaDeDic[i][factor]
            i+=1
        if chek != True : mcdN *= factor ** min 
    return mcdN



import doctest
doctest.testmod()


