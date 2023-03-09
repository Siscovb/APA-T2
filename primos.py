"""
Kirian Rodríguez Alonso

Módulo de gestión de números primos

Exemples: 
 [ numero for numero in range(2, 50) if esPrimo(numero) ]
La salida debe ser [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47].

 primos(50)
La salida debe ser (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47) 

 descompon(36 * 175 * 143)
La salida debe ser (2, 2, 3, 3, 5, 5, 7, 11, 13).


Al ejecutar mcm(90, 14), la salida debe ser 630.
Al ejecutar mcd(924, 780), la salida debe ser 12.
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
    Devuelve una tupla con la descomposicion en factores primos de su argumento
    """

    factores=tuple()
    for factor in primos(numero+1):
        while numero%factor==0:
            numero=numero//factor
            factores=factores+(factor,)
    return factores



def fact2dic(numero1, numero2):
    
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores = set(factores1) | set(factores2)
    "comprensiones -> {exprKey : exprVal for elemento in iterable if condicion}"
    dic1 = {factor: 0 for factor in factores}
    dic2 = {factor: 0 for factor in factores}
    
    for factor in factores1: 
        dic1[factor] += 1

    for factor in factores2: 
        dic2[factor] += 1
    
    return dic1, dic2

def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    """

    dic1, dic2 = fact2dic(numero1,numero2)
    mcm = 1
    for factor in dic1:
        mcm *= factor**max(dic1[factor], dic2[factor])
    return mcm






def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    """



import doctest
doctest.testmod()