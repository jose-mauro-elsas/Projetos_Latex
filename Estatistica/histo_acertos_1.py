import matplotlib.pyplot as plt
import numpy as np

freq = np.array([8, 12, 28, 32, 17, 3])      # frequências
xi   = np.array([45, 46, 47, 48, 49, 50])    # valores de Xi (centros)

fig, ax = plt.subplots()

ax.bar(xi, freq, width=1.0, align='center', edgecolor='k', linewidth=2)

ax.set_xlabel('Xi')
ax.set_ylabel('Frequência')
ax.set_xticks(xi)
ax.set_xlim(xi.min()-0.5, xi.max()+0.5)

plt.show()
