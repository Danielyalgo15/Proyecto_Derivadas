
def ingresar_datos():
    print("\nINGRESO DE MEDICIONES DEL VEHICULO")
    print("----------------------------------")

    while True:
        try:
            cantidad = int(input("¿Cuantas mediciones ingresaras?: "))

            if cantidad < 5:
                print("Necesitas ingresar al menos 5 mediciones.")
                continue

            break

        except ValueError:
            print("Ingresa un numero entero.")

    tiempos = []
    posiciones = []

    for i in range(cantidad):
        print(f"\nMEDICION {i + 1}")

        while True:
            try:
                tiempo = float(input("Tiempo (s): ").replace(",", "."))
                posicion = float(input("Posicion (m): ").replace(",", "."))

                if tiempos and tiempo <= tiempos[-1]:
                    print("El tiempo debe ser mayor al anterior.")
                    continue

                tiempos.append(tiempo)
                posiciones.append(posicion)
                break

            except ValueError:
                print("Ingresa valores numericos validos.")

    # Comprobar que los intervalos de tiempo sean iguales
    h = tiempos[1] - tiempos[0]

    for i in range(1, cantidad - 1):
        intervalo = tiempos[i + 1] - tiempos[i]

        if abs(intervalo - h) > 0.000001:
            raise ValueError(
                "Los tiempos deben tener intervalos iguales."
            )

    return tiempos, posiciones, h
