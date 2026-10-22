from __future__ import annotations

from pathlib import Path
import requests

from .util import CABECALHOS, criar_pasta, tamanho_legivel


def baixar(
    url: str,
    destino: Path,
    *,
    existente: Path | None = None,
    sobrescrever: bool = False,
    timeout: int = 120,
) -> Path | None:
    criar_pasta(destino.parent)

    if existente and existente.exists() and existente.stat().st_size > 0:
        print(f"[JÁ EXISTE] {existente}")
        return existente

    if destino.exists() and destino.stat().st_size > 0 and not sobrescrever:
        print(f"[JÁ EXISTE] {destino}")
        return destino

    temporario = destino.with_suffix(destino.suffix + ".part")
    inicio = temporario.stat().st_size if temporario.exists() else 0
    cabecalhos = dict(CABECALHOS)
    if inicio:
        cabecalhos["Range"] = f"bytes={inicio}-"

    print(f"[BAIXANDO] {url}")
    try:
        with requests.get(
            url,
            headers=cabecalhos,
            stream=True,
            timeout=timeout,
            allow_redirects=True,
        ) as resposta:
            if inicio and resposta.status_code != 206:
                inicio = 0
                temporario.unlink(missing_ok=True)

            resposta.raise_for_status()
            total_parcial = int(resposta.headers.get("content-length", 0))
            total = inicio + total_parcial
            modo = "ab" if inicio else "wb"
            gravado = inicio

            with temporario.open(modo) as arquivo:
                for bloco in resposta.iter_content(chunk_size=1024 * 1024):
                    if not bloco:
                        continue
                    arquivo.write(bloco)
                    gravado += len(bloco)
                    if total:
                        print(
                            f"\r  {gravado / total * 100:6.2f}% "
                            f"({tamanho_legivel(gravado)} / {tamanho_legivel(total)})",
                            end="",
                        )
                    else:
                        print(f"\r  {tamanho_legivel(gravado)}", end="")

        print()
        temporario.replace(destino)
        print(f"[OK] {destino}")
        return destino

    except (requests.RequestException, OSError) as erro:
        print()
        print(f"[ERRO] {destino.name}: {erro}")
        return None
