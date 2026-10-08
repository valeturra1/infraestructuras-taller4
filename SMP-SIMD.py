import threading
import numpy as np
import time

tamañoMatriz = 10000
tamañoBloque = 1000

# para filas suma horizontal (eje=1), para columnas suma vertical (eje=0)
DIRECCION = "filas"
if DIRECCION == "filas":
    EJE = 1
else:
    EJE = 0


def versionParalela(bloque, resultado, i):
    # suma por filas o columnas del bloque dependiendo del eje
    sumasParciales = np.sum(bloque, axis=EJE)
    # se suman todas las sumas parciales y se guarda el resultado en la lista de resultados
    resultado[i] = np.sum(sumasParciales)


def versionSecuencial(matriz):
    inicio = time.perf_counter()

    filas = len(matriz)
    columnas = len(matriz[0])
    total = 0.0

    if DIRECCION == "filas":
        for i in range(filas):
            fila = matriz[i].tolist()          # convierte la fila i a lista
            for j in range(columnas):
                total = total + fila[j]
    else:
        for j in range(columnas):
            columna = matriz[:, j].tolist()    # convierte la columna j a lista
            for i in range(filas):
                total = total + columna[i]

    final = time.perf_counter()

    tiempo = final - inicio
    return tiempo, total


if __name__ == "__main__":
    m1 = np.random.rand(tamañoMatriz, tamañoMatriz)

    bloques = []
    hilos = []

    # dividimos en bloques de 1000x1000
    for i in range(0, tamañoMatriz, tamañoBloque):
        for j in range(0, tamañoMatriz, tamañoBloque):
            bloques.append(m1[i:i + tamañoBloque, j:j + tamañoBloque])

    resultados = [0.0] * len(bloques)

    inicioParalelo = time.perf_counter()

    for i in range(len(bloques)):
        hilo = threading.Thread(target=versionParalela, args=(bloques[i], resultados, i))
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    sumaParalela = sum(resultados)

    finParalelo = time.perf_counter()
    tiempoParalelo = finParalelo - inicioParalelo

    tiempoSecuencial, sumaSecuencial = versionSecuencial(m1)

    # Verificación: ambas sumas deben coincidir (fuera de la medición de tiempo)
    coinciden = np.isclose(sumaParalela, sumaSecuencial, rtol=1e-9)

    aceleracion = tiempoSecuencial / tiempoParalelo

    print(f"Direccion de suma: {DIRECCION}")
    print(f"Tiempo secuencial: {tiempoSecuencial:.4f} s")
    print(f"Tiempo paralelo:   {tiempoParalelo:.4f} s")
    print(f"Aceleracion:       {aceleracion:.4f}")
    print(f"Suma secuencial:   {sumaSecuencial:.4f}")
    print(f"Suma paralela:     {sumaParalela:.4f}")
    print(f"Las sumas coinciden: {coinciden}")