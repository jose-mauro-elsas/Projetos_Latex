# Pendências da reorganização — versão 2

## 1. Arquivos externos que não vieram no envio

Não é necessário reenviar os quatro arquivos já recebidos. Este inventário apenas identifica as dependências que eles citam.

- `formas_de_leito_e_estruturas.tex`

O arquivo principal declara `referencias.bib` duas vezes. Foram recuperadas as bibliografias do ZIP unificado, das notas antigas e do glossário, mas ainda faltam algumas chaves usadas pelas notas mais recentes. O arquivo ausente de formas de leito impede recuperar os seus textos específicos; o capítulo de estruturas escrito diretamente nas notas foi preservado e recebeu os complementos de flaser/wavy/lenticular e hummocky/swaley do ZIP unificado. As figuras de Wentworth, da carta cronoestratigráfica, de bioestratigrafia, de bacia sedimentar, de Hjulström e de Siccar Point foram recuperadas. Os PDFs antigos vieram no último ZIP e servem para conferência; eles não contêm todas as adições do `.tex` enviado separadamente.

## 2. Classificações e diagramas a conferir

- O triângulo e o prisma estão na parte de laboratório, conforme indicação expressa do autor.
- Os diagramas foram renderizados a partir dos códigos fornecidos; isso preserva seus campos e rótulos, sem validar a correspondência com a figura de Nichols/Pettijohn.
- O esquema curto do ZIP associa ortoconglomerado a suporte por clastos e paraconglomerado a suporte por matriz. As notas detalhadas explicitam também o critério aproximado de 15% de matriz e suas variações. Foi mantida a versão detalhada e sinalizada a diferença.
- As classificações genéticas e composicionais das rochas sedimentares não devem ser lidas como categorias necessariamente exclusivas. O glossário contém uma explicação sobre origens mistas; ela foi incorporada ao capítulo 8.
- Verificar a distinção entre desconformidade e paraconformidade nos diferentes trechos sobre discordâncias. Ambas as exposições foram conservadas no capítulo 10, com seus respectivos contextos.
- As afirmações históricas, as simplificações dos processos e os limites numéricos foram reorganizados, mas ainda não passaram por uma revisão bibliográfica completa.

## 3. Cor dos minerais — trecho separado para revisão

A tabela abaixo é uma transcrição da anotação original, não uma tabela validada de identificação. Ela associa cores a causas de maneira muito geral e precisa esclarecer se se refere a minerais, sedimentos ou condições de oxidação/redução. O verbete “Minerais: cor e traço”, mais contextualizado, foi colocado no laboratório.

| **Cor**        | **Provável Causa**            |
|:---------------|:------------------------------|
| Vermelho       | Oxidação                      |
| Amarelo/marrom | Enxofre ou Hidróxido          |
| Verde          | Reduzido                      |
| Cinza          | Menor concentração de Carbono |
| Preto          | Carbono + Matéria Orgânica    |
| Sarapintado    | Redução de íons               |
| Branco         | Eliminação de íons            |

Cores dos minerais

## 4. Classificação inicial — trechos preservados para revisão

A tabela inicial tinha relações pouco claras entre as colunas. Foi retirada da leitura principal e preservada abaixo. O capítulo 8 reúne as definições e a organização mais desenvolvida que já estavam no glossário.

| **ROCHAS SEDIMENTARES** |                             |               |
|:------------------------|:----------------------------|:--------------|
| Clásticas               |                             | Não clásticas |
| Vulcanoclásticas        |                             | Carbonatos    |
|                         | $\hookrightarrow$ Turfas    | Evaporitos    |
|                         | $\hookrightarrow$ Argilitos | Outros        |
| Terrígenas              |                             |               |
| Carbonáticas (CaCO$_3$) |                             |               |

Rochas sedimentares

A lista original após “São formados” era:

1.  Evaporitos,

2.  Carbonatos,

    - Sulfatos,

    - Cloritos.

Outras rochas sedimentares

1.  Carvão,

2.  Ironstones

3.  Depósitos silicosos

O termo “Cloritos” da lista acima deve ser conferido no material da aula, assim como a posição de sulfatos e carbonatos no encadeamento. Nenhuma correção científica foi presumida nesta transcrição.

## 5. Bowen e Goldich

Anotação original: “Nota: a série de Bowman invertida é a série de Goldich.”

O diagrama fornecido tem o título **Série de Reação de Bowen**. O nome foi uniformizado nos títulos do caderno. O ZIP unificado já contém uma explicação da relação com Goldich e uma referência `goldich1938`; esse texto foi incorporado ao capítulo 4. A frase original permanece aqui apenas para conferência.

## 6. Complementos das notas manuscritas

Reservar os seguintes destinos para o material que vier depois:

| Conteúdo da anotação | Destino |
| --- | --- |
| Explicação de conceito ou processo | Capítulo correspondente da teoria |
| Descrição de amostra ou procedimento de aula | Laboratório, com data e identificação |
| Detalhe sobre o triângulo ou o prisma | L3 ou L4 |
| Termo isolado com definição | Glossário, se couber no escopo |
| Contradição com o texto existente | Pendência de revisão, preservando as duas fontes |
| Repetição sem informação nova | Registro de repetição; evitar outra cópia na leitura principal |

## 7. O que foi preservado

