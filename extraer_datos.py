
import csv

with open("ngsim_vehiculo.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    filas = list(lector)

# Agrupar por ubicación para no mezclar carreteras
ubicaciones = {}

for fila in filas:
    lugar = fila["location"]
    ubicaciones.setdefault(lugar, []).append(fila)

# Elegir la ubicación con más registros
lugar = max(ubicaciones, key=lambda x: len(ubicaciones[x]))
filas = ubicaciones[lugar]

# Ordenar por fotograma
filas.sort(key=lambda x: int(x["frame_id"]))

# Buscar 15 registros consecutivos
seleccion = []

for i in range(len(filas) - 14):
    grupo = filas[i:i + 15]

    consecutivos = all(
        int(grupo[j + 1]["frame_id"]) -
        int(grupo[j]["frame_id"]) == 1
        for j in range(14)
    )

    if consecutivos:
        seleccion = grupo
        break

if not seleccion:
    print("No se encontraron 15 registros consecutivos.")
else:
    tiempo_inicial = int(seleccion[0]["global_time"])

    print("Ubicación:", lugar)
    print("Cantidad de mediciones: 15")
    print()

    for fila in seleccion:
        tiempo = (int(fila["global_time"]) - tiempo_inicial) / 1000
        posicion = float(fila["local_y"]) * 0.3048

        print(f"{tiempo:.1f}, {posicion:.6f}")
