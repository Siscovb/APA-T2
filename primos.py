""""
PAU PERÁLVAREZ CASASAMPERE

"""


def esPrimo(numero):
    """
    Devuelve **True** si su argumento es primo, 
    y False si no lo es.

    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    """
    for prueba in range(2, int(numero ** 0.5) + 1):                             
        if numero % prueba == 0: return False

    return True 


def primos(numero):
    """
    Devuelve una **tupla** con todos los números primos 
    menores que su argumento.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

    """
    return tuple([ prueba for prueba in range(2, 50) if esPrimo(prueba) ])


def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores 
    primos de su argumento.

    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)

    """
    resultado = []

    for i in primos(numero):
        while numero % i == 0:
            resultado.append(i)
            numero //= i

    return tuple(resultado)


# from collections import Counter as C  


# def mcm(numero1, numero2):
#     """
#     Devuelve el mínimo común múltiplo de sus argumentos.

#     >>> mcm(90, 14)
#     630

#     """
#     numero1D = C(descompon(numero1))
#     numero2D = C(descompon(numero2))

#     #Combinamos las descomposiciones factoriales en un solo 'diccionario' 
#     #(contador). 
#     #En caso de igualdad nos quedamos con el exponente más grande
#     factoritzacion = numero1D | numero2D  

#     mcm = 1 
#     for factor, exp in factoritzacion.items():
#         mcm *= (factor**exp)

#     return mcm


# def mcd(numero1, numero2):
#     """
#     Devuelve el máximo común divisor de sus argumentos.

#     >>> mcd(924, 780)
#     12

#     """
#     numero1D = C(descompon(numero1))
#     numero2D = C(descompon(numero2))

#     #Combinamos las descomposiciones factoriales en un solo contador. 
#     #En caso de igualdad nos quedamos con el exponente más pequeño
#     factoritzacion = numero1D & numero2D  

#     mcd = 1 
#     for factor, exp in factoritzacion.items():
#         mcd *= (factor**exp)

#     return mcd


#MÈTODE SENSE BIBLIOTECA COUNTER:


def dicFact(numero1,numero2):
    """
    Devuelve el factor primo de un número con su correspondiente exponente. 
    La función tiene como argumento dos números.

    >>> dicFact(90,14)
    ({2: 1, 3: 2, 5: 1, 7: 0}, {2: 1, 3: 0, 5: 0, 7: 1})
    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)

    factores = set(factores1 + factores2)  # conjunto, ya que son números únicos
    dicfact1 ={factor : 0 for factor in factores } 
    dicfact2 ={factor : 0 for factor in factores} 
    for factor in factores1 : dicfact1[factor] += 1
    for factor in factores2 : dicfact2[factor] += 1
  
    return dicfact1, dicfact2
    

def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    La función tiene como argumento dos números.

    >>> mcm(90, 14)
    630
    """
    mcm = 1
    dicFact1, dicFact2 = dicFact(numero1, numero2)
    for factor in  dicFact1 | dicFact2:
        mcm *= factor ** max(dicFact1[factor], dicFact2[factor])
    return mcm
    

def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    La función tiene como argumento dos números.

    >>> mcd(924, 780)
    12
    """
    mcd = 1
    dicFact1, dicFact2 = dicFact(numero1, numero2)
    for factor in  dicFact1 | dicFact2:
        mcd *= factor ** min(dicFact1[factor], dicFact2[factor])
    return mcd


def dicFactN(*numeros):
    """
    Devuelve el factor primo de un número con su 
    correspondiente exponente. 

    >>> dicFactN(12, 18, 20)
    {12: {2: 2, 3: 1}, 18: {2: 1, 3: 2}, 20: {2: 2, 5: 1}}
    """
    diccionario = {}

    for numero in numeros:
        factores = descompon(numero)
        dicfact = {factor : 0 for factor in factores } 
        for factor in factores : dicfact[factor] += 1
        diccionario[numero] = dicfact
    return diccionario

def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.

    >>> mcmN(42, 60, 70, 63)
    1260
    """
    #Obtenim el diccionari de factors primers per a cada un dels números
    diccionario = dicFactN(*numeros)
    mcm = 1

    #Iterem sobre un conjunt que conté la unió/tots els factors primers
    #dels numeros que ens han donat a la entrada.
    #Ena primera iteració, es busca el exponent màxim en cada número de 
    #l'entrada per el primer factor primer

    for factor in set().union(*diccionario.values()):
        max_exp = 0
        for num in diccionario:
            if factor in diccionario[num]:
                max_exp = max(max_exp, diccionario[num][factor])
        mcm *= factor ** max_exp
    return mcm

    #POSSIBLE SOLUCIÓ UTILITZANT LA FUNCIÓ MCM CREADA ANTERIORMENT:

    # mcm_total = 1
    # for numero in numeros:
    #     mcm_total = mcm(mcm_total, numero)
    # return mcm_total


def mcdN(*numeros):
    """
    Devuelve el máximo común divisor de sus argumentos.

    >>> mcdN(820, 630, 1050, 1470)
    10
    """
    #Obtenim el diccionari de factors primers per a cada un dels números
    diccionario = dicFactN(*numeros)   

    #s'obtenen els factors primers per al primer numero de la llista numeros  
    factores_comunes = set(diccionario[numeros[0]].keys())      
    
    #Recorrem el diccionari per buscar els valors comuns (interseccions))
    for dic in diccionario.values():
        factores_comunes = factores_comunes.intersection(set(dic.keys()))
    mcd = 1

    #Elevem cada factor comu a l'exponent més petit
    for factor in factores_comunes:
        exponentes = [dic[factor] for dic in diccionario.values()]
        mcd *= pow(factor, min(exponentes))
    return mcd


import doctest
doctest.testmod()

