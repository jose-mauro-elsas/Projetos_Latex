import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Funções
# ----------------------------
# Reta: ajuste como quiser (ex.: y = x + 4)
m, c = 1.0, -4.0

# Domínio
x = np.linspace(0, 8.5, 10)
y_line = m*x + c

#cor das curvas
#plt.plot(y_line, color='red')

# Parábola "deitada": y = ±sqrt(2x)
x_par = np.linspace(0, 8.5, 600)

y_par_pos = np.sqrt(2*x_par)
y_par_neg = -np.sqrt(2*x_par)
plt.grid(True)
# ----------------------------
# Figura
# ----------------------------
fig, ax = plt.subplots(figsize=(9, 4))

# Limites (ajuste conforme o que você quer enquadrar)
ax.set_xlim(-0.5, 10)
ax.set_ylim(-5, 6.0)

# ----------------------------
# Cara "PGF": spines e eixos em zero
# ----------------------------
""" ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Eixos passando por (0,0)
ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))

# Linha do eixo mais fina
ax.spines["bottom"].set_linewidth(1.0)
ax.spines["left"].set_linewidth(1.0)

# Ticks só em baixo e esquerda (PGF-like)
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left") """

# (Opcional) simplificar ticks
# ax.set_xticks([0, 2, 4, 6, 8])
# ax.set_yticks([-2, 0, 2, 4, 6])

# ----------------------------
# Setas nas pontas dos eixos (sem "tampar" o desenho)
# ----------------------------
xmin, xmax = ax.get_xlim()
ymin, ymax = ax.get_ylim()

# seta do eixo x
ax.annotate(
    "", xy=(xmax, 0), xytext=(xmax-0.25, 0),
    arrowprops=dict(arrowstyle="->", lw=1.0, color="black"),
    clip_on=False
)

# seta do eixo y
ax.annotate(
    "", xy=(0, ymax), xytext=(0, ymax-0.35),
    arrowprops=dict(arrowstyle="->", lw=1.0, color="black"),
    clip_on=False
)

# ----------------------------
# Plots (curvas por cima do eixo)
# ----------------------------
ax.plot(x, y_line, lw=2, color="black", zorder=3, label=r"$y=x+4$")
ax.plot(x_par, y_par_pos, lw=2, color="black", zorder=3, label=r"$y^2=2x$")
ax.plot(x_par, y_par_neg, lw=2, color="black", zorder=3)

# Rótulos discretos (tipo PGF)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")

# Grade leve (opcional)
# ax.grid(True, linewidth=0.5, alpha=0.3)

# Evita que o layout mexa demais (mais previsível que tight_layout)
plt.subplots_adjust(left=0.06, right=0.98, bottom=0.14, top=0.95)

plt.show()