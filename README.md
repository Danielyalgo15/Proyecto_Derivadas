# Simulador de Movimiento de un Vehículo

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un simulador de movimiento de un vehículo utilizando Python y métodos numéricos.

El programa permite calcular la velocidad mediante diferentes métodos de diferenciación numérica y resolver una ecuación diferencial utilizando los métodos de Euler y Runge-Kutta de cuarto orden (RK4).

También genera tablas comparativas, calcula errores y produce gráficas para analizar los resultados.

## Modelo matemático

La función de posición utilizada es:

\[
x(t)=x_0+v_0t+\frac{a_0}{2}t^2+\frac{j}{6}t^3
\]

Donde:
- \(x_0\): posición inicial.
- \(v_0\): velocidad inicial.
- \(a_0\): aceleración inicial.
- \(j\): variación de la aceleración.
- \(t\): tiempo transcurrido.

## Métodos implementados

### Diferenciación numérica
- Diferencia hacia adelante.
- Diferencia hacia atrás.
- Diferencia centrada.
- Método de cinco puntos.
- Extrapolación de Richardson.

### Resolución de ecuaciones diferenciales
- Método de Euler.
- Método de Runge-Kutta de cuarto orden (RK4).

## Estructura del proyecto

| Archivo | Descripción |
|---|---|
| `main.py` | Ejecuta el programa principal. |
| `funciones.py` | Contiene las funciones matemáticas del movimiento. |
| `metodos_numericos.py` | Implementa los métodos de diferenciación. |
| `ecuaciones_diferenciales.py` | Implementa Euler y RK4. |
| `graficas.py` | Genera las gráficas comparativas. |
| `requirements.txt` | Contiene las dependencias del proyecto. |

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

Crear y activar un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Iniciar el simulador con:

```bash
python main.py
```

El programa solicitará los parámetros del vehículo. Se pueden ingresar valores personalizados o presionar Enter para utilizar los valores predeterminados.

## Resultados

El programa muestra:

- Una tabla comparativa de los cinco métodos de diferenciación.
- Una tabla de resultados de Euler y RK4.
- Los errores respecto a las soluciones exactas.
- Tres gráficas generadas automáticamente:

1. `grafica_posicion.png`
2. `grafica_velocidad.png`
3. `grafica_errores.png`

## Autor

Danielyalgo15

## Repositorio

[Proyecto_Derivadas - GitHub](https://github.com/Danielyalgo15/Proyecto_Derivadas)
# Proyecto_Derivadas
