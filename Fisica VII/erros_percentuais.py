import numpy as np
import matplotlib.pyplot as plt

x_labels = ['R1', 'R2', 'R3', 'R4', 'R5']
y1 = [47., 100., 150., 330., 470.]
y2 = [46.6, 100., 153., 331., 473.]

x = np.arange(len(x_labels))   # posições numéricas: 0,1,2,3,4
largura = 0.35

plt.figure()

plt.bar(x - largura/2, y1, width=largura, label='Nominal')
plt.bar(x + largura/2, y2, width=largura, label='Lido')

plt.title('Gráfico comparativo: nominal vs. lido')
plt.xlabel('Resistores')
plt.ylabel(r'Resistência ($\Omega$)')
plt.xticks(x, x_labels)
plt.legend()

plt.show()