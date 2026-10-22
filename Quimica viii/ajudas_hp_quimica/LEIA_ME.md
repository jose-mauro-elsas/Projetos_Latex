# AJUDA — Equações das práticas de química

Os cinco programas seguem o formato de páginas do AJUDA enviado. Os arquivos sem extensão são objetos binários HP49/50; os `.txt` contêm a transcrição legível das mesmas páginas.

## Instalação e uso

Copie os arquivos sem extensão para o cartão. Pelo FILES da HP, copie cada objeto para a pasta indicada abaixo. Execute seu nome para abrir a ajuda; feche cada página para avançar. Não é necessário substituir o AJUDA antigo.

| Arquivo | Pasta de destino |
|---|---|
| AJALC | ALCAL |
| AJCLO | CLORE |
| AJDUR | DUREZ |
| AJOXI | OXIG |
| AJSUL | SULFA |

As entradas numéricas usam as unidades indicadas. As equações gerais CVGM/CVPC precisam existir também em CLORE e DUREZ. CMX recebe manualmente o valor da concentração escolhida.

Sem volume de branco registrado, usamos zero para não aplicar correção. Se um problema fornecer branco, use o valor fornecido.

Os objetos foram montados com o mesmo comando de exibição do arquivo enviado e verificados estruturalmente. A execução na HP física ainda precisa ser conferida.

## ALCAL — AJALC

```text
ALCAL 1/8
ORDEM
ALC5 > CVC5
Comparar P com T/2
CAR5 > BIC5
```

```text
ALCAL 2/8
ALC5: alcalinidade
CH5: HCl, mol/L
VH5: HCl gasto, mL
VA5: amostra, mL
Resolver A5: mol/L H+
```

```text
ALCAL 3/8
ALC5: fazer 2 vezes
P: VH5 ate fenolft.
T: VH5 ate metila
CH5 e VA5 iguais
Anotar P e T separados
```

```text
ALCAL 4/8
CVC5: converter A5
AC5=50000*A5
A5: mol/L H+ consumido
AC5: mg/L como CaCO3
Fazer para P e T
```

```text
ALCAL 5/8
CAR5: carbonato
Usar se 0<P<T/2
P5: P, mg/L CaCO3
CO5=2*P5
CO5: mg/L como CaCO3
```

```text
ALCAL 6/8
BIC5: bicarbonato
Usar se 0<P<T/2
P5 e T5: mg/L CaCO3
BI5=T5-2*P5
BI5: mg/L como CaCO3
```

```text
ALCAL 7/8
CONDICOES
P=0: so bicarbonato
P=T/2: so carbonato
P>T/2: outras relacoes
CAR5/BIC5 nao servem
```

```text
ALCAL 8/8
UNIDADES
CO5/BI5: equivalentes
expressos como CaCO3
Nao sao mg/L reais
dos ions CO3 e HCO3
```

## CLORE — AJCLO

```text
CLORE 1/7
ORDEM
PAD6 > CLOR6
CVGM > CVPC
Resultado: Cl original
```

```text
CLORE 2/7
PAD6: padronizar AgNO3
CN6: NaCl, mol/L
VN6: NaCl, mL
VP6: AgNO3 gasto, mL
BP6: branco, mL
```

```text
CLORE 3/7
PAD6: resolver CA6
CA6: AgNO3, mol/L
Ag+ e Cl- reagem 1:1
Sem branco registrado:
BP6=0, sem correcao
```

```text
CLORE 4/7
CLOR6: titular amostra
CA6: vem de PAD6
VT6: AgNO3 gasto, mL
BT6: branco, mL
Sem correcao: BT6=0
```

```text
CLORE 5/7
CLOR6: diluicao
VI6: amostra orig., mL
VF6: vol. final, mL
VL6: vol. titulado, mL
CL6: Cl- orig., mol/L
```

```text
CLORE 6/7
CVGM: Cl- em mg/L
CMX: copiar valor CL6
MMX: 35.45 g/mol
MGX=CMX*MMX*1000
Resolver MGX: mg/L
```

