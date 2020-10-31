#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Alarcon Ezequiel"
__email__ = "zekalarcon@gmail.com"


condicion = False


def ej1():
    # Ejercicios con bucles "while"

    x = 0
    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea menor a 6>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" incremente "1" en cada iteración

    while x < 6:    # reemplace "condicion" por lo que crea necesario
        print("Valor de x =", x)
        # Coloque la línea de código para que "X" incremente "1"
        x = x + 1
    
    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea mayor o igual a 0>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" decremente "1" en cada iteración

    while x >= 0:    # reemplace "condicion" por lo que crea necesario
        print("Valor de x =", x)
        # Coloque la línea de código para que "X" decremente "1"
        x = x - 1


def ej2():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de colores, utilizar "for"
    # para imprimir en pantalla todos los colores
    colores = ['rojo', 'naranja', 'verde', 'azul']

    for i in colores:
        print(i)
    else:
        print('Loop terminado')    
        

    # Itere el "for" utilizando la lista como parámetro
    # y utilizar como elemento del "for" cada color
    # for color ...

    for color in colores:
        print(color)
    else:
        print('Loop terminado')    
               

    # Itere el "for" utilizando el tamaño de la lista
    # como parámetro y utilizar el índice para acceder a
    # los elementos de la lista
    # for i ...

    colores_len = len(colores)

    for i in range(colores_len):
        print(f'Indice: {i} Color: {colores[i]}')
        
        
        


def ej3():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de números, utilizar "for"
    # para recorrer toda la lista y realizar la sumatoria de todos los números
    # La sumatoria se deberá ir guardando en la variable "suma"
    numeros = [1, 5, -1, 6, 10, 2, -5]
    suma = 0   # Variable ya inicializada, la suma arranca en cero

    for num in numeros:
        suma += num
        print(f'Numero sumado: {num} Total: {suma}')


def ej4():
    # Ejercicios con bucles "while"

    x = 0
    # Realizar un bucle "while" cuya condición de continuidad
    # sea que <x sea menor a 10> y que <x sea distinto de 6>
    # Colocar ambas condiciones como condicion del "while" realizando
    # una condición compuesta (utilice el operador "and" o "or" según corresponda)
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print

    while x < 10 and x != 6:
        print(x)
        x += 2
    else:
        print(f'x={x} Loop terminado')    

    # Realice el mismo bucle "while" pero en vez de estar formado por una condición
    # compuesta, que el "while" siga iterando mientras <x sea menos a 10>, y dentro del
    # "while" consultar si <x es igual a 6>, y en ese caso realizar una interrupción del bucle
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print

    x = 0
    # Aca si dejo el valor anterior de <X = 6> no entra.
    # Lo puse en <0> para probar que pasaba.
    while x < 10:
        if x == 6:
            print(f'x = {x} Loop terminado')
            break
        else:
            print(x)
            x += 2



def ej5():
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y calcule la sumatoria total de todos los números dentro de esa secuencia
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior

    # fin....

    # for ... in range(....)

    # Imprimir el valor de la sumatoria

    inicio = int(input('Ingrese el primer número de la secuencia\n'))
    fin = int(input('Ingrese el ultimo número de la secuencia\n'))

    suma = 0

    for i in range(inicio, fin + 1):          # Si ubico el print dentro del bloque imprime
        suma += i                         # cada vez que recorre el rango
    print(f'La suma total de los numeros entre el rango {inicio} y {fin} es: {suma}')


def ej6():
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y cuente cuantes números son negativos y cuantos números son mayor o igual a cero
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior

    # fin....

    # Inicializo el contador en 0
    #cantidad_numeros_negativos

    # for ... in range(....)

    # Imprimir el valor de la cantidad de números positivos y negativos

    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    fin = int(input('Ingrese el ultimo número de la secuencia\n'))

    positivos = 0
    negativos = 0
    igual_cero = 0 

    for i in range(inicio, fin + 1):
        if i > 0:
            positivos += 1      # Aca si utilizo el print en cada caso me recorre 
        elif i < 0:            # todo el rango e imprimi uno por uno. 
            negativos += 1     # Por eso lo puse al final
        else:
            igual_cero += 1        
    print(f'Cantidad de numeros positivos entre el rango {inicio} y {fin}: {positivos}')
    print(f'Cantidad de numeros impares entre el rango {inicio} y {fin}: {negativos}')
    print(f'Cantidad de ceros entre el rango {inicio} y {fin}: {igual_cero}')


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
    #ej6()
