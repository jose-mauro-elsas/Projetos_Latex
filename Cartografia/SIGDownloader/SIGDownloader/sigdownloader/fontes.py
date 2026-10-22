from __future__ import annotations

import json
import shutil
from pathlib import Path
from urllib.parse import urlparse
import webbrowser

from .config import CATALOGO_EMBUTIDO, PASTA_DOCUMENTACAO


def carregar_fontes() -> dict:
    if not CATALOGO_EMBUTIDO.exists():
        raise FileNotFoundError(
            f"Catálogo de fontes não encontrado: {CATALOGO_EMBUTIDO}"
        )
    return json.loads(CATALOGO_EMBUTIDO.read_text(encoding="utf-8"))


def listar_fontes() -> None:
    catalogo = carregar_fontes()
    print("\nFONTES OFICIAIS")
    print("-" * 100)
    for indice, item in enumerate(catalogo.get("fontes", []), start=1):
        url = item.get("url_direta") or item.get("pagina_oficial") or "-"
        print(
            f"{indice:>2}. {item.get('tema', '-'):<23} "
            f"{item.get('orgao', '-'):<18} "
            f"{item.get('situacao', '-')}"
        )
        print(f"    {url}")


def abrir_fonte() -> None:
    catalogo = carregar_fontes()
    fontes = catalogo.get("fontes", [])
    listar_fontes()

    escolha = input("\nNúmero da fonte a abrir [Enter cancela]: ").strip()
    if not escolha:
        return

    try:
        indice = int(escolha) - 1
        item = fontes[indice]
    except (ValueError, IndexError):
        print("[ERRO] Número de fonte inválido.")
        return

    url = item.get("url_direta") or item.get("pagina_oficial")
    if not url:
        print("[ERRO] A fonte não possui URL cadastrada.")
        return

    if webbrowser.open(url):
        print(f"[OK] Navegador aberto: {url}")
    else:
        print(f"[AVISO] Não foi possível abrir automaticamente: {url}")


def instalar_catalogo_documentacao() -> None:
    PASTA_DOCUMENTACAO.mkdir(parents=True, exist_ok=True)
    destino = PASTA_DOCUMENTACAO / "catalogo_fontes_sig_brasil.json"
    shutil.copy2(CATALOGO_EMBUTIDO, destino)
    print(f"[OK] Catálogo de fontes: {destino}")


def _latex_escape(texto: str) -> str:
    substituicoes = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(substituicoes.get(c, c) for c in texto)


def gerar_tabela_latex() -> None:
    catalogo = carregar_fontes()
    PASTA_DOCUMENTACAO.mkdir(parents=True, exist_ok=True)
    destino = PASTA_DOCUMENTACAO / "tabela_dados_obtidos_sig.tex"

    cabecalho = r"""% Requer: booktabs, longtable, array, url e xurl.
\begingroup
\small
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{1.18}
\begin{longtable}{
>{\raggedright\arraybackslash}p{2.25cm}
>{\raggedright\arraybackslash}p{4.10cm}
>{\raggedright\arraybackslash}p{2.65cm}
>{\raggedright\arraybackslash}p{2.65cm}
>{\raggedright\arraybackslash}p{5.30cm}
}
\caption{Dados geoespaciais obtidos ou localizados para o repositório SIG Brasil}
\label{tab:dados_sig_brasil}\\
\toprule
\textbf{Tema} & \textbf{Dado/produto} & \textbf{Formato} &
\textbf{Situação} & \textbf{URL oficial ou direta} \\
\midrule
\endfirsthead
\multicolumn{5}{c}{\tablename\ \thetable\ -- continuação} \\
\toprule
\textbf{Tema} & \textbf{Dado/produto} & \textbf{Formato} &
\textbf{Situação} & \textbf{URL oficial ou direta} \\
\midrule
\endhead
\midrule
\multicolumn{5}{r}{Continua na próxima página.} \\
\endfoot
\bottomrule
\endlastfoot
"""
    linhas = [cabecalho]
    for item in catalogo.get("fontes", []):
        url = item.get("url_direta") or item.get("pagina_oficial") or ""
        linhas.append(
            f"{_latex_escape(item.get('tema', ''))} & "
            f"{_latex_escape(item.get('produto', ''))} & "
            f"{_latex_escape(item.get('formato', ''))} & "
            f"{_latex_escape(item.get('situacao', ''))} & "
            rf"\url{{{url}}} \\"
        )
    linhas.append("\\end{longtable}\n\\endgroup\n")
    destino.write_text("\n".join(linhas), encoding="utf-8")
    print(f"[OK] Tabela LaTeX: {destino}")
