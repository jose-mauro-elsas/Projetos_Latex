import os
import numpy as np
import pandas as pd

# caminho do arquivo de entrada
arquivo_entrada = "D:/LaTex_Projects/Estatistica/Estat_II/dados.xlsx"

# lê a planilha
df = pd.read_excel(arquivo_entrada, header=None)

# pega a coluna A, converte para número e remove vazios/textos
x = pd.to_numeric(df.iloc[:, 0], errors="coerce").dropna().to_numpy()

# cálculos
media = np.mean(x)
mediana = np.median(x)
variancia = np.var(x, ddof=1)
desvio = np.std(x, ddof=1)
maximo = np.max(x)
minimo = np.min(x)
n = len(x)

# tabela de resultados
resultados = pd.DataFrame({
    "Medida": [
        "Média",
        "Mediana",
        "Variância",
        "Desvio padrão",
        "N",
        "Valor máximo",
        "Valor mínimo"
    ],
    "Valor": [
        round(media, 2),
        round(mediana, 2),
        round(variancia, 2),
        round(desvio, 2),
        n,
        round(maximo, 2),
        round(minimo, 2)
    ]
})

# arquivo de saída na mesma pasta
pasta = os.path.dirname(arquivo_entrada)
arquivo_saida = os.path.join(pasta, "resultados_descritivos.xlsx")

# salva
resultados.to_excel(arquivo_saida, index=False)

print(f"Arquivo lido: {arquivo_entrada}")
print(f"Arquivo salvo em: {arquivo_saida}")
print()
print(f"Média = {media:.2f}")
print(f"Mediana = {mediana:.2f}")
print(f"Variância = {variancia:.2f}")
print(f"Desvio padrão = {desvio:.2f}")
print(f"N = {n}")
print(f"Valor máximo = {maximo:.2f}")
print(f"Valor mínimo = {minimo:.2f}")