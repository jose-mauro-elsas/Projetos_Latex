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
