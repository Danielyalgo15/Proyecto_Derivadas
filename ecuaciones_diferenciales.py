"""
Métodos numéricos para resolver la ecuación diferencial
del movimiento de un vehículo.

Incluye el método de Euler y Runge-Kutta de cuarto orden (RK4).
"""


def metodo_euler(x0, v0, a0, j, h, tiempo):
    """
    Resuelve la ecuación diferencial utilizando el método de Euler.

    Parámetros:
        x0: posición inicial (m).
        v0: velocidad inicial (m/s).
        a0: aceleración inicial (m/s²).
        j: variación de la aceleración (m/s³).
        h: tamaño del paso de cálculo.
        tiempo: tiempo total de simulación (s).

    Retorna:
        Listas con los tiempos, posiciones y velocidades calculadas.
    """
    x = x0
    v = v0
    t = 0

    posiciones = [x]
    velocidades = [v]
    tiempos = [t]

    while t < tiempo:
        x_nuevo = x + h * v
        v_nuevo = v + h * (a0 + j * t)

        x = x_nuevo
        v = v_nuevo
        t = t + h

        posiciones.append(x)
        velocidades.append(v)
        tiempos.append(t)

    return tiempos, posiciones, velocidades


def metodo_rk4(x0, v0, a0, j, h, tiempo):
    """
    Resuelve la ecuación diferencial utilizando Runge-Kutta
    de cuarto orden (RK4).

    Parámetros:
        x0: posición inicial (m).
        v0: velocidad inicial (m/s).
        a0: aceleración inicial (m/s²).
        j: variación de la aceleración (m/s³).
        h: tamaño del paso de cálculo.
        tiempo: tiempo total de simulación (s).

    Retorna:
        Listas con los tiempos, posiciones y velocidades calculadas.
    """
    x = x0
    v = v0
    t = 0

    posiciones = [x]
    velocidades = [v]
    tiempos = [t]

    while t < tiempo:
        k1x = v
        k1v = a0 + j * t

        k2x = v + (h / 2) * k1v
        k2v = a0 + j * (t + h / 2)

        k3x = v + (h / 2) * k2v
        k3v = a0 + j * (t + h / 2)

        k4x = v + h * k3v
        k4v = a0 + j * (t + h)

        x = x + (h / 6) * (k1x + 2*k2x + 2*k3x + k4x)
        v = v + (h / 6) * (k1v + 2*k2v + 2*k3v + k4v)

        t = t + h

        posiciones.append(x)
        velocidades.append(v)
        tiempos.append(t)

    return tiempos, posiciones, velocidades
