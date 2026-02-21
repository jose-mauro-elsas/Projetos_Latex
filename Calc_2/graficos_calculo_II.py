import matplotlib.pyplot as plt
import numpy as np

plt.figure("Gráfico da Parábola Horizontal")
plt.figure (figsize=(6, 4))
x = np.linspace(0, 10, 200)
plt.axis(ymin = -5)
plt.axis(ymax= 5)

y_pos = np.sqrt(2*x)
y_neg = -np.sqrt(2*x)
y1 = x - 4
plt.title("Área entre y=x+4 e y=raiz de 0.5x")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.plot(x, y_pos)
plt.plot(x, y_neg)
plt.plot(x, y1)

plt.show()