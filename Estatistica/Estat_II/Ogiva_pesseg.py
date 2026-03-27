import numpy as np
import matplotlib.pyplot as plt

dados = [11.1, 4.4, 10.7, 23.5, 26.2, 12.5, 6.1, 15.8, 14.8, 3.5,
         32.4, 27.5, 25.0, 22.6, 16.2, 7.8, 32.8, 18.2, 16.0, 14.5,
         21.0, 18.5, 12.2, 19.1, 3.2, 16.4, 16.4, 12.6, 7.4, 8.1,
         11.2, 15.1, 4.7, 9.2, 12.9, 22.3, 6.0, 13.7, 10.0, 19.1]

bins = [3, 8, 13, 18, 23, 28, 33]
pesos = np.ones(len(dados)) / len(dados) * 100

# histograma
plt.hist(dados, bins=bins, weights=pesos, edgecolor='black')

# frequências por classe
freq_abs, _ = np.histogram(dados, bins=bins)
freq_rel = freq_abs / len(dados) * 100
freq_acum = np.cumsum(freq_rel)

# ogiva começando em 0
x_acum = bins
y_acum = np.concatenate(([0], freq_acum))

plt.plot(x_acum, y_acum, marker='o')

# ticks no ponto médio das classes
ticks = [(bins[i] + bins[i+1]) / 2 for i in range(len(bins)-1)]
rotulos = [f'{bins[i]}-{bins[i+1]}' for i in range(len(bins)-1)]
plt.xticks(ticks, rotulos)

plt.title('Histograma e frequência acumulada da produção de 40 pessegueiros')
plt.xlabel('Classes de produção')
plt.ylabel('Frequência (%)')

plt.show()