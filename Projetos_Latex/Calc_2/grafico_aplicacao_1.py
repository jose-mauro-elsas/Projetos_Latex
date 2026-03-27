import numpy as np
import matplotlib.pyplot as plt

#===================================
# Dados duas curvas
#===================================
a, b =1.0, 5.5
x=np.linspace (a, b, 600)
#curva de cima e de baixo, só para parecer com o desenho
f=2.2 + 0.35*np.sin(1.2*(x-a)) + 0.15*np.sin(2.7*(x-a)+0.6)
g = 1.2 + 0.25*np.cos(1.1*(x-a) + 0.4) - 0.10*np.sin(2.4*(x-a))

# ----------------------------
# 2) Figura / eixos
# ----------------------------
fig, ax = plt.subplots(figsize=(9, 4))

# (opcional) esconder a "caixa"
for s in ["top", "right", "left", "bottom"]:
    ax.spines[s].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

# Limites (garanta que 0 está dentro!)
xmin, xmax = -0.5, 8.5
ymin, ymax = -0.2, 3.2
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

# Eixos com seta se encontrando em (0,0)
ax.annotate("", xy=(xmax-0.2, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", lw=2))
ax.annotate("", xy=(0, ymax-0.2), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", lw=2))

# ----------------------------
# 3) Desenho das curvas e da região hachurada
# ----------------------------
ax.plot(x, f, lw=2, color="black")
ax.plot(x, g, lw=2, color="black")

# Região entre curvas (hachura)
ax.fill_between(
    x, g, f,
    facecolor="none",
    edgecolor="black",
    hatch="//",
    linewidth=0.0,   # evita “dupla borda” feia; as curvas já são a borda
)

# Linhas verticais em a e b
ax.plot([a, a], [0, g[0]], lw=2, color="black")
ax.plot([b, b], [0, g[-1]], lw=2, color="black")

# Marcas e rótulos a e b no eixo x
ax.text(a, -0.12, "a", ha="center", va="top", fontsize=14)
ax.text(b, -0.12, "b", ha="center", va="top", fontsize=14)

# ----------------------------
# 4) Texto da integral (à direita, como no caderno)
# ----------------------------
ax.text(6.0, 1.7, r"$A \;=\; \int_a^b (f(x)-g(x))\,dx$", fontsize=18)
plt.tight_layout()
plt.show()