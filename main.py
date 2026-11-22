"""
Programa principal del simulador de movimiento de un vehículo.

Permite ingresar parámetros, comparar métodos de diferenciación,
resolver la ecuación diferencial mediante Euler y RK4,
mostrar tablas de errores y generar gráficas.
"""

from funciones import posicion, velocidad_exacta

from metodos_numericos import (
    diferencia_adelante,
    diferencia_atras,
    diferencia_centrada,
    cinco_puntos,
    richardson
)

from graficas import graficar_movimiento
from ecuaciones_diferenciales import metodo_euler, metodo_rk4


def pedir_valor(mensaje, valor_default):
    """
    Solicita un valor numérico al usuario.

    Parámetros:
        mensaje: descripción del dato solicitado.
        valor_default: valor utilizado si el usuario presiona Enter.

    Retorna:
        Valor numérico ingresado o valor predeterminado.
    """
    entrada = input(f"{mensaje} [{valor_default}]: ")

    if entrada.strip() == "":
        return valor_default

    return float(entrada)


# Presentacion inicial del simulador
print("SIMULADOR DE MOVIMIENTO DE UN VEHICULO")
print("--------------------------------------")
print("Presiona Enter para utilizar el valor predeterminado.\n")


# Solicitud de los parametros del vehiculo
x0 = pedir_valor("Posicion inicial (m)", 0)
v0 = pedir_valor("Velocidad inicial (m/s)", 3)
a0 = pedir_valor("Aceleracion inicial (m/s²)", 1)
j = pedir_valor("Variacion de aceleracion (m/s³)", 0.06)


# Solicitud de los parametros de evaluacion
t = pedir_valor("Tiempo de evaluacion (s)", 5)
h = pedir_valor("Paso de calculo (h)", 0.1)


# Validacion de los datos ingresados
if h <= 0 or t <= 2*h:
    print("Error: h debe ser positivo y t debe ser mayor que 2h.")

else:
    # Definicion de la funcion de posicion
    f = lambda tiempo: posicion(tiempo, x0, v0, a0, j)

    # Calculo de la velocidad exacta
    exacta = velocidad_exacta(t, v0, a0, j)


    # Comparacion de los cinco metodos de diferenciacion
    resultados = {
        "Diferencia hacia adelante": diferencia_adelante(f, t, h),
        "Diferencia hacia atras": diferencia_atras(f, t, h),
        "Diferencia centrada": diferencia_centrada(f, t, h),
        "Cinco puntos": cinco_puntos(f, t, h),
        "Richardson": richardson(f, t, h)
    }

    # Mostrar tabla de resultados y errores
    print("\nCOMPARACION DE METODOS NUMERICOS")
    print("---------------------------------------------------------------")
    print(f"{'Metodo':<30} {'Resultado':>12} {'Error':>12}")
    print("---------------------------------------------------------------")

    for metodo, resultado in resultados.items():
        error = abs(exacta - resultado)

        print(f"{metodo:<30} {resultado:>12.6f} {error:>12.8f}")

    print("---------------------------------------------------------------")
    print(f"{'Valor exacto':<30} {exacta:>12.6f}")


    # Resolucion de la ecuacion diferencial mediante Euler y RK4
    tiempos_euler, posiciones_euler, velocidades_euler = metodo_euler(
        x0, v0, a0, j, h, t
    )

    tiempos_rk4, posiciones_rk4, velocidades_rk4 = metodo_rk4(
        x0, v0, a0, j, h, t
    )


    # Calculo de los valores exactos y errores
    posicion_exacta = posicion(t, x0, v0, a0, j)

    error_pos_euler = abs(posicion_exacta - posiciones_euler[-1])
    error_pos_rk4 = abs(posicion_exacta - posiciones_rk4[-1])

    error_vel_euler = abs(exacta - velocidades_euler[-1])
    error_vel_rk4 = abs(exacta - velocidades_rk4[-1])


    # Mostrar tabla comparativa de Euler y RK4
    print("\nRESOLUCION DE LA ECUACION DIFERENCIAL")
    print("-------------------------------------------------------------------")
    print(f"{'Metodo':<15} {'Posicion (m)':>15} {'Error pos.':>13} {'Velocidad':>13} {'Error vel.':>12}")
    print("-------------------------------------------------------------------")

    print(f"{'Exacta':<15} {posicion_exacta:>15.6f} {'-':>13} {exacta:>13.6f} {'-':>12}")

    print(f"{'Euler':<15} {posiciones_euler[-1]:>15.6f} {error_pos_euler:>13.6f} {velocidades_euler[-1]:>13.6f} {error_vel_euler:>12.6f}")

    print(f"{'RK4':<15} {posiciones_rk4[-1]:>15.6f} {error_pos_rk4:>13.6f} {velocidades_rk4[-1]:>13.6f} {error_vel_rk4:>12.6f}")

    print("-------------------------------------------------------------------")


    # Generacion de las graficas comparativas
    graficar_movimiento(
        x0, v0, a0, j, t,
        tiempos_euler, posiciones_euler, velocidades_euler,
        tiempos_rk4, posiciones_rk4, velocidades_rk4
    )

    print("\nGraficas guardadas correctamente.")
