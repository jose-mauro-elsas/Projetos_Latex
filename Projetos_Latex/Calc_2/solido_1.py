import numpy as np
import matplotlib.pyplot as plt

# ===== Curva geratriz y=f(x) =====
x = np.linspace(0, 2.5, 200)
y = (x - 2)**2 + 1

# ===== Rotação em torno do eixo x =====
theta = np.linspace(0, 2*np.pi, 200)

X, TH = np.meshgrid(x, theta)                 # grade para varrer a rotação
R = (X - 2)**2 + 1                            # raio = y = f(x)
Y = R * np.cos(TH)
Z = R * np.sin(TH)

# ===== Plot 3D =====
fig = plt.figure("Sólido de Revolução", figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(X, Y, Z, linewidth=0, antialiased=True, alpha=0.9)

ax.set_title("Sólido de revolução de y=(x-2)^2+1 em torno do eixo x")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()