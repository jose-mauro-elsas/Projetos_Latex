
## Volumes de HCl consumidos

Os volumes médios experimentais obtidos foram:

- Fenolftaleína (P): **0,57 mL**
- Alaranjado de metila (T): **12,57 mL**

Esses valores são os **volumes de ácido consumidos**. Ainda precisamos calcular as alcalinidades correspondentes.

| O enunciado pede… | O que você procura |
|---|---|
| Alcalinidade à fenolftaleína, P | Alcalinidade calculada usando o volume de HCl gasto até a viragem da fenolftaleína |
| Alcalinidade total, T | Alcalinidade calculada usando o volume de HCl gasto até a viragem do alaranjado de metila |
| Resultado em mol/L de H⁺ consumido | Quantidade de ácido consumido dividida pelo volume da amostra |
| Resultado em mg/L como CaCO₃ | Conversão da alcalinidade já calculada |
| Contribuições de carbonato e bicarbonato | Comparação entre P e T/2, expressos na mesma unidade |

## Concentração do HCl

Usamos a concentração do HCl: **0,00869 mol/L**, calculada anteriormente pela relação:

$$
C_1V_1 = C_2V_2
$$

Ela informa quantos mols de HCl existem em cada litro da solução da bureta.

Agora essa concentração é um dado conhecido. Sabemos a concentração do ácido na bureta e medimos quanto dele foi gasto.

Com esses dois dados, calculamos quantos mols de ácido foram necessários para neutralizar a alcalinidade da amostra. Para obter a alcalinidade em mol/L de H⁺ consumido, dividimos essa quantidade pelo volume da amostra.

# Alcalinidade: identificação dos dados e cálculo de P e T na HP50g

Referência: relatório 6 — Alcalinidade da água do mar, correspondente à prática 5 da apostila.

## 1. O que foi medido no laboratório

Os valores **0,57 mL** e **12,57 mL** são as médias arredondadas dos volumes de HCl consumidos nas titulações, obtidos pela diferença entre as leituras final e inicial da bureta.

- **0,57 mL:** volume gasto até a viragem da fenolftaleína, usado para calcular a alcalinidade **P**.
- **12,57 mL:** volume gasto até a viragem do alaranjado de metila, usado para calcular a alcalinidade total **T**.

Esses volumes ainda não são os valores de alcalinidade: são os dados usados para calculá-los.

## 2. Os três dados necessários

| Grandeza | Variável na HP | Valor |
|---|---|---:|
| Concentração do HCl da bureta | `CH5` | 0,00869 mol/L |
| Volume de HCl consumido | `VH5` | 0,57 mL para P; 12,57 mL para T |
| Volume da amostra de água analisada | `VA5` | 50,00 mL em cada titulação |

A concentração do HCl é um dado conhecido nesta etapa, após o preparo da solução por diluição. O volume da amostra permanece igual nas duas titulações; muda o volume de ácido consumido.

## 3. Por que usar essa equação

Concentração multiplicada pelo volume de HCl fornece a quantidade de matéria de ácido consumida:

$$
n_{\mathrm{HCl}}=C_{\mathrm{HCl}}V_{\mathrm{HCl}}.
$$

Para essa conta isolada, com concentração em mol/L, o volume deve estar em litros. Como cada mol de HCl fornece um mol de H⁺, essa quantidade corresponde à quantidade de H⁺ consumida na neutralização.

Dividindo pelo volume da amostra, encontramos a alcalinidade por litro de água:

$$
A=\frac{C_{\mathrm{HCl}}V_{\mathrm{HCl}}}{V_{\mathrm{amostra}}}.
$$

Na razão entre os volumes, podemos usar ambos em mL: o fator de conversão para litros se cancela. A unidade do resultado continua sendo **mol/L de H⁺ consumido**.

## 4. Digitação e uso na HP50g

Na pasta `QUIM / PRAT / ALCAL`, a equação originalmente chamada `AL5` foi renomeada para `ALC5`:

```text
A5=CH5*VH5/VA5
```

`ALC5` é o nome da equação guardada. `A5` é a variável que recebe o resultado.

### Alcalinidade à fenolftaleína: P

Informe:

```text
CH5 = 0.00869
VH5 = 0.57
VA5 = 50
```

Selecione **`A5`** e mande resolver:

$$
P=\frac{0{,}00869\times0{,}57}{50}
=9{,}9066\times10^{-5}\ \mathrm{mol/L}.
$$

Na notação científica da HP:

```text
9.9066E-5
```

### Alcalinidade total: T

Mantenha `CH5` e `VA5` e altere apenas o volume de HCl:

```text
CH5 = 0.00869
VH5 = 12.57
VA5 = 50
```

Selecione novamente **`A5`** e mande resolver:

$$
T=\frac{0{,}00869\times12{,}57}{50}
=2{,}184666\times10^{-3}\ \mathrm{mol/L}.
$$

Na notação científica da HP:

```text
2.184666E-3
```

