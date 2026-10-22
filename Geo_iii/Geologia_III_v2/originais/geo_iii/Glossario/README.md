# Glossário de Geologia - versão consolidada

Arquivos principais:

- `Glossario_Geologia_UERJ.tex`
- `referencias_geologia.bib`
- `uerj_logo.png`

Compilação:

```powershell
lualatex -interaction=nonstopmode -file-line-error Glossario_Geologia_UERJ.tex
biber Glossario_Geologia_UERJ
lualatex -interaction=nonstopmode -file-line-error Glossario_Geologia_UERJ.tex
lualatex -interaction=nonstopmode -file-line-error Glossario_Geologia_UERJ.tex
```

Principais ajustes desta versão:

- verbetes consolidados e ordenados alfabeticamente;
- comandos `\letra` sem repetição;
- integração dos verbetes sobre ciclo das rochas, dobras, estruturas sedimentares, magmatismo, metamorfismo, tectônica de placas e Wegener;
- correção da posição dos verbetes iniciados por R e S;
- preâmbulo ajustado para LuaLaTeX com `fontspec`;
- `biblatex` carregado antes de `hyperref`;
- bibliografia ampliada para estruturas geológicas e tectônica de placas.
