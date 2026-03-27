import numpy as np
import matplotlib.pyplot as plt

x1 = (2.1, 4.1, 6.2, 8.3, 10.5, 12.5, 14.7, 16.8, 18.9, 21.0)
#print(x)

y1 = (2.64, 5.53, 8.46, 11.4, 14.35, 17.31, 20.2, 23.1, 26.1, 29.1)

plt.title('Gráfico 1: VCC vs. VCA')
plt.xlabel('Tensão de Corrente Alternada (VCA)')
plt.ylabel('Tensão de corrente contínua (VCC)')
plt.plot(x1, y1, marker = 'o')
plt.grid()
plt.show()