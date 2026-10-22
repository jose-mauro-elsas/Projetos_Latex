from __future__ import annotations

from . import __version__
from .anm import baixar_sigmine
from .catalogo import gerar_catalogo, mostrar_status
from .copernicus import gerar_comandos
from .fontes import (
    abrir_fonte,
    gerar_tabela_latex,
    instalar_catalogo_documentacao,
    listar_fontes,
)
from .gebco import preparar_gebco
from .ibge import baixar_bc250, baixar_malhas, baixar_populacao
from .migracao import migrar_estrutura_antiga
from .sgb import baixar_geologia


def atualizar_tudo() -> None:
    migrar_estrutura_antiga()
    baixar_malhas()
    baixar_bc250()
    baixar_populacao()
    baixar_sigmine()
    baixar_geologia()
    preparar_gebco()
    gerar_comandos()
    gerar_catalogo()
    instalar_catalogo_documentacao()
    gerar_tabela_latex()


def executar() -> None:
    migrar_estrutura_antiga()

    acoes = {
        "1": atualizar_tudo,
        "2": baixar_malhas,
        "3": baixar_bc250,
        "4": baixar_populacao,
        "5": baixar_sigmine,
        "6": baixar_geologia,
        "7": preparar_gebco,
        "8": gerar_comandos,
        "9": mostrar_status,
        "10": gerar_catalogo,
        "11": listar_fontes,
        "12": abrir_fonte,
        "13": instalar_catalogo_documentacao,
        "14": gerar_tabela_latex,
    }

    while True:
        print(f"""
SIGDownloader v{__version__}

[1] Atualizar tudo
[2] IBGE - malhas
[3] IBGE - BC250
[4] IBGE - população
[5] ANM - SIGMINE
[6] SGB - geologia
[7] GEBCO - preparar download
[8] Copernicus - gerar comandos
[9] Mostrar status do repositório
[10] Atualizar catálogo local dos arquivos
[11] Mostrar fontes oficiais
[12] Abrir uma fonte oficial no navegador
[13] Copiar catálogo de fontes para Documentacao
[14] Gerar tabela LaTeX das fontes
[0] Sair
""")
        escolha = input("Escolha: ").strip()
        if escolha == "0":
            print("Encerrado.")
            return

        acao = acoes.get(escolha)
        if not acao:
            print("Opção inválida.")
            continue

        try:
            acao()
        except KeyboardInterrupt:
            print("\nOperação interrompida.")
        except Exception as erro:
            print(f"[ERRO NÃO TRATADO] {type(erro).__name__}: {erro}")
