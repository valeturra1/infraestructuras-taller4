import numpy as np
import time
import matplotlib.pyplot as plt

TAMAÑO = 1000


def versionNumpy(m1, m2):
    inicio = time.perf_counter()

    multiplicacion = np.dot(m1, m2)  # Hacemos el producto matricial con Numpy usando la funcion dot

    fin = time.perf_counter()

    resultado = fin - inicio

    return resultado


def versionBucle(n, m1, m2):
    inicio = time.perf_counter()
    
    multiplicacion = [[0.0] * n for i in range(n)]  # Creamos la matriz para guardar el resultado de la multiplicacion, inicializada con ceros

    for i in range(n):      # i recorre las filas de m1
        for j in range(n):  # j recorre las columnas de m2
            suma = 0.0
            for k in range(n):   # k recorre los elementos de la fila i y de la columna j
                suma = suma + m1[i, k] * m2[k, j]
            multiplicacion[i][j] = suma

    fin = time.perf_counter()

    resultado = fin - inicio
    
    return resultado


if __name__ == "__main__":
    # Creamos dos matrices con Numpy de numeros aleatorios entre 0 y 1
    m1 = np.random.rand(TAMAÑO, TAMAÑO)
    m2 = np.random.rand(TAMAÑO, TAMAÑO)

    tiempoNumpy = versionNumpy(m1, m2)
    print(f"La función que utiliza Numpy terminó en: {tiempoNumpy:.2f} s")

    tiempoBucle = versionBucle(TAMAÑO, m1, m2)
    print(f"La función que utiliza un bucle tradicional (for) terminó en: {tiempoBucle:.2f} s")

    aceleracion = tiempoBucle / tiempoNumpy
    print(f"La aceleración obtenida al utilizar Numpy es de: {aceleracion:.2f}")

    # Grafico de barras con escala logaritmica
    nombres = ["Numpy", "Bucle for"]
    tiempos = [tiempoNumpy, tiempoBucle]
    barras = plt.bar(nombres, tiempos, color=["tab:blue", "tab:orange"])
    plt.yscale("log")
    plt.ylabel("Tiempo (s, escala logaritmica)")
    plt.title("Multiplicacion de matrices 1000x1000")
    for barra, t in zip(barras, tiempos):
        plt.text(barra.get_x() + barra.get_width() / 2, t, f"{t:.2f} s",
                 ha="center", va="bottom")
    plt.show()