import matplotlib.pyplot as plt

cells = list(range(1, 11))
angles = [182.8, 188.1, 190.5, 192.6, 194.5, 196.0, 198.4, 201.0, 203.0, 205.2]
vel = [106.7, 154.2, 194.7, 204.2, 200.6, 186.7, 173.7, 160.9, 144.4, 130.0]

fig, axes = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

# gráfico superior: direção
axes[0].plot(cells, angles, marker='o')
axes[0].set_ylabel("Direção (graus)")
axes[0].set_title("Variação da direção com a profundidade")
axes[0].grid(True)

# gráfico inferior: velocidade
axes[1].plot(cells, vel, marker='o')
axes[1].set_xlabel("Célula")
axes[1].set_ylabel("Velocidade (mm/s)")
axes[1].set_title("Variação da velocidade com a profundidade")
axes[1].grid(True)

plt.tight_layout()
plt.savefig("direcao_velocidade_cells.png", dpi=300, bbox_inches="tight")
plt.close()