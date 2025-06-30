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
## Tradução e mudança de tom em textos (Grok 3)

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

## Criação de figuras (Microsoft Copilot)

Para essa tarefa, tentarei ser bastante criativo e pedidei ao Microsoft Copilot, já instalado no W11, a criação de um quadro surrealista, seguindo o estilo de Salvador Dalí. Eu fui bastante detalhado no prompt e dei idéias que são presentes na obra de Dalí, de quem sou fã.

### O prompt usado

Crie um quadro surrealista, ao estilo de Salvador Dalí, que contenha um elefante alado com pernas longas, que tenha um cenário desértico escarpado, como o Grand Canyon, algumas árvores secas com relógios derretidos e um céu de tempestade, mas com um brilho forte emanando por entre as nuvens.

Ficou compatível com a temática Dalí, muito bom, mas não é um puro-sangue, longe disso. O resultado foi o seguinte:

![quadro](https://github.com/msccobra/Explora-o-das-funcionalidades-da-IA/blob/Images/Crie%20um%20quadro%20surre.png)

## Análise de sentimento (Claude Sonnet 4)

Para esse trecho, pegarei alguns comentários de notícias em grandes portais e pedirei que a IA faça uma análise de sentimento deles.

### Caso 1 ([Derrota do Flamengo por 4 a 2 no Mundial de clubes para o Bayern München](https://www.uol.com.br/esporte/futebol/ultimas-noticias/2025/06/29/flamengo-x-bayern-de-munique---mundial-de-clubes.htm))

A IA leu a imagem que está no [link](https://github.com/msccobra/Explora-o-das-funcionalidades-da-IA/blob/Images/C1.jpg), e fez a análise de sentimento. O resultado foi colado, sem edições.

#### Análise de Sentimento dos Comentários

Este documento apresenta a análise de sentimento de comentários extraídos de uma postagem em rede social.

#### Metodologia

A análise foi realizada identificando palavras-chave, tom emocional e contexto de cada comentário, classificando os sentimentos em uma escala de positivo a negativo.

#### Comentários Analisados

##### 1. Pedro Berrettini Jr
**Comentário:** "Cadê a soberba ?? Chora Mauro Cesar. Chora RMP. kkkkk"

- **Sentimento:** Negativo/Crítico
- **Indicadores:**
  - Uso de expressões depreciativas ("Cadê a soberba")
  - Tom de zombaria com "kkkkk"
  - Direcionamento crítico a pessoas específicas
- **Intensidade:** Moderada

##### 2. Luis Marcelo Inaco Cirino
**Comentário:** "Não consigo parar de rir. O Felipe Luiz era o novo Guardiola para a imprensa."

- **Sentimento:** Negativo/Desapontado
- **Indicadores:**
  - Ironia evidente ("não consigo parar de rir")
  - Crítica indireta ao desempenho
  - Sarcasmo sobre expectativas da imprensa
- **Intensidade:** Moderada

##### 3. Ivan Leite Albanese
**Comentário:** "Quartas de final do Primeiro Mundial de verdade é apenas para Gigantes. Tchau Cheirinho. Avanti Palestra!"

- **Sentimento:** Negativo/Provocativo
- **Indicadores:**
  - Diminuição da conquista ("apenas para Gigantes")
  - Provocação direta ("Tchau Cheirinho")
  - Tom de rivalidade esportiva
- **Intensidade:** Moderada a Alta

##### 4. Marcos Silva
**Comentário:** "Volte pra casa Varmengo mediocre!!! Quando não tem influência da Grobo, VAR ou crime organizado, este time fica medíocre. Harry Kane mandou 2 abraços kkkkkkkkkk"

- **Sentimento:** Muito Negativo/Revoltado
- **Indicadores:**
  - Linguagem agressiva ("mediocre", "Varmengo")
  - Acusações graves (crime organizado)
  - Frustração evidente com arbitragem
  - Uso excessivo de "k" indicando deboche
- **Intensidade:** Muito Alta

##### 5. Eduardo Lima de Moraes
**Comentário:** "Os Flamimimengos esqueceram que: se é Bayer, é bom."

- **Sentimento:** Negativo/Sarcástico
- **Indicadores:**
  - Uso de termo pejorativo ("Flamimimengos")
  - Ironia sobre a qualidade do adversário
  - Tom de desdém disfarçado
- **Intensidade:** Moderada

### Resumo da Análise

#### Distribuição de Sentimentos
- **Negativos:** 5 comentários (100%)
- **Neutros:** 0 comentários (0%)
- **Positivos:** 0 comentários (0%)

#### Características Gerais
- **Contexto:** Aparenta ser sobre evento esportivo (futebol)
- **Tons predominantes:** Sarcasmo, provocação, frustração
- **Alvos das críticas:** Jogadores, técnicos, arbitragem, imprensa
- **Indicadores de rivalidade:** Presença de apelidos pejorativos e provocações entre torcidas

#### Palavras-chave Identificadas
- **Negativas:** mediocre, soberba, crime organizado
- **Sarcásticas:** kkkkk, Flamimimengos, Varmengo
- **Provocativas:** Tchau, Chora, Avanti Palestra

### Conclusão

Todos os comentários analisados apresentam sentimento predominantemente negativo, variando entre crítica construtiva, sarcasmo, provocação e revolta. O contexto sugere reações a um resultado esportivo desfavorável, com torcedores expressando frustração através de diferentes níveis de negatividade e rivalidade típica do ambiente futebolístico brasileiro.

---

*Análise realizada através de processamento de linguagem natural e identificação de padrões emocionais em texto.*

## Caso 2 ([Brasileira não regatada em vulcão](https://noticias.uol.com.br/internacional/ultimas-noticias/2025/06/29/vaquinha-agam-rinjani-cancelada.htm)

A IA leu a [imagem](https://github.com/msccobra/Explora-o-das-funcionalidades-da-IA/blob/Images/C2.png) para fazer a análise a seguir:

### Análise de Sentimento - Comentários sobre VOOA

Este documento apresenta a análise de sentimento de comentários relacionados à empresa VOOA e uma situação envolvendo voluntário e taxas de serviço.

#### Metodologia

A análise foi realizada identificando palavras-chave, tom emocional e contexto de cada comentário, classificando os sentimentos em uma escala de positivo a negativo.

#### Comentários Analisados

##### 1. Júlio Pereira
**Comentário:** "Preferem não dar nada para o voluntário a abrir mão da taxa absurda que estão cobrando? Isso mostra que são parasitas e que não merecem respeito e muito menos confiança."

- **Sentimento:** Muito Negativo/Indignado
- **Indicadores:**
  - Linguagem extremamente ofensiva ("parasitas")
  - Crítica direta à política de preços ("taxa absurda")
  - Questionamento moral da empresa
  - Perda total de confiança
  - Tom de indignação e revolta
- **Intensidade:** Muito Alta
- **Aspectos criticados:** Política de preços, tratamento ao voluntário, caráter da empresa

##### 2. Luiz Carlos Amorim
**Comentário:** "Sabemos que de graça nem injeção na testa, mas cobrar 20% também é exagero, a Voaa precisa ajustar seu negócio."

- **Sentimento:** Negativo/Crítico Construtivo
- **Indicadores:**
  - Reconhecimento da realidade comercial
  - Crítica moderada mas direta ("é exagero")
  - Sugestão de melhoria ("precisa ajustar")
  - Tom equilibrado e racional
  - Uso de ditado popular para contextualizar
- **Intensidade:** Moderada
- **Aspectos criticados:** Percentual da taxa, modelo de negócio

##### 3. Alberto Lazzarini Neto
**Comentário:** "Gente ele arriscou a vida para buscar o corpo, ele merece uma recompensa"

- **Sentimento:** Positivo/Empático
- **Indicadores:**
  - Reconhecimento do risco assumido pelo voluntário
  - Defesa clara da pessoa envolvida
  - Tom de solidariedade e justiça
  - Empatia com a situação
  - Senso de merecimento
- **Intensidade:** Moderada a Alta
- **Aspectos destacados:** Coragem do voluntário, justiça da recompensa

##### 4. Maurício Pombar Trindade
**Comentário:** "Como dizia minha avó: ficou pior a emenda do que o soneto ou o remendo do que o rasgo. Criaram expectativas e frustraram a todos. Uma atitude lamentável da empresa que, evidentemente, busca o lucro (nada errado nisso), mas que não foi devidamente transparente (como admitiu) e não soube lidar com as críticas, optando por devolver o dinheiro (obrigação) e, repita-se, frustrar a todos que se engajaram nesse processo. Quem perdeu mais? A própria empresa, que não soube retirar algo proveitoso com a experiência negativa. Não seria muito melhor se procurassem remediar o lapso, até por uma questão humanitária, repassando o valor integral da vaquinha ao abnegado voluntário? Decerto, deixariam de embolsar 100 k de imediato, mas ganhariam muito mais ao apagar os arranhões deixados na empresa em razão do alcance das redes sociais. Seguramente, sairiam melhor na foto. Nota para a equipe de marketing da VOOA = ZERO"

- **Sentimento:** Muito Negativo/Analítico Crítico
- **Indicadores:**
  - Crítica estruturada e fundamentada
  - Uso de ditados populares para enfatizar ("pior a emenda que o soneto")
  - Análise detalhada de gestão de crise
  - Reconhecimento parcial (busca por lucro é legítima)
  - Crítica severa à transparência e gestão
  - Sugestões estratégicas de melhoria
  - Avaliação categórica negativa (nota zero)
  - Tom professoral/consultivo
- **Intensidade:** Muito Alta
- **Aspectos criticados:** Gestão de crise, transparência, estratégia de marketing, gestão de expectativas

#### Resumo da Análise

##### Distribuição de Sentimentos
- **Muito Negativos:** 2 comentários (50%)
- **Negativos:** 1 comentário (25%)
- **Positivos:** 1 comentário (25%)
- **Neutros:** 0 comentários (0%)

#### Características por Tipo de Comentário

#### Comentários Negativos (75%)
- **Críticas à empresa:** Política de preços, transparência, gestão
- **Tons variados:** Indignação, análise crítica, sugestão construtiva
- **Linguagem:** De moderada a extremamente crítica

#### Comentários Positivos (25%)
- **Foco no voluntário:** Reconhecimento do risco e mérito
- **Tom empático:** Solidariedade com a pessoa envolvida

#### Principais Temas Identificados

1. **Política de Taxas:** Críticas ao percentual cobrado (20%)
2. **Tratamento ao Voluntário:** Discussão sobre recompensa justa
3. **Gestão Empresarial:** Críticas à transparência e gestão de crise
4. **Aspecto Humanitário:** Reconhecimento do risco assumido pelo voluntário

#### Palavras-chave por Sentimento

**Negativas:**
- Extremas: parasitas, absurda, lamentável, zero
- Moderadas: exagero, ajustar, frustrar
- Técnicas: transparente, gestão de crise, marketing

**Positivas:**
- arriscou, merece, recompensa, abnegado

#### Níveis de Elaboração

1. **Comentários Simples:** Diretos e emocionais (Júlio, Alberto)
2. **Comentários Moderados:** Equilibrados com sugestões (Luiz Carlos)
3. **Comentários Complexos:** Análise detalhada e estratégica (Maurício)

### Conclusão

A análise revela uma percepção predominantemente negativa (75%) da situação envolvendo a VOOA, com críticas focadas em três aspectos principais:

1. **Política comercial** considerada abusiva
2. **Gestão de crise** avaliada como inadequada  
3. **Questões éticas** relacionadas ao tratamento do voluntário

O único sentimento positivo identificado está direcionado ao voluntário, não à empresa, indicando uma clara separação entre a avaliação da pessoa física (positiva) e da pessoa jurídica (negativa).

Os comentários variam de críticas construtivas com sugestões de melhoria até indignação total com linguagem ofensiva, sugerindo diferentes níveis de engajamento e expectativa dos usuários em relação à empresa.

---

*Análise realizada através de processamento de linguagem natural e identificação de padrões emocionais em texto.*

# Conclusão

Com isso, concluímos a exploração de alguns dos usos das ferramentas de IA generativa do mercado. Existem muitas mais e muitas mais irão surgir no futuro. Aqui procurei dar apenas uma rápida "pincelada" no tema.


