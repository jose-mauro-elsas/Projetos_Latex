GLOSSÁRIO DE GEOLOGIA - ARQUIVO-BASE UERJ

Arquivos:
- glossario_geologia_uerj.tex: fonte principal em LaTeX
- uerj_logo.png: marca institucional obtida no portal oficial da Uerj
- glossario_geologia_uerj.pdf: prévia compilada

Compilação recomendada:
1. Abra glossario_geologia_uerj.tex no VS Code/LaTeX Workshop ou TeXworks.
2. Selecione LuaLaTeX.
3. Compile duas vezes para atualizar o sumário e os cabeçalhos.

Como acrescentar um termo:

\begin{verbete}{Nome do termo}
Definição e explicações.
\relacao{Resumo da relação entre os termos associados.}
\vertambem{outro termo, outro conceito}
\end{verbete}

Ao mudar a inicial, insira antes:

\letra{B}

O cabeçalho usa as marcas dos verbetes para exibir o primeiro e o último termo da página.
