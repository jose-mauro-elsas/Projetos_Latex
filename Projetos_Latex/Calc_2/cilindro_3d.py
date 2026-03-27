import numpy as np
import matplotlib.pyplot as plt

# resolução
Ntheta = 200
Ny = 60

theta = np.linspace(0, 2*np.pi, Ntheta)
y = np.linspace(0, 2, Ny)  # comprimento do cilindro ao longo de y

Theta, Y = np.meshgrid(theta, y)

r = 0.6  # raio do cilindro

# círculo no plano xz
X = r * np.cos(Theta)
Z = r * np.sin(Theta)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(X, Y, Z, alpha=0.5, edgecolor='k', linewidth=0.2)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Cilindro em torno do eixo y")

plt.show()