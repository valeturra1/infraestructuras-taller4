from concurrent.futures import ThreadPoolExecutor
import numpy as np
import time

#Función que recibe los índices de la matriz en tuplas, los  desempaqueta y
# convierte en un bloque de la matriz de numpy
#y suma ese bloque con numpy.sum(), retornando el resultado
def sumarBloque(coordenadas):


    numBloqueHorizontal, numBloqueVertical = coordenadas

    fila_inicio = numBloqueHorizontal*100
    fila_fin = (numBloqueHorizontal+1)*100

    columna_inicio = numBloqueVertical*100
    columna_fin = (numBloqueVertical+1)*100

    bloque = matrix[fila_inicio:fila_fin, columna_inicio:columna_fin]

    return np.sum(bloque)
            


#Función que recorre el arreglo de resultados y las acumula en una variable final que representa la suma
#de toda la matriz, retorna esta variable
def sumaTotal():
    suma = 0
    for number in resultados:
        suma += number
    return suma

#Implementación secuencial de sumar cada bloque y guarda el resultado
def versionSecuencial():

    for coordenada in coordenadasBloques:
        resultados.append(sumarBloque(coordenada))



if __name__ == "__main__":

    matrix = np.random.randint(1, 101, size=(1000, 1000))

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
