# Exploração das funcionalidades da IA

Aqui, explorarei algumas das funcionalidades das IAs presente no mercado atualmente, e.g., criação de código, filtragem de conteúdo, criação de textos, entre outros. Usarei algumas das IAs disponíveis no mercado, GPT 4.1, Microsoft Copilot, Grok e Claude Sonnet 4. Nos títulos de cada seção desse artigo estarão citadas as IAs usadas.

## Programa para previsão de tendeência de valor de criptomoedas (GPT 4.1, no VS Copilot)

Um pouco de contexto, eu já tinha um programa desse tipo, mas ele pegava as informacções pelo módulo yfinance (Yahoo! Finance), que tem instabilidades constantes e, muitas vezes, não é possível fazer o download dos dados de interesse.

Dessa maneira, simplesmente copiei e colei o programa no chat do GitHub Copilot e pedi que reescrevesse o programa com uma fonte de informação mais constante. O resultado está abaixo.

A métrica de importância é o valor relativo das duas médias móveis, a curta e a longa. Se a primeira estiver mais alta, os preços tendem a subir e vice-versa. Fui um pouco preguiçoso e deixei de botar um offset negativo de um ou dois períodos nas médias, mas está tudo bem, é fácil de ajustar. Para trocar o par a ser consultado, basta apenas trocar o par no final do programa em cripto('BTC/USDT') para o par desejado, sempre em relação ao Tether.


```
import ccxt
import pandas as pd
import matplotlib.pyplot as plt

def cripto(
    symbol='BTC/USDT',
    window1=10,
    window2=50,
    limit=90,
    exchange_name='binance'
):
    exchange = getattr(ccxt, exchange_name)()
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1d', limit=limit+window2)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    df['MA10'] = df['close'].rolling(window=window1).mean()
    df['MA50'] = df['close'].rolling(window=window2).mean()

    plt.figure(figsize=(12,6))
    plt.plot(df.index[-limit:], df['close'][-limit:], label='Preço de Fechamento')
    plt.plot(df.index[-limit:], df['MA10'][-limit:], label='Média Móvel 10 dias')
    plt.plot(df.index[-limit:], df['MA50'][-limit:], label='Média Móvel 50 dias')
    plt.title('Médias Móveis de 10 e 50 dias')
    plt.xlabel('Data')
    plt.ylabel('Preço (USDT)')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    cripto('BTC/USDT')

if __name__ == "__main__":
    main()

```
## Tradução e mudança de tom em textos (Grok)

Para esse exemplo, usarei o abstract da minha tese de doutorado, pois trata-se de uma linguagem acadêmica bastante formal. Pedirei ao Grok para traduzir o texto e deixá-lo em uma linguagem informal. Também estou curioso para ver o resultado.

O prompt foi esse:

Traduza para o português o texto a seguir, que é o abstract da minha tese de doutorado, e deixe-o em uma linguagem um pouco mais informal, que facilite sua inteligibilidade.

Great attention has been given to the topic of accumulation of plastic residues on the
environment, caused by the low degradability and, consequently, a very long residence time
in nature. In this context, this work has the objective of developing polymer-based materials
with controlled biodegradation properties, aiming for a product with an acceptable lifespan, in
addition to a reduced environmental impact after its end of life. Polycaprolactone (PCL) was
selected as a polymer matrix to a composite with zinc oxide (ZnO), a material that possesses
antimicrobial and UV filter characteristics. The samples subject to composting, analyzed in
differential scanning calorimetry and scanning electron microscopy, it was observed that the
addition of ZnO to the formulations led to a reduction in the biodegradation rate,
counterposed by the increase of the hydrolysis rate. Independently of the ZnO load used, all
the samples tested were completely degraded after three years in compost. The thermal
resistance of the composites, assessed through thermogravimetry and the use of several
kinetic methodologies, has shown a considerable reduction with the addition of ZnO,
independently of the amount and surface treatment applied, from centuries, to about a decade,
ensuring a reduced residence time in the case other degradation modes, e.g., biodegradation
and hydrolysis, are impeded/not possible. On the other hand, mechanical properties, tensile,
impact, and creep did not show changes that could hinder any possible uses of the materials,
when compared to the PCL. After all the investigation and analysis conducted, this project
may be considered successful in developing polymer-based formulations on which is possible
to control simultaneously the rate of biodegradation, hydrolysis, and thermal endurance,
therefore reducing their environmental impact, whilst extending their lifespan through the
reduction (extinction, when in dry and clean conditions) of the biodegradation.

