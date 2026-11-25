# Análisis de Velocidad de un Vehículo mediante Diferenciación Numérica

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un programa en Python para analizar el movimiento de un vehículo mediante métodos de diferenciación numérica.

El programa permite ingresar manualmente mediciones de tiempo y posición, con las cuales aproxima la velocidad del vehículo utilizando cinco métodos numéricos.

Además, genera gráficas que permiten visualizar el comportamiento de la posición y la velocidad, así como comparar los resultados obtenidos por cada método.

## Modelo matemático

El objetivo principal es aproximar la primera derivada de la posición respecto al tiempo:

\[
v(t)=\frac{dx(t)}{dt}
\]

Donde:

- \(v(t)\): velocidad del vehículo.
- \(x(t)\): posición del vehículo.
- \(t\): tiempo transcurrido.

Para realizar los cálculos, el programa utiliza mediciones discretas de posición y tiempo ingresadas por el usuario.

## Métodos numéricos implementados

Se implementan cinco métodos para aproximar la primera derivada:

1. Diferencias hacia adelante.
2. Diferencias hacia atrás.
3. Diferencias centradas.
4. Fórmula de cinco puntos.
5. Extrapolación de Richardson.

Estos métodos permiten comparar distintas aproximaciones de la velocidad en un mismo instante.

## Funcionamiento del programa

El programa sigue el siguiente procedimiento:

1. Solicita la cantidad de mediciones que se desean ingresar.
2. Recibe los valores de tiempo (segundos) y posición (metros).
3. Comprueba que los tiempos sean crecientes y tengan intervalos uniformes.
4. Permite seleccionar el instante en el que se calculará la velocidad.
5. Aplica los cinco métodos de diferenciación numérica.
6. Muestra los resultados obtenidos.
7. Genera automáticamente tres gráficas.

## Estructura del proyecto

| Archivo o carpeta | Descripción |
|---|---|
| `main.py` | Ejecuta el programa principal y coordina el análisis. |
| `datos.py` | Permite ingresar y validar las mediciones manualmente. |
| `metodos_numericos.py` | Contiene las funciones de diferenciación numérica. |
| `graficas.py` | Genera las gráficas del movimiento y compara los métodos. |
| `requirements.txt` | Contiene las dependencias necesarias. |
| `graficas/` | Almacena las imágenes generadas por el programa. |
| `evidencias/` | Contiene las capturas de pantalla del proyecto. |

## Requisitos

- Python 3.
- Matplotlib.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/Danielyalgo15/Proyecto_Derivadas.git
```

Ingresar a la carpeta:

```bash
cd Proyecto_Derivadas
```

Crear un entorno virtual:

```bash
python3 -m venv venv
```

Activar el entorno virtual en Linux o WSL Ubuntu:

```bash
source venv/bin/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Iniciar el programa con:

```bash
python main.py
```

El programa solicitará la cantidad de mediciones y posteriormente los valores de tiempo y posición correspondientes.

**Consideraciones para ingresar los datos:**

- Se necesitan al menos cinco mediciones.
- Los tiempos deben ser crecientes.
- Los intervalos entre mediciones deben ser iguales.
- El tiempo se expresa en segundos y la posición en metros.

## Resultados

El programa muestra las aproximaciones de velocidad obtenidas mediante los cinco métodos de diferenciación numérica.

También genera automáticamente las siguientes gráficas:

1. `grafica_posicion.png`: representa la posición del vehículo respecto al tiempo.
2. `grafica_velocidad.png`: muestra las velocidades aproximadas mediante los cinco métodos.
3. `comparacion_metodos.png`: compara los resultados de los cinco métodos en un mismo instante.

Todas las gráficas se almacenan en la carpeta `graficas/`.

## Autor

Danielyalgo15

## Repositorio

[Proyecto_Derivadas - GitHub](https://github.com/Danielyalgo15/Proyecto_Derivadas)
