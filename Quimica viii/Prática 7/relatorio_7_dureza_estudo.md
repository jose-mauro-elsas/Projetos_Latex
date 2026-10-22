# Relatório 7 — Dureza da água: roteiro de estudo

## 1. O que estamos medindo?

A dureza está associada principalmente ao cálcio e ao magnésio presentes na água. Neste experimento, fazemos duas titulações com EDTA:

- A titulação total mede cálcio **mais** magnésio.
- A titulação seletiva de cálcio mede somente cálcio.
- O magnésio é calculado pela diferença entre o total e o cálcio.

O EDTA reage na proporção **1 mol de EDTA para 1 mol de Ca²⁺ ou Mg²⁺**. A carga 2+ dos íons não introduz um fator 2 nessa relação.

## 2. Dados conhecidos e médias

| Dado | Valor |
|---|---:|
| Concentração do EDTA | 0,009512 mol/L |
| Volume original de amostra em cada titulação | 5,00 mL |
| Volumes de EDTA na titulação total | 35,1; 35,2; 36,1 mL |
| Volumes de EDTA na titulação de cálcio | 6,3; 6,0; 6,3 mL |

As médias são:

$$
\overline{V}_{\mathrm{total}}=\frac{35{,}1+35{,}2+36{,}1}{3}=35{,}466666\ldots\ \mathrm{mL}
$$

Durante o estudo, usamos **35,467 mL**.

$$
\overline{V}_{\mathrm{Ca}}=\frac{6{,}3+6{,}0+6{,}3}{3}=6{,}2\ \mathrm{mL}
$$

Essas médias ainda são **volumes**, não concentrações.

Não temos volumes de branco registrados. Nos cálculos abaixo, usamos `BT7=0` e `BC7=0` para não aplicar correção de branco; isso não significa que um branco tenha sido medido e encontrado igual a zero.

## 3. Concentração total — TOT7

Concentração do EDTA multiplicada pelo volume gasto fornece a quantidade de EDTA consumida. Pela proporção 1:1, essa é também a quantidade total de cálcio e magnésio. Dividindo pelo volume original da amostra, obtemos a concentração total.

$$
C_{\mathrm{total}}=\frac{C_{\mathrm{EDTA}}(V_{\mathrm{total}}-V_{\mathrm{branco}})}{V_{\mathrm{amostra}}}
$$

Na HP, objeto **TOT7**:

```text
CT7=CE7*(VT7-BT7)/VA7
```

| Variável | Significado | Entrada |
|---|---|---:|
| CE7 | Concentração do EDTA, em mol/L | 0,009512 |
| VT7 | Volume médio de EDTA para o total, em mL | 35,467 |
| BT7 | Volume de branco, em mL | 0 |
| VA7 | Volume original da amostra, em mL | 5 |
| CT7 | Concentração total de Ca²⁺ + Mg²⁺, em mol/L | Resolver |

$$
CT7=\frac{0{,}009512\times35{,}467}{5}=0{,}0674724208\ \mathrm{mol/L}
$$

Os volumes podem ser inseridos em mL porque estão na mesma unidade no numerador e no denominador, e sua razão é adimensional. A unidade final permanece mol/L.

**VA7 é 5 mL:** a água adicionada para realizar a titulação não muda a quantidade de íons retirada da amostra original.

## 4. Concentração de cálcio — CAL7

A lógica é a mesma, mas usamos o volume de EDTA da titulação seletiva de cálcio.

Na HP, objeto **CAL7**:

```text
CC7=CE7*(VC7-BC7)/VA7
```

Mantenha `CE7=0,009512` e `VA7=5`. Informe `VC7=6,2` e `BC7=0`. Resolva **CC7**.

$$
CC7=\frac{0{,}009512\times6{,}2}{5}=0{,}01179488\ \mathrm{mol/L}
$$

Esse resultado é a concentração de **Ca²⁺**.

## 5. Concentração de magnésio — MAG7

Como o total contém cálcio e magnésio, retiramos a concentração do cálcio para encontrar a do magnésio.

$$
[\mathrm{Mg}^{2+}]=C_{\mathrm{total}}-[\mathrm{Ca}^{2+}]
$$

Na HP, objeto **MAG7**:

```text
CM7=CT7-CC7
```

Resolva **CM7**, aproveitando os valores guardados de CT7 e CC7.

$$
CM7=0{,}0674724208-0{,}01179488=0{,}0556775408\ \mathrm{mol/L}
$$

No estudo, anotamos aproximadamente **5,5677E-2 mol/L**. Preserve o valor completo na calculadora para as próximas conversões.

## 6. Dureza total como CaCO₃ — DUR7

A dureza total é expressa como uma concentração equivalente de CaCO₃. Cada mol de Ca²⁺ ou Mg²⁺ corresponde a um mol de CaCO₃ nessa expressão da dureza.

Usamos a massa molar do CaCO₃, **100,09 g/mol**, e multiplicamos por 1000 para converter g/L em mg/L.

Na HP, objeto **DUR7**:

```text
DC7=CT7*100.09*1000
```

