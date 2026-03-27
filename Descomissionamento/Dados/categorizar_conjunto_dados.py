from __future__ import annotations

from pathlib import Path
import re
import html
import pandas as pd

IN_CSV = Path(r"C:\LaTex_Projects\Descomissionamento\Dados\conjunto-dados.csv")
OUT_DIR = IN_CSV.parent / "_categorias"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_XLSX = OUT_DIR / "conjunto-dados__categorias_para_revisao.xlsx"

df = pd.read_csv(IN_CSV, sep=";", dtype=str, encoding="utf-8-sig", encoding_errors="replace")

def clean_text(x: str) -> str:
    x = "" if x is None else str(x)
    x = html.unescape(x)                 # E&amp;P -> E&P
    x = re.sub(r"<[^>]+>", " ", x)       # remove tags HTML
    x = re.sub(r"\s+", " ", x).strip()
    return x

nome = df.get("Nome", pd.Series([""] * len(df))).fillna("").astype(str)
desc_raw = df.get("Descrição", pd.Series([""] * len(df))).fillna("").astype(str)
tags = df.get("Tags", pd.Series([""] * len(df))).fillna("").astype(str)
org = df.get("Organização", pd.Series([""] * len(df))).fillna("").astype(str)

desc = desc_raw.map(clean_text)
txt = (nome + " " + desc + " " + tags).str.lower()

# Regras conservadoras: categoria, regex(es), peso, motivo
RULES = [
    # ---- Downstream / Dados Estratégicos (novas) ----
    ("Infraestrutura de Abastecimento (Tancagem/Armazen.)",
     [r"\btancagem\b", r"\barmazen", r"\btanque\b", r"\binstala", r"\bterminal\b"],
     3, "tancagem/armazenamento/infraestrutura de abastecimento"),

    ("Participações Governamentais (Royalties/PE)",
     [r"\bparticipa", r"\broya", r"\bparticipa[cç][aã]o especial\b", r"\bpre[cç]o de refer", r"\bparticipa[cç][aã]o especial\b"],
     3, "participações governamentais (royalties/PE/preço referência)"),

    ("Comércio Exterior (Import/Export)",
     [r"\bimporta", r"\bexporta", r"\bcom[eé]rcio exterior\b"],
     3, "importações/exportações"),

    ("Abastecimento / Mercado (Vendas & Comercialização)",
     [r"\bvendas?\b", r"\bcomercializa", r"\bdistribuid", r"\bconsumidor", r"\bmercado\b",
      r"\bderivados de petr[oó]leo\b", r"\bcombust", r"\bbiocombust", r"\bg[aá]s natural\b",
      r"\bglp\b", r"\bgasolina\b", r"\bdiesel\b", r"\bquerosene\b", r"\basfalto\b"],
     2, "abastecimento/mercado (vendas/comercialização/combustíveis)"),

    # ---- As suas categorias originais ----
    ("Regulação / Normas",
     [r"\bresolu", r"\blei\b", r"\bdecreto\b", r"\bportaria\b", r"\binstru"],
     3, "menciona instrumento normativo"),

    ("Publicações / Anuários / Estatísticas",
     [r"\banu[aá]rio\b", r"\bestat[ií]stic", r"\bboletim\b", r"\brelat[oó]rio\b"],
     2, "parece publicação/anuário/relatório"),

    ("Dados Técnicos / Acervo",
     [r"\bbdep\b", r"\bdados t[eé]cnic", r"\bs[ií]smic", r"\bpo[çc]os?\b", r"\bamostras?\b"],
     3, "parece acervo/dados técnicos"),

    ("Atividades / Investimentos",
     [r"\binvestimento", r"\batividad", r"\bprevis[aã]o\b", r"\brealizad"],
     2, "parece atividade/investimento (previsão/realizado)"),

    ("Produção / Séries",
     [r"\bprodu[cç][aã]o\b", r"\bs[eé]rie", r"\bvolume\b"],
     2, "parece produção/séries"),

    ("Planejamento / Programas / Processos",
     [r"\bpdi\b", r"\bprocess", r"\bprogram", r"\baditamento\b", r"\bcontrat"],
     2, "parece processo/programa/contrato"),
]

def score_row(text: str) -> tuple[str, str, str, int]:
    # retorna (categoria, confianca, motivo, score)
    best = ("Outros / Indefinido", "baixa", "sem match", 0)

    for cat, patterns, weight, why in RULES:
        hits = 0
        for pat in patterns:
            if re.search(pat, text, flags=re.IGNORECASE):
                hits += 1
        score = hits * weight
        if score > best[3]:
            # confiança simples: depende do score e do tipo
            conf = "alta" if score >= 6 else ("média" if score >= 3 else "baixa")
            best = (cat, conf, f"{why} (hits={hits})", score)

    return best

res = txt.map(score_row)
df_out = df.copy()
df_out["descricao_limpa"] = desc
df_out["categoria_sugerida"] = res.map(lambda x: x[0])
df_out["confianca"] = res.map(lambda x: x[1])
df_out["motivo"] = res.map(lambda x: x[2])
df_out["score"] = res.map(lambda x: x[3])

# Coluna para você preencher (sem alterar nada do resto)
df_out["categoria_final"] = ""

# Ordena colunas principais na frente
front = ["Organização", "Nome", "categoria_sugerida", "confianca", "motivo", "categoria_final", "Tags", "Descrição", "descricao_limpa"]
front = [c for c in front if c in df_out.columns]
df_out = df_out[front + [c for c in df_out.columns if c not in front]]

df_out.to_excel(OUT_XLSX, index=False)
print("OK:", OUT_XLSX)
print(df_out["categoria_sugerida"].value_counts())