def media(datos):
    """Media aritmética de una lista de números."""
    return sum(datos) / len(datos)


def varianza(datos):
    """Varianza poblacional: promedio de las desviaciones al cuadrado."""
    m = media(datos)
    suma = 0
    for x in datos:
        suma += (x - m) ** 2
    return suma / len(datos)


datos = [2, 4, 4, 4, 5, 5, 7, 9]
print("Media:", media(datos))
print("Varianza:", varianza(datos))

def varianza_muestral(datos):
    """Varianza muestral: promedio de las desviaciones al cuadrado con n-1 en el denominador."""
    m = media(datos)
    suma = 0
    for x in datos:
        suma += (x - m) ** 2
    return suma / (len(datos) - 1)

print("Varianza muestral:", varianza_muestral(datos))