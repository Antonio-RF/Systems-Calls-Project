# Anotações do Artigo Científico "A Sense of Self for Unix Processes":

## Introduction:

O projeto tem como objetivo criar métodos de segurança computacional baseados em sistemas imunes naturais e em como eles conseguem
distinguir eles de outros sistemas. 

- Importante pré requesito para um sistema é sobre: CONHECER ELE MESMO (como o próprio título do artigo já diz).

É possível ver ao longo do artigo científico que esses sistemas imunes naturais ajudaram a criar métodos como melhorar a tradicional
criptografia entre outros.

***"Related Work":*** Nessa parte do artigo, são estudados diferentes tipos de sistemas imunes naturais e o foco dessa parte são suas
funções secundárias, como os mecanismos inflamatórios desses sistemas (pensando em sistemas imunes naturais).

### Atenção: 
- O primeiro problema identificado nesse detector de vírus computacional é exatamente sobre conhecer sobre o sistema (Self), pois no meio computacional
as coisas mudam muito mais que no sistema imune natural, como foi o exemplo do artigo em relação a um usuário baixar outros apps, editar
arquivos, entre outros. Afinal, os usuários e as máquinas computacionais são usualmente adicionados às redes computacionais.
- O segundo problema identificado é o sistema entender bem o bastante de si mesmo a ponto de identificar acessos de fora do sistema (indevidos).

Termina-se a introdução falando de que o artigo em específico é importante para mostrar que muitos métodos da segurança computacional, como os de
identificar algum invasor na rede, são muito complexos e complicados, o que podem ser feitos de formas mais simples e, assim, prevenir de algumas 
invasões parciais de intrusos de formas mais tranquilas.

## Related Word:

### Essa parte começa falando sobre os 2 tipos diferentes de identificar invasores:

***Detecção indevida de invasores:*** Conhece-se a assinatura dos invasores e elas são usadas para identificá-los.

***Detecção de invasão por anomalia:*** Basicamente consiste em comportamentos fora do normal de sistemas, que são tratados então como
invasores.

Nesse artigo científico, será estudado apenas a ***detecção de invasão por anomalia***.

Não que um usuário não possa mudar de preferencias, mas essa mudança ocorre de forma devagar, e quando acontece de forma instantânea é identificada
como a ação de um invasor naquele sistema, e será esse o foco do estudo em si.

Encerra-se essa parte do artigo científico falando um pouco sobre as referências [9, 14], as quais fazem uma construção de perfis de usuários
baseando-se em determinar comportamentos normais, como se fossem as raízes. 

A proposta para determinar intrusos que esse artigo científico traz é muito parecida com a dessa referência anteriormente mencionada, porém com a diferença de que a representação do comportamento normal é feita de forma mais simples. Os cientistas da Universidade do México confiam em exemplos de execuções de programas normais em vez de uma especificação formal do comportamento esperado de um programa, e eles ignoram os parâmetros. A vantagem de se fazer isso é não precisar determinar uma especificação de um comportamento vindo do código do programa, eles simplesmente conseguem acumular essas especificações de comportamento traçando as execuções normais do programa.

## Defining Self:

Danos aos sistemas são causados pela execução de programas que chamam o sistema. Então, os cientistas desse artigo científico se restringem a focar nessas chamadas ao sistema quando os programas são executados, porém olhando somente para os "processos privilegiados"(as raízes). Esses processos são
mais importantes pois cuidam de mais funções no sistema, e o comportamento deles é mais limitado e pouco flexível. 

***limitações:*** Existem algumas limitações, e uma delas é identificar um intruso se mascarando de outro usuário, o qual conseguiu a senha daquele sistema de uma forma legal.

Como já dito anteriormente, o comportamento normal dos sistemas é observado através dos chamamentos ao sistema que aquela máquina faz, considerando-se
um comportamento fora do comum quando acontece um grande número de chamados e um comportamento mais normal quando acontece poucos chamados ao sistema,
com sequências de tamanho 5,6 e 11. 

A ideia principal é construir um banco de dados dos comportamentos normais para cada área interessada do sistema, estruturas essas que serão construídas e terão sua própria arquitetura, versão de software e configuração. No final, a ideia é juntar todos esses bancos de dados e construir com isso, as 
características únicas que fazem aquele sistema ser ele mesmo (self). 

No final, fala-se sobre como esse tipo de definição de comportamento normal ignora alguns aspectos do processo de comportamento, como os parâmetros 
passados para os chamados de sistemas. 

### A filosofia principal desse programa é vermos quão perto conseguimos chegar nas mesmas presunções que grandes análises fazem com apenas suposições simples!

## Details:

### Existem dois estágios para identificar intrusos:

***Primeiro estágio:*** Identificar traços de comportamentos normais e construir um banco de dados com eles (observando os chamados aos sistemas).

***Segundo estágio:*** Identificar traços que podem conter comportamento anormal, olhando para as assinaturas que não estão presentes no banco de 
dados anteriormente construído.

O banco de dados é construído segundo um número de janelas pré definido chamado de "K". Após esse número ser definido, faz-se uma tabela para ver
quais são os k chamados após um certo chamado. Por exemplo, se K=3 e temos um chamado "open", temos que ver quais são os 3 chamados após "open".

Eles calcularam que na construção do segundo estágio, o maior número de discrepâncias que poderiam ser encontradas seria ***R = k (L , (k + 1)=2)***,
com k sendo o número de janelas anteriormente mencionadas e L o tamanho da sequência. Ademais, o custo desse algoritmo é O(N), com N sendo o tamanho
dos traços, em relação aos chamados aos sistemas. 

## Experiments:

