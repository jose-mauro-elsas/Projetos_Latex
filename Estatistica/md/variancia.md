# Variância e desvio padrão

A variância mede a dispersão dos valores em relação à média. Ela utiliza todos os dados do conjunto e, por elevar os desvios ao quadrado, evita que desvios positivos e negativos se anulem. Quanto maior a variância, maior a dispersão.

## Variância para dados não agrupados

Considere os dados $x_1,x_2,\ldots,x_n$.

### População

A variância populacional é calculada usando todos os elementos da população:

$$
\sigma^2=\frac{\sum_{i=1}^{n}(x_i-\mu)^2}{n},
$$

em que $\mu$ é a média populacional e $n$ é o tamanho da população. Uma forma equivalente, útil para o cálculo, é:

$$
\sigma^2=\overline{x^2}-\mu^2
=\frac{\sum_{i=1}^{n}x_i^2-\frac{\left(\sum_{i=1}^{n}x_i\right)^2}{n}}{n}.
$$

Aqui, $\overline{x^2}$ é a média dos quadrados dos valores; $\mu^2$ é o quadrado da média populacional.

### Amostra

A variância amostral, usada para estimar a variância populacional, é:

$$
s^2=\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1},
$$

em que $\bar{x}$ é a média amostral e $n$ é o tamanho da amostra. Na forma computacional:

$$
s^2=\frac{\sum_{i=1}^{n}x_i^2-\frac{\left(\sum_{i=1}^{n}x_i\right)^2}{n}}{n-1}
=\left(\overline{x^2}-\bar{x}^{,2}\right)\frac{n}{n-1}.
$$

O divisor $n-1$ corresponde aos graus de liberdade: conhecidos a média e $n-1$ desvios, o último desvio fica determinado. Para um mesmo conjunto de dados, se $\sigma^2$ for a variância calculada com divisor $n$, então $s^2=\frac{n}{n-1}\sigma^2$.

### Exemplo: dados não agrupados

Calcular a variância amostral de $\{1,2,3,5,9\}$:

$$
\bar{x}=\frac{1+2+3+5+9}{5}=4.
$$

| $x_i$ | $(x_i-\bar{x})^2$ |
|---:|---:|
| 1 | 9 |
| 2 | 4 |
| 3 | 1 |
| 5 | 1 |
| 9 | 25 |
| **Soma** | **40** |

$$
s^2=\frac{40}{5-1}=10.
$$

## Variância para dados agrupados sem intervalos de classe

Se os valores distintos $x_1,\ldots,x_m$ possuem frequências $f_1,\ldots,f_m$, então:

$$
n=\sum_{i=1}^{m}f_i,\qquad
\bar{x}=\frac{\sum_{i=1}^{m}x_if_i}{n}.
$$

Para a população:

$$
\sigma^2=\frac{\sum_{i=1}^{m}(x_i-\mu)^2f_i}{n}
=\frac{\sum_{i=1}^{m}x_i^2f_i-\frac{\left(\sum_{i=1}^{m}x_if_i\right)^2}{n}}{n}.
$$

Para uma amostra:

$$
s^2=\frac{\sum_{i=1}^{m}(x_i-\bar{x})^2f_i}{n-1}
=\frac{\sum_{i=1}^{m}x_i^2f_i-\frac{\left(\sum_{i=1}^{m}x_if_i\right)^2}{n}}{n-1}.
$$

### Exemplo: número de filhos por professor

| Filhos por professor ($x_i$) | Frequência ($f_i$) | $x_if_i$ | $(x_i-\bar{x})^2f_i$ |
|---:|---:|---:|---:|
| 0 | 4 | 0 | 9 |
| 1 | 8 | 8 | 2 |
| 2 | 4 | 8 | 1 |
| 3 | 2 | 6 | 4,5 |
| 4 | 2 | 8 | 12,5 |
| **Soma** | **20** | **30** | **29** |

$$
\bar{x}=\frac{30}{20}=1{,}5\ \text{filho por professor}.
$$

A variância e o desvio padrão **amostrais** são:

$$
s^2=\frac{29}{20-1}=\frac{29}{19}\approx1{,}53,
\qquad
s=\sqrt{\frac{29}{19}}\approx1{,}24.
$$

> **Observação:** a tabela original chama os dados de pesquisa populacional, mas aplica o divisor amostral $n-1$. Se os 20 professores forem toda a população de interesse, a variância populacional será $29/20=1{,}45$ e o desvio padrão populacional será aproximadamente $1{,}20$.

## Dados agrupados em intervalos de classe

Nos cálculos aproximados com dados agrupados em classes, usa-se o ponto médio $x_i$ de cada classe e sua frequência $f_i$ nas fórmulas anteriores.

### Exemplo: estaturas de 40 alunos

| Estatura (cm) | $f_i$ | Ponto médio $x_i$ | $x_if_i$ | $x_i-\bar{x}$ | $(x_i-\bar{x})^2$ | $(x_i-\bar{x})^2f_i$ |
|:---|---:|---:|---:|---:|---:|---:|
| 150 a 154 | 4 | 152 | 608 | −9 | 81 | 324 |
| 154 a 158 | 9 | 156 | 1 404 | −5 | 25 | 225 |
| 158 a 162 | 11 | 160 | 1 760 | −1 | 1 | 11 |
| 162 a 166 | 8 | 164 | 1 312 | 3 | 9 | 72 |
| 166 a 170 | 5 | 168 | 840 | 7 | 49 | 245 |
| 170 a 174 | 3 | 172 | 516 | 11 | 121 | 363 |
| **Soma** | **40** | | **6 440** | | | **1 240** |

$$
\bar{x}=\frac{6\,440}{40}=161\ \mathrm{cm}.
$$

Considerando os 40 alunos uma amostra:

$$
s^2=\frac{\sum_{i=1}^{6}(x_i-\bar{x})^2f_i}{n-1}
=\frac{1\,240}{39}\approx31{,}79\ \mathrm{cm}^2,
\qquad
s=\sqrt{\frac{1\,240}{39}}\approx5{,}64\ \mathrm{cm}.
$$

O cálculo é aproximado porque substitui as estaturas individuais pelos pontos médios das classes.

## Propriedades da variância

- Somar ou subtrair uma constante $c$ de todos os valores não altera a variância: $\operatorname{Var}(X+c)=\operatorname{Var}(X)$.
- Multiplicar todos os valores por $c$ multiplica a variância por $c^2$: $\operatorname{Var}(cX)=c^2\operatorname{Var}(X)$.
- Dividir todos os valores por $c\ne0$ divide a variância por $c^2$: $\operatorname{Var}(X/c)=\operatorname{Var}(X)/c^2$.
