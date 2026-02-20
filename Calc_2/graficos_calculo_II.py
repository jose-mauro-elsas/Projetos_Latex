import matplotlib.pyplot as plt
import numpy as np

plt.figure("Gráfico da Parábola Horizontal")
x = np.linspace(0, 10, 200)
y = np.sqrt(2*x)
plt.title("Parábola horizontal")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.plot(x, y)

plt.show()