Para responder diversas dúvidas em relação ao comportamento normal de um certo sistema, os cientistas da universidade do México decidiram trabalhar com 
o chamado ao sistema "sendmail", o qual segundo eles é um programa variável e complexo que pode ser usado para esse fim, existindo ainda por cima diversos
ataques documentados que podem servir para testes.

Eles acreditam que se tiverem sucesso com o "sendmail", terão sucesso com qualquer outro procecsso privilegiado do Unix.

## Building a normal database:

Começa-se fazendo uma pergunta importante: Nós devemos identificar o comportamento normal do sendmail através de testes como mensagens artificiais 
ou observar um usuário real e torcer para que ele consiga cobrir todos os spectros do comportamento normal ?

Os cientistas optaram por escolher mandar 112 mensagens construidas artificilmente, a fim de cobrir todas as variâncias, pois se não cobrissem poderia
falhar em detectar invasores.

Depois do banco de dados ser feito através dessas 1.5 milhões de chamadas ao sistema, o próximo passo é como descobrir se os próximos comportamentos
são normais ou anormais. Basicamente, o jeito mais fácil e óbvio seria contar quantas anomalias apareceram e qual a porcentagem delas no total de 
comportamentos analisados. Esses dados em um mundo ideal deveriam ser 0 para comportamentos normais, porém em um mundo real deveria-se colocar um
número limite de anomalias encontradas permitidas em um comportamento normal. Por fim, como os cientistas desse estudo não estão atrás de achar uma
reposta específica nem algo binário, eles decidiram simplesmente reportar os números.

Nessa parte do artigo volta-se a uma antiga pergunta: e o tamanho do banco de dados ?. Isso é interessante por 2 razões:

***Primeira razão:***  O tamanho do banco de dados não pode ser nem muito pequeno, por causa que não seria preciso pelas poucas informações, e nem
muito grande, pois custaria muito para o programa funcionar online.

***Segunda razão:*** O tamanho do banco de dados pode nos fornecer uma estimativa de quanto é a variância no comportamento normal do sendmail.

### Foram usadas os seguintes procedimentos para se criar um banco de dados do comportamento normal do sendmail:

- 1. Enumerar diferentes variâncias de entradas em operações do sendmail.
- 2. Gerar exemplos de mensagens para que o sendmail exiba essa variância.
- 3. Construir um banco de dados com as sequencias conseguidas no procedimento 2.
- 4. Continuar gerando mensagens normais, vendo quando são anomalias e as registrando como tais no banco de dados do comportamento normal.

Os cientistas criaram 3 bancos de dados com tamanho 5, 6 e 11 de janelas, os quais foram feitos com diversos tipos de variações, em busca do maior
número possível de comportamentos normais para os bancos de dados. No final, o resultado esperado chegou e os 3 bancos de dados reconheceram 0 anomalias
em suas análises. 

## Distinguishing Between Processes:

Os cientistas estudam sobre a distinção desse processo (sendmail) em relação aos outros. Segundo a tabela levantada por eles, há uma grande distinção
(cerca de 5-32% para sequências de tamanho de janela 6) entre o sendmail e outros tipos de processos. Portanto, descobre-se como é fácil
distinguir os comportamentos desses difentes processos, usando somente as sequências de informações obtidas. 

## Anomalous Behavior:

### Os cientistas geraram 3 traços que diferem de comportamentos normais do sendmail:
- 1. Traços de intrusões bem sucedidas no sendmail.
- 2. Traços de tentativas de intrusão no sendmail que falharam.
- 3. Traços de condições de erro.

Em cada um dos casos eles testaram com o banco de dados de comportamento normal do sendmail, e também testaram com traços de intrusões bem sucedidas
no "lpr". Eles executaram e traçaram 4 tipos de ataques diferentes. 

Depois da análise da tabela 3 contendo as porcentagens e a quantidade de anomalias detectadas nesses ataques, é possível se referir que o banco de dados
do comportamento normal do sendmail conseguiu funcionar corretamente e identificar os invasores, mesmo com o decode tendo uma taxa muito pequena de 0.3%.

Uma segunda e terceira onda de ataques são feitas com outros diferentes mecanismos, como dispositivos de script remotos, os quais o banco de dados
identifica atividade anormal também, mesmo que com um índice baixo (0.4-2.7%).

## Discussion:

Começa-se essa parte do artigo falando de como esse experimento serviu para mostrar que pode sim mostrar algumas atividades de intrusos com um algoritmo
fácil de se fazer e relativamente modesto em questão de armazenamento. Ademais, sugere-se até que esse algoritmo seja implementado em sistemas onlines.

Os cientistas deixam claro que os experimentos feitos nessa pesquisa são preliminares e que para obter melhorias de formas para encontrar intrusos
por esse método é preciso mais pesquisa e testes.

Eles também enfatizam a importãncia dos chamados aos sistemas (system calls) que ajudam o projeto a funcionar, tendo como duas propriedades importantes do programa envolvendo esses chamados. Porém, eles deixam claro também que se um invasor usar outros métodos que não estão relacionados com essas 2 propriedades importantes, o sistema pode sim ser invadido.

Termina-se essa discussão falando sobre o longo caminho que é até atingir de fato as características de um sistema imune natural. Correlacionando muitas coisas que faltaram no projeto com o sistema imune natural, os cientistas acabam por concluir também que essas linhas de um sistema sabendo definir si mesmo poderão ser usadas para futuros projetos.  

## Conclusions:

Os cientistas concluem o artigo dizendo novamente que esse é um projeto preliminar e deixando claro que existem outros tipos de ataques que o método deles não consegue detectar. Porém, é eficiente monitorar pequenas sequências de System Calls e essa técnica pode sim ser usada em um ***sistema imune computacional online*** somente como uma das diversas formas de se identificar anomalias.





























