"""
Arnau Montiel Morales

Modulo de gestión de números primos

Exemples: 
>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90,14)
630

>>> mcd(924,780)
12

>>> mcmN(42,60,70,63)
1260

>>> mcdN(840,630,1050,1470)
210

"""

def esPrimo(numero):
    """
     Devuelve True si su argumento es primo, y False si no lo es.
    """

    for prova in range(2,int(numero**0.5+1)):
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
    Devuelve una **tupla** con la descomposicion en factores primos.
    """
    factores= tuple()
    for factor in primos(numero+1):
        while numero % factor == 0:
            numero = numero // factor
            factores= factores + (factor,)

    return factores

def fact2dic(numero1,numero2):
    """
    Crea dos diccionarios,cada uno para su argumento ,con los valores del factor y el exponente. ej: 12={2:2,3:1}  2*2*3*1=12
    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores = set(factores1) | set(factores2) #tupla  a 2 conjuntos 
    
    dic1= {factor : 0 for factor in factores}
    dic2={factor : 0 for factor in factores}
    for factor in factores1:
        dic1[factor]+=1
        
        
    for factor in factores2:
        dic2[factor]+=1 
        
    return dic1, dic2

def mcm(numero1,numero2):
    """
    Devuelve minimo común múltiplo de sus argumentos.
    """
    dic1, dic2= fact2dic(numero1,numero2)
    mcm = 1 
    for factor in dic1:
        mcm *= factor** max(dic1[factor],dic2[factor]) #mcm*
    return mcm

def mcd(numero1,numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    """
    dic1, dic2= fact2dic(numero1,numero2)
    mcd = 1 
    for factor in dic2:
        mcd *= factor ** min(dic1[factor],dic2[factor])
    return mcd
    
def fact2dicN(numero):
    """
    Crea dos diccionarios,cada uno para su argumento ,con los valores del factor y el exponente. ej: 12={2:2,3:1}  2*2*3*1=12
    """
    factoresN = descompon(numero)
    ##factores2 = descompon(numero2)
    factores = set(factoresN) #tupla  a 2 conjuntos 
    
    dic1= {factor : 0 for factor in factores}
    ##dic2={factor : 0 for factor in factores}
    for factor in factoresN:
        dic1[factor]+=1
        
        
    ##for factor in factores2:
       ## dic2[factor]+=1 
        
    return dic1##, dic2


def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos para un numeros arbitrario de argumentos.
    """
    
    lista_dic=[]
    
    for factor in range(0,len(numeros)):
             
       N= numeros[factor] 
       dic1 = fact2dicN(N)
       
       lista_dic.append(dic1)  
       
    mcm = 1 
    mcm2 = 1 
    mcm1 = 1
    mcm3 = 1 
    mcm4 = 1 
    iterador= iter(lista_dic)
    dic1 = next(iterador)                
    ##print(dic1)
    dic2 = next(iterador)
    ##print(dic2)
    dic3 = next(iterador)
    ##print(dic3)
    dic4 = next(iterador)
    ##print(dic4)
  
    for factor in dic1:
      
      mcm1*= factor** max(dic1.values()) #mcm*
      mcm2*= factor** max(dic2.values())
      mcm3*= factor** max(dic3.values())
      mcm4*= factor** max(dic4.values())
      
      mcm = mcm1+ mcm2 +mcm3+ mcm4
    return mcm


def mcdN(*numeros):
    """
    Devuelve el máximo común divisor de sus argumentos para un numeros arbitrario de argumentos.
    """
    lista_dic=[]
    
    for factor in range(0,len(numeros)):
             
       N= numeros[factor] 
       dic1 = fact2dicN(N)
       
       lista_dic.append(dic1)  
       
    mcm = 1 
    mcm2 = 1 
    mcm1=1
    mcm3 = 1 
    mcm4 = 1 
    iterador= iter(lista_dic)
    dic1 = next(iterador)
                     
    ##print(dic1)
    
    dic2 = next(iterador)
    ##print(dic2)
    dic3 = next(iterador)
    ##print(dic3)
    dic4 = next(iterador)
    ##print(dic4)
  
    for factor in dic1:
      
      mcm1*= factor** min(dic1.values()) #mcm*
      mcm2*= factor** min(dic2.values())
      mcm3*= factor** min(dic3.values())
      mcm4*= factor** min(dic4.values())
      
      mcm = mcm1+ mcm2 +mcm3+ mcm4
    return mcm


import doctest
doctest.testmod()