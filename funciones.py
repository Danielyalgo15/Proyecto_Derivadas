"""
Funciones matemáticas del simulador de movimiento de un vehículo.

Contiene las ecuaciones analíticas de posición, velocidad y aceleración.
"""


def posicion(t, x0, v0, a0, j):
    """
    Calcula la posición del vehículo en un instante determinado.

    Parámetros:
        t: tiempo transcurrido (s).
        x0: posición inicial (m).
        v0: velocidad inicial (m/s).
        a0: aceleración inicial (m/s²).
        j: variación de la aceleración (m/s³).

    Retorna:
        Posición del vehículo en metros.
    """
    x = x0 + v0*t + (a0/2)*t**2 + (j/6)*t**3
    return x


def velocidad_exacta(t, v0, a0, j):
    """
    Calcula la velocidad exacta mediante la derivada de posición.

    Parámetros:
        t: tiempo transcurrido (s).
        v0: velocidad inicial (m/s).
        a0: aceleración inicial (m/s²).
        j: variación de la aceleración (m/s³).

    Retorna:
        Velocidad del vehículo en m/s.
    """
    v = v0 + a0*t + (j/2)*t**2
    return v


def aceleracion_exacta(t, a0, j):
    """
    Calcula la aceleración exacta del vehículo.

    Parámetros:
        t: tiempo transcurrido (s).
        a0: aceleración inicial (m/s²).
        j: variación de la aceleración (m/s³).

    Retorna:
        Aceleración del vehículo en m/s².
    """
    a = a0 + j*t
    return a