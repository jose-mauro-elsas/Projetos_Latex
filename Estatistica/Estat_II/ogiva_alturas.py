import numpy as np
import matplotlib.pyplot as plt

dados = [162, 164, 170, 160, 166, 163, 165, 157, 158, 169,
         148, 159, 176, 163, 152, 166, 175, 157, 164, 172,
         169, 155, 157, 164, 172, 154, 163, 165, 178, 165,
         170, 171, 158, 150, 162, 166, 172, 158, 168, 164]

bins = [148, 154, 160, 166, 172, 178]
pesos = np.ones(len(dados)) / len(dados) * 100

plt.hist(dados, bins=bins, weights=pesos, edgecolor='black')

x_acum = [148, 154, 160, 166, 172, 178]
y_acum = [0.0, 7.5, 30.0, 62.5, 85.0, 100.0]

plt.plot(x_acum, y_acum, marker='o')

plt.xticks(
    [151, 157, 163, 169, 175],
    ['148–154', '154–160', '160–166', '166–172', '172–178']
)

plt.title('Histograma e Frequência Acumulada')
plt.xlabel('Classes de altura')
plt.ylabel('Frequência (%)')

plt.show()