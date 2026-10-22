from __future__ import annotations

from pathlib import Path

from .config import PASTA_SGB, URL_SGB
from .downloader import baixar
from .util import arquivo_existente, escolher_link, listar_links

PAGINAS = (
    "https://geosgb.sgb.gov.br/downloads/",
    "https://geosgb.sgb.gov.br/geosgb/downloads.html",
)


def descobrir_mapa_brasil() -> str | None:
    if URL_SGB:
        return URL_SGB

    for pagina in PAGINAS:
        try:
            links = listar_links(pagina)
        except Exception:
            continue

        for termos in (
            ("mapa", "geologico", "brasil"),
            ("integracao", "geologica", "brasil"),
            ("litoestratigrafia", "brasil"),
        ):
            url = escolher_link(links, termos, (".zip", ".rar", ".7z"))
            if url:
                return url
    return None


def baixar_geologia() -> None:
    pasta = PASTA_SGB
    existente = arquivo_existente(
        [pasta],
        ("*.zip", "*.rar", "*.7z", "*.gpkg"),
    )
    if existente:
        print(f"[JÁ EXISTE] {existente}")
        return

    pasta.mkdir(parents=True, exist_ok=True)
    url = descobrir_mapa_brasil()

    if not url:
        instrucoes = pasta / "DOWNLOAD_MANUAL_SGB.txt"
        instrucoes.write_text(
            "A descoberta automática do arquivo geológico nacional falhou.\n"
            "Abra https://geosgb.sgb.gov.br/downloads/ e procure o produto "
            "nacional mais recente.\n"
            "Uma URL direta pode ser informada em URL_SGB, no config.py.\n",
            encoding="utf-8",
        )
        print(f"[AÇÃO MANUAL] {instrucoes}")
        return

    nome = Path(url.split("?")[0]).name or "Mapa_Geologico_Brasil.zip"
    baixar(url, pasta / nome)