## 5. Como evitar a troca de volumes

**`VH5` é o volume do ácido; `VA5` é o volume da amostra.** Ao passar de P para T, mude somente `VH5`, de 0,57 para 12,57. Mantenha `VA5=50` e `CH5=0.00869`.

Confira também qual campo está selecionado ao mandar resolver: nesta etapa, a incógnita é sempre `A5`. Resolver outro campo pode alterar um dado conhecido.

Os resultados acima usam as médias arredondadas a duas casas decimais. O relatório pode apresentar pequenas diferenças por usar as médias com mais casas no cálculo.

P e T representam a capacidade de neutralização expressa em mol/L de H⁺ consumido; não são a concentração de H⁺ livre na água após a titulação.

O próximo passo é converter as alcalinidades de mol/L de H⁺ consumido para mg/L como CaCO₃.
Você já encontrou, usando os volumes médios arredondados:
- P: $9{,}9066\times10^{-5}$ mol/L
- T: $2{,}184666\times10^{-3}$ mol/L
A conversão é:
$$
A_{\mathrm{mg/L\ como\ CaCO_3}} = A_{\mathrm{mol/L}} \times 50\,000
$$
Esse fator vem do CaCO₃: 1 mol de CaCO₃ neutraliza 2 mol de H⁺. Portanto, cada mol de H⁺ consumido corresponde a aproximadamente 50 g, ou 50 000 mg, de CaCO₃.

Na HP, use a CVC5:
AC5=50000*A5
Comece por P: coloque A5=9,9066E-5 e resolva para AC5.

Os resultados são:
- 4,9533 mg/L
- 109,2333 mg/L

Agora vamos comparar P com T/2 para identificar as contribuições à alcalinidade.
Temos, em mg/L como CaCO₃:
- P = 4,9533
- T = 109,2333
- T/2 = 54,61665

O os resultados com CAR5 são:

- 9,9066 mg/L
- 218,233 mg/L

Com T5=109,2333 e P5=4,9533, dá 99,3267. Para anotar com duas casas, ambos dão 99,33 mg/L como CaCO₃.

| Resultado | mg/L como CaCO₃ |
|---|---:|
| Alcalinidade à fenolftaleína, P | 4,95 |
| Alcalinidade total, T | 109,23 |
| Contribuição do hidróxido | 0 |
| Contribuição do carbonato | 9,91 |
| Contribuição do bicarbonato | 99,33 |

## Relatório 7

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


| Pasta | Equação | O que faz | Resultado e unidade |
|---|---|---|---|
| ALCAL | **ALC5** | Calcula a alcalinidade usando o volume de HCl consumido; aplicada separadamente a P e T | **A5:** mol/L de H⁺ consumido |
| ALCAL | **CVC5** | Converte a alcalinidade para equivalente de CaCO₃ | **AC5:** mg/L como CaCO₃ |
| ALCAL | **CAR5** | Calcula a contribuição do carbonato: 2P¹ | **CO5:** mg/L como CaCO₃ |
| ALCAL | **BIC5** | Calcula a contribuição do bicarbonato: T − 2P¹ | **BI5:** mg/L como CaCO₃ |
| CLORE | **PAD6** | Determina a concentração de AgNO₃ por titulação de NaCl padrão | **CA6:** mol/L |
| CLORE | **CLOR6** | Calcula a concentração de cloreto na amostra original, considerando a diluição | **CL6:** mol/L de Cl⁻ |
| DUREZ | **TOT7** | Calcula a concentração total de cálcio e magnésio | **CT7:** mol/L de Ca²⁺ + Mg²⁺ |
| DUREZ | **CAL7** | Calcula a concentração de cálcio | **CC7:** mol/L de Ca²⁺ |
| DUREZ | **MAG7** | Calcula a concentração de magnésio: total − cálcio | **CM7:** mol/L de Mg²⁺ |
| DUREZ | **DUR7** | Converte a concentração total em dureza equivalente de CaCO₃ | **DC7:** mg/L como CaCO₃ |
| OXIG | **PAD10** | Determina a concentração de tiossulfato usando KIO₃ | **CT10:** mol/L |
| OXIG | **OX10** | Calcula o oxigênio dissolvido a partir da titulação com tiossulfato | **O10:** mg/L de O₂ |
| SULFA | **PES11** | Subtrai as massas dos filtros e calcula a massa média de precipitado | **MB11:** g de BaSO₄ |
| SULFA | **SUL11** | Calcula a concentração de sulfato a partir da massa de BaSO₄ | **CS11:** mg/L de SO₄²⁻ |
| SULFA | **POR11** | Converte a concentração de sulfato de mg/L para porcentagem | **PS11:** % m/V |
| CONV² | **CVGM** | Converte a concentração em mol/L para concentração em massa, usando a massa molar | **MGX:** mg/L da espécie escolhida |
| CONV² | **CVPC** | Converte a concentração em mol/L para porcentagem em massa por volume | **PCX:** % m/V da espécie escolhida |