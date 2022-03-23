# Todos-Ps-Cross

 Documentação dos Programas do Ps 

 

Muito Fácil - 1 - Ângulo em radianos: 

Inicialmente, no programa se é puxado a biblioteca “math” para utilizar o número pi. Antes de chamar a função, o x é o input da entrada, na qual é pedido ao usuário que ele digite um ângulo em radianos, depois é chamada a função “function”, tendo como 	parâmetro “num” que tem o valor de “x”, fornecido pelo usuário anteriormente. Na função function se é feito os cálculos para 	transformar o ângulo em radianos para graus, utilizando a 	equação y = 180/pi. Tendo o valor do ângulo em graus sendo 	salvo em y, se tem o “return” com o ângulo em radianos no fim da execução da função. O while é para deixar o programa rodando em repetição. 

 

Muito Fácil - 2 – Horas, meses, semanas...: 

Na entrada do programa se é pedido ao usuário que ele digite um valor de horas, esse valor é salvo em “horas” e logo em seguida utilizado como parâmetro (“hr”) na função “function” que é puxada logo após. Em function, se é declarado uma lista (“list”) que salvará os valores encontrados. Logo, temos o “m”, onde se é salvo o valor de meses e em seguida é salvo na “list”, o “s” que é salvo o valor de semanas e é salvo na “list”, o “mi” que é salvo o valor em minutos e em seguida salvo em “list”, o “seg” que é salvo o valor em segundos e em seguida salvo em “list”, o “mil” que é salvo o valor em milissegundos e em seguida salvo em “list”. Ao final do processo, se tem o return da função que retorna os números que estão em “list”.  

 

Fácil - 1 - Repetição de item: 

Na entrada se é pedido ao usuário, primeiramente, para que ele digite uma string (a palavra que será repetida), que é salvo em “item” e depois um número (número de repetições da palavra) que é salvo em “n”. Depois “item” e “n” são utilizados como parâmetros para a função “function” que por meio de um “for” salva a palavra repetida no número de vezes desejado, dentro de uma lista (“list”). E por fim se tem o retorno da função que retornará a “list” já com o “item” repetido “n” vezes. 

 

Fácil - 2 - Binário: 

Na entrada se é pedido um número ao usuário que é salvo em “x”. Em seguida o “x” é utilizado como parâmetro para a função “function” que é puxada. Em function, o x é transformado em binário pela variável “y” (y=bin(x)) e se é dado início ao contador “cont”, então por meio de um “for” cada caractere de y é analisado ao transforma– lo em um string (“str(y)”), assim para cada 1 que aparece em “y”, se é somado mais um ao valor de “cont”. Por fim a função da retorno ao número inicial,” x”, ao cont (que é o número de “1” no binário) e ao “y” (que é “x” representado em binário). 

Os números binários representados em python, fornecidos por “bin” se iniciam com “0b” e em seguida se tem o número em binário. 

 

Médio - 1 - Distância entre dois pontos: 

Inicialmente se é puxado a biblioteca “math” para se realizar as operações matemáticas necessárias. 

Na entrada o usuário fornece as coordenadas x e y do primeiro ponto (“x”, “y”) e em seguida as coordenadas do segundo ponto (“x1”, y1”), os quatro pontos são usados como parâmetros para a função “function”, a qual calcula a distância entre os dois pontos na variável “d”. Por fim a função retorna os pontos calculados e a distância entre eles (“d”). 

 

Médio - 2 – CrossBots:  

Na entrada o usuário fornece um número salvo em “num” que eu usado como parâmetro para a função “function”, após recebido o valor fornecido, ele é analisado na função por meio de “if’s”. Então, se o valor for divisível por 3 e não for divisível por 5, a função retorna “Cross”, se o valor for divisível por 5 e não for divisível por 3, a função retorna “Bots”, se o valor for divisível tanto por 3, quanto por 5, a função retorna “CrossBots” e se o valor não for divisível nem por 3 e nem por 5, a função retorna o próprio valor fornecido pelo usuário. 

O “while” é para deixar o programa rodando em repetição. 

 

Médio - 3 – Sumo: 

 Inicialmente o estado do robo é definido como 'straight', na qual o robo anda reto, mas com um "if" foi definido que se ele nâo encontrar algo com algum dos sensores, tanto o direito quanto o esquerdo na distância entre 0 e 300cm, o seu estatdo fica em "turning", até que algum de seus sensores encontre algo, apartir dai, se o sensor direito ou o esquerdo receber um valor <300, o estado do robo muda pra "straight" indo na direção que ele encontrou o outro robo do "ringue" para retirá- lo do circulo. Caso o sensor direito e o esquerdo fiquem com valores distintos por muito tempo, pode indicar que o robo travo em algo como no outro robo, logo o valor da diferença de distancia dos dois sensores é salva em "z" e o contador "cont" (definido como "cont=120" no inicio do programa) determina um tepo maximo, que se após o cont zerar e z nao tiver mudado o robo entra no state 'stop', caso haja mudança no valor de z, o que pode indicar que ele "destravou" o estado retorna a "straight". Para o robo não sair do campo, se o sensor (front_lest ou front_right) retornarem um valor > 0.35, indica que ele está no limite do circulo, com isso o robo entra em estado "turning" e o tanto que o robo irá virar é definido com a variável "aux" que a partir da biblioteca "rndom", retorna um valor aleatório entre 5 e 14, com isso o "aux" como a diminuir 1 de seu valor e enquanto o "aux for diferente de zero, o robo continua em estado de virando ("turning"), caso contrário, o robo fica em estado "straight". 

 

Difícil - 3 – Pi: 

O programa é baseado em uma teoria de que em um círculo inscrito em um quadrado, temos a relação de a Área do círculo dividida pela Area do quadrado é igual ao número de pontos que cabem dentro do círculo dividido pelo número de pontos que cabem dentro do quadrado, resultando na fórmula de pi = 4*cont (pontos no círculo) / n (pontos no quadrado). Assim, na lógica do programa pegamos um círculo de diâmetro 1, inscrito em um quadrado de raio 1, assim ao pegarmos números aleatórios entre 0 e 1 para “x” e “y”, verificamos se eles são pontos dentro do círculo aplicando (x*x + y*y) < 1, se for verdade, esse ponto está dentro do círculo e o contador soma um. O n é o número total de pontos analisados e o número de pontos dentro do quadrado, uma vez que ao delimitarmos o de valor de o a 1, limitando para a área de dentro do quadrado. Como cabem infinitos pontos no círculo e no quadrado, quanto maior for “n”, obteremos um pi cada vez mais preciso. 

Nesse programa se é puxado a biblioteca “random” de python. 

Se é puxado a função “function”, que tem parâmetro “n”, que fornece quantas vezes a operação irá acontecer. Na função se é iniciado um contador “cont”, logo em seguida se tem um “for” que vai fazer o loop “n” vezes. No “for” as variáveis “x” e “y” vão receber números aleatórios de entre 0 e 1, utilizando –se de “random.uniform”, por “n” vezes. A cada valor recebido de “x” e “y”, esses valores são passados em um “if”, onde se (x*x +y*y) for menor que 1, será adicionado mais um ao contador. Depois na função, o valor de pi será calculado por 4 vezes cont, dividido por n, e a função retornará o valor de “pi”. 
