import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4.0, 4.0, 400)

sigma = 1.0
y = (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-0.5*((x/sigma)**2)) + 0.02

fig, ax = plt.subplots(figsize=(6, 4))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position(('data', 0))

ax.set_title("Curva leptocúrtica")
ax.plot(x, y)
ax.grid(True)
ax.set_xlabel("x")
ax.set_ylabel("y")

ax.set_ylim(0, 0.45)   # fixa a escala do y para não “enganar” visualmente
plt.show()