As fontes efetivamente utilizadas estão preservadas em `originais`; o grande ZIP de livros e exercícios continua como arquivo enviado e está inventariado. A conversão integral das notas e as conversões dos 13 capítulos do ZIP unificado estão em `arquivo`, para conferir a ordem anterior e recuperar os trechos separados. As referências incompletas continuam identificadas por chave. Os diagramas têm imagens para o Markdown e os códigos em `diagramas_tex`. Os exercícios regionais foram transcritos separadamente e suas afirmações precisam de revisão; ainda faltam as notas manuscritas das práticas.

## 8. Chaves bibliográficas encontradas nas notas e no ZIP

O glossário usa `nocite{*}` no original, sem vincular referências individualmente aos verbetes. Sua bibliografia foi recuperada; o mapa de fontes que também veio no ZIP foi preservado como guia de revisão, sem transformar suas sugestões em citações já confirmadas.

- `anp_reconcavo`
- `boggs2012`
- `dott1964`
- `folk1970detrital`
- `fossen2016`
- `geolsoc_siccar`
- `geolsoc_smith`
- `goldich1938`
- `hampton1996submarine`
- `harms1975`
- `heilbron2016`
- `iverson2003gravity`
- `jacksonhudec2017`
- `kgsclassificacao`
- `magnavita2005`
- `miall1978`
- `milhomem2023baciassedimentares`
- `mit2007siliciclastic`
- `nichols2009`
- `powers1953`
- `rudwick1997`
- `trosdtorf2005glacial`
- `tucker2001`
- `usgs2004landslide`
- `uspconglomerado`
- `wentworth1922`
- `zerfass2008foraminiferos`

## 9. Referências ainda não recuperadas

- `folk1970detrital`
- `hampton1996submarine`
- `iverson2003gravity`
- `kgsclassificacao`
- `mit2007siliciclastic`
- `trosdtorf2005glacial`
- `usgs2004landslide`
- `uspconglomerado`

## 10. Convenção dos limites granulométricos

O guia anterior inclui 2 mm na areia; o glossário inclui esse limite no cascalho. Foi usado no laboratório o quadro mais explícito do glossário, que indica as desigualdades. A diferença de convenção está preservada nas cópias de conferência. Verificar a convenção adotada pelo professor.

## 11. Discrepâncias na figura de Wentworth enviada

Na figura abaixo, a classe “Boulder” aparece como “250–100” e “Coarse silt” como “0.031–0.625”. Esses registros diferem do quadro do glossário e exigem conferência na fonte. A imagem foi afastada da sequência principal de estudo, mantendo sua integridade.

![image](imagens/fonte_m1u5_table5_5_the_wentworth_scale.png)

## 12. Exercícios regionais e bibliografia do glossário

As apresentações antigas atribuem nomes, medidas, idades e interpretações tectônicas a falhas regionais. Esses dados foram transcritos como registro e precisam ser cotejados com os mapas e publicações citados, antes de voltarem à teoria. Campos com valor zero em tabelas cartográficas também precisam ser interpretados com a documentação do dado. A lista de termos e o mapa de fontes por verbete foram preservados como pendências, sem desenvolver novos conceitos nesta etapa.


## 12. Caderno manuscrito incorporado em 9 de outubro de 2026

O PDF original foi preservado. As páginas 6 e 9 repetem, respectivamente, as páginas 4 e 7 e não geraram novo conteúdo. As notas de Cartografia da página 7/9 não foram incorporadas ao texto de Geologia.

- Página 1: mão encobre parte da reação; página 2: margem direita cortada. Não foi inventado o texto ausente.
- Páginas 4/6: limites de seleção e sua associação resumida com maturidade precisam de confirmação da convenção usada na aula. Não foram acrescentados como tabela numérica validada.
- Página 5: a lista numerada do triângulo contém sinais de repetição e nomes pouco claros. Os percentuais dos exercícios foram incorporados, mas o gabarito nominal não foi forçado. A fração “grossa” foi interpretada como cascalho para o exercício, com aviso.
- Páginas 8/14/19/23: referências e abreviações incompletas (inclusive Galloway/Pritchard e RFS/RFI); identificar as obras e confirmar o uso na disciplina.
- Página 13: percentuais de abundância de rochas e lista econômica permanecem sem contexto/fonte suficiente.
- Página 18: velocidades de geleiras não foram generalizadas, pois faltam contexto e referência.
- Páginas 21–23: foram desenvolvidos os conceitos de componentes carbonáticos. “Pisoide = formado em caverna” e “peloide = necessariamente fecal” não foram adotados como definições gerais. A classificação completa de Folk não estava no caderno; o quadro de exemplos foi acrescentado a partir de fonte identificada.

## 13. Imagens de hidrólise e evaporitos

As duas imagens anteriormente enviadas foram incorporadas sem alteração de seus pixels. A imagem de hidrólise usa H₂SO₃/HSO₃⁻; a reação digitada para alteração por ácido carbônico usa H₂CO₃/HCO₃⁻. São espécies diferentes e as expressões não devem ser misturadas. Não se presume que a imagem tenha sido criada com a intenção de representar uma reação diferente ou que sua notação esteja confirmada: o original fica disponível para comparação.

O gráfico de evaporitos é explicitamente esquemático. Seus percentuais não têm fonte quantitativa identificada e não foram promovidos a limites universais de precipitação. A figura permanece acompanhada dessa indicação.

## 14. Limites desta atualização

A atualização cobre os complementos legíveis do caderno e revisa pontualmente conceitos novos. Não equivale a uma verificação completa de todos os capítulos herdados da primeira versão. Permanecem as chaves bibliográficas ausentes e o arquivo externo de formas de leito. Os textos longos e fontes anteriores foram preservados.
