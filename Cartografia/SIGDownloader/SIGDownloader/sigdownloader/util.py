from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

CABECALHOS = {
    "User-Agent": "SIGDownloader/0.4.0 (uso acadêmico; dados públicos oficiais)"
}


def criar_pasta(pasta: Path) -> Path:
    pasta.mkdir(parents=True, exist_ok=True)
    return pasta


def obter_sopa(url: str, timeout: int = 60) -> BeautifulSoup:
    resposta = requests.get(url, headers=CABECALHOS, timeout=timeout)
    resposta.raise_for_status()
    return BeautifulSoup(resposta.text, "html.parser")


def listar_links(url: str, timeout: int = 60) -> list[str]:
    sopa = obter_sopa(url, timeout=timeout)
    return [
        urljoin(url, elemento["href"])
        for elemento in sopa.find_all("a", href=True)
    ]


def escolher_link(
    links: list[str],
    incluir: tuple[str, ...] = (),
    extensoes: tuple[str, ...] = (),
    excluir: tuple[str, ...] = (),
) -> str | None:
    candidatos: list[str] = []
    for link in links:
        texto = link.lower()
        if incluir and not all(t.lower() in texto for t in incluir):
            continue
        if extensoes and not texto.endswith(tuple(e.lower() for e in extensoes)):
            continue
        if excluir and any(t.lower() in texto for t in excluir):
            continue
        candidatos.append(link)

    if not candidatos:
        return None

    def chave(link: str):
        numeros = tuple(int(n) for n in re.findall(r"\d+", link))
        return numeros, link.lower()

    return max(candidatos, key=chave)


def arquivo_existente(
    pastas: list[Path],
    padroes: tuple[str, ...],
) -> Path | None:
    candidatos: list[Path] = []
    for pasta in pastas:
        if not pasta.exists():
            continue
        for padrao in padroes:
            candidatos.extend(
                p for p in pasta.rglob(padrao)
                if p.is_file() and p.stat().st_size > 0
            )
    if not candidatos:
        return None
    return max(candidatos, key=lambda p: p.stat().st_mtime)


def tamanho_legivel(numero: int) -> str:
    valor = float(numero)
    for unidade in ("B", "KB", "MB", "GB", "TB"):
        if valor < 1024 or unidade == "TB":
            return f"{valor:.1f} {unidade}"
        valor /= 1024
    return f"{numero} B"
