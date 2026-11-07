import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Ejercicio 1: suma de dos dados (10 000 veces)
sumas = rng.integers(1, 7, size=10_000) + rng.integers(1, 7, size=10_000)
valores = np.arange(2, 13)
teorico = np.array([6 - abs(k - 7) for k in valores]) / 36

ax1.hist(sumas, bins=np.arange(1.5, 13.5), density=True, alpha=0.7, label="Simulación")
ax1.plot(valores, teorico, "ro-", label="Teórica")
ax1.set_title("Suma de dos dados")
ax1.set_xlabel("Suma")
ax1.legend()

# Ejercicio 2: promedio de 30 lanzamientos, repetido 5 000 veces
n, repeticiones = 30, 5_000
promedios = rng.integers(1, 7, size=(repeticiones, n)).mean(axis=1)

mu, sigma = 3.5, (35 / 12) ** 0.5
sigma_prom = sigma / np.sqrt(n)
x = np.linspace(promedios.min(), promedios.max(), 200)
normal = np.exp(-((x - mu) ** 2) / (2 * sigma_prom**2)) / (sigma_prom * np.sqrt(2 * np.pi))

ax2.hist(promedios, bins=40, density=True, alpha=0.7, label="Simulación")
ax2.plot(x, normal, "r-", label="Normal(3.5, σ/√30)")
ax2.set_title("Promedio de 30 lanzamientos")
ax2.legend()

plt.tight_layout()
plt.show()