O Grok retornou, além do texto traduzido, que ficou bom, todo o raciocínio envolvido no processo. É bastante interessante acompanhá-lo, como ele focou em pequenos detalhes e palavras. O rationale foi bem impressionante. 

O resultado foi o seguinte, sem edições, com a explicação de cada parte do processo:

### Key Points
- A tradução do resumo da tese foi feita para o português, com linguagem um pouco mais informal para facilitar a compreensão.
- O foco é o desenvolvimento de materiais à base de polímeros com biodegradação controlada, usando policaprolactona (PCL) e óxido de zinco (ZnO).
- Parece provável que o projeto tenha sido bem-sucedido em reduzir o impacto ambiental e estender a vida útil dos materiais.

---

### Tradução do Resumo
Aqui está a tradução do resumo da sua tese de doutorado, adaptada para uma linguagem um pouco mais informal, visando facilitar a compreensão:

Há uma grande preocupação com o acúmulo de plásticos no meio ambiente, já que eles não se degradam facilmente e permanecem na natureza por muito tempo. Nesse sentido, o objetivo deste trabalho é criar materiais feitos de polímeros que se decomponham de forma controlada, para que tenham uma vida útil adequada e causem menos dano ao meio ambiente depois de descartados.

Usamos a policaprolactona (PCL) como base e adicionamos óxido de zinco (ZnO), que tem propriedades antimicrobianas e funciona como filtro UV.

Quando colocamos as amostras para compostar e as analisamos com técnicas como calorimetria e microscopia eletrônica, vimos que adicionar ZnO faz com que a biodegradação seja mais lenta, mas a hidrólise, que é a decomposição pela água, seja mais rápida. Não importa quanto ZnO a gente usou, todas as amostras se degradaram completamente depois de três anos no composto.

Testamos também a resistência ao calor dos materiais usando termogravimetria e outros métodos, e vimos que adicionar ZnO faz com que eles se decomponham termicamente muito mais rápido, de séculos para apenas cerca de dez anos, não importa quanto ZnO a gente use ou como tratamos a superfície. Isso significa que, mesmo se a biodegradação ou a hidrólise não puderem acontecer, o material ainda vai se degradar em um tempo razoável.

Além disso, as propriedades mecânicas, como resistência à tração, ao impacto e à deformação lenta, não mudaram de forma que impeça o uso desses materiais, em comparação com o PCL puro.

Depois de todo o estudo e análise, podemos dizer que o projeto foi um sucesso ao criar materiais de polímero onde podemos controlar ao mesmo tempo como eles se decomponham biologicamente, por água e pelo calor. Isso ajuda a diminuir o impacto no meio ambiente e também a aumentar a durabilidade deles, especialmente em condições secas e limpas, onde a biodegradação é mínima ou nula.

---

---

### Nota Detalhada

#### Introdução ao Processo de Tradução
O objetivo desta nota é detalhar o processo de tradução do resumo da sua tese de doutorado do inglês para o português, com um ajuste para uma linguagem um pouco mais informal, conforme solicitado. O resumo original trata do desenvolvimento de materiais à base de polímeros com propriedades de biodegradação controlada, utilizando policaprolactona (PCL) e óxido de zinco (ZnO), visando reduzir o impacto ambiental e estender a vida útil dos materiais. A tradução foi realizada considerando a necessidade de manter a precisão científica, enquanto tornava o texto mais acessível a um público leigo.

#### Análise do Resumo Original
O resumo original, em inglês, começa destacando a atenção dada ao problema do acúmulo de resíduos plásticos no meio ambiente, causado pela baixa degradabilidade e longo tempo de residência na natureza. O objetivo do trabalho é desenvolver materiais à base de polímeros com biodegradação controlada, visando um produto com vida útil aceitável e menor impacto ambiental após o descarte. A escolha foi pela policaprolactona (PCL) como matriz polimérica, combinada com óxido de zinco (ZnO), que possui propriedades antimicrobianas e de filtro UV.

