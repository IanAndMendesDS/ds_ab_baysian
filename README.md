# Teste A/B Bayesiano

# 0.0 Guideline

Esse é um projeto de Data Science, focado em estatística aplicada através do uso do Teste A/B. No qual o objetivo era provar estatísticamente qual página apresenta maior sucesso na captura de leads,
trazendo uma resposta no menor tempo possível. Para isso foi utilizado o teste A/B Bayesiano, junto com o conceito de Multi-Armed-Bandit.

O conjunto de dados foi feito de forma sintética através de um scrapper.

# 1.0 Descrição do problema
A empresa iSketch, localizada em São Paulo, fabrica e disponibiliza um software com foco no desenvolvimento 3D de projetos para construção civil, como forma de prototipagem de grandes projetos.

Para usar o software, o cliente precisa adquirir uma licença de uso que se renova anualmente.

Uma das melhores estratégias de aquisição de clientes da iSketch é a captura do email dos clientes em troca de uma Newsletter com conteúdos semanais sobre construção civil.
A assinatura da newsletter permite começar um relacionamento entre a iSketch e as pessoas, a fim de mostrar as vantagens de utilizar o software para criar protótipos de construções civis.

Portanto, a melhoria de conversão da página de captura de email, ofertando a newsletter em troca, é crucial para o crescimento do número de clientes.

Sendo assim, o coordenador de Marketing da empresa pediu ao time de Designers que criassem uma nova página de captura de email com uma pequena modificação nas cores do botão de “sign-up”,
a fim de aumentar a conversão da página.

O time de Designers criaram uma página com o botão de “sign-up” vermelho para ser testada contra a página atual que possui o botão de “sign-up” azul.
O coordenador de Marketing tem pressa em testar a nova página, pois a empresa vem adquirindo poucos clientes nas últimas semanas e isso pode comprometer o faturamento anual da empresa.

O time de Cientistas de Dados da iSketch foi acionando com a missão de testar a nova página de captura de email o mais rápido possível.
A primeira idéia foi planejar um experimento de teste A/B entre as duas páginas por um período de 7 dias, para concluir a efetividade da mudança da cor do botão.
Porém, o coordenador de Marketing categoricamente disse ao time de dados que não poderia esperar 7 dias e solicitou que concluíssem em menos tempo.

## 1.1 Problema de Negócio
Juntamente com o time de negócio, propor soluções para ajudar na avaliação da nova página de captura. O entregável deve responder a seguinte pergunta:
- A nova página apresenta uma conversão maior ou pior que a página atual?
  - A resposta precisa vir o mais rápido possível!

# 2.0 Descrição dos dados
A base de dados foi gerada de forma sintética, foram criadas duas páginas fictícias para simular os clicks nas páginas, análogo a casos reais através de cookies.
O dataset gerado apresenta as seguintes features:

| Atributo | Descrição |
| -- | -- |
| click | Marcador de click (1: para click, 0: não click)|
| visit | visita na página |
| group | Definição do grupo de usuários entre grupo de tratamento e controle |

## 2.1 Premissas adotadas
Para realização do projeto, foram utilizadas as seguintes premissas:
- A feature "visit" sempre tera o valor 1, considerando que o usuário entrou na página.
- O problema considera que a resposta deve ser a mais rápida possível, mas não foi simulado quantos usuários entream por dia, foi considerado cada entrada de usuário como um dia para o plot dos gráficos,
apenas para representar a passagem de tempo.
- Como foi imposto o fator limitante de tempo, teste estátisticos frequentista acaba sendo limitado, portando foi utilizado o Teste A/B Bayesiano, juntamente com o MAB, com intuito de controlar a amostragem das páginas.

# 3.0 Estratégia de Solução
Para a resolução do problema foi utilizado a metodologia CRISP-DM
<img width="1080" height="1080" alt="crisp" src="https://github.com/user-attachments/assets/72e39235-4d84-43ab-b277-40ebc605b021" />

## 3.1 Fases do CRIPS
1. Definição do Problema de Negócio: Identificar stakeholders e objetivos.
2. Compreensão do Negócio: Alinhar expectativas e prototipar soluções.
3. Coleta de Dados: Fazer a coleta de dados.
4. Limpeza de Dados: Tratar valores ausentes, outliers e inconsistências.
5. Análise Exploratória: Descobrir padrões e criar hipóteses.
6. Modelagem dos Dados: Aplicar transformações estatísticas.
7. Treinamento de Algoritmos: Avaliação de modelos.
8. Avaliação de Desempenho: Seleção do melhor modelo.
9. Deploy da Solução: Publicação do projeto.

