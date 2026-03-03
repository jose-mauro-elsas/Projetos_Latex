from pathlib import Path
import pandas as pd

IN_XLSX = Path(r"C:\LaTex_Projects\Descomissionamento\Dados\_descomissionamento\ANP_descomissionamento_somente.xlsx")
OUT_XLSX = IN_XLSX.with_name("ANP_descomissionamento_somente_normalizado.xlsx")

def split_macro(df: pd.DataFrame, col: str) -> pd.DataFrame:
    if col not in df.columns:
        return df
    s = df[col].fillna("").astype(str)
    parts = s.str.split(" - ", n=1, expand=True)
    df[col + "__macro"] = parts[0].str.strip()
    df[col + "__detalhe"] = parts[1].fillna("").str.strip()
    return df

prev_qtd = pd.read_excel(IN_XLSX, sheet_name="prev_atividade_bacia", dtype=str)
prev_inv = pd.read_excel(IN_XLSX, sheet_name="prev_invest_atividade", dtype=str)
real_inv = pd.read_excel(IN_XLSX, sheet_name="real_invest_atividade", dtype=str)

# Descobre o nome da coluna de atividade em cada aba
def pick(df, cands):
    low = {c.lower(): c for c in df.columns}
    for c in cands:
        if c.lower() in low:
            return low[c.lower()]
    return None

c1 = pick(prev_qtd, ["TIPO ATIVIDADE", "Tipo Atividade", "ATIVIDADE"])
c2 = pick(prev_inv, ["ATIVIDADE", "Tipo Atividade", "TIPO ATIVIDADE"])
c3 = pick(real_inv, ["Tipo Atividade", "ATIVIDADE", "TIPO ATIVIDADE"])

if c1: prev_qtd = split_macro(prev_qtd, c1)
if c2: prev_inv = split_macro(prev_inv, c2)
if c3: real_inv = split_macro(real_inv, c3)

with pd.ExcelWriter(OUT_XLSX, engine="openpyxl") as w:
    prev_qtd.to_excel(w, sheet_name="prev_atividade_bacia", index=False)
    prev_inv.to_excel(w, sheet_name="prev_invest_atividade", index=False)
    real_inv.to_excel(w, sheet_name="real_invest_atividade", index=False)

print("OK:", OUT_XLSX)
print("Colunas criadas:")
print(" -", c1, "->", c1+"__macro", c1+"__detalhe" if c1 else "")
print(" -", c2, "->", c2+"__macro", c2+"__detalhe" if c2 else "")
print(" -", c3, "->", c3+"__macro", c3+"__detalhe" if c3 else "")