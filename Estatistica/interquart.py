# Importação das bibliotecas
import matplotlib.pyplot as plt
import numpy as np

#Gerando os valores de x
x = np.linspace(-4.0, 4.0, 200)


#f(x)
y = ((np.sqrt(np.pi))**(-1))*((np.exp(-(x**2)/2))+0.05)

fig, ax = plt.subplots(figsize=(6, 4))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.annotate(
    '',
    xy=(-4, 1), xytext=(-4, 0),
    xycoords=('data', 'axes fraction'),
    arrowprops=dict(arrowstyle='-|>', linewidth=1)
)


ax.spines['bottom'].set_position(('data', 0))   # eixo x em y=0


ax.set_title("Distribuição Interquartílica")
ax.plot(x, y, color="blue")
ax.grid(True)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.plot([-2, -2], [0, 0.10456423626596997], color='red', linewidth=1, linestyle=(0, (8, 6)))

ax.plot([ 0,  0], [0, 0.5923990627251441], color='red', linewidth=1, linestyle=(0, (8, 6)))

ax.plot([ 2,  2], [0, 0.10456423626596997], color='red', linewidth=1, linestyle=(0, (8, 6)))
plt.show()

