# Segunda tarea de APA 2023: Manejo de números primos

## Nom i cognoms Oriol Garcia Moreiras

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

### Tests unitarios

La cadena de documentación del fichero debe incluir los tests unitarios de las cinco funciones. En concreto, deberán
comprobarse las siguientes condiciones:

- `esPrimo(numero)`:  Al ejecutar `[ numero for numero in range(2, 50) if esPrimo(numero) ]`, la salida debe ser
                      `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]`.
- `primos(numeor)`: Al ejecutar `primos(50)`, la salida debe ser `(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)`.
- `descompon(numero)`: Al ejecutar `descompon(36 * 175 * 143)`, la salida debe ser `(2, 2, 3, 3, 5, 5, 7, 11, 13)`.
- `mcm(num1, num2)`: Al ejecutar `mcm(90, 14)`, la salida debe ser `630`.
- `mcd(num1, num2)`: Al ejecutar `mcd(924, 780)`, la salida debe ser `12`.

### Entrega

#### Ejecución de los tests unitarios

Inserte a continuación una captura de pantalla que muestre el resultado de ejecutar el fichero `primos.py` con la opción
*verbosa*, de manera que se muestre el resultado de la ejecución de los tests unitarios.

<img src="img/tests_unitarios.png" width="450" align="center">

#### Código desarrollado

Inserte a continuación el contenido del fichero `primos.py` usando los comandos necesarios para que se realice el realce sintáctico en Python del mismo.

**CÓDIGO:**
-------

### _Tests unitarios:_
```c
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
```

### _Función esPrimo:_
Devuelve True si su argumento es primo y False si no lo es.
```c
def esPrimo(numero):
     for proba in range(2, int (numero**0.5 + 1)):
        if numero % proba == 0:
            return False
    return True
```

### _Función primos:_
Devuelve una tupla con todos los números primos menores que su argumento.
```c
def primos(numero):
    return tuple ([proba for proba in range(2, numero) if esPrimo(proba)])
```

### _Función descompon:_
Devuelve una tupla con la descomposición en factores primos de su argumento.
```c
def descompon(numero):
    factores = tuple()
    for factor in primos(numero + 1):
        while numero%factor == 0:
            numero = numero/factor
            factores = factores + (factor,)

    return factores
```

### _Función fact2dic:_
Devuelve la descomposición del numero1 (base) y numero2 (exponente).
```c
def fact2dic(numero1, numero2):
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores = set(factores1) | set(factores2)
    dic1 =  {factor : 0 for factor in factores}
    dic2 =  {factor : 0 for factor in factores}
    for factor in factores1: 
        dic1[factor] += 1

    for factor in factores2: 
        dic2[factor] += 1
    
    return dic1, dic2
```

### _Función mcm:_
Devuelve el maximo común múltiplo de sus argumentos.
```c
def mcm(numero1, numero2):
    dic1, dic2 = fact2dic(numero1, numero2)
    mcm = 1
    for factor in dic1:
        mcm *= factor**max(dic1[factor], dic2[factor])
    return mcm
```

### _Función mcd:_
Devuelve el mínimo común divisor de sus argumentos.
```c
def mcd(numero1, numero2):
    dic1, dic2 = fact2dic(numero1, numero2)
    mcd = 1
    for factor in dic1:
        mcd *= factor**min(dic1[factor], dic2[factor])
    return 
```

### _Función mcmN:_
Devuelve el maximo común múltiplo de sus argumentos.
```c
desc, lista = (), []
    total = 1
    for i in range(len(numeros)):
        desc += (descompon(numeros[i]), )
        for j in descompon(numeros[i]):
            lista.append(j)
    tots = set(lista)
    dic_total = {item:0 for item in tots}
    for i in range(len(numeros)):
        dic = {item:0 for item in tots}
        for num in desc[i]:
            dic[num] += 1
        for num in tots:
            if(dic_total[num] < dic[num]):
                dic_total[num] = dic[num]  
    for num in tots:
        total *= num**dic_total[num]
    return total
```

### _Función mcmD:_
Devuelve el maximo común divisor de sus argumentos.
```c
desc, lista = (), []
    total = 1    
    for i in range(len(numeros)):
        desc += (descompon(numeros[i]), )
        for j in descompon(numeros[i]):
            lista.append(j)
    tots = set(lista)
    dic_total = {item:0 for item in tots}
    for i in desc[0]:
        dic_total[i] += 1
    for i in range(len(numeros)):
        dic = {item:0 for item in tots}
        for num in desc[i]:
            dic[num] += 1
        for num in tots:
            if(dic_total[num] > dic[num]):
                dic_total[num] = dic[num]  
    for num in tots:
        total *= num**dic_total[num]
    return total
```


#### Subida del resultado al repositorio GitHub ¿y *pull-request*?

El fichero `primos.py`, la imagen con la ejecución de los tests unitarios y este mismo fichero, `README.md`, deberán
subirse al repositorio GitHub mediante la orden `git push`. Si los profesores de la asignatura consiguen montar el
sistema a tiempo, la entrega se formalizará realizando un *pull-request* al propietario del repositorio original.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y visualizarse correctamente en el repositorio,
incluyendo la imagen con la ejecución de los tests unitarios y el realce sintáctico del código fuente insertado.
