from __future__ import annotations

from pathlib import Path
import pandas as pd

IN_DIR = Path(r"C:\LaTex_Projects\Descomissionamento\Dados")
OUT_DIR = IN_DIR / "_descomissionamento"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_XLSX = OUT_DIR / "ANP_descomissionamento_somente.xlsx"

def to_float_ptbr(s: pd.Series) -> pd.Series:
    x = s.astype(str).str.strip().str.strip('"')
    x = x.str.replace(".", "", regex=False)   # milhar
    x = x.str.replace(",", ".", regex=False)  # decimal
    return pd.to_numeric(x, errors="coerce")

def read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, sep=",", dtype=str, encoding="utf-8-sig", encoding_errors="replace")

def find_col(df: pd.DataFrame, candidates: list[str]) -> str | None:
    cols_lower = {c.lower(): c for c in df.columns}
    for cand in candidates:
        key = cand.lower()
        if key in cols_lower:
            return cols_lower[key]
    return None

def only_descom(df: pd.DataFrame, col_candidates: list[str]) -> pd.DataFrame:
    col = find_col(df, col_candidates)
    if not col:
        return df.iloc[0:0].copy()
    m = df[col].fillna("").str.lower().str.startswith("descomissionamento")
    out = df[m].copy()
    out["_COL_ATIVIDADE_"] = col
    return out

# --- 1) Previsão (quantidades por bacia) ---
p1 = IN_DIR / "previsao-atividade-bacia.csv"
df1 = only_descom(read_csv(p1), ["TIPO ATIVIDADE", "Tipo Atividade", "ATIVIDADE", "Atividade"])
if "QUANTIDADE ATIVIDADE" in df1.columns:
    df1["QUANTIDADE ATIVIDADE_num"] = to_float_ptbr(df1["QUANTIDADE ATIVIDADE"])

# --- 2) Previsão (investimento por atividade) ---
p2 = IN_DIR / "investimento-atividade.csv"
df2 = only_descom(read_csv(p2), ["ATIVIDADE", "Atividade", "TIPO ATIVIDADE", "Tipo Atividade"])
for col in ["INVESTIMENTO R$", "INVESTIMENTO US$", "Investimento R$", "Investimento US$"]:
    if col in df2.columns:
        df2[col + "_num"] = to_float_ptbr(df2[col])

# --- 3) Realizado 2022–2024 (investimento por atividade) ---
p3 = IN_DIR / "investimento-atividade-realizado-2022-2024.csv"
df3 = only_descom(read_csv(p3), ["Tipo Atividade", "TIPO ATIVIDADE", "ATIVIDADE", "Atividade"])
for col in ["INVESTIMENTO R$", "INVESTIMENTO US$", "Investimento R$", "Investimento US$"]:
    if col in df3.columns:
        df3[col + "_num"] = to_float_ptbr(df3[col])

with pd.ExcelWriter(OUT_XLSX, engine="openpyxl") as w:
    df1.to_excel(w, sheet_name="prev_atividade_bacia", index=False)
    df2.to_excel(w, sheet_name="prev_invest_atividade", index=False)
    df3.to_excel(w, sheet_name="real_invest_atividade", index=False)

print("OK:", OUT_XLSX)
print("Linhas:")
print(" prev_atividade_bacia:", len(df1))
print(" prev_invest_atividade:", len(df2))
print(" real_invest_atividade:", len(df3))

# Diagnóstico: quais atividades foram capturadas
def col_used(df: pd.DataFrame) -> str | None:
    return df["_COL_ATIVIDADE_"].iloc[0] if len(df) and "_COL_ATIVIDADE_" in df.columns else None

if len(df1):
    c = col_used(df1)
    print("\nTipos (previsao-atividade-bacia):", c)
    print(df1[c].value_counts().to_string())
if len(df2):
    c = col_used(df2)
    print("\nAtividades (investimento-atividade):", c)
    print(df2[c].value_counts().to_string())
if len(df3):
    c = col_used(df3)
    print("\nAtividades (realizado-2022-2024):", c)
    print(df3[c].value_counts().to_string())