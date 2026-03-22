import math

def compara_soluciones():
    """
    Comparacion de Soluciones Analiticas y Numericas
    EDO separable: dy/dt = y * (1 - y), y(0) = 0.5
    Intervalo: t in [0, 1], paso h = 0.2

    Resolucion analitica (separacion de variables):
    dy / (y*(1-y)) = dt
    Fracciones parciales: 1/(y*(1-y)) = 1/y + 1/(1-y)
    Integrando: ln|y| - ln|1-y| = t + C
    ln(y/(1-y)) = t + C
    Con y(0)=0.5: C = ln(0.5/0.5) = ln(1) = 0
    y/(1-y) = e^t => y(t) = e^t / (1 + e^t) = 1/(1 + e^(-t))
    """

    # Parametros
    h = 0.2
    t0 = 0
    tf = 1
    y0 = 0.5
    n = round((tf - t0) / h)

    # f(t, y) = dy/dt = y*(1-y)  (ecuacion logistica)
    def f(t, y):
        return y * (1 - y)

    # Solucion analitica: y(t) = 1 / (1 + e^(-t))
    def solucion_analitica(t):
        return 1.0 / (1.0 + math.exp(-t))

    # Arrays para almacenar resultados
    t_vals = [t0]
    y_euler = [y0]
    y_analitica = [solucion_analitica(t0)]
    errores_abs = [0]
    errores_rel = [0]

    t = t0
    y = y0

    # Iteracion del metodo de Euler
    for i in range(n):
        y = y + h * f(t, y)
        t = t0 + (i + 1) * h
        t = round(t, 3)

        analitica = solucion_analitica(t)
        err_abs = abs(analitica - y)
        err_rel = (err_abs / abs(analitica)) * 100 if analitica != 0 else 0

        t_vals.append(t)
        y_euler.append(y)
        y_analitica.append(analitica)
        errores_abs.append(err_abs)
        errores_rel.append(err_rel)

    # Imprimir resultados
    print("================================================")
    print("COMPARACION: SOLUCION ANALITICA vs METODO DE EULER")
    print("================================================")
    print("EDO: dy/dt = y*(1-y)  (ecuacion logistica separable)")
    print("Condicion inicial: y(0) = 0.5")
    print("Intervalo: [0, 1], h = 0.2")
    print()
    print("Resolucion analitica:")
    print("  Separando variables: dy/(y*(1-y)) = dt")
    print("  Fracciones parciales e integrando:")
    print("  y(t) = 1/(1 + e^(-t))  (funcion sigmoide)")
    print()
    print("t\t| Euler\t\t| Analitica\t| Err Abs\t| Err Rel(%)")
    print("------------------------------------------------------------")

    for i in range(len(t_vals)):
        print(f"{t_vals[i]:.1f}\t| {y_euler[i]:.6f}\t| {y_analitica[i]:.6f}\t| {errores_abs[i]:.6f}\t| {errores_rel[i]:.4f}")

    print("------------------------------------------------------------")
    print()
    print("=== ANALISIS DE RESULTADOS ===")
    print(f"Error absoluto maximo: {max(errores_abs):.6f}")
    print(f"Error relativo maximo: {max(errores_rel):.4f}%")
    print()
    print("Conclusion: El metodo de Euler proporciona una aproximacion")
    print("razonable pero acumula error en cada paso. Con h=0.2 el error")
    print("es moderado. Reducir h mejoraria la precision a costa de mas pasos.")


if __name__ == "__main__":
    compara_soluciones()
