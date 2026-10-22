# boxplot_bowley.py
# Gera um boxplot (A, B, D) em Matplotlib e salva em PDF/PNG para incluir no LaTeX.
# (sem seaborn; sem definir cores)

from pathlib import Path
import matplotlib.pyplot as plt

# ----------------------------
# Dados (os mesmos do seu texto)
# ----------------------------
A = [2, 3, 3, 4, 4, 5, 6, 7, 20]                 # assimetria positiva (cauda à direita)
B = [6, 7, 8, 9, 10, 11, 12, 13, 14]             # aproximadamente simétrico
D = [10, 12, 14, 20, 25, 26, 30, 35, 60]         # exemplo do Bowley

data = [A, B, D]
labels = ["A", "B", "D"]

# ----------------------------
# Saída
# ----------------------------
OUTDIR = Path("figs")  # ajuste se quiser (ex.: Path("Estatistica/figs"))
OUTDIR.mkdir(parents=True, exist_ok=True)

pdf_path = OUTDIR / "boxplot_bowley.pdf"
png_path = OUTDIR / "boxplot_bowley.png"

# ----------------------------
# Figura
# ----------------------------
fig, ax = plt.subplots(figsize=(8, 3.2))

bp = ax.boxplot(
    data,
    labels=labels,
    vert=False,          # boxplots horizontais (combina com seu layout anterior)
    whis=1.5,            # "bigodes" padrão (1.5*IQR)
    showmeans=False,     # se quiser média, mude para True
    showfliers=True,     # mostra outliers como pontos
)

ax.set_xlabel("valores")
ax.set_title("Boxplots: A, B e D")

ax.grid(True, which="major")
ax.set_axisbelow(True)

# Ajuste fino de margens (evita cortar rótulos)
fig.tight_layout()

# ----------------------------
# Salvar
# ----------------------------
fig.savefig(pdf_path)                 # ótimo para LaTeX
fig.savefig(png_path, dpi=200)        # útil para preview rápido
plt.close(fig)

print(f"OK: {pdf_path}")
print(f"OK: {png_path}")