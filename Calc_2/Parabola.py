import numpy as np
import matplotlib.pyplot as plt


# Parábola : y = x^2
x = np.linspace(0, 5, 100)
y = x**2

fig, ax = plt.subplots()
ax.plot(x, y)

# 1. Move o eixo esquerdo e o de baixo para a origem (0,0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# 2. Esconde as bordas superior (top) e direita (right)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 3. traça linhas verticais.
x_linhas_verticais = np.linspace(0.1, 5.0, 25)

# Armazenar todos os comprimentos calculados
comprimentos_calculados = []

for linha_vertical in x_linhas_verticais:
    # Cada 'comprimento' deve ser igual ao seu valor 'y' correspondente na parábola (y = x^2)
    comprimento = linha_vertical**2
    comprimentos_calculados.append(comprimento)
    # Desenha a linha vertical do eixo x até a curva
    ax.vlines(linha_vertical, 0, comprimento, color='green', linestyle=':', alpha=0.7)

print("Todos os comprimentos calculados para as linhas verticais:", comprimentos_calculados)

# Adiciona uma linha vertical vermelha tracejada no x = 2 (exemplo, pode ser removido se não for necessário)
# ax.axvline(x=2, color='red', linestyle='--', alpha=0.5)

# Adiciona fill_between para preencher a área sob a curva
# Filtra os pontos x e y que estão dentro do intervalo de x_linhas_verticais
# O fill_between usa os valores do 'x' original da parábola para um preenchimento contínuo
fill_x = x[(x >= x_linhas_verticais.min()) & (x <= x_linhas_verticais.max())]
fill_y = fill_x**2
ax.fill_between(fill_x, fill_y, color='skyblue', alpha=0.3)

plt.grid("both")
plt.show()

