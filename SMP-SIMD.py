import threading
import numpy as np
import time

tamañoMatriz = 10000
tamañoBloque = 1000

def versionParalela(bloque, resultado, i):
    a


def versionSecuencial(matriz):
    inicio = time.time()
    b
    final = time.time()

    tiempo = final - inicio
    return tiempo


if __name__ == "__main__":
    m1 = np.random.rand(tamañoMatriz, tamañoMatriz)

    bloques = []
    hilos = []
    
    for i in range(0, tamañoMatriz, tamañoBloque):
        for j in range(0, tamañoMatriz, tamañoBloque):
            bloques.append(m1[i:i+tamañoBloque, j:j+tamañoBloque])

    resultados = [0.0] * len(bloques)


    inicioParalelo = time.time()

    for i in range(len(bloques)):
        hilo = threading.Thread(target=versionParalela, args=(bloques[i], resultados, i))
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    sumaTotal = sum(resultados)

    finParalelo = time.time()

    tiempoParalelo = finParalelo - inicioParalelo
    tiempoSecuencial = versionSecuencial(m1)
    