```text
CLORE 7/7
CVPC: Cl- em % m/V
CMX: copiar valor CL6
MMX: 35.45 g/mol
PCX=CMX*MMX/10
Resolver PCX: % m/V
```

## DUREZ — AJDUR

```text
DUREZ 1/9
ORDEM
TOT7 > CAL7 > MAG7
DUR7 > CVGM > CVPC
Converter Ca e Mg
```

```text
DUREZ 2/9
TOT7: Ca+Mg total
CE7: EDTA, mol/L
VT7: EDTA total, mL
BT7: branco, mL
VA7: amostra orig., mL
```

```text
DUREZ 3/9
TOT7: resolver CT7
CT7: Ca+Mg, mol/L
EDTA: proporcao 1:1
Agua adicionada nao
muda VA7 original
```

```text
DUREZ 4/9
CAL7: so calcio
CE7 e VA7: mesmos
VC7: EDTA para Ca, mL
BC7: branco Ca, mL
CC7: Ca, mol/L
```

```text
DUREZ 5/9
MAG7: magnesio
CM7=CT7-CC7
CT7: total, mol/L
CC7: calcio, mol/L
CM7: magnesio, mol/L
```

```text
DUREZ 6/9
DUR7: dureza total
DC7=CT7*100.09*1000
CT7: total, mol/L
DC7: mg/L como CaCO3
Usar CT7, nao CM7
```

```text
DUREZ 7/9
CVGM: massa por litro
CMX: CC7 ou CM7
MMX: massa molar g/mol
Ca:40.08; Mg:24.31
MGX: mg/L do ion
```

```text
DUREZ 8/9
CVPC: porcentagem
CMX: CC7 ou CM7
MMX: Ca ou Mg, g/mol
PCX=CMX*MMX/10
PCX: % m/V do ion
```

```text
DUREZ 9/9
ATENCAO
Copiar CC7/CM7 a CMX
Trocar MMX com o ion
Ca e Mg: massa real
DC7: equiv. de CaCO3
```

## OXIG — AJOXI

```text
OXIG 1/6
ORDEM
PAD10 > OX10
Pratica 10 apostila
Relatorio 8
```

```text
OXIG 2/6
PAD10: tiossulfato
MK10: massa KIO3, g
MMK10: KIO3, g/mol
VP10: padroniz., mL
CT10: resolver, mol/L
```

```text
OXIG 3/6
PAD10: significado
1 mol KIO3 equivale a
6 mol de tiossulfato
6000 = 6 x 1000
VP10 em mL
```

```text
OXIG 4/6
OX10: oxigenio
CT10: vem de PAD10
VO10: titulacao, mL
MO10: O2, 32 g/mol
VA10: amostra, mL
```

```text
OXIG 5/6
OX10: resultado
Resolver O10: mg/L O2
4 mol tiossulfato
para 1 mol de O2
Ja inclui conversao
```

```text
OXIG 6/6
VOLUMES DIFERENTES
VP10: padronizacao
VO10: amostra de agua
VA10: agua analisada
Todos em mL
```

## SULFA — AJSUL

```text
SULFA 1/6
ORDEM
PES11 > SUL11 > POR11
Pratica 11 apostila
Relatorio 9
```

```text
SULFA 2/6
PES11: precipitado
MT1/MT2: filtro+BaSO4
MF1/MF2: filtro vazio
Todas as massas em g
MB11: media BaSO4, g
```

```text
SULFA 3/6
PES11: significado
Subtrair cada filtro
do total correspondente
Depois tirar a media
Resolver MB11
```

```text
SULFA 4/6
SUL11: sulfato
MB11: vem de PES11, g
MMS11: SO4, 96.06
MMB11: BaSO4, 233.39
Massas molares: g/mol
```

```text
SULFA 5/6
SUL11: concentracao
VA11: amostra orig. mL
Resolver CS11: mg/L
1 mol BaSO4 = 1 mol SO4
Agua extra nao muda VA11
```

```text
SULFA 6/6
POR11: porcentagem
CS11: vem de SUL11
PS11=CS11/10000
Resolver PS11: % m/V
Nao usar MB11 aqui
```
