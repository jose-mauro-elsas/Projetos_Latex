import numpy as np
import matplotlib.pyplot as plt

plt.figure("Gráfico 1")
x = np.linspace(0.5, 2.5, 200)
c = 1.0
y = np.full_like(x, c)

plt.plot(x, y)
plt.title("Gráfico para sólido de revolução ")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.plot(x, y)
plt.show()
