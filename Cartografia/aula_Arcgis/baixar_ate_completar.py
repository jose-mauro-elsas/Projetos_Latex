#!/usr/bin/env python3
from __future__ import annotations

import csv
import shutil
import subprocess
import time
import urllib.request
import zipfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

INTERVALO_MINUTOS = 30
TENTATIVAS_POR_URL = 2
TIMEOUT_SEGUNDOS = 300

@dataclass(frozen=True)
class Download:
    nome: str
    pasta: str
    arquivo: str
    urls: tuple[str, ...]

DOWNLOADS = (
    Download("Limite do Brasil", "01_IBGE", "BR_Pais.zip", (
        "https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2025/Brasil/BR_Pais_2025.zip",
        "https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2024/Brasil/BR_Pais_2024.zip",
    )),
    Download("Unidades da Federação", "01_IBGE", "BR_UF.zip", (
        "https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2025/Brasil/BR_UF_2025.zip",
        "https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2024/Brasil/BR_UF_2024.zip",
    )),
    Download("Municípios do Brasil", "01_IBGE", "BR_Municipios.zip", (
        "https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2025/Brasil/BR_Municipios_2025.zip",
        "https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2024/Brasil/BR_Municipios_2024.zip",
    )),
    Download("SIGMINE — Rio de Janeiro", "02_ANM", "SIGMINE_RJ.zip", (
        "https://dadosabertos.anm.gov.br/SIGMINE/PROCESSOS_MINERARIOS/RJ.zip",
    )),
)

def zip_valido(caminho: Path) -> bool:
    if not caminho.is_file() or caminho.stat().st_size < 500:
        return False
    try:
        with zipfile.ZipFile(caminho) as zf:
            return bool(zf.namelist()) and zf.testzip() is None
    except (zipfile.BadZipFile, OSError):
        return False

def baixar_python(url: str, temporario: Path) -> None:
    inicio = temporario.stat().st_size if temporario.exists() else 0
    headers = {"User-Agent": "Mozilla/5.0", "Accept": "*/*"}
    if inicio:
        headers["Range"] = f"bytes={inicio}-"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=TIMEOUT_SEGUNDOS) as resposta:
        modo = "ab" if inicio and getattr(resposta, "status", 200) == 206 else "wb"
        with temporario.open(modo) as saida:
            while True:
                bloco = resposta.read(1024 * 1024)
                if not bloco:
                    break
                saida.write(bloco)

def baixar_curl(url: str, temporario: Path) -> None:
    curl = shutil.which("curl.exe") or shutil.which("curl")
    if not curl:
        raise RuntimeError("curl.exe não encontrado.")
    comando = [
        curl, "--location", "--fail",
        "--retry", "3", "--retry-delay", "10",
        "--connect-timeout", "30",
        "--max-time", str(TIMEOUT_SEGUNDOS),
        "--continue-at", "-",
        "--output", str(temporario),
        url,
    ]
    resultado = subprocess.run(comando)
    if resultado.returncode != 0:
        raise RuntimeError(f"curl terminou com código {resultado.returncode}")

def tentar_item(item: Download, raiz: Path) -> dict[str, str]:
    pasta = raiz / item.pasta
    pasta.mkdir(parents=True, exist_ok=True)
    destino = pasta / item.arquivo
    temporario = destino.with_suffix(destino.suffix + ".part")

    if zip_valido(destino):
        print(f"OK, já existe: {destino}")
        return {"item": item.nome, "status": "concluído", "arquivo": str(destino),
                "url": "", "erro": "", "data": datetime.now().isoformat(timespec="seconds")}

    if destino.exists():
        destino.unlink()

    ultimo_erro = ""
    for url in item.urls:
        for tentativa in range(1, TENTATIVAS_POR_URL + 1):
            print(f"\n{item.nome} — tentativa {tentativa}/{TENTATIVAS_POR_URL}")
            print(url)
            try:
                baixar_python(url, temporario)
            except Exception as erro_python:
                ultimo_erro = f"Python: {erro_python}"
                print(f"Falha pelo Python: {erro_python}")
                try:
                    baixar_curl(url, temporario)
                except Exception as erro_curl:
                    ultimo_erro += f" | curl: {erro_curl}"
                    print(f"Falha também com curl: {erro_curl}")

            if zip_valido(temporario):
                temporario.replace(destino)
                print(f"CONCLUÍDO: {destino}")
                return {"item": item.nome, "status": "concluído", "arquivo": str(destino),
                        "url": url, "erro": "", "data": datetime.now().isoformat(timespec="seconds")}

            if temporario.exists() and temporario.stat().st_size < 500:
                temporario.unlink()
            time.sleep(10)

    print(f"PENDENTE: {item.nome}")
    return {"item": item.nome, "status": "pendente", "arquivo": str(destino),
            "url": "", "erro": ultimo_erro,
            "data": datetime.now().isoformat(timespec="seconds")}

def gravar_relatorio(raiz: Path, resultados: list[dict[str, str]]) -> None:
    caminho = raiz / "relatorio_downloads.csv"
    campos = ["item", "status", "arquivo", "url", "erro", "data"]
    with caminho.open("w", encoding="utf-8-sig", newline="") as arq:
        escritor = csv.DictWriter(arq, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(resultados)

def main() -> None:
    raiz = Path.cwd()
    print(f"Pasta: {raiz.resolve()}")
    print(f"Nova rodada a cada {INTERVALO_MINUTOS} minutos.")
    print("Use Ctrl+C para interromper; depois execute novamente para continuar.")

    rodada = 0
    try:
        while True:
            rodada += 1
            print("\n" + "=" * 68)
            print(f"RODADA {rodada} — {datetime.now():%d/%m/%Y %H:%M:%S}")
            print("=" * 68)

            resultados = [tentar_item(item, raiz) for item in DOWNLOADS]
            gravar_relatorio(raiz, resultados)

            concluidos = sum(r["status"] == "concluído" for r in resultados)
            print(f"\nSituação: {concluidos}/{len(resultados)} arquivos concluídos.")

            if concluidos == len(resultados):
                print("TODOS OS ARQUIVOS FORAM BAIXADOS E VALIDADOS.")
                break

            print(f"Aguardando {INTERVALO_MINUTOS} minutos...")
            time.sleep(INTERVALO_MINUTOS * 60)

    except KeyboardInterrupt:
        print("\nPrograma interrompido. Execute novamente para continuar.")

if __name__ == "__main__":
    main()
