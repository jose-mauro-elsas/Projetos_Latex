from __future__ import annotations

from .config import PASTA_ANM, REPOSITORIO, UF_SIGMINE
from .downloader import baixar
from .util import arquivo_existente

BASE = "https://dadosabertos.anm.gov.br/SIGMINE/PROCESSOS_MINERARIOS/"


def baixar_sigmine() -> None:
    uf = UF_SIGMINE.upper()
    pasta_canonica = PASTA_ANM / "SIGMINE"

    # Também reconhece arquivos criados por versões antigas.
    pastas_verificadas = [
        pasta_canonica,
        REPOSITORIO / "03_ANM" / "SIGMINE",
    ]
    existente = arquivo_existente(
        pastas_verificadas,
        (f"*SIGMINE*{uf}*.zip", f"{uf}.zip"),
    )
    if existente:
        print(f"[JÁ EXISTE] {existente}")
        return

    baixar(f"{BASE}{uf}.zip", pasta_canonica / f"SIGMINE_{uf}.zip")