$$
DC7=0{,}0674724208\times100{,}09\times1000
\approx6753{,}3\ \mathrm{mg/L\ como\ CaCO_3}
$$

Usamos **CT7**, pois a dureza total inclui os dois íons. Esse resultado não é a soma das massas reais de cálcio e magnésio em mg/L.

## 7. Converter cada íon para mg/L — CVGM

Para calcular a massa real de cada íon por litro, usamos sua própria massa molar:

$$
C_{\mathrm{mg/L}}=C_{\mathrm{mol/L}}\times M\times1000
$$

Na HP, objeto **CVGM**:

```text
MGX=CMX*MMX*1000
```

| Variável | Significado |
|---|---|
| CMX | Concentração do íon que será convertido, em mol/L |
| MMX | Massa molar desse íon, em g/mol |
| MGX | Resultado em mg/L |

### Cálcio

Coloque em **CMX** o valor de **CC7**, e use `MMX=40,08`.

$$
C_{\mathrm{Ca}}=0{,}01179488\times40{,}08\times1000
=472{,}7387904\ \mathrm{mg/L}
$$

Resultado arredondado: **472,7 mg/L de Ca²⁺**.

### Magnésio

Coloque em **CMX** o valor de **CM7**, e use `MMX=24,31`.

Com o valor completo obtido usando a média de 35,467 mL:

$$
C_{\mathrm{Mg}}=0{,}0556775408\times24{,}31\times1000
\approx1353{,}5210\ \mathrm{mg/L}
$$

Resultado arredondado: **1353,5 mg/L de Mg²⁺**.

Se for usado `CMX=0,055677`, como na digitação realizada durante o estudo, o resultado será **1353,50787 mg/L**. A pequena diferença vem do arredondamento da concentração antes da conversão.

## 8. Converter cada íon para % m/V — CVPC

**% m/V significa gramas de soluto em 100 mL de solução.** Ao multiplicar mol/L pela massa molar, obtemos g/L; dividimos por 10 para obter g por 100 mL.

$$
C_{\%\,m/V}=\frac{C_{\mathrm{mol/L}}\times M}{10}
$$

Na HP, objeto **CVPC**:

```text
PCX=CMX*MMX/10
```

**PCX** é o resultado numérico em % m/V. As variáveis CMX e MMX têm os mesmos significados da CVGM.

### Cálcio

Mantenha `CMX=0,01179488` e `MMX=40,08`. Resolva **PCX**.

$$
C_{\mathrm{Ca}}=\frac{0{,}01179488\times40{,}08}{10}
=0{,}04727387904\%\ m/V
$$

### Magnésio

Use em CMX a concentração do magnésio e `MMX=24,31`.

Com `CMX=0,055677`, obtivemos no estudo:

$$
C_{\mathrm{Mg}}=\frac{0{,}055677\times24{,}31}{10}
=0{,}135350787\%\ m/V
$$

Com o valor completo de CM7, o resultado é aproximadamente **0,1353521% m/V**. Ambos arredondam para **0,13535% m/V**.

## 9. Ordem das equações dentro de DUREZ

| Ordem | Objeto | Para que serve | Resultado |
|---|---|---|---|
| 1 | TOT7 | Titulação total | CT7, em mol/L |
| 2 | CAL7 | Titulação seletiva de cálcio | CC7, em mol/L |
| 3 | MAG7 | Total menos cálcio | CM7, em mol/L |
| 4 | DUR7 | Converter o total para dureza | DC7, em mg/L como CaCO₃ |
| 5 | CVGM | Converter cálcio e depois magnésio | MGX, em mg/L de cada íon |
| 6 | CVPC | Converter cálcio e depois magnésio | PCX, em % m/V de cada íon |

**MAG7 depende de TOT7 e CAL7. DUR7 depende somente de TOT7.**

As equações compartilham valores quando usam o mesmo nome de variável na mesma pasta. Entretanto, **CMX não é CC7 nem CM7**: é necessário colocar em CMX a concentração do íon escolhido. Depois de calcular o magnésio, CMX e MMX permanecem com os dados do magnésio; confira-os antes de voltar ao cálcio.

Para aproveitar CMX e MMX entre as conversões, também é possível fazer **CVGM e CVPC para o cálcio**, e depois **CVGM e CVPC para o magnésio**.

## 10. Resultados finais

| Grandeza | Resultado arredondado |
|---|---:|
| Concentração total de Ca²⁺ + Mg²⁺ | 0,067472 mol/L |
| Concentração de Ca²⁺ | 0,01179488 mol/L |
| Concentração de Mg²⁺ | aproximadamente 0,0556775 mol/L |
| Cálcio | 472,7 mg/L |
| Cálcio | 0,04727% m/V |
| Magnésio | 1353,5 mg/L |
| Magnésio | 0,13535% m/V |
| Dureza total | 6753,3 mg/L como CaCO₃ |

**Guarde todas as casas na HP e arredonde apenas ao apresentar o resultado.** O uso da média completa de 35,466666… mL, em lugar de 35,467 mL, também causa pequenas diferenças nas últimas casas.
