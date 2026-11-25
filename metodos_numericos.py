
"""
Metodos numericos para aproximar la primera derivada.
"""


def diferencia_adelante(posiciones, i, h):
    return (posiciones[i + 1] - posiciones[i]) / h


def diferencia_atras(posiciones, i, h):
    return (posiciones[i] - posiciones[i - 1]) / h


def diferencia_centrada(posiciones, i, h):
    return (posiciones[i + 1] - posiciones[i - 1]) / (2 * h)


def cinco_puntos(posiciones, i, h):
    return (
        posiciones[i - 2]
        - 8 * posiciones[i - 1]
        + 8 * posiciones[i + 1]
        - posiciones[i + 2]
    ) / (12 * h)


def richardson(posiciones, i, h):
    d_h = diferencia_centrada(posiciones, i, h)

    d_2h = (
        posiciones[i + 2] - posiciones[i - 2]
    ) / (4 * h)

    return (4 * d_h - d_2h) / 3


def calcular_metodos(posiciones, i, h):
    return [
        diferencia_adelante(posiciones, i, h),
        diferencia_atras(posiciones, i, h),
        diferencia_centrada(posiciones, i, h),
        cinco_puntos(posiciones, i, h),
        richardson(posiciones, i, h)
    ]

