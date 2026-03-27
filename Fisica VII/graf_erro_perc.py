import numpy as np
import matplotlib.pyplot as plt

resistores = ['R1', 'R2', 'R3', 'R4', 'R5']
nominal = np.array([47., 100., 150., 330., 470.])
medido  = np.array([46.6, 100., 153., 331., 473.])

epsilon = np.abs((medido - nominal)) / nominal * 100

fig, ax = plt.subplots()

barras = ax.bar(resistores, epsilon)

ax.set_title(r'Diferença percentual dos resistores')
ax.set_xlabel('Resistores')
ax.set_ylabel(r'$\epsilon$ (%)')
ax.axhline(0, linewidth=1)

for barra, e in zip(barras, epsilon):
    altura = barra.get_height()
    if altura >= 0:
        y_texto = altura + 0.01
        va = 'bottom'
    else:
        y_texto = altura - 0.01
        va = 'top'

    ax.text(
        barra.get_x() + barra.get_width()/2,
        y_texto,
        f'{e:.1f}%'.replace('.', ','),
        ha='center',
        va=va
    )

plt.show()