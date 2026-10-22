# Covariância e correlação linear

## 1. Relação entre duas variáveis quantitativas

Até aqui, estudamos medidas que descrevem uma variável isoladamente, como média, variância e desvio padrão. Entretanto, muitas análises estatísticas procuram verificar se existe alguma relação entre **duas variáveis quantitativas** observadas nos mesmos indivíduos ou elementos da amostra.

Alguns exemplos são:

- altura e massa corporal de uma pessoa;
- temperatura e salinidade da água do mar;
- velocidade do vento e altura das ondas;
- tempo de estudo e nota obtida em uma prova.

Cada observação é representada por um par ordenado:

$$
(x_i,y_i),
$$

em que $x_i$ é o valor da variável $X$ e $y_i$ é o valor correspondente da variável $Y$ na mesma observação.

Antes de calcular qualquer medida numérica, é recomendável representar os pares de valores em um **diagrama de dispersão**.

## 2. Diagrama de dispersão

No diagrama de dispersão, os valores da variável $X$ são colocados no eixo horizontal, enquanto os valores da variável $Y$ são colocados no eixo vertical. Cada par $(x_i,y_i)$ aparece como um ponto no gráfico.

O gráfico permite observar três características importantes da relação entre as variáveis:

1. **Direção**: positiva, negativa ou sem direção evidente;
2. **Forma**: linear ou não linear;
3. **Intensidade**: pontos mais próximos ou mais afastados de uma tendência.

### Relação positiva

Quando os valores de $X$ aumentam e os valores de $Y$ também tendem a aumentar, a relação apresenta direção positiva. No gráfico, os pontos mostram uma tendência ascendente da esquerda para a direita.

### Relação negativa

Quando os valores de $X$ aumentam e os valores de $Y$ tendem a diminuir, a relação apresenta direção negativa. Nesse caso, os pontos mostram uma tendência descendente da esquerda para a direita.

### Ausência de relação linear evidente

Quando os pontos ficam muito dispersos e não apresentam uma tendência crescente ou decrescente, pode não haver uma relação linear evidente. Isso não significa necessariamente que as variáveis sejam completamente independentes, pois pode existir uma relação não linear.

## 3. Covariância

A covariância é uma medida numérica que indica como duas variáveis variam conjuntamente em relação às suas médias.

Para compreender a ideia, observamos os produtos:

$$
(x_i-\bar{x})(y_i-\bar{y}).
$$

Esses produtos podem ser interpretados da seguinte forma:

- se $x_i$ e $y_i$ estiverem ambos acima de suas médias, o produto será positivo;
- se $x_i$ e $y_i$ estiverem ambos abaixo de suas médias, o produto também será positivo;
- se um valor estiver acima de sua média e o outro abaixo, o produto será negativo.

Portanto, quando as duas variáveis tendem a aumentar ou diminuir juntas, predominam produtos positivos. Quando uma tende a aumentar enquanto a outra diminui, predominam produtos negativos.

### Covariância amostral

Para uma amostra com $n$ pares de observações, a covariância amostral é calculada por:

$$
s_{XY}=\frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{n-1}.
$$

Nessa expressão:

- $x_i$ e $y_i$ são os valores de cada par de observações;
- $\bar{x}$ é a média da variável $X$;
- $\bar{y}$ é a média da variável $Y$;
- $n$ é o número de pares de observações;
- $s_{XY}$ é a covariância amostral entre $X$ e $Y$.

### Interpretação do sinal da covariância

- $s_{XY}>0$: as variáveis apresentam tendência conjunta positiva;
- $s_{XY}<0$: as variáveis apresentam tendência conjunta negativa;
- $s_{XY}\approx 0$: não há tendência **linear** conjunta evidente.

O valor da covariância depende das unidades e das escalas das duas variáveis. Se $X$ for medido em metros e $Y$ em segundos, por exemplo, a unidade da covariância será metro-segundo. Além disso, uma simples mudança de escala pode alterar bastante seu valor numérico.

Por essa razão, a covariância é útil principalmente para indicar a **direção** da relação, mas seu módulo não possui uma escala padronizada que permita avaliar facilmente a intensidade da associação.

## 4. Coeficiente de correlação linear de Pearson

