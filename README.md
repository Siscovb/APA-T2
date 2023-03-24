# Segunda tarea de APA 2023: Manejo de números primos

## Nom i cognoms
Albert Giménez Arnal
## Fichero `primos.py`

- El alumno debe escribir el fichero `primos.py` que incorporará distintas funciones relacionadas con el manejo
  de los números primos.

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno y los tests unitarios
  de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido de la función, los
  argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el uso de los estándares marcados
  por PEP-8. También se valorará su eficiencia computacional.

### Determinación de la *primalidad* y descomposición de un número en factores primos

Incluya en el fichero `primos.py` las tres funciones siguientes:

- `esPrimo(numero)`   Devuelve `True` si su argumento es primo, y `False` si no lo es.
- `primos(numero)`    Devuelve una **tupla** con todos los números primos menores que su argumento.
- `descompon(numero)` Devuelve una **tupla** con la descomposición en factores primos de su argumento.

### Obtención del mínimo común múltiplo y el máximo común divisor

Usando las tres funciones del apartado anterior (y cualquier otra que considere conveniente añadir), escriba otras
dos que calculen el máximo común divisor y el mínimo común múltiplo de sus argumentos:

- `mcm(numero1, numero2)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(numero1, numero2)`:  Devuelve el máximo común divisor de sus argumentos.

Estas dos funciones deben cumplir las condiciones siguientes:

- Aunque se trate de una solución sub-óptima, en ambos casos deberá partirse de la descomposición en factores
  primos de los argumentos usando las funciones del apartado anterior.

- Aunque también sea sub-óptimo desde el punto de vista de la programación, ninguna de las dos funciones puede
  depender de la otra; cada una debe programarse por separado.

### Obtención del mínimo común múltiplo y el máximo común divisor para un número arbitrario de argumentos

Escriba las funciones `mcmN()` y `mcdN()`, que calculan el mínimo común múltiplo y el máximo común divisor para un
número arbitrario de argumentos:

- `mcmN(*numeros)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcdN(*numeros)`:  Devuelve el máximo común divisor de sus argumentos.

### Tests unitarios

La cadena de documentación del fichero debe incluir los tests unitarios de las cinco funciones. En concreto, deberán
comprobarse las siguientes condiciones:

- `esPrimo(numero)`:  Al ejecutar `[ numero for numero in range(2, 50) if esPrimo(numero) ]`, la salida debe ser
                      `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]`.
- `primos(numeor)`: Al ejecutar `primos(50)`, la salida debe ser `(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)`.
- `descompon(numero)`: Al ejecutar `descompon(36 * 175 * 143)`, la salida debe ser `(2, 2, 3, 3, 5, 5, 7, 11, 13)`.
- `mcm(num1, num2)`: Al ejecutar `mcm(90, 14)`, la salida debe ser `630`.
- `mcd(num1, num2)`: Al ejecutar `mcd(924, 780)`, la salida debe ser `12`.
- `mcmN(numeros)`: Al ejecutar `mcmN(42, 60, 70, 63)`, la salida debe ser `1260`.
- `mcdN(numeros)`: Al ejecutar `mcdN(840, 630, 1050, 1470)`, la salida debe ser `210`.

### Entrega

#### Ejecución de los tests unitarios

Inserte a continuación una captura de pantalla que muestre el resultado de ejecutar el fichero `primos.py` con la opción
*verbosa*, de manera que se muestre el resultado de la ejecución de los tests unitarios.

<img src="Captura1.PNG" width="480" align="center">


La ejecución del test unitario para la función descompon se ha ejecutado con números más sencillos ya que mi PC no podía con un número tan grande

#### Código desarrollado

Inserte a continuación el contenido del fichero `primos.py` usando los comandos necesarios para que se realice el
realce sintáctico en Python del mismo.

```python
"""Albert Giménez Arnal

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




```
#### Subida del resultado al repositorio GitHub ¿y *pull-request*?

El fichero `primos.py`, la imagen con la ejecución de los tests unitarios y este mismo fichero, `README.md`, deberán
subirse al repositorio GitHub mediante la orden `git push`. Si los profesores de la asignatura consiguen montar el
sistema a tiempo, la entrega se formalizará realizando un *pull-request* al propietario del repositorio original.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y visualizarse correctamente en el repositorio,
incluyendo la imagen con la ejecución de los tests unitarios y el realce sintáctico del código fuente insertado.
