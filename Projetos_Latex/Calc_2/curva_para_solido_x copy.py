import numpy as np
import matplotlib.pyplot as plt

plt.figure("Gráfico 1")
x = np.linspace(0, 2.5, 200)
y = ((x-2)**2)+1
plt.title("Gráfico para sólido de revolução ")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.plot(x, y)
plt.show()