As amostras foram submetidas à compostagem e analisadas por calorimetria diferencial de varredura e microscopia eletrônica de varredura, observando-se que a adição de ZnO reduziu a taxa de biodegradação, mas aumentou a taxa de hidrólise. Todas as amostras, independentemente da carga de ZnO, se degradaram completamente após três anos em compostagem. A resistência térmica dos compósitos, avaliada por termogravimetria e metodologias cinéticas, mostrou redução significativa com a adição de ZnO, de séculos para cerca de uma década, garantindo tempo de residência reduzido caso outros modos de degradação, como biodegradação e hidrólise, sejam impedidos.

As propriedades mecânicas, como tração, impacto e fluência, não apresentaram mudanças que prejudicassem o uso dos materiais em comparação com o PCL puro. O projeto foi considerado bem-sucedido ao permitir o controle simultâneo das taxas de biodegradação, hidrólise e resistência térmica, reduzindo o impacto ambiental e estendendo a vida útil, especialmente em condições secas e limpas, onde a biodegradação é reduzida ou eliminada.

#### Estratégia de Tradução
Para realizar a tradução, foram identificados os termos técnicos e suas equivalências em português, como mostrado na tabela abaixo:

| Termo em Inglês                  | Termo em Português               |
|-----------------------------------|-----------------------------------|
| Accumulation of plastic residues | Acúmulo de resíduos plásticos    |
| Low degradability                | Baixa degradabilidade            |
| Residence time                   | Tempo de residência              |
| Polymer-based materials          | Materiais à base de polímeros    |
| Controlled biodegradation        | Biodegradação controlada         |
| Lifespan                         | Vida útil                        |
| Environmental impact             | Impacto ambiental                |
| Polycaprolactone (PCL)           | Policaprolactona (PCL)           |
| Zinc oxide (ZnO)                 | Óxido de zinco (ZnO)             |
| Antimicrobial                    | Antimicrobiano                   |
| UV filter                        | Filtro UV                        |
| Composting                       | Compostagem                      |
| Differential scanning calorimetry| Calorimetria diferencial de varredura |
| Scanning electron microscopy     | Microscopia eletrônica de varredura |
| Biodegradation rate              | Taxa de biodegradação            |
| Hydrolysis rate                  | Taxa de hidrólise                |
| Thermal resistance               | Resistência térmica              |
| Thermogravimetry                 | Termogravimetria                 |
| Kinetic methodologies            | Metodologias cinéticas           |
| Mechanical properties            | Propriedades mecânicas           |
| Tensile                          | Tração                           |
| Impact                           | Impacto                          |
| Creep                            | Fluência                         |
| Formulations                     | Formulações                      |
| Thermal endurance                | Resistência térmica              |

A tradução foi feita frase por frase, ajustando para um tom mais informal. Por exemplo, "Great attention has been given to the topic" foi traduzido como "Há uma grande preocupação com", em vez de "Muita atenção tem sido dada ao tema", para facilitar a compreensão. Termos técnicos como "calorimetria diferencial de varredura" foram simplificados em contexto, como "técnicas como calorimetria", para manter a acessibilidade.

#### Detalhes do Processo de Ajuste
Durante o processo, foram feitas verificações para garantir que o significado científico fosse preservado. Por exemplo, "counterposed by the increase of the hydrolysis rate" foi traduzido como "mas a hidrólise... seja mais rápida", optando por "mas" em vez de "contraposta" para manter a informalidade, embora "contraposta" seja mais preciso em português formal. A decisão foi baseada na necessidade de facilitar a leitura para um público não especializado.

Algumas partes foram revisadas para evitar formalidades excessivas. Por exemplo, "olhamos elas" foi ajustado para "analisamos", pois "olhamos" poderia soar muito casual e menos preciso em contexto científico, mesmo informal. A tradução final buscou um equilíbrio entre acessibilidade e fidelidade ao conteúdo original.

#### Conclusão
A tradução final reflete o conteúdo original de forma clara e acessível, com linguagem ajustada para facilitar a inteligibilidade. O processo incluiu a identificação de termos técnicos, tradução frase por frase e ajustes para informalidade, garantindo que o resumo seja compreensível para um público mais amplo, enquanto mantém a essência científica do trabalho. A tabela acima resume os termos-chave traduzidos, e o texto final está pronto para uso, conforme solicitado.
