import random


def simular_dado(n):
    """Lanza un dado n veces y devuelve un diccionario {cara: veces}."""
    frecuencias = {cara: 0 for cara in range(1, 7)}
    for _ in range(n):
        cara = random.randint(1, 6)
        frecuencias[cara] += 1
    return frecuencias


def analizar(n):
    frecuencias = simular_dado(n)

    print(f"\n--- {n} lanzamientos ---")
    for cara, veces in frecuencias.items():
        print(f"Cara {cara}: {veces} veces, frecuencia relativa = {veces / n:.4f}")

    # La media se calcula con las frecuencias: suma(cara * veces) / n
    media = sum(cara * veces for cara, veces in frecuencias.items()) / n
    print(f"Media observada: {media:.4f}")
    print(f"Valor esperado:  3.5")
    print(f"Error absoluto:  {abs(media - 3.5):.4f}")


if __name__ == "__main__":
    for n in [100, 10_000, 1_000_000]:
        analizar(n)
        