# Comparacion de Soluciones Analiticas y Numericas

## Descripcion del Problema

Este proyecto resuelve una **ecuacion diferencial ordinaria (EDO) separable** utilizando dos enfoques:
1. **Solucion analitica** mediante separacion de variables
2. **Solucion numerica** mediante el metodo de Euler

## EDO a resolver

```
dy/dt = y * (1 - y),   y(0) = 0.5
```

Esta es la **ecuacion logistica**, una EDO separable de primer orden.

## Parametros

- **Intervalo:** t ∈ [0, 1]
- **Paso:** h = 0.2
- **Condicion inicial:** y(0) = 0.5

## Resolucion Analitica

Separando variables:

```
dy / (y * (1 - y)) = dt
```

Usando fracciones parciales:

```
1/(y*(1-y)) = 1/y + 1/(1-y)
```

Integrando ambos lados:

```
ln|y| - ln|1-y| = t + C
ln(y / (1-y)) = t + C
```

Aplicando la condicion inicial y(0) = 0.5:

```
C = ln(0.5 / 0.5) = ln(1) = 0
```

Por lo tanto:

```
y/(1-y) = e^t
y(t) = e^t / (1 + e^t) = 1 / (1 + e^(-t))
```

La solucion exacta es la **funcion sigmoide**.

## Metodo de Euler

El metodo de Euler aproxima la solucion iterativamente:

```
y_{n+1} = y_n + h * f(t_n, y_n)
```

Donde f(t, y) = y * (1 - y)

## Como ejecutar

```bash
python3 comparaSoluciones.py
```

## Requisitos

- Python 3.x
- Modulo `math` (incluido en la libreria estandar)

## Resultados

El programa imprime una tabla comparativa con:
- Valores de Euler vs valores analiticos en cada paso
- Error absoluto y relativo
- Error maximo acumulado

## Conclusion

El metodo de Euler proporciona una aproximacion razonable pero acumula error en cada paso. Con h=0.2 el error es moderado. Reducir h mejoraria la precision a costa de mas pasos de calculo.
