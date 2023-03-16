import doctest

#DEFINICIÓN de Número Primo:
#Número entero que solamente es divisible por él mismo y por la unidad (1)
#############################################################################
def esPrimo (numero):
    """
    Devuelve True si su argumento es primo, y False si no lo es
    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    if numero < 2: 
        return False
    else:
        for aux in range(2,numero):
            if numero % aux == 0:
                return False
        return True

#############################################################################
def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    tupla_primos = tuple([item for item in range(numero) if esPrimo(item)])
    return tupla_primos

#############################################################################
def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    # he intentado hacerlo usando en vez de range(2,numero+1), 
    # la tupla con los primos hasta numero primos(numero),
    # Pero me ocupaba mucho tiempo de cálculo y nunca me llegaba a terminar.
 
    factors = []
    for i in range(2,numero+1):
        while numero % i == 0:
            factors.append(i)
            numero //= i
        if numero < 2:
            break
    return tuple(factors)


#############################################################################
def mcd_eucleides(numero1, numero2): #mcd con algoritmo de euclides
    if numero1*numero2 == 0: 
        return 0
    elif int(numero1)!= numero1 or int(numero2)!= numero2:
        print("No se admiten valores NO enteros")
    elif (numero1 or numero2) < 0  :
        return 1
    else:
        while numero1 != numero2:
            if numero1 > numero2:
                numero1 -= numero2
            else:
                numero2-=numero1
        return numero1

#############################################################################
def n_veces_lista (lista):
    cont =[]
    for i in set(lista):
            c= lista.count(i)
            cont.append([i,c])
    return cont

#############################################################################
def mcm (numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcm(90, 14)
    630
    """
    desc1 = descompon(numero1)
    desc2 = descompon(numero2)
    primos_cont1 = n_veces_lista(desc1)
    primos_cont2 = n_veces_lista(desc2)

    resultat = 1
    for i in range(0, len(primos_cont1)):

        if primos_cont1[i][0] not in set(desc2):
            resultat*= (primos_cont1[i][0]**primos_cont1[i][1])

        for y in range(0, len(primos_cont2)):

            if primos_cont1[i][0] == primos_cont2[y][0]:
                
                if primos_cont1[i][1] > primos_cont2[y][1]:
                    resultat *= (primos_cont1[i][0]**primos_cont1[i][1])
                else:
                    resultat *= (primos_cont1[y][0]**primos_cont1[y][1])
    
    for y in range(0,len(primos_cont2)):
        if primos_cont2[y][0] not in set(desc1):
            resultat *= (primos_cont2[y][0]**primos_cont2[y][1])
                
            
    return resultat

#############################################################################
def mcd (numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcd(924, 780)
    12
    """
    # Caso de que alguno de los dos valores sea 0:
    if numero1*numero2 == 0: 
        return 0 # mcd = 0
        
    
    #caso valores no enteros:
    elif int(numero1)!= numero1 or int(numero2)!= numero2: 
        print("No se admiten valores NO enteros")
        return 0
    
    #caso valores negativos:
    elif (numero1 or numero2) < 0 : 
        return 1
    
    #Otros casos:
    else:
        #listas con los primos repetidos en la descomposición del otro numero
        primos_aux =[item for item in descompon(numero1) if item in descompon(numero2)]
        primos_aux2 =[item for item in descompon(numero2) if item in descompon(numero1)]
        
        #lista de listas con valores [[n_primo, n_veces que aparece],[n_primo2, n_veces que aparece2],...]
        primos_cont1 = n_veces_lista(primos_aux)
        primos_cont2 = n_veces_lista(primos_aux2)

        resultat = 1
        for i in range(0, len(primos_cont1)):
            if primos_cont1[i][1] < primos_cont2[i][1]: 
                resultat *= (primos_cont1[i][0]**primos_cont1[i][1])
            else:
                resultat *= (primos_cont2[i][0]**primos_cont2[i][1])

        return resultat
#############################################################################
def mcmN (*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcmN(42, 60, 70, 63)
    1260
    """
    factor_dict = {}
    for num in numeros:
        for factor, count in n_veces_lista(descompon(num)):
            factor_dict[factor] = max(factor_dict.get(factor, 0), count)
    mcm = 1
    for factor, count in factor_dict.items():
        mcm *= factor ** count
    return mcm

#############################################################################
def mcdN (*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcdN(820, 630, 1050, 1470)
    10
    """
    factor_dict = {}
    for num in numeros:
        num_factor_dict = n_veces_lista(descompon(num))
        for factor, count in num_factor_dict:
            if factor not in factor_dict:
                factor_dict[factor] = [count]
            else:
                factor_dict[factor].append(count)
            #print(factor_dict)

    mcd = 1
    for factor, counts in factor_dict.items():
        if len(counts) == len(numeros):
            mcd *= factor ** min(counts)
    #print(factor_dict.items())
    return mcd

doctest.testmod()