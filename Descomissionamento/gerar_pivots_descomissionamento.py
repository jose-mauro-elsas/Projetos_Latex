from __future__ import annotations

from pathlib import Path
import pandas as pd

IN_XLSX = Path(r"C:\LaTex_Projects\Descomissionamento\Dados\_descomissionamento\ANP_descomissionamento_somente.xlsx")
OUT_XLSX = IN_XLSX.with_name("ANP_descomissionamento_pivots.xlsx")

def to_float(x: pd.Series) -> pd.Series:
    return pd.to_numeric(x, errors="coerce")

# --- Lê abas ---
prev_qtd = pd.read_excel(IN_XLSX, sheet_name="prev_atividade_bacia", dtype=str)
prev_inv = pd.read_excel(IN_XLSX, sheet_name="prev_invest_atividade", dtype=str)
real_inv = pd.read_excel(IN_XLSX, sheet_name="real_invest_atividade", dtype=str)

# --- Normaliza nomes de colunas de atividade ---
def pick_col(df, candidates):
    low = {c.lower(): c for c in df.columns}
    for cand in candidates:
        if cand.lower() in low:
            return low[cand.lower()]
    return None

col_prev_qtd_act = pick_col(prev_qtd, ["TIPO ATIVIDADE", "Tipo Atividade", "ATIVIDADE"])
col_prev_inv_act = pick_col(prev_inv, ["ATIVIDADE", "Tipo Atividade", "TIPO ATIVIDADE"])
col_real_inv_act = pick_col(real_inv, ["Tipo Atividade", "ATIVIDADE", "TIPO ATIVIDADE"])

# --- Converte ano e métricas ---
for df in (prev_qtd, prev_inv, real_inv):
    if "ANO" in df.columns:
        df["ANO"] = pd.to_numeric(df["ANO"], errors="coerce").astype("Int64")
    if "Ano" in df.columns:
        df["Ano"] = pd.to_numeric(df["Ano"], errors="coerce").astype("Int64")

# Quantidade prevista
qcol = "QUANTIDADE ATIVIDADE_num" if "QUANTIDADE ATIVIDADE_num" in prev_qtd.columns else "QUANTIDADE ATIVIDADE"
if qcol in prev_qtd.columns:
    prev_qtd["QTD"] = to_float(prev_qtd[qcol])

# Investimentos previstos
for base in ["INVESTIMENTO R$", "INVESTIMENTO US$", "Investimento R$", "Investimento US$"]:
    numcol = base + "_num"
    if numcol in prev_inv.columns:
        if "R$" in base:
            prev_inv["INV_RS"] = to_float(prev_inv[numcol])
        else:
            prev_inv["INV_USD"] = to_float(prev_inv[numcol])

# Investimentos realizados
for base in ["INVESTIMENTO R$", "INVESTIMENTO US$", "Investimento R$", "Investimento US$"]:
    numcol = base + "_num"
    if numcol in real_inv.columns:
        if "R$" in base:
            real_inv["INV_RS"] = to_float(real_inv[numcol])
        else:
            real_inv["INV_USD"] = to_float(real_inv[numcol])

# --- Pivôs ---
# 1) QTD prevista: ANO x ATIVIDADE
pivot_qtd_ano = prev_qtd.pivot_table(
    index="ANO",
    columns=col_prev_qtd_act,
    values="QTD",
    aggfunc="sum",
    fill_value=0
).reset_index()

# 2) QTD prevista: ANO x BACIA x ATIVIDADE (mais detalhada)
pivot_qtd_ano_bacia = prev_qtd.pivot_table(
    index=["ANO", "BACIA", "AMBIENTE"],
    columns=col_prev_qtd_act,
    values="QTD",
    aggfunc="sum",
    fill_value=0
).reset_index()

# 3) Investimento previsto: ANO x ATIVIDADE (R$ e US$)
pivot_prev_rs = prev_inv.pivot_table(
    index="ANO",
    columns=col_prev_inv_act,
    values="INV_RS",
    aggfunc="sum",
    fill_value=0
).reset_index()

pivot_prev_usd = prev_inv.pivot_table(
    index="ANO",
    columns=col_prev_inv_act,
    values="INV_USD",
    aggfunc="sum",
    fill_value=0
).reset_index()

# 4) Investimento realizado: Ano x Atividade (R$ e US$)
ano_real = "Ano" if "Ano" in real_inv.columns else "ANO"
pivot_real_rs = real_inv.pivot_table(
    index=ano_real,
    columns=col_real_inv_act,
    values="INV_RS",
    aggfunc="sum",
    fill_value=0
).reset_index()

pivot_real_usd = real_inv.pivot_table(
    index=ano_real,
    columns=col_real_inv_act,
    values="INV_USD",
    aggfunc="sum",
    fill_value=0
).reset_index()

# --- Escreve ---
with pd.ExcelWriter(OUT_XLSX, engine="openpyxl") as w:
    prev_qtd.to_excel(w, sheet_name="base_prev_qtd", index=False)
    prev_inv.to_excel(w, sheet_name="base_prev_inv", index=False)
    real_inv.to_excel(w, sheet_name="base_real_inv", index=False)

    pivot_qtd_ano.to_excel(w, sheet_name="pivot_qtd_ano", index=False)
    pivot_qtd_ano_bacia.to_excel(w, sheet_name="pivot_qtd_ano_bacia", index=False)

    pivot_prev_rs.to_excel(w, sheet_name="pivot_prev_inv_rs", index=False)
    pivot_prev_usd.to_excel(w, sheet_name="pivot_prev_inv_usd", index=False)

    pivot_real_rs.to_excel(w, sheet_name="pivot_real_inv_rs", index=False)
    pivot_real_usd.to_excel(w, sheet_name="pivot_real_inv_usd", index=False)

print("OK:", OUT_XLSX)