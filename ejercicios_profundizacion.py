#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Ezequiel Alarcon"
__email__ = "zekalarcon@gmail.com"


# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('Comenzamos a ponernos serios!')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuente cuantos números ingresados hay, y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''
    # inicio = ....
    # fin = ....

    # cantidad_numeros ....
    # sumatoria ....

    # bucle.....

    # Al terminar el bucle calcular el promedio como:
    # promedio = sumatoria / cantidad_numeros

    # Imprimir resultado en pantalla
    
    inicio = int(input('Ingrese primer numero:\n'))
    fin = int(input('Ingrese ultimo numero:\n'))
    
    cantidad_num = []
    contador = 0 

    for i in range(inicio, fin + 1):
        cantidad_num.append(i)
        num_len = len(cantidad_num)
        contador += i
    print(f'La cantidad de numeros entre el rango {inicio} y {fin} es: {num_len}')
    print(f'La suma total de los numeros dentro del rango {inicio} y {fin} es: {contador}')

   

def ej2():

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa

    Se debe debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''
    while True:
        print("Mi Calculadora (^_^)")
        print('Ingrese dos numeros para realizar las siguientes operaciones:')

        num_1 = int(input('Ingrese primer numero:\n'))
        num_2 = int(input('Ingrese segundo numero:\n'))
    
        print(
            '-Ingrese el simbolo (+) para suma\n'
            '-Ingrese el simbolo (-) para resta\n'
            '-Ingrese el simbolo (*) para multiplicacion\n'
            '-Ingrese el simbolo (/) para division\n'
            '-Ingrese el simbolo (**) para exponente/potencia\n'
            '-Escriba (FIN) en simbolo para terminar programa'
        )

        simbolo = str(input('Ingrese simbolo:\n'))
    
        if simbolo == '+':
            suma = num_1 + num_2
            print(f'La suma entre {num_1} y {num_2} es: {suma}')
        elif simbolo == '-':
            resta = num_1 - num_2
            print(f'La resta entre {num_1} y {num_2} es: {resta}')
        elif simbolo == '*':
            multiplicacion = num_1 * num_2
            print(f'La multiplicacion entre {num_1} y {num_2} es: {multiplicacion}')
        elif simbolo == '/':
            division = num_1 / num_2
            print(f'La division entre {num_1} y {num_2} es: {division}')
        elif simbolo == '**':
            potencia = num_1 ** num_2
            print(f'La potencia entre {num_1} y {num_2} es: {potencia}')
        elif simbolo == 'FIN':
            print('Mi Calculadora (^_^) terminada')
            break    
        else:
            print('El simbolo ingresado es incorrecto')


