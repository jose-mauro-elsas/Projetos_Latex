import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6, 4))


x = np.linspace (-4, 5, 400)
y1=np.exp(x)
y2=np.sqrt(x)

plt.subplot (1, 2, 1)
plt.title("exp(x)")

plt.grid(True)
plt.plot(x, y1)

plt.subplot (1, 2, 2)
plt.title ("raiz de x")
plt.grid(True)
plt.plot(x, y2)
plt.show()


