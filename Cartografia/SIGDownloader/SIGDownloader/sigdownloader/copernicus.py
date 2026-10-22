from __future__ import annotations

from .config import (
    DATA_FINAL, DATA_INICIAL, LESTE, NORTE, OESTE,
    PASTA_COPERNICUS, PROFUNDIDADE_MAX, PROFUNDIDADE_MIN, SUL,
)

DATASET_TEMPERATURA = "cmems_mod_glo_phy-thetao_anfc_0.083deg_P1D-m"
DATASET_CORRENTES = "cmems_mod_glo_phy-cur_anfc_0.083deg_P1D-m"


def _comando(dataset: str, variaveis: list[str], arquivo: str) -> str:
    variaveis_cli = " ".join(f'--variable "{v}"' for v in variaveis)
    saida = PASTA_COPERNICUS / arquivo
    return (
        "copernicusmarine subset ^\n"
        f'  --dataset-id "{dataset}" ^\n'
        f"  {variaveis_cli} ^\n"
        f"  --minimum-longitude {OESTE} ^\n"
        f"  --maximum-longitude {LESTE} ^\n"
        f"  --minimum-latitude {SUL} ^\n"
        f"  --maximum-latitude {NORTE} ^\n"
        f"  --minimum-depth {PROFUNDIDADE_MIN} ^\n"
        f"  --maximum-depth {PROFUNDIDADE_MAX} ^\n"
        f'  --start-datetime "{DATA_INICIAL}T00:00:00" ^\n'
        f'  --end-datetime "{DATA_FINAL}T23:59:59" ^\n'
        f'  --output-filename "{saida}"'
    )


def gerar_comandos() -> None:
    pasta = PASTA_COPERNICUS / "comandos"
    pasta.mkdir(parents=True, exist_ok=True)

    (pasta / "baixar_temperatura.bat").write_text(
        "@echo off\n"
        + _comando(
            DATASET_TEMPERATURA,
            ["thetao"],
            "temperatura_superficial_2025.nc",
        )
        + "\npause\n",
        encoding="utf-8",
    )
    (pasta / "baixar_correntes.bat").write_text(
        "@echo off\n"
        + _comando(
            DATASET_CORRENTES,
            ["uo", "vo"],
            "correntes_superficiais_2025.nc",
        )
        + "\npause\n",
        encoding="utf-8",
    )
    (pasta / "LEIA-ME.txt").write_text(
        "A ferramenta Copernicus Marine suporta versões específicas do Python.\n"
        "Use um ambiente Python 3.13 para instalar e executar:\n\n"
        "py -3.13 -m venv .venv-copernicus\n"
        ".\\.venv-copernicus\\Scripts\\Activate.ps1\n"
        "python -m pip install copernicusmarine\n"
        "copernicusmarine login\n\n"
        "Depois execute os arquivos .bat desta pasta.\n",
        encoding="utf-8",
    )
    print(f"[OK] Comandos Copernicus: {pasta}")
