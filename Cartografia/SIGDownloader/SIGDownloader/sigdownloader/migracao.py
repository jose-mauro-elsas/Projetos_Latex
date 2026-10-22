from __future__ import annotations

import filecmp
import shutil
from pathlib import Path

from .config import (
    PASTA_ANM,
    PASTA_COPERNICUS,
    PASTA_GEBCO,
    PASTA_SGB,
    REPOSITORIO,
)


def _mover_conteudo(origem: Path, destino: Path) -> int:
    """Move o conteúdo sem sobrescrever nem apagar arquivos diferentes."""
    if not origem.exists():
        return 0

    movidos = 0
    for arquivo in origem.rglob("*"):
        if not arquivo.is_file():
            continue

        relativo = arquivo.relative_to(origem)
        novo = destino / relativo
        novo.parent.mkdir(parents=True, exist_ok=True)

        if novo.exists():
            if filecmp.cmp(arquivo, novo, shallow=False):
                arquivo.unlink()
                movidos += 1
                continue

            indice = 1
            candidato = novo.with_name(
                f"{novo.stem}_migrado_{indice}{novo.suffix}"
            )
            while candidato.exists():
                indice += 1
                candidato = novo.with_name(
                    f"{novo.stem}_migrado_{indice}{novo.suffix}"
                )
            novo = candidato

        shutil.move(str(arquivo), str(novo))
        movidos += 1

    for pasta in sorted(
        (p for p in origem.rglob("*") if p.is_dir()),
        key=lambda p: len(p.parts),
        reverse=True,
    ):
        try:
            pasta.rmdir()
        except OSError:
            pass

    try:
        origem.rmdir()
    except OSError:
        pass

    return movidos


def migrar_estrutura_antiga() -> None:
    migracoes = (
        (REPOSITORIO / "03_ANM" / "SIGMINE", PASTA_ANM / "SIGMINE"),
        (REPOSITORIO / "04_SGB" / "Geologia", PASTA_SGB),
        (REPOSITORIO / "05_GEBCO", PASTA_GEBCO),
        (REPOSITORIO / "06_COPERNICUS", PASTA_COPERNICUS),
    )

    total = 0
    for origem, destino in migracoes:
        quantidade = _mover_conteudo(origem, destino)
        if quantidade:
            print(
                f"[MIGRAÇÃO] {origem} -> {destino} "
                f"({quantidade} arquivo(s))"
            )
            total += quantidade

        pai = origem.parent
        if pai != REPOSITORIO and pai.exists():
            try:
                pai.rmdir()
            except OSError:
                pass

    if total:
        print("[OK] Estrutura antiga consolidada.")
