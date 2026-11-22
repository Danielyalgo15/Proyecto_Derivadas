"""
Métodos numéricos para aproximar derivadas.

Incluye diferencias hacia adelante, hacia atrás, centradas,
la fórmula de cinco puntos y la extrapolación de Richardson.
"""


def diferencia_adelante(f, t, h):
    """
    Aproxima la primera derivada mediante diferencias hacia adelante.

    Parámetros:
        f: función que se desea derivar.
        t: punto donde se calcula la derivada.
        h: tamaño del paso.

    Retorna:
        Valor aproximado de la primera derivada.

    Error de truncamiento: O(h).
    """
    return (f(t + h) - f(t)) / h


def diferencia_atras(f, t, h):
    """
    Aproxima la primera derivada mediante diferencias hacia atrás.

    Parámetros:
        f: función que se desea derivar.
        t: punto donde se calcula la derivada.
        h: tamaño del paso.

    Retorna:
        Valor aproximado de la primera derivada.

    Error de truncamiento: O(h).
    """
    return (f(t) - f(t - h)) / h


def diferencia_centrada(f, t, h):
    """
    Aproxima la primera derivada mediante diferencias centradas.

    Parámetros:
        f: función que se desea derivar.
        t: punto donde se calcula la derivada.
        h: tamaño del paso.

    Retorna:
        Valor aproximado de la primera derivada.

    Error de truncamiento: O(h²).
    """
    return (f(t + h) - f(t - h)) / (2 * h)


def cinco_puntos(f, t, h):
    """
    Aproxima la primera derivada mediante la fórmula centrada
    de cinco puntos.

    Parámetros:
        f: función que se desea derivar.
        t: punto donde se calcula la derivada.
        h: tamaño del paso.

    Retorna:
        Valor aproximado de la primera derivada.

    Error de truncamiento: O(h⁴).
    """
    return (
        f(t - 2*h)
        - 8*f(t - h)
        + 8*f(t + h)
        - f(t + 2*h)
    ) / (12 * h)


def richardson(f, t, h):
    """
    Mejora la aproximación de la derivada mediante extrapolación
    de Richardson, utilizando diferencias centradas con pasos
    h y h/2.

    Parámetros:
        f: función que se desea derivar.
        t: punto donde se calcula la derivada.
        h: tamaño inicial del paso.

    Retorna:
        Aproximación mejorada de la primera derivada.
    """
    d1 = diferencia_centrada(f, t, h)
    d2 = diferencia_centrada(f, t, h/2)

    resultado = (4*d2 - d1) / 3

    return resultado
