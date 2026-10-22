import numpy as np
import matplotlib.pyplot as plt


# Dados transcritos da folha de laboratório
posicao = np.arange(1, 11)

vp1 = np.array([1.9, 3.9, 6.0, 8.2, 10.3, 12.4, 14.5, 16.6, 18.7, 20.8])
vs1 = np.array([5.2, 11.2, 17.1, 23.1, 29.2, 35.2, 41.2, 47.1, 52.8, 58.6])

vp2 = np.array([2.1, 4.5, 7.0, 9.4, 11.9, 14.3, 16.8, 19.2, 21.7, 24.2])
vs2 = np.array([0.4, 1.0, 1.7, 2.3, 3.0, 3.6, 4.3, 4.9, 5.6, 6.3])

razao1 = vs1 / vp1
razao2 = vs2 / vp2

# ddof=1 fornece o desvio padrão amostral
media1 = np.mean(razao1)
media2 = np.mean(razao2)
desvio1 = np.std(razao1, ddof=1)
desvio2 = np.std(razao2, ddof=1)

teorica1 = 1200 / 300
teorica2 = 300 / 1200
erro1 = abs(media1 - teorica1) / teorica1 * 100
erro2 = abs(media2 - teorica2) / teorica2 * 100

print("Circuito 1")
print("Vs/Vp =", np.round(razao1, 4))
print(f"Média = {media1:.4f}")
print(f"Desvio padrão amostral = {desvio1:.4f}")
print(f"Diferença relativa para o valor teórico = {erro1:.2f}%")

print("\nCircuito 2")
print("Vs/Vp =", np.round(razao2, 4))
print(f"Média = {media2:.4f}")
print(f"Desvio padrão amostral = {desvio2:.4f}")
print(f"Diferença relativa para o valor teórico = {erro2:.2f}%")


# Gráficos de Vs em função de Vp
fig, eixos = plt.subplots(1, 2, figsize=(11, 4.6))

x1 = np.linspace(0, vp1.max() * 1.05, 200)
eixos[0].scatter(vp1, vs1, color="#1f77b4", label="Dados experimentais", zorder=3)
eixos[0].plot(x1, teorica1 * x1, "--", color="#d62728", label="Modelo ideal: $V_s=4V_p$")
eixos[0].plot(x1, media1 * x1, color="#2ca02c", label=fr"Razão média: $V_s={media1:.3f}V_p$")
eixos[0].set_title("Circuito 1: primário com 300 espiras")
eixos[0].set_xlabel("$V_p$ (V)")
eixos[0].set_ylabel("$V_s$ (V)")
eixos[0].grid(alpha=0.25)
eixos[0].legend(fontsize=8)

x2 = np.linspace(0, vp2.max() * 1.05, 200)
eixos[1].scatter(vp2, vs2, color="#1f77b4", label="Dados experimentais", zorder=3)
eixos[1].plot(x2, teorica2 * x2, "--", color="#d62728", label="Modelo ideal: $V_s=0{,}25V_p$")
eixos[1].plot(x2, media2 * x2, color="#2ca02c", label=fr"Razão média: $V_s={media2:.3f}V_p$")
eixos[1].set_title("Circuito 2: primário com 1200 espiras")
eixos[1].set_xlabel("$V_p$ (V)")
eixos[1].set_ylabel("$V_s$ (V)")
eixos[1].grid(alpha=0.25)
eixos[1].legend(fontsize=8)

fig.tight_layout()
fig.savefig("Figs/tensoes_transformador.png", dpi=300, bbox_inches="tight")
plt.close(fig)


# Comparação direta em painéis com escalas próprias para facilitar a leitura
fig, eixos = plt.subplots(1, 2, figsize=(9.5, 4.6))
for eixo, nome, teorica, media, desvio in zip(
    eixos,
    ["Circuito 1", "Circuito 2"],
    [teorica1, teorica2],
    [media1, media2],
    [desvio1, desvio2],
):
    eixo.bar(0, teorica, width=0.58, color="#9ecae1", label="Razão teórica")
    eixo.bar(1, media, width=0.58, yerr=desvio, capsize=5,
             color="#3182bd", label="Média experimental")
    eixo.set_xticks([0, 1], ["Teórica", "Experimental"])
    eixo.set_ylabel("Razão $V_s/V_p$")
    eixo.set_title(nome)
    eixo.set_ylim(0, max(teorica, media + desvio) * 1.18)
    eixo.grid(axis="y", alpha=0.25)

eixos[0].legend(loc="upper right")
fig.suptitle("Razões de transformação teóricas e experimentais")
fig.tight_layout()
fig.savefig("Figs/comparacao_razoes.png", dpi=300, bbox_inches="tight")
plt.close(fig)
