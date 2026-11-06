from media_varianza import media, varianza


def desviacion_estandar(datos):
    """Raíz cuadrada de la varianza poblacional."""
    return varianza(datos) ** 0.5


def mediana(datos):
    """Valor central de los datos ordenados."""
    ordenados = sorted(datos)
    n = len(ordenados)
    medio = n // 2
    if n % 2 == 1:
        return ordenados[medio]
    return (ordenados[medio - 1] + ordenados[medio]) / 2


def moda(datos):
    """Valor que más se repite (si hay empate, devuelve el primero que alcanzó ese conteo)."""
    frecuencias = {}
    for x in datos:
        frecuencias[x] = frecuencias.get(x, 0) + 1

    moda_valor = None
    max_conteo = 0
    for valor, conteo in frecuencias.items():
        if conteo > max_conteo:
            max_conteo = conteo
            moda_valor = valor
    return moda_valor


if __name__ == "__main__":
    datos = [2, 4, 4, 4, 5, 5, 7, 9]
    print("Media:", media(datos))
    print("Varianza:", varianza(datos))
    print("Desviación estándar:", desviacion_estandar(datos))
    print("Mediana:", mediana(datos))
    print("Moda:", moda(datos))