## 3.2 Planejamento da solução:
### 3.2.1 Entendimento da diferença entre os tipos de teste de hipóteses
Esse passo foi criado para gerar o entedimento sobre o motivo de escolher o teste bayesiano ao invés do frequentista devido ao tipo de problema.

### 3.2.2 Design de Experimento
Passo utilizado para desenhar e planejar os códigos e como eles se interligam.

### 3.2.3 Criação das páginas sintéticas
Para aplicar o teste, foram criadas duas páginas que seriam avaliadas e utilizar um webscrapper para simular as interações dos usuários com a página

### 3.2.4 Aplicação e avaliação do Teste Bayesiano
Com os dados gerados a partir do scrapper foi aplicado o teste bayesiano para validar as hipoteses.

### 3.2.5 Aplicação do MAB
A metologia utilizada foi adaptada para aplicação do MAB, que após ser validado foi aplicado com a avaliação do teste bayesiano.

# 4.0 Frequetista x Bayesiano

O teste A/B geralmente é utilizado para comparar diferentes versões de um produto, site ou estratégia e determinar qual é o mais eficaz.
Sendo os modelos utilizados o **Frequentista** e o **Bayesiano**

O método frequentista baseia-se na teoria da frequência de eventos e usa métricas como p-value para determinar se há uma diferença estatísticamente significativa entre as versões testas.
Algumas características são:
- Requer uma tamanho de amostra pré definido.
- Não pode ser interrompido antes sem comprometer os resultados
- Baseia-se em testes tradicionais de hipóteses para determinar signicância estatística.

Já o método bayesiano utiliza probabilidade para atualizar estimativas com base em novos dados, permitindo uma análise mais flexível.
Algumas características são:
- Não exige um tamanho fixo de amostra
- Fornece uma probabilidade direta de uma variação ser melhor que a outra
- Permite uma abordagem mais adaptável e contínua na tomada de decisão

## 4.1 Frequentista
Desas forma, foi gerado um conjunto de dados com as quantidades de visitas e cliques em duas páginas e utilizado o Teste A/B com o intuito de descobrir qual página apresenta maior conversão
Os seguintes resultados foram obtidos:

<img width="1309" height="582" alt="image" src="https://github.com/user-attachments/assets/5bc481bd-d8aa-4213-9135-50fe6f7e5fae" />


Nos gráficos da esquerda é possível observar que desde os primeiros dias o CTR (Click-Through Rate) da página B é maior que o da página A.

Contudo, a diferença entre os CTR's das páginas não é muito alto, para validar se uma página era realmente melhor do que a outra foi utilizado um teste de hipóteses no qual 
podemos ver o resultado no gráfico da direta. Nos primeiros dias o p-valor é bem alto devido a quantidade de dados e também pela diferença pequena entre as conversões das páginas.
Até por volta dos dias 50-60 não era possível tirar uma conclusão, mesmo que o CTR da página B fosse maior que o da página A, não haviam amostras suficientes para provar que era estatísticamente significativo.

A partir do 60 o p-valor se estabelece como menor que 0.05, rejeitando a hipotese nula (que não há diferença entre as conversões da página A e B) e assim provando estatísticamente que a página B apresenta uma
maior conversão que a página A

## 4.2 Bayesiano
Para o teste baysiano foi gerado os seguintes gráficos:

<img width="1214" height="505" alt="image" src="https://github.com/user-attachments/assets/0c6d004b-be2f-4af6-bb15-ff79a9871104" />

Ao invés de utilizar o p-valor, é utilizado a probabilidade do CTR da página B ser maior que o CTR da página A e com o erro atrelado ao se fazer essa escolha.

Pelo gráfico da esqueda é possível observar que desde o inicio a probabilidade de B ser maior do que A é maior que a probabilidade de A ser maior que B.
Contudo a partir do dia 20 vemos que a probabilidade de B ser maior que A ultrapassar os 90%.
Ao mesmo tempo, através do gráfico da direita é possível ver o erro atrelado ao se fazer essa escolha. No dia 20 é possível perceber que o erro ao escolher B se estabiliza. 
O que não quer dizer que não há chances de A ser melhor que B, contudo seria muito difícil de acontecer. Assim, como a probabilidade de B ser maior que A passa de 90% e o erro atrelado ao fazer essa escolha é menor que o threshold definido, podemos escolher a página B como melhor que a A.

Importante dizer que isso não prova que a conversão de B é estatísticamente maior que a conversão da página A. Entretanto, os dados mostram que a chance dessa premissa ser verdadeira é muito alta.
Logo com o método Baysiano a decisão foi tomada no dia 20, cerca de 38 dias a menos que o método frequentista. Reduzindo o periodo de teste da empresa e otimizando os ganhos.

