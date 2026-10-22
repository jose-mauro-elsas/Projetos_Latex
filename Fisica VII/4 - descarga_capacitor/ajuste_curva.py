import sys
from pathlib import Path

import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Pasta onde estao o script e a subpasta Figs
pasta_saida = Path(__file__).resolve().parent / "Figs"
pasta_saida.mkdir(exist_ok=True)


# Verificacao do ambiente
print(sys.executable)
print(f"SciPy: {scipy.__version__}")


# Dados experimentais
t = np.arange(0.0, 14.5, 0.5)

ddp = np.array([
    14.27, 8.53, 5.09, 2.97, 1.79, 1.071, 0.648, 0.4,
    0.245, 0.157, 0.103, 0.067, 0.044, 0.03, 0.0225,
    0.0169, 0.0132, 0.0108, 0.0092, 0.008, 0.0072,
    0.0065, 0.006, 0.0055, 0.0051, 0.0048, 0.0045,
    0.0043, 0.0041
])


# Primeiro grafico: somente os dados experimentais
fig_dados, ax_dados = plt.subplots(figsize=(7, 5))

ax_dados.scatter(t, ddp, color="blue")
ax_dados.set_xlabel("t (min)")
ax_dados.set_ylabel("DDP (V)")
ax_dados.set_title("Descarregamento do capacitor - dados experimentais")
ax_dados.grid(True, alpha=0.3)

fig_dados.tight_layout()
fig_dados.savefig(
    pasta_saida / "dados_experimentais.png",
    dpi=300,
    bbox_inches="tight"
)


# Modelo matematico: V(t) = a exp(-bt) + c
def modelo_exponencial(t, a, b, c):
    return a * np.exp(-b * t) + c


# Ajuste nao linear por minimos quadrados
parametros, covariancia = curve_fit(
    modelo_exponencial,
    t,
    ddp,
    p0=[14, 1, 0]
)

a, b, c = parametros


# Valores previstos nos tempos experimentais e coeficiente R^2
ddp_estimada = modelo_exponencial(t, a, b, c)

sq_residuos = np.sum((ddp - ddp_estimada) ** 2)
sq_total = np.sum((ddp - np.mean(ddp)) ** 2)
r_quadrado = 1 - sq_residuos / sq_total


# Constante de tempo e resistencia de entrada do voltimetro
capacitancia = 1000e-6  # F
tau_min = 1 / b
tau_s = 60 * tau_min
resistencia_ohm = tau_s / capacitancia

print(f"a = {a:.6f} V")
print(f"b = {b:.6f} min^-1")
print(f"c = {c:.6f} V")
print(f"R^2 = {r_quadrado:.6f}")
print(f"tau = {tau_min:.6f} min = {tau_s:.2f} s")
print(f"Rv = {resistencia_ohm:.2f} ohm")
print(f"Rv = {resistencia_ohm / 1000:.2f} kohm")


# Pontos para desenhar uma curva suave
t_curva = np.linspace(t.min(), t.max(), 300)
ddp_curva = modelo_exponencial(t_curva, a, b, c)


# Segundo grafico: dados experimentais e ajuste exponencial
fig, ax = plt.subplots(figsize=(7, 5))

ax.scatter(
    t,
    ddp,
    label="Dados experimentais",
    color="blue"
)

ax.plot(
    t_curva,
    ddp_curva,
    label="Ajuste exponencial",
    color="red"
)

ax.set_xlabel("t (min)")
ax.set_ylabel("DDP (V)")
ax.set_title("Descarregamento do capacitor")
ax.grid(True, alpha=0.3)
ax.legend()

fig.tight_layout()
fig.savefig(
    pasta_saida / "ajuste_exponencial.png",
    dpi=300,
    bbox_inches="tight"
)


# Mostra os dois graficos
plt.show()
