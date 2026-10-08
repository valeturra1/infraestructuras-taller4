from concurrent.futures import ThreadPoolExecutor
import numpy as np
import time
import random

#Función que recibe los índices de la matriz en tuplas, los  desempaqueta y
# con dos fors recorre los rangos formados por los índices,
# acumulando cada valor en una variable que al final retorna
def sumarBloque(coordenadas):

    suma = 0

    numBloqueHorizontal, numBloqueVertical = coordenadas

    fila_inicio = numBloqueHorizontal*100
    fila_fin = (numBloqueHorizontal+1)*100

    columna_inicio = numBloqueVertical*100
    columna_fin = (numBloqueVertical+1)*100


    for i in range(fila_inicio, fila_fin):
        for j in range(columna_inicio, columna_fin):
            suma += matrix[i][j]




    return suma


#Función que recorre el arreglo de resultados y las acumula en una variable final que representa la suma
#de toda la matriz, retorna esta variable
def sumaTotal():
    suma = 0
    for number in resultados:
        suma += number
    return suma

#Implementación secuencial de sumar cada bloque y guardar el resultado
def versionSecuencial():

    for coordenada in coordenadasBloques:
        resultados.append(sumarBloque(coordenada))



if __name__ == "__main__":

    #Inicialización de la matriz
    matrix = []

    for i in range(1000):
        row = []

        for j in range(1000):
            numeroAleatorio = random.randint(1, 100)

            row.append(numeroAleatorio)

        matrix.append(row)
    
    #Coordenadas de los bloques en la matriz, tuplas de coordenadas en X y Y
    coordenadasBloques = []

    for numBloqueHorizontal in range(10):
        for numBloqueVertical in range(10):
             coordenadasBloques.append((numBloqueHorizontal, numBloqueVertical))

    #Versión secuencial. Se inicializa el arreglo de resultados, se llena con versionSecuencial() y se
    #suman sus elementos y se guarda en sumaSecuencial
    time1S = time.perf_counter()

    resultados = []
    versionSecuencial()
    sumaSecuencial = sumaTotal()

    time2S = time.perf_counter()
    
    timeSecuencial = time2S-time1S

    #Versión paralela. El pool de hilos hace map de la función sumarBloque con las coordenadas ya definidas,
    #los resultados se guardan en una lista, y esa lista se recorre, se suma y se guarda el resultado
    #en sumaParalela
    time1P = time.perf_counter()

    with ThreadPoolExecutor(max_workers=100) as executor:
        resultados = list(executor.map(sumarBloque, coordenadasBloques))
    sumaParalela = sumaTotal()

    time2P = time.perf_counter()

    timeParalelo = time2P-time1P


    aceleracion = timeSecuencial/timeParalelo

    print(f"Tiempo secuencial: {timeSecuencial}\nTiempo paralelo: {timeParalelo}\nAceleración: {aceleracion}\n")
    print(f"Suma paralela: {sumaParalela}\nSuma secuencial: {sumaSecuencial}\n")