# 5.0 Multi-Amerd-Badit (MAB)
O Multi-Armed Bandit (MAB) é uma abordagem de experimentação que equilibra exploração (testar diferentes opções) e exploitation (aproveitar a melhor opção conhecida). Diferente do teste A/B tradicional, onde o tráfego é fixo entre variantes, o MAB ajusta dinamicamente a alocação com base no desempenho de cada opção.

No Teste A/B Bayesiano, utilizamos distribuições probabilísticas (como a distribuição Beta) para modelar a incerteza sobre cada variante. Ao combinar isso com MAB, podemos atualizar as probabilidades conforme novos dados chegam, permitindo que a melhor alternativa receba mais tráfego progressivamente.

## 5.1 Planejamento do teste

O seguinte planejamento foi feito:

<img width="1211" height="790" alt="image" src="https://github.com/user-attachments/assets/1e996554-4c4d-4765-a27e-a2b3ca3767ce" />

Nesse teste foi utilizado o MAB como uma forma de "política" para escolher qual página será exibida para o visitante, o papel dessa política é identificar qual página tem a probabilidade de ser melhor que 
a outra utilizando os dados atuais e com isso otimizar a amostragem da página, mostrando cada vez mais a página com a maior conversão. Essa política ainda mostra a página com a probabilidade menor (apesar de 
ser em um frequencia mais baixa) e continua coletando dados para realizar os cálculos, até o momento que uma página tenha amostras suficientes para mostrar que é melhor que a concorrente.

# 6.0 Resultados
Através dos testes realizados foram obtidos os seguintes gráficos:
<img width="989" height="490" alt="image" src="https://github.com/user-attachments/assets/fd2b46a0-7c83-4422-b4ff-cacb73786351" />


<img width="868" height="480" alt="Figure_1" src="https://github.com/user-attachments/assets/f271a2fe-2e56-4307-a909-d1546a429dc0" />

Com as taxas de cliques aplicadas era esperado que com a utilização do MAB a página de tratamento fosse exibida mais vezes que a página de controle, através do primeiro gráfico podemos observar esse comportamento,
no qual a partir do dia 50 a página B foi mostrada mais frequentemente que a página A.

No segundo gráfico vemos que a probabilidade da página de tratamento ser melhor que a página de controle passou de 90% próximo à 150 interações, mais do que no teste Baysiano anterior. Contudo, no teste anterior
seriam necessárias várias interações para tomar a decisão, enquanto que com o utilização do MAB e a otimização automática da amostragem das páginas, a pior página foi exibida menos vezes aos clientes.

Portanto, esse projeto mostra como a utilização do MAB com o teste AB bayesiano pode otimizar não apenas a tomada de decisão de sair da fase de exploração para tomar a decisão de qual página é melhor,
mas de fazer essa mudança na amostragem de forma gradual e coerente com os resultados encontrados.

# 7.0 Resultado de Negócios
A página que apresenta a maior conversão é a página de tratamento. Contudo, essa tomada de decisão foi feita de forma mais rápida do que seria em um Teste AB Frequentista, 
devido a utilização do Teste AB Bayesiano, onde foi visto que a probabiliade da página de tratamento ser melhor que a página atual foi maior desde o começo.
Assim, a decisão pôde ser tomada de forma rápida com a ideia de otimizar o ganho através das páginas.

Além disso, utilizando o MAB foi possível fazer ainda melhor. Com o Multi-Armed Bandit com a política do Thompson Agent foi possível aplicar a lógica do Teste AB Bayesiano
no próprio sistema de amostragem das páginas, fazendo com que a página com melhor conversão fosse mostrada mais vezes desde o início, otimizando o ganho da página mesmo antes de tomar
a decisão de qual página é melhor.

# 8.0 Conclusão
Nesse projeto, foram realizadas todas as etapas necessárias para a implementação de um projeto completo de Data Science focado na utilização do Teste A/B. Foi utilizado o método de gerenciamento de projeto chamado CRISP
e obteve-se um desempenho satisfatório em compreender a utilização do Teste A/B Bayesiano juntamente com MAB e aplicar em um problema real.

# 9.0 Aprendizados e Trabalhos Futuros

- Aprendizados

  - Compreender e aplicar Teste A/B Bayesiano.
  - Compreender e aplicar do MAB e seus agentes.
  - Compreender e aplicar de webscrapping.

- Trabalhos Futuros

  - Coletar datasets de Test A/B e aplicar ambos os testes para provar suas diferenças em outros tipos de negócio.