def ej3():
    print("Mi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_clase / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudinte se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe caluclar el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_clase / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''
    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable

    # Realice aquí el bucle para recorrer todas las notas
    # y cacular la sumatoria

    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas

    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado

    # Imprima en pantalla al cantidad de ausentes
    
    suma = 0

    for i in notas:
        suma += i
    promedio = suma / len(notas)

    if promedio >= 90:
        print(f'Al promedio del alumno: {promedio:.0f} Le corresponde la calificacion: A')
    elif promedio >= 80:
        print(f'Al promedio del alumno: {promedio:.0f} Le corresponde la calificacion: B')
    elif promedio >= 70:
        print(f'Al promedio del alumno: {promedio:.0f} Le corresponde la calificacion: C')
    elif promedio >= 60:
        print(f'Al promedio del alumno: {promedio:.0f} Le corresponde la calificacion: D')
    elif promedio < 60:
        print(f'Al promedio del alumno: {promedio:.0f} Le corresponde la calificacion: F')  
    
    
    validas = []
    ausentes = []
    
    for nota in notas:
        if nota > 0:
            validas.append(nota)
            validas_len = len(validas)
        elif nota < 0:
            ausentes.append(nota)
            ausentes_len = len(ausentes)
                
    print(f'Notas validas: {validas_len}')
    print(f'Alumno ausente: {ausentes_len}')
     


def ej4():
    print("Mi primer pasito en data analytics")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica /ej5>,
    copielo a este ejercicio y modifíquelo para cumplir el
    siguiente requerimiento

    En este ejercicio se lo provee de una lista de temperatuas,
    esa lista de temperatuas corresponde a los valores de temperaturas
    tomados durante una temperorada del año en Buenos Aires.
    Ustede deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo

    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados

    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperatuas

    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted.
    
    NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
    el máximo y el mínimo utilizando los mismos métodos vistos
    durante la clase (ejemplos_clase)
    '''

    temperatura_max = None      # Aquí debe ir almacenando la temp máxima
    temperatura_min = None      # Aquí debe ir almacenando la temp mínima
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
    temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

    # Colocar el bucle aqui......

    for temp in temp_dataloger:
        if temperatura_max is None or temp > temperatura_max:
            temperatura_max = temp
        elif temperatura_min is None or temp < temperatura_min:
            temperatura_min = temp

    for i in temp_dataloger:
        temperatura_sumatoria += i        
    temperatura_promedio = temperatura_sumatoria / len(temp_dataloger)

    print(f'Temperatura maxima: {temperatura_max}')        
    print(f'Temperatura minima: {temperatura_min}')
    print(f'La suma de todas las temperaturas es: {temperatura_sumatoria:.1f}')    # Aca si dejo todos los decimales 
    print(f'El promedio de las temperaturas dadas es: {temperatura_promedio:.1f}') # me da igual que la funcion sum()

   
    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp

    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp


    print('Corroborando resultados anteriores con funciones max(), min(), sum()')
    print(max(temp_dataloger))
    print(min(temp_dataloger))
    print(sum(temp_dataloger))

    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:

    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 24
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24

    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''

    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo
    
    if temperatura_min >= 19 and temperatura_max <= 28:
        print(f'Temperatura minima {temperatura_min}, temperatura maxima {temperatura_max}, Estacion verano')
    elif temperatura_min >= 11 and temperatura_max < 24:
        print(f'Temperatura minima {temperatura_min}, temperatura maxima {temperatura_max}, Estacion otoño')
    elif temperatura_min >= 8 and temperatura_max <= 14:
        print(f'Temperatura minima {temperatura_min}, temperatura maxima {temperatura_max}, Estacion invierno')
    elif temperatura_min >= 10 and temperatura_max <= 24: 
        print(f'Temperatura minima {temperatura_min}, temperatura maxima {temperatura_max}, Estacion primavera')     



def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Obtener la palabra más grande por orden alfabético (usando el operador ">")
    2 - Obtener la palabra más grande por cantidad de letras (longitud de la palabra)
    3 - Salir del programa

    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)

    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:

    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?
    
    NOTA: No se debe ordenar la lista de palabras, se debe obtener
    el máximo utilizando el mismos métodos vistos durante la clase
    (ejemplos_clase), tal como el ejercicio anterior. Ordenar una
    lista representa un problema mucho más complejo que solo
    buscar el máximo.

    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")

  '''
    
    lista_palabras = []
    palabra_maxima = None
    palabra_len = None
    
    while True:
        print('Ingrese 5 palabras y elija una opcion para ver el resultado:\n')
        print(
            '- Ingrese 1 para obtener la palabra más grande por orden alfabético\n'
            '- Ingrese 2 para obtener la palabra más grande por cantidad de letras\n'
            '- Ingrese 3 para salir del programa\n'
        )

        opcion = int(input('Elija una opcion:\n'))

        if opcion == 3:
            print('Programa terminado')
            break
        if opcion > 3:
            print('Opcion incorrecta')
            continue
          
        
        while len(lista_palabras) < 5:
            palabra = str(input('Ingrese palabras cualesquiera\n'))
            lista_palabras.append(palabra)

        if opcion == 1:    
            for palabra in lista_palabras:
                if palabra_maxima is None or palabra > palabra_maxima:
                    palabra_maxima = palabra
                lista_palabras =[]    
            print(f'La palabra mayor alfabeticamente es: {palabra_maxima}')

        if opcion == 2:
            for palabra in lista_palabras:
                if palabra_len is None or len(palabra) > palabra_len:
                    palabra_len = len(palabra)
                    palabra_larga = palabra
                lista_palabras = []    
            print(f'La palabra mas larga {palabra_larga} contiene {palabra_len} letras')
            
         

        








if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
