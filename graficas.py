
"""
Modulo encargado de generar las graficas del proyecto.

Genera:
- Posicion respecto al tiempo.
- Velocidad aproximada respecto al tiempo.
- Comparacion de los cinco metodos numericos.
"""

import os
import matplotlib.pyplot as plt

from metodos_numericos import calcular_metodos


def graficar_movimiento(tiempos, posiciones, h):

    os.makedirs("graficas", exist_ok=True)

    cantidad = len(tiempos)

    nombres = [
        "Diferencias hacia adelante",
        "Diferencias hacia atras",
        "Diferencias centradas",
        "Cinco puntos",
        "Richardson"
    ]

    # GRAFICA 1: POSICION
    plt.figure(figsize=(10, 5))

    plt.plot(
        tiempos,
        posiciones,
        marker=".",
        markersize=4,
        label="Posicion registrada"
    )

    plt.xlabel("Tiempo (s)")
    plt.ylabel("Posicion (m)")
    plt.title("Posicion del vehiculo respecto al tiempo")
    plt.grid()
    plt.legend()

    plt.savefig(
        "graficas/grafica_posicion.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # GRAFICA 2: VELOCIDAD
    velocidades = {
        nombre: [float("nan")] * cantidad
        for nombre in nombres
    }

    for i in range(2, cantidad - 2):

        resultados = calcular_metodos(posiciones, i, h)

        for nombre, valor in zip(nombres, resultados):
            velocidades[nombre][i] = valor

    plt.figure(figsize=(11, 6))

    for nombre, valores in velocidades.items():
        plt.plot(
            tiempos,
            valores,
            label=nombre
        )

    plt.xlabel("Tiempo (s)")
    plt.ylabel("Velocidad (m/s)")
    plt.title("Velocidad aproximada del vehiculo")
    plt.grid()
    plt.legend()

    plt.savefig(
        "graficas/grafica_velocidad.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # GRAFICA 3: COMPARACION DE METODOS
    indice_central = cantidad // 2

    valores = calcular_metodos(
        posiciones,
        indice_central,
        h
    )

    nombres_cortos = [
        "Adelante",
        "Atras",
        "Centrada",
        "Cinco puntos",
        "Richardson"
    ]

    plt.figure(figsize=(11, 6))

    plt.bar(nombres_cortos, valores)

    plt.xlabel("Metodos numericos")
    plt.ylabel("Velocidad (m/s)")
    plt.title("Comparacion de los cinco metodos")
    plt.grid(axis="y")

    plt.savefig(
        "graficas/comparacion_metodos.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print("\nGraficas guardadas correctamente en la carpeta graficas.")
