from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from .config import REPOSITORIO
from .util import tamanho_legivel

BASES = [
    ("Malhas territoriais", "IBGE", ["01_IBGE/Malhas"]),
    ("BC250", "IBGE", ["02_IBGE_BC250"]),
    ("População", "IBGE", ["03_IBGE_POPULACAO"]),
    ("SIGMINE", "ANM", ["04_ANM/SIGMINE"]),
    ("Geologia", "SGB", ["05_SGB/Geologia"]),
    ("Batimetria", "GEBCO", ["06_OCEANOGRAFIA/GEBCO"]),
    ("Temperatura e correntes", "Copernicus", ["06_OCEANOGRAFIA/Copernicus"]),
]

IGNORAR_PREFIXOS = ("DOWNLOAD_", "LEIA-ME")


def _arquivos_reais(pastas: list[str]) -> list[Path]:
    arquivos: list[Path] = []
    for relativa in pastas:
        pasta = REPOSITORIO / relativa
        if pasta.exists():
            arquivos.extend(
                p for p in pasta.rglob("*")
                if p.is_file()
                and p.stat().st_size > 0
                and not p.name.upper().startswith(IGNORAR_PREFIXOS)
            )
    return arquivos


def gerar_catalogo() -> None:
    registros = []
    for nome, instituicao, pastas in BASES:
        arquivos = _arquivos_reais(pastas)
        registros.append({
            "nome": nome,
            "instituicao": instituicao,
            "pastas_verificadas": pastas,
            "status": "instalado" if arquivos else "pendente",
            "arquivos": [
                {
                    "caminho": str(p.relative_to(REPOSITORIO)),
                    "tamanho_bytes": p.stat().st_size,
                    "modificado_em": datetime.fromtimestamp(
                        p.stat().st_mtime
                    ).isoformat(timespec="seconds"),
                }
                for p in arquivos
            ],
        })

    REPOSITORIO.mkdir(parents=True, exist_ok=True)
    destino = REPOSITORIO / "catalogo_sig.json"
    destino.write_text(
        json.dumps(registros, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"[OK] Catálogo local: {destino}")


def mostrar_status() -> None:
    print("\nSTATUS DO REPOSITÓRIO")
    print("-" * 82)
    if not REPOSITORIO.exists():
        print("O repositório ainda não existe.")
        return

    for nome, instituicao, pastas in BASES:
        arquivos = _arquivos_reais(pastas)
        tamanho = sum(p.stat().st_size for p in arquivos)
        estado = "INSTALADO" if arquivos else "PENDENTE"
        print(
            f"{estado:<10} {instituicao:<12} {nome:<28} "
            f"{len(arquivos):>4} arquivo(s)  {tamanho_legivel(tamanho):>10}"
        )
