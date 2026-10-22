# Ajustes não lineares linearizáveis

Os modelos exponencial e potência são diferentes, embora ambos possam ser linearizados por meio de logaritmos.

## 1. Modelo exponencial

O modelo exponencial é:

$$
y=\alpha\beta^x.
$$

Aplicando o logaritmo natural:

$$
\begin{aligned}
\ln y
&=\ln\left(\alpha\beta^x\right)\\
&=\ln\alpha+\ln\left(\beta^x\right)\\
&=\ln\alpha+x\ln\beta.
\end{aligned}
$$

Definindo:

$$
Y=\ln y,\qquad A=\ln\alpha,\qquad B=\ln\beta,
$$

obtemos a equação linear:

$$
Y=A+Bx.
$$

Portanto, faz-se a regressão linear de $\ln y$ em função de $x$. Depois do ajuste:

$$
\alpha=e^A
\qquad\text{e}\qquad
\beta=e^B.
$$

Esse modelo é indicado quando $y$ varia aproximadamente por uma **proporção ou porcentagem constante** a cada unidade acrescentada a $x$.

Exemplos:

- crescimento populacional;
- crescimento de bactérias;
- juros compostos;
- decaimento radioativo;
- carga ou descarga de capacitores.

Interpretação de $\beta$:

- $\beta>1$: crescimento exponencial;
- $0<\beta<1$: decaimento exponencial;
- $\beta=1$: $y$ permanece constante.

Por exemplo:

$$
y=10(1{,}2)^x
$$

representa um crescimento de $20\%$ a cada unidade acrescentada a $x$.

## 2. Modelo potência

O modelo potência é:

$$
y=\beta x^\alpha.
$$

Aplicando o logaritmo natural:

$$
\begin{aligned}
\ln y
&=\ln\left(\beta x^\alpha\right)\\
&=\ln\beta+\ln\left(x^\alpha\right)\\
&=\ln\beta+\alpha\ln x.
\end{aligned}
$$

Observe que o termo constante é $\ln\beta$, e não $\ln\alpha$.

Definindo:

$$
Y=\ln y,\qquad X=\ln x,\qquad A=\ln\beta,
$$

obtemos:

$$
Y=A+\alpha X.
$$

Portanto, faz-se a regressão linear de $\ln y$ em função de $\ln x$. Depois do ajuste:

$$
\beta=e^A,
$$

enquanto $\alpha$ é diretamente o coeficiente angular da reta.

Esse modelo é indicado quando existe uma relação de **escala** entre as variáveis.

Exemplos:

- área em função de um comprimento: $A\propto L^2$;
- volume em função de um comprimento: $V\propto L^3$;
- relações alométricas entre massa e tamanho de organismos;
- velocidade, vazão ou energia relacionadas a potências de outra variável.

Por exemplo:

$$
y=3x^2.
$$

Se $x$ dobrar, $y$ será multiplicado por:

$$
2^2=4.
$$

## Comparação prática

| Modelo | Equação | Regressão linearizada | Característica |
|---|---|---|---|
| Exponencial | $y=\alpha\beta^x$ | $\ln y$ contra $x$ | Acréscimos iguais em $x$ produzem razões iguais em $y$ |
| Potência | $y=\beta x^\alpha$ | $\ln y$ contra $\ln x$ | Multiplicar $x$ por um fator multiplica $y$ por outro fator |

Uma forma prática de distinguir os modelos é:

- se o gráfico de $\ln y$ em função de $x$ formar aproximadamente uma reta, o modelo exponencial pode ser adequado;
- se o gráfico de $\ln y$ em função de $\ln x$ formar aproximadamente uma reta, o modelo potência pode ser adequado.

## Condições e cuidados

- Para linearizar o modelo exponencial, é necessário que $y>0$.
- Para linearizar o modelo potência, é necessário que $x>0$ e $y>0$.
- A escolha do modelo deve considerar o significado físico do fenômeno e o comportamento dos resíduos, não apenas o maior $R^2$.
- O ajuste após a transformação logarítmica minimiza os erros na escala de $\ln y$. Portanto, ele não é necessariamente idêntico ao ajuste não linear feito diretamente na escala original de $y$.
