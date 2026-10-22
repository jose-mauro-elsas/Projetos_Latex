from __future__ import annotations

from .config import (
    LESTE,
    NORTE,
    OESTE,
    PASTA_GEBCO,
    SUL,
    URL_GEBCO,
)
from .downloader import baixar
from .util import arquivo_existente


def preparar_gebco() -> None:
    pasta = PASTA_GEBCO
    existente = arquivo_existente(
        [pasta],
        ("*.tif", "*.tiff", "*.nc", "*.zip"),
    )
    if existente:
        print(f"[JÁ EXISTE] {existente}")
        return

    pasta.mkdir(parents=True, exist_ok=True)

    if URL_GEBCO:
        baixar(URL_GEBCO, pasta / "GEBCO_recorte.zip")
        return

    instrucoes = pasta / "DOWNLOAD_GEBCO.txt"
    instrucoes.write_text(
        "GEBCO — recorte batimétrico\n"
        "Abra https://download.gebco.net/\n\n"
        f"West:  {OESTE}\nEast:  {LESTE}\n"
        f"South: {SUL}\nNorth: {NORTE}\n\n"
        "Formato recomendado: GeoTIFF ou NetCDF.\n"
        "Não baixe a grade global sem necessidade.\n",
        encoding="utf-8",
    )
    print(f"[AÇÃO MANUAL] {instrucoes}")
