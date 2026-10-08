import numpy as np
import time
import matplotlib.pyplot as plt

TAMAÑO = 1000


def versionNumpy(m1, m2):
    inicio = time.perf_counter()

    multiplicacionNumpy = np.dot(m1, m2)  # Hacemos el producto matricial con Numpy usando la funcion dot

    fin = time.perf_counter()

    resultado = fin - inicio

    return resultado, multiplicacionNumpy


def versionBucle(n, l1, l2):
    inicio = time.perf_counter()
    
    # Creamos la matriz para guardar el resultado de la multiplicacion, inicializada con ceros
    multiplicacionBucles = []

    for i in range(n):
        fila = []

        for j in range(n):
            fila.append(0.0)

        multiplicacionBucles.append(fila)

    for i in range(n):      # i recorre las filas de l1
        for j in range(n):  # j recorre las columnas de l2
            suma = 0.0
            for k in range(n):   # k recorre los elementos de la fila i y de la columna j
                suma = suma + l1[i][k] * l2[k][j]
            multiplicacionBucles[i][j] = suma

    fin = time.perf_counter()

    resultado = fin - inicio
    
    return resultado, multiplicacionBucles


if __name__ == "__main__":
    # Creamos dos matrices con Numpy de numeros aleatorios entre 0 y 1
    m1 = np.random.rand(TAMAÑO, TAMAÑO)
    m2 = np.random.rand(TAMAÑO, TAMAÑO)

    # Convertirmos las matrices con los mismos números en listas de listas
    l1 = m1.tolist()
    l2 = m2.tolist()

    

    tiempoNumpy, multiplicacionNumpy = versionNumpy(m1, m2)
    print(f"La función que utiliza Numpy terminó en: {tiempoNumpy:.2f} s")

    tiempoBucle, multiplicacionBucles = versionBucle(TAMAÑO, l1, l2)
    print(f"La función que utiliza un bucle tradicional (for) terminó en: {tiempoBucle:.2f} s")

    # Comparación de resultados
    coinciden = np.allclose(multiplicacionNumpy, np.array(multiplicacionBucles))
    print(f"Los resultados coinciden: {coinciden}")

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