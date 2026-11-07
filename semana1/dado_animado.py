import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

LANZAMIENTOS_POR_FRAME = 10
FRAMES = 300
TOTAL = LANZAMIENTOS_POR_FRAME * FRAMES

frecuencias = [0] * 6
n = 0
suma = 0
historial_n = []
historial_media = []

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Gráfico 1: frecuencias relativas por cara
caras = range(1, 7)
barras = ax1.bar(caras, [0] * 6, color="steelblue")
ax1.axhline(1 / 6, color="red", linestyle="--", label="1/6 teórico")
ax1.set_ylim(0, 0.4)
ax1.set_xlabel("Cara")
ax1.set_ylabel("Frecuencia relativa")
ax1.legend()

# Gráfico 2: media acumulada
(linea,) = ax2.plot([], [], color="steelblue")
ax2.axhline(3.5, color="red", linestyle="--", label="Valor esperado 3.5")
ax2.set_xlim(0, TOTAL)
ax2.set_ylim(1, 6)
ax2.set_xlabel("Número de lanzamientos")
ax2.set_ylabel("Media acumulada")
ax2.legend()


def actualizar(frame):
    global n, suma
    for _ in range(LANZAMIENTOS_POR_FRAME):
        cara = random.randint(1, 6)
        frecuencias[cara - 1] += 1
        suma += cara
        n += 1

    for barra, f in zip(barras, frecuencias):
        barra.set_height(f / n)

    historial_n.append(n)
    historial_media.append(suma / n)
    linea.set_data(historial_n, historial_media)
    fig.suptitle(f"Lanzamientos: {n}   Media: {suma / n:.3f}")


animacion = FuncAnimation(fig, actualizar, frames=FRAMES, interval=30, repeat=False)

animacion.save("dado_animado.mp4", writer="ffmpeg", fps=30)

plt.tight_layout()
plt.show()
animacion.save("dado.mp4", writer="ffmpeg", fps=30, dpi=100,
               progress_callback=lambda i, n: print(f"Frame {i + 1}/{n}") if i % 30 == 0 else None)