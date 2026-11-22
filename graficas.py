"""
Módulo encargado de generar las gráficas del simulador.

Genera gráficas comparativas de posición, velocidad
y errores numéricos utilizando Matplotlib.
"""

import matplotlib.pyplot as plt
from funciones import posicion, velocidad_exacta


def graficar_movimiento(
    x0, v0, a0, j, tiempo_evaluacion,
    tiempos_euler, posiciones_euler, velocidades_euler,
    tiempos_rk4, posiciones_rk4, velocidades_rk4
):
    """
    Genera las gráficas de posición, velocidad y errores.

    Parámetros:
        x0: posición inicial (m).
        v0: velocidad inicial (m/s).
        a0: aceleración inicial (m/s²).
        j: variación de la aceleración (m/s³).
        tiempo_evaluacion: duración de la simulación (s).
        tiempos_euler: tiempos calculados por Euler.
        posiciones_euler: posiciones calculadas por Euler.
        velocidades_euler: velocidades calculadas por Euler.
        tiempos_rk4: tiempos calculados por RK4.
        posiciones_rk4: posiciones calculadas por RK4.
        velocidades_rk4: velocidades calculadas por RK4.

    Genera:
        grafica_posicion.png
        grafica_velocidad.png
        grafica_errores.png
    """

    # Calcular los valores de la solucion exacta
    tiempos = [
        i * 0.1 for i in range(int(tiempo_evaluacion * 10) + 1)
    ]

    posiciones_exactas = [
        posicion(t, x0, v0, a0, j) for t in tiempos
    ]

    velocidades_exactas = [
        velocidad_exacta(t, v0, a0, j) for t in tiempos
    ]

    # Grafica comparativa de posicion
    plt.figure(figsize=(10, 5))

    plt.plot(tiempos, posiciones_exactas,
             label="Solucion exacta", linewidth=2)

    plt.plot(tiempos_euler, posiciones_euler,
             label="Metodo de Euler", linestyle="--")

    plt.plot(tiempos_rk4, posiciones_rk4,
             label="Metodo RK4", linestyle=":")

    plt.xlabel("Tiempo (s)")
    plt.ylabel("Posicion (m)")
    plt.title("Comparacion de posicion del vehiculo")
    plt.grid()
    plt.legend()

    plt.savefig("grafica_posicion.png", dpi=300, bbox_inches="tight")
    plt.close()

    # Grafica comparativa de velocidad
    plt.figure(figsize=(10, 5))

    plt.plot(tiempos, velocidades_exactas,
             label="Solucion exacta", linewidth=2)

    plt.plot(tiempos_euler, velocidades_euler,
             label="Metodo de Euler", linestyle="--")

    plt.plot(tiempos_rk4, velocidades_rk4,
             label="Metodo RK4", linestyle=":")

    plt.xlabel("Tiempo (s)")
    plt.ylabel("Velocidad (m/s)")
    plt.title("Comparacion de velocidad del vehiculo")
    plt.grid()
    plt.legend()

    plt.savefig("grafica_velocidad.png", dpi=300, bbox_inches="tight")
    plt.close()

    # Calcular los errores de posicion de Euler y RK4
    errores_euler = []
    errores_rk4 = []

    for i in range(len(tiempos_euler)):
        tiempo_actual = tiempos_euler[i]

        valor_exacto = posicion(
            tiempo_actual, x0, v0, a0, j
        )

        error_euler = abs(valor_exacto - posiciones_euler[i])
        error_rk4 = abs(valor_exacto - posiciones_rk4[i])

        errores_euler.append(error_euler)
        errores_rk4.append(error_rk4)

    # Grafica comparativa de errores
    plt.figure(figsize=(10, 5))

    plt.plot(tiempos_euler, errores_euler,
             label="Error de Euler")

    plt.plot(tiempos_rk4, errores_rk4,
             label="Error de RK4")

    plt.xlabel("Tiempo (s)")
    plt.ylabel("Error absoluto (m)")
    plt.title("Comparacion de errores numericos")
    plt.grid()
    plt.legend()

    plt.savefig("grafica_errores.png", dpi=300, bbox_inches="tight")
    plt.close()

    print("Graficas comparativas guardadas correctamente.")
