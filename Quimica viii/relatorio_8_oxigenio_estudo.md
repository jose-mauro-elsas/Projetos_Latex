# Relatório 8 — Oxigênio dissolvido pelo método de Winkler

## 1. Organização do cálculo

O relatório 8 corresponde à **prática 10 da apostila**. Por isso, as equações e as variáveis na HP usam o número 10.

Na pasta **OXIG**, usamos duas equações nesta ordem:

| Ordem | Equação | O que faz | Resultado |
|---|---|---|---|
| 1 | PAD10 | Determina a concentração do tiossulfato da bureta | CT10, em mol/L |
| 2 | OX10 | Usa essa concentração para calcular o oxigênio dissolvido na amostra | O10, em mg/L de O₂ |

**PAD10 e OX10 são nomes de equações.** MK10, MMK10, VP10 e CT10 são variáveis que aparecem dentro da PAD10.

As médias são calculadas antes de usar as equações, como preparação dos dados.

## 2. Massa média de iodato de potássio

As massas de KIO₃ usadas na padronização foram **0,0150 g e 0,0152 g**.

$$
\overline{m}_{\mathrm{KIO_3}}=\frac{0{,}0150+0{,}0152}{2}=0{,}0151\ \mathrm{g}
$$

Esse resultado é uma **massa**, ainda não uma concentração. Ele será informado em **MK10**.

## 3. Concentração do tiossulfato — PAD10

Primeiro precisamos conhecer a concentração do tiossulfato que será usado para titular a amostra de água.

A massa de KIO₃ dividida por sua massa molar fornece a quantidade de iodato em mol. Pelas reações da padronização, **1 mol de KIO₃ corresponde a 6 mol de tiossulfato**.

$$
n_{\mathrm{tiossulfato}}=6\frac{m_{\mathrm{KIO_3}}}{M_{\mathrm{KIO_3}}}
$$

Dividindo essa quantidade pelo volume de tiossulfato gasto na padronização, em litros, encontramos sua concentração.

Na HP, objeto **PAD10**:

```text
CT10=6000*MK10/(MMK10*VP10)
```

| Variável | Significado | Entrada ou resultado |
|---|---|---|
| MK10 | Massa média de KIO₃ | 0,0151 g |
| MMK10 | Massa molar do KIO₃ | 214 g/mol |
| VP10 | Volume médio de tiossulfato gasto na padronização | 15,7 mL |
| CT10 | Concentração do tiossulfato | Resolver, em mol/L |

O fator **6000 = 6 × 1000** reúne a proporção da reação e a conversão do volume de mL para L.

$$
CT10=\frac{6000\times0{,}0151}{214\times15{,}7}
\approx0{,}02696589\ \mathrm{mol/L}
$$

Na HP, encontramos aproximadamente **2,6966E-2 mol/L**.

**Preserve o valor completo de CT10 na calculadora:** ele será uma entrada da OX10. Como as duas equações usam o mesmo nome de variável na mesma pasta, o valor pode ser aproveitado diretamente.

## 4. Volume médio gasto na amostra de água

Os volumes de tiossulfato nas três titulações da amostra foram **1,6; 1,9; 1,2 mL**.

$$
\overline{V}=\frac{1{,}6+1{,}9+1{,}2}{3}
=1{,}566666\ldots\ \mathrm{mL}
$$

Durante o estudo, usamos **1,5667 mL**. Esse valor será informado em **VO10**.

Não confunda os dois volumes:

| Variável | Em qual etapa foi medido? | Valor |
|---|---|---:|
| VP10 | Padronização do tiossulfato com KIO₃ | 15,7 mL |
| VO10 | Titulação da amostra de água para determinar O₂ | 1,5667 mL |

## 5. Oxigênio dissolvido — OX10

No método de Winkler, as reações estabelecem a relação de **4 mol de tiossulfato para 1 mol de O₂**.

Assim, a concentração do tiossulfato multiplicada pelo volume gasto permite encontrar a quantidade de tiossulfato consumida. Dividimos essa quantidade por 4 para obter a quantidade de oxigênio.

Depois, multiplicamos pela massa molar do O₂ e dividimos pelo volume da amostra para obter a concentração em massa.

Na HP, objeto **OX10**:

```text
O10=CT10*VO10*MO10*1000/(4*VA10)
```

| Variável | Significado | Entrada ou resultado |
|---|---|---|
| CT10 | Concentração do tiossulfato | Valor completo guardado da PAD10, em mol/L |
| VO10 | Volume médio de tiossulfato gasto na amostra | 1,5667 mL |
| MO10 | Massa molar do O₂ | 32 g/mol |
| VA10 | Volume da amostra de água | 50 mL |
| O10 | Concentração de oxigênio dissolvido | Resolver, em mg/L de O₂ |

O **4** vem da proporção da reação. O **1000** converte gramas em miligramas. Como VO10 e VA10 estão ambos em mL, a razão entre eles mantém a mesma relação que teríamos usando ambos em litros.

$$
O10=\frac{0{,}02696589\times1{,}5667\times32\times1000}{4\times50}
\approx6{,}7596\ \mathrm{mg/L\ de\ O_2}
$$

Resultado final arredondado:

$$
\boxed{O10=6{,}76\ \mathrm{mg/L\ de\ O_2}}
$$

Não é necessário usar CVGM depois: **OX10 já fornece o resultado em mg/L de O₂**.

## 6. Resultados e sequência na HP

| Etapa | Resultado |
|---|---:|
| Massa média de KIO₃ | 0,0151 g |
| Concentração do tiossulfato — PAD10 | aproximadamente 0,02696589 mol/L |
| Volume médio de tiossulfato gasto na amostra | 1,5667 mL |
| Oxigênio dissolvido — OX10 | 6,76 mg/L de O₂ |

1. Calcular a massa média de KIO₃.
2. Abrir **PAD10**, informar MK10, MMK10 e VP10, e resolver CT10.
3. Calcular o volume médio de tiossulfato gasto na amostra.
4. Abrir **OX10**, aproveitar CT10, informar VO10, MO10 e VA10, e resolver O10.

Guarde todas as casas nos cálculos e arredonde somente ao apresentar o resultado. Usar a média completa de 1,566666… mL em vez de 1,5667 mL altera apenas as últimas casas; o resultado final permanece **6,76 mg/L**.
