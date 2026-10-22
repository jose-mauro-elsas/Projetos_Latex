from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urljoin

from .config import PASTA_BC250, PASTA_MALHAS, PASTA_POPULACAO
from .downloader import baixar
from .util import arquivo_existente, escolher_link, listar_links

MALHAS_BASE = (
    "https://geoftp.ibge.gov.br/organizacao_do_territorio/"
    "malhas_territoriais/malhas_municipais/"
)
BC250_BASE = (
    "https://geoftp.ibge.gov.br/cartas_e_mapas/"
    "bases_cartograficas_continuas/bc250/"
)
POPULACAO_BASE = "https://ftp.ibge.gov.br/Estimativas_de_Populacao/"


def _diretorio_mais_recente(base: str, expressao: str) -> str | None:
    candidatos = []
    for link in listar_links(base):
        nome = link.rstrip("/").split("/")[-1]
        correspondencia = re.fullmatch(expressao, nome, flags=re.IGNORECASE)
        if correspondencia and link.endswith("/"):
            ano = int(correspondencia.group(1))
            candidatos.append((ano, link))
    return max(candidatos)[1] if candidatos else None


def _diretorio_brasil(ano_url: str) -> str | None:
    links = listar_links(ano_url)
    for nome in ("brasil", "br"):
        encontrados = [
            link for link in links
            if link.endswith("/")
            and link.rstrip("/").split("/")[-1].lower() == nome
        ]
        if encontrados:
            return encontrados[0]
    return None


def baixar_malhas() -> None:
    ano_url = _diretorio_mais_recente(MALHAS_BASE, r"municipio_(\d{4})")
    if not ano_url:
        print("[ERRO] Ano mais recente das malhas não localizado.")
        return

    brasil_url = _diretorio_brasil(ano_url)
    if not brasil_url:
        print("[ERRO] Diretório Brasil das malhas não localizado.")
        return

    links = listar_links(brasil_url)
    itens = (
        ("BR_Pais.zip", ("br_pais_",), ("BR_Pais*.zip",)),
        ("BR_UF.zip", ("br_uf_",), ("BR_UF*.zip",)),
        ("BR_Municipios.zip", ("br_municipios_",), ("BR_Municipios*.zip",)),
    )

    for nome_local, termos, padroes in itens:
        existente = arquivo_existente([PASTA_MALHAS], padroes)
        url = escolher_link(links, termos, (".zip",))
        if not url:
            print(f"[NÃO LOCALIZADO] {nome_local}")
            continue
        baixar(url, PASTA_MALHAS / nome_local, existente=existente)


def baixar_bc250() -> None:
    existente = arquivo_existente(
        [PASTA_BC250],
        ("*BC250*GPKG*.zip", "*bc250*gpkg*.zip", "*.gpkg.zip", "BC250_GPKG.zip"),
    )
    if existente:
        print(f"[JÁ EXISTE] {existente}")
        return

    versao = _diretorio_mais_recente(BC250_BASE, r"versao(\d{4})")
    if not versao:
        print("[ERRO] Versão da BC250 não localizada.")
        return

    # O IBGE já usou grafias diferentes para esta pasta.
    for nome_pasta in ("geopackage/", "geopakage/"):
        pagina = urljoin(versao, nome_pasta)
        try:
            links = listar_links(pagina)
        except Exception:
            continue

        url = (
            escolher_link(links, ("gpkg",), (".zip",))
            or escolher_link(links, ("bc250",), (".zip",))
        )
        if url:
            baixar(url, PASTA_BC250 / "BC250_GPKG.zip")
            return

    print("[ERRO] GeoPackage da BC250 não localizado.")


def baixar_populacao() -> None:
    existente = arquivo_existente(
        [PASTA_POPULACAO],
        ("*Populacao*.xls*", "POP*.xls*", "*.ods"),
    )
    if existente:
        print(f"[JÁ EXISTE] {existente}")
        return

    ano_url = _diretorio_mais_recente(
        POPULACAO_BASE,
        r"Estimativas_(\d{4})",
    )
    if not ano_url:
        print("[ERRO] Diretório mais recente de população não localizado.")
        return

    links = listar_links(ano_url)
    url = escolher_link(
        links,
        ("pop",),
        (".xls", ".xlsx", ".ods"),
        excluir=("dou",),
    )
    if not url:
        url = escolher_link(links, (), (".xls", ".xlsx", ".ods"))
    if not url:
        print("[ERRO] Planilha populacional não localizada.")
        return

    extensao = Path(url.split("?")[0]).suffix or ".xls"
    baixar(url, PASTA_POPULACAO / f"Estimativas_Populacao{extensao}")
