from pathlib import Path

VERSAO = "0.4.0"

# Repositório de dados. Altere somente se o seu caminho for diferente.
REPOSITORIO = Path(r"D:\LaTex_Projects\Cartografia\SIG_BRASIL")

# Recorte inicial para produtos oceanográficos.
OESTE = -54.0
LESTE = -38.0
SUL = -30.0
NORTE = -17.0

DATA_INICIAL = "2025-01-01"
DATA_FINAL = "2025-12-31"

PROFUNDIDADE_MIN = 0.0
PROFUNDIDADE_MAX = 1.0

# Pode ser preenchida quando uma URL direta oficial for conhecida.
URL_SGB = None
URL_GEBCO = None

# Unidade da Federação usada no SIGMINE.
UF_SIGMINE = "RJ"

PASTA_MALHAS = REPOSITORIO / "01_IBGE" / "Malhas"
PASTA_BC250 = REPOSITORIO / "02_IBGE_BC250"
PASTA_POPULACAO = REPOSITORIO / "03_IBGE_POPULACAO"
PASTA_ANM = REPOSITORIO / "04_ANM"
PASTA_SGB = REPOSITORIO / "05_SGB" / "Geologia"
PASTA_GEBCO = REPOSITORIO / "06_OCEANOGRAFIA" / "GEBCO"
PASTA_COPERNICUS = REPOSITORIO / "06_OCEANOGRAFIA" / "Copernicus"
PASTA_DOCUMENTACAO = REPOSITORIO / "Documentacao"

CATALOGO_EMBUTIDO = (
    Path(__file__).resolve().parent
    / "dados"
    / "catalogo_fontes_sig_brasil.json"
)
