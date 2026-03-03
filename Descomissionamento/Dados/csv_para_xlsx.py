from pathlib import Path
import pandas as pd
import csv

IN_DIR = Path(r"C:\LaTex_Projects\Descomissionamento\Dados")
OUT_XLSX = IN_DIR / "ANP_descomissionamento.xlsx"

CAND_SEPS = [';', ',', '\t', '|']

def safe_sheet_name(name: str, used: set[str]) -> str:
    for ch in r'[]:*?/\\':
        name = name.replace(ch, "_")
    base = name[:31]
    s = base
    i = 2
    while s in used:
        suffix = f"_{i}"
        s = base[:31-len(suffix)] + suffix
        i += 1
    used.add(s)
    return s

def try_read(path: Path, sep: str, engine: str, fallback: bool):
    kw = dict(sep=sep, engine=engine)
    if fallback:
        kw.update(dict(quoting=csv.QUOTE_NONE, escapechar='\\', on_bad_lines='skip'))
    df = pd.read_csv(
        path,
        dtype=str,
        encoding="utf-8-sig",
        encoding_errors="replace",
        **kw
    )
    return df, kw

csvs = sorted(IN_DIR.glob("*.csv"))
if not csvs:
    raise SystemExit(f"Nenhum .csv em {IN_DIR}")

used = set()

with pd.ExcelWriter(OUT_XLSX, engine="openpyxl") as writer:
    for p in csvs:
        sheet = safe_sheet_name(p.stem, used)

        best = None  # (ncols, nrows, df, kw)
        last_err = None

        # Testa separadores e engines; escolhe o que gera MAIS colunas
        for sep in CAND_SEPS:
            for engine in ("c", "python"):
                for fallback in (False, True):
                    try:
                        df, kw = try_read(p, sep, engine, fallback)
                        ncols = len(df.columns)
                        nrows = len(df)
                        cand = (ncols, nrows, df, kw)
                        if (best is None) or (cand[0] > best[0]) or (cand[0] == best[0] and cand[1] > best[1]):
                            best = cand
                    except Exception as e:
                        last_err = e

        if best is None:
            pd.DataFrame({"arquivo":[p.name], "erro":[str(last_err)]}).to_excel(writer, sheet_name=sheet, index=False)
            print(f"FALHOU: {p.name} -> {last_err}")
        else:
            ncols, nrows, df, kw = best
            df.to_excel(writer, sheet_name=sheet, index=False)
            print(f"OK: {p.name} (sep={kw['sep']} eng={kw['engine']} fb={'on_bad_lines' in kw}) linhas={nrows} cols={ncols}")

print(f"OK: {OUT_XLSX}")
