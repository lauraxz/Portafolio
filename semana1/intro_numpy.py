import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# 1. Arrays y operaciones vectorizadas
a = np.array([2, 4, 4, 4, 5, 5, 7, 9])
print("Media:", a.mean())
print("Varianza:", a.var())              # poblacional (ddof=0)
print("Varianza muestral:", a.var(ddof=1))
print("Desv. estándar:", a.std())

# 2. Dado vectorizado: un millón de lanzamientos sin ciclo for
lanzamientos = rng.integers(1, 7, size=1_000_000)
print("Media del dado:", lanzamientos.mean())

# 3. Frecuencias relativas
caras, conteos = np.unique(lanzamientos, return_counts=True)
plt.bar(caras, conteos / lanzamientos.size)
plt.axhline(1 / 6, color="pink", linestyle="--")
plt.xlabel("Cara")
plt.ylabel("Frecuencia relativa")
plt.show()