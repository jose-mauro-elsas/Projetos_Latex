from pathlib import Path
import pandas as pd
import re

# Pasta onde está o xlsx
ROOT = Path(r"C:\LaTex_Projects\Tabela_de_Materias")

# Ajuste para o nome real do arquivo:
XLSX_IN = ROOT / "Tabela_de_Materias.xlsx"

# Saídas
XLSX_OUT = ROOT / "Tabela_de_Materias__SEM_TRAVA.xlsx"
CSV_OUT  = ROOT / "Tabela_de_Materias__SEM_TRAVA.csv"

df = pd.read_excel(XLSX_IN, sheet_name=0)

# 1) Limpa colunas "Unnamed: ..."
df = df.loc[:, ~df.columns.astype(str).str.match(r"^Unnamed", na=False)]

# 2) Remove colunas 100% vazias (muito comum na coluna de ícone)
df = df.dropna(axis=1, how="all")

# 3) Normaliza nomes de coluna (se tiver "Trava", "Trava Crédito", etc.)
cols_norm = df.columns.astype(str).str.strip().str.replace(r"\s+", " ", regex=True)
df.columns = cols_norm

# 4) Se ainda existir algo como "Trava", remove por nome
padrao_trava = re.compile(r"^trava(\s*cr[eé]dito)?$", re.IGNORECASE)
cols_trava = [c for c in df.columns if padrao_trava.match(c)]
if cols_trava:
    df = df.drop(columns=cols_trava)

# 5) Remoção robusta de "coluna lixo": vazia, só espaços, só zeros, ou mistura disso
def _is_lixo(s: pd.Series) -> bool:
    # converte para string, preservando NaN como vazio
    txt = s.astype("string").fillna("").str.replace("\u00A0", " ", regex=False).str.strip()

    # considera lixo se quase tudo é vazio
    frac_vazio = (txt == "").mean()

    # considera lixo se quase tudo é "0" (ou "0.0") ou vazio
    so_zero_ou_vazio = txt.isin(["", "0", "0.0"]).mean()

    # regra: se >= 95% vazio OU >= 95% zero/vazio, é lixo
    return (frac_vazio >= 0.95) or (so_zero_ou_vazio >= 0.95)

cols_lixo = [c for c in df.columns if _is_lixo(df[c])]

# se encontrar, remove
if cols_lixo:
    df = df.drop(columns=cols_lixo)

# plano B final: ainda sobrou uma última coluna suspeita? (usa a mesma regra)
if len(df.columns) > 0 and _is_lixo(df.iloc[:, -1]):
    df = df.iloc[:, :-1]

# Salva "base limpa"
df.to_excel(XLSX_OUT, index=False)
df.to_csv(CSV_OUT, index=False, encoding="utf-8-sig")  # utf-8-sig ajuda Excel a abrir com acentos

print("Colunas lidas:", list(df.columns))
print("Amostra (últimas colunas):")
print(df.iloc[:5, -3:])  # 5 primeiras linhas, 3 últimas colunas

print("Colunas finais:", list(df.columns))
print("Arquivos gerados:")
print(" -", XLSX_OUT)
print(" -", CSV_OUT)