O coeficiente de correlação linear de Pearson transforma a covariância em uma medida adimensional e padronizada. Para isso, divide-se a covariância pelo produto dos desvios padrão das duas variáveis:

$$
r=\frac{s_{XY}}{s_Xs_Y}.
$$

Substituindo as expressões da covariância e dos desvios padrão, também podemos escrever:

$$
r=
\frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}
{\sqrt{\sum_{i=1}^{n}(x_i-\bar{x})^2}\,
 \sqrt{\sum_{i=1}^{n}(y_i-\bar{y})^2}}.
$$

O coeficiente de correlação sempre se encontra no intervalo:

$$
-1\leq r\leq 1.
$$

Como $s_X$ e $s_Y$ são sempre positivos, o sinal de $r$ é o mesmo sinal da covariância.

## 5. Interpretação do coeficiente de correlação

O sinal do coeficiente indica a **direção** da relação linear:

- $r>0$: correlação linear positiva;
- $r<0$: correlação linear negativa;
- $r\approx 0$: correlação linear ausente ou muito fraca.

O módulo $|r|$ indica o grau de aproximação dos pontos a uma linha reta:

- quanto mais próximo de $1$, mais forte é a associação linear;
- quanto mais próximo de $0$, mais fraca é a associação linear.

Os casos extremos são:

- $r=1$: correlação linear positiva perfeita;
- $r=-1$: correlação linear negativa perfeita;
- $r=0$: ausência de correlação **linear**.

Como orientação inicial, e não como regra universal, pode-se utilizar a seguinte classificação para o módulo de $r$:

| Módulo de $r$ | Interpretação aproximada |
|---:|:---|
| $0,00\leq |r|<0,20$ | muito fraca |
| $0,20\leq |r|<0,40$ | fraca |
| $0,40\leq |r|<0,60$ | moderada |
| $0,60\leq |r|<0,80$ | forte |
| $0,80\leq |r|\leq 1,00$ | muito forte |

Esses limites são apenas referências. A interpretação adequada depende da área de estudo, da qualidade das medições, do tamanho da amostra e do fenômeno analisado. Por isso, é recomendável apresentar o valor calculado de $r$ e examinar também o diagrama de dispersão, em vez de informar somente uma classificação verbal.

Por exemplo:

- $r=0{,}87$ indica uma correlação linear positiva muito forte;
- $r=-0{,}72$ indica uma correlação linear negativa forte;
- $r=0{,}08$ indica uma correlação linear positiva muito fraca, praticamente sem tendência linear.

## 6. Cuidados na interpretação

### Correlação não implica causalidade

Uma correlação elevada entre duas variáveis não demonstra, por si só, que uma delas cause alterações na outra. A associação pode resultar da ação de uma terceira variável, de uma coincidência ou de uma relação indireta entre os fenômenos.

### O coeficiente de Pearson mede relações lineares

É possível obter um valor de $r$ próximo de zero mesmo quando existe uma relação não linear forte entre as variáveis. O diagrama de dispersão é essencial para perceber esse tipo de comportamento.

### Valores extremos podem alterar o resultado

O coeficiente de correlação é sensível a valores discrepantes. Um único ponto muito afastado dos demais pode aumentar, diminuir ou até inverter a correlação observada. Por isso, os valores extremos devem ser investigados, mas não eliminados automaticamente.

### A correlação deve ser analisada no contexto

O valor de $r$ resume apenas a direção e a intensidade da associação linear. Uma análise completa deve considerar o gráfico, a natureza das variáveis, o tamanho da amostra, possíveis erros de medição e o conhecimento sobre o fenômeno estudado.

## Síntese

A sequência lógica da análise é:

1. representar os pares de observações em um diagrama de dispersão;
2. observar a direção, a forma e a intensidade aparente da relação;
3. calcular a covariância para identificar a direção da variação conjunta;
4. calcular o coeficiente de correlação para obter uma medida padronizada da associação linear;
5. interpretar o valor de $r$ em conjunto com o gráfico e com o contexto dos dados.

Assim, a covariância fornece a base matemática da correlação, enquanto o coeficiente de correlação facilita a comparação e a interpretação da relação linear entre duas variáveis.
