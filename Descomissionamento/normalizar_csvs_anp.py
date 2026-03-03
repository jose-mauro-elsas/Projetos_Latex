from __future__ import annotations

from pathlib import Path
import re
import pandas as pd

IN_DIR = Path(r"C:\LaTex_Projects\Descomissionamento\Dados")
OUT_DIR = IN_DIR / "_clean_csv"
OUT_XLSX = IN_DIR / "ANP_descomissionamento_tipado.xlsx"

OUT_DIR.mkdir(parents=True, exist_ok=True)

CAND_SEPS = [",", ";", "\t", "|"]

NUM_RE = re.compile(r"""
^\s*"?                  # espaços + aspas opcionais
-?                      # sinal opcional
(
  (\d{1,3}(\.\d{3})+)    # milhar com ponto: 1.234 ou 12.345.678
  |
  \d+                    # ou inteiro simples
)
(,\d+)?                  # decimal com vírgula opcional
"?\s*$                   # aspas opcionais + espaços
""", re.VERBOSE)

def detect_sep(path: Path, nlines: int = 30) -> str:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()[:nlines]
    if not lines:
        return ","
    # escolhe o separador com contagem mais "consistente" nas primeiras linhas
    best = None  # (score, sep)
    for sep in CAND_SEPS:
        counts = [ln.count(sep) for ln in lines if ln.strip()]
        if not counts:
            continue
        # queremos: média alta e pouca variação
        mean = sum(counts) / len(counts)
        var = sum((c - mean) ** 2 for c in counts) / len(counts)
        score = mean - (var ** 0.5)  # penaliza inconsistência
        if (best is None) or (score > best[0]):
            best = (score, sep)
    return best[1] if best else ","

def looks_numeric_series(s: pd.Series, min_frac: float = 0.80) -> bool:
    x = s.dropna().astype(str).str.strip()
    x = x[x != ""]
    if len(x) == 0:
        return False
    ok = x.apply(lambda v: bool(NUM_RE.match(v)))
    return (ok.mean() >= min_frac)

def to_float_ptbr(s: pd.Series) -> pd.Series:
    x = s.astype(str).str.strip().str.strip('"')
    x = x.str.replace(".", "", regex=False)   # remove milhar
    x = x.str.replace(",", ".", regex=False)  # decimal vírgula -> ponto
    return pd.to_numeric(x, errors="coerce")

def main() -> None:
    csvs = sorted(IN_DIR.glob("*.csv"))
    if not csvs:
        raise SystemExit(f"Nenhum .csv em {IN_DIR}")

    used_sheets: set[str] = set()

    def safe_sheet(name: str) -> str:
        for ch in r'[]:*?/\\':
            name = name.replace(ch, "_")
        base = name[:31]
        s = base
        i = 2
        while s in used_sheets:
            suf = f"_{i}"
            s = base[:31 - len(suf)] + suf
            i += 1
        used_sheets.add(s)
        return s

    with pd.ExcelWriter(OUT_XLSX, engine="openpyxl") as writer:
        for p in csvs:
            sep = detect_sep(p)

            df = pd.read_csv(
                p,
                sep=sep,
                dtype=str,
                encoding="utf-8-sig",
                encoding_errors="replace",
                engine="c",
            )

            # Tipagem mínima segura:
            if "ANO" in df.columns:
                df["ANO"] = pd.to_numeric(df["ANO"], errors="coerce").astype("Int64")

            # Detecta e tipa colunas numéricas (ex.: "0,00", "1.234,56")
            numeric_cols = []
            for col in df.columns:
                if col == "ANO":
                    continue
                if looks_numeric_series(df[col]):
                    df[col] = to_float_ptbr(df[col])
                    numeric_cols.append(col)

            # 1) Escreve CSV limpo para Excel pt-BR: sep=';' e decimal=','
            out_csv = OUT_DIR / p.name
            df.to_csv(out_csv, index=False, sep=";", encoding="utf-8-sig", decimal=",")

            # 2) Escreve aba no XLSX tipado
            sheet = safe_sheet(p.stem)
            df.to_excel(writer, sheet_name=sheet, index=False)

            print(f"OK: {p.name}  sep_in='{sep}'  rows={len(df)} cols={len(df.columns)}  num={numeric_cols}")

    print(f"\nOK: CSVs normalizados em {OUT_DIR}")
    print(f"OK: XLSX tipado em {OUT_XLSX}")

if __name__ == "__main__":
    main()