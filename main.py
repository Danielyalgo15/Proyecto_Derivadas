
from datos import ingresar_datos
from metodos_numericos import calcular_metodos
from graficas import graficar_movimiento


def main():
    print("=" * 55)
    print(" ANALISIS DE VELOCIDAD DE UN VEHICULO")
    print(" METODOS DE DIFERENCIACION NUMERICA")
    print("=" * 55)

    try:
        # 1. Ingresar mediciones
        tiempos, posiciones, h = ingresar_datos()

        print("\nMEDICIONES REGISTRADAS")
        print("-" * 40)

        for i in range(len(tiempos)):
            print(
                f"Tiempo: {tiempos[i]:.3f} s | "
                f"Posicion: {posiciones[i]:.3f} m"
            )

        # 2. Seleccionar el instante para calcular la velocidad
        print("\nSELECCION DEL INSTANTE")
        print(f"Puedes elegir un indice entre 2 y {len(tiempos) - 3}.")

        indice = int(input("Ingresa el indice de la medicion: "))

        if indice < 2 or indice > len(tiempos) - 3:
            raise ValueError("El indice seleccionado no es valido.")

        # 3. Calcular las velocidades
        resultados = calcular_metodos(posiciones, indice, h)

        print("\nRESULTADOS DE DIFERENCIACION NUMERICA")
        print("-" * 50)

        nombres = [
            "Diferencias hacia adelante",
            "Diferencias hacia atras",
            "Diferencias centradas",
            "Cinco puntos",
            "Extrapolacion de Richardson"
        ]

        for nombre, velocidad in zip(nombres, resultados):
            print(f"{nombre}: {velocidad:.6f} m/s")

        # 4. Generar graficas
        graficar_movimiento(tiempos, posiciones, h)

        print("\nAnalisis completado.")
        print("Las graficas se encuentran en la carpeta 'graficas'.")

    except ValueError as error:
        print(f"\nERROR: {error}")

    except Exception as error:
        print(f"\nERROR INESPERADO: {error}")


if __name__ == "__main__":
    main()
