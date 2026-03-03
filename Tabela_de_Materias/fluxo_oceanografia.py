import pandas as pd

# Lista de arestas (pré → pós)
edges = [
    # Matemática
    ("Cálculo I", "Cálculo II"),
    ("Cálculo II", "Equações Diferenciais IV"),
    ("Equações Diferenciais IV", "Matemática Especial I"),
    ("Matemática Especial I", "Astronomia e Navegação"),

    # Física
    ("Física V", "Física VI"),
    ("Física VI", "Física VII"),
    ("Física VII", "Física VIII"),
    ("Física VIII", "Oceanografia Física I"),
    ("Oceanografia Física I", "Oceanografia Física II"),
    ("Oceanografia Física II", "Oceanografia Física III"),

    # Biologia
    ("Fund. Biologia I", "Fund. Biologia II"),
    ("Fund. Biologia II", "Fund. Biologia III"),
    ("Fund. Biologia III", "Ecologia Marinha"),
    ("Ecologia Marinha", "Oceanografia Biológica I"),
    ("Oceanografia Biológica I", "Oceanografia Biológica II"),
    ("Oceanografia Biológica II", "Oceanografia Biológica III"),
    ("Oceanografia Biológica III", "Oceanografia Descritiva"),

    # Geologia
    ("Geologia Geral I", "Geologia II"),
    ("Geologia II", "Geologia III"),
    ("Geologia III", "Neontologia"),
    ("Neontologia", "Oceanografia Geológica I"),
    ("Oceanografia Geológica I", "Oceanografia Geológica II"),

    # Química
    ("Química I", "Química VII"),
    ("Química VII", "Química VIII"),
    ("Química VIII", "Química IX"),
    ("Química IX", "Oceanografia Química I"),
    ("Oceanografia Química I", "Oceanografia Química II"),
    ("Oceanografia Química II", "Poluição no Mar"),

    # Cartografia / Clima
    ("Fund. Cartografia", "Cartografia X"),
    ("Cartografia X", "Climatologia III"),
    ("Climatologia III", "Meteorologia I"),
    ("Meteorologia I", "Meteorologia II"),

    # Estatística
    ("Estatística II", "Estatística III"),
    ("Estatística III", "Mecânica dos Fluidos III"),
    ("Mecânica dos Fluidos III", "Hidrografia II"),
]

df = pd.DataFrame(edges, columns=["pre", "pos"])
df.to_csv("prereqs_oceanografia.csv", index=False)

print("Arquivo prereqs_oceanografia.csv criado.")

# -------------------------
# Exemplo: descobrir matérias liberadas
# -------------------------

cursadas = {
    "Cálculo I",
    "Cálculo II",
    "Equações Diferenciais IV",
    "Física V",
    "Física VI",
    "Fund. Biologia I",
    "Fund. Biologia II",
}

liberadas = []

for pre, pos in edges:
    if pre in cursadas and pos not in cursadas:
        liberadas.append(pos)

print("\nPossivelmente liberadas:")
for m in sorted(set(liberadas)):
    print("-", m)