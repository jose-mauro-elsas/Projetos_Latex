import numpy as np
import matplotlib.pyplot as plt

plt.figure("Gráfico do Cosseno")
x = np.linspace(0, 2*np.pi, 360)
y = np.cos(x)
plt.title("Gráfico do Cosseno")
plt.xlabel("Ângulo (rad)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.plot(x, y)

plt.figure("Gráfico do Seno")
x = np.linspace(0, 2*np.pi, 360)
y = np.sin(x)
plt.title("Gráfico do Seno")
plt.xlabel("Ângulo (rad)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.plot(x, y)

plt.figure("Gráfico da Tangente")
x = np.linspace(0, 2*np.pi, 360)
y = np.tan(x)
plt.title("Gráfico da Tangente")
plt.xlabel("Ângulo (rad)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.plot(x, y)

plt.show()