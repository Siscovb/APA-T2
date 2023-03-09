"""
Kirian Rodríguez Alonso

Módulo de gestión de números primos

Exemples: 
>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
La salida debe ser [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47].
"""

def esPrimo(numero):
    """
    Devuelve True si su argumento es primo y False si no lo es
    """
    for Prueba in range(2, numero):
        if numero % Prueba == 0 :
            return False
    return True




import doctest
doctest.testmod()