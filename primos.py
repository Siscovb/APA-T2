"""
Joan Marc Fuentes Soler 

Practica 2: Modulo de gestión de numeros primos

"""

def esPrimo(numero):
    """
    Devuelve True si su argumento es primo y False si no lo es.
    >>> [numero for numero in range(2,50) if esPrimo(numero)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    for prueba in range(2,int(numero**0.5+1)):
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
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    >>> descompon(36 * 175 * 143) 
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    factores = tuple()
    for factor in primos(numero+1):
        while numero % factor == 0 :
            numero = numero / factor
            factores = factores + (factor,)
    return factores

def fact2dic(numero1,numero2):

    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores = set(factores1) | set(factores2)
    dic1 = {factor:0 for factor in factores}
    dic2 = {factor:0 for factor in factores}
    for factor in factores1:
        dic1[factor] += 1
    for factor in factores2:
        dic2[factor] += 1
    return dic1,dic2

def mcm(numero1,numero2): 
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcm(90, 14)
    630
    """
    dic1,dic2 = fact2dic(numero1,numero2)
    mcm = 1
    for factor in dic1:
        mcm *= factor**max(dic1[factor],dic2[factor])
    return mcm

def mcd(numero1,numero2): 
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcd(924, 780)
    12
    """
    dic1,dic2 = fact2dic(numero1,numero2)
    mcd = 1
    for factor in dic1:
        mcd *= factor**min(dic1[factor],dic2[factor])
    return mcd


def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de los numeros dados en la funcion
    >>> mcmN(42, 60, 70, 63)
    1260
    """
    descompon_, lista = (), []
    resultado = 1
    for i in range(len(numeros)):
        descompon_ += (descompon(numeros[i]), )
        for j in descompon(numeros[i]):
            lista.append(j)
    valores_lista = set(lista)
    valores_total = {item:0 for item in valores_lista}
    for i in range(len(numeros)):
        valores = {item:0 for item in valores_lista}
        for n in descompon_[i]:
            valores[n] += 1
        for n in valores_lista:
            if(valores_total[n] < valores[n]):
                valores_total[n] = valores[n]  
    for n in valores_lista:
        resultado *= n**valores_total[n]
    return resultado

def mcdN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    descompon_, lista = (), []
    resultado = 1    
    for i in range(len(numeros)):
        descompon_ += (descompon(numeros[i]), )
        for j in descompon(numeros[i]):
            lista.append(j)
    valores_lista = set(lista)
    valores_total = {item:0 for item in valores_lista}
    for i in descompon_[0]:
        valores_total[i] += 1
    for i in range(len(numeros)):
        valores = {item:0 for item in valores_lista}
        for n in descompon_[i]:
            valores[n] += 1
        for n in valores_lista:
            if(valores_total[n] > valores[n]):
                valores_total[n] = valores[n]  
    for n in valores_lista:
        resultado *= n**valores_total[n]
    return resultado

import doctest
doctest.testmod()