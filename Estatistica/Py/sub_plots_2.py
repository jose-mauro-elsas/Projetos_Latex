import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUTDIR = Path(r"C:\Latex_Projects\Estatistica\Figs")
OUTDIR.mkdir(parents=True, exist_ok=True)

x = np.linspace(-6, 6, 800)

sigma1 = 0.6   # mais estreita (pico maior)
sigma2 = 2.0   # mais larga (pico menor)

y1 = (1/(sigma1*np.sqrt(2*np.pi))) * np.exp(-0.5*((x/sigma1)**2))
y2 = (1/(sigma2*np.sqrt(2*np.pi))) * np.exp(-0.5*((x/sigma2)**2))

fig, ax = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

ax[0].plot(x, y1)
ax[0].set_title(r"Curva leptocúrtica")
ax[0].grid(True)

ax[1].plot(x, y2)
ax[1].set_title(r"Curva planicúrtica")
ax[1].grid(True)

# garante limites iguais (opcional, mas deixa “travado”)
ymax = max(y1.max(), y2.max())
for a in ax:
    a.set_xlim(x.min(), x.max())
    a.set_ylim(0, ymax*1.05)

fig.tight_layout()
fig.savefig(OUTDIR / "fig_lepto_plani.png", bbox_inches="tight")
plt.show()