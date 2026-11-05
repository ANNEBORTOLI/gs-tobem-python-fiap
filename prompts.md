# 🤖 Prompts usados com IA · Python

**Projeto:** TôBem · FIAP Global Solution 2026.2 · CitizenTech
**Integrantes:** Gabriel Almeida (RM 575525) e Anne Bortoli (RM 574750)
**Ferramenta:** Claude (Anthropic)

## 📝 Como usamos a IA

Usamos o Claude como apoio para planejar o programa, propor o código por etapas, explicar cada parte e sugerir testes. Definimos três regras de trabalho logo no início:

1. **Código incremental:** a IA passava um passo por vez, e nós digitávamos, testávamos e fazíamos o commit antes de pedir o próximo.
2. **Só o que vimos em aula:** listas, `if/elif/else`, `for`, `while` e funções.
3. **Um teste para cada função:** toda função nova veio acompanhada de um teste.

Abaixo estão os principais prompts, o que a IA respondeu e o que nós decidimos.

---

## 1. 🧭 Planejamento

**Prompt:**

> Agora vamos fazer o desafio da disciplina de Computational Thinking with Python. Antes de executar qualquer código, quero que você me passe o código de forma incremental para que eu possa ir fazendo os commits no repositório do GitHub. Primeiro vamos discutir o que será feito com base nos entregáveis da matéria.

**Resposta da IA:** relacionou cada critério de avaliação a uma parte do programa, propôs o menu, os registros simulados e uma sequência de commits. Perguntou quais recursos de Python já tínhamos visto.

**Nossa decisão:** respondemos que só tínhamos visto funções. A IA adaptou o plano.

## 2. 🗂️ Organização do menu

**Prompt:**

> Como sugestão de desenvolvimento incremental, acredito que podemos montar a lógica do menu no main e seguir a partir desse ponto, fica mais organizado e fácil de entender. O que acha?

**Prompt seguinte:**

> Já podemos colocar essa lógica dentro da função main e chamá-la ao rodar. Concorda?

**Resposta da IA:** concordou e reorganizou a sequência de passos, com o menu primeiro e as opções preenchidas depois. Explicou por que `main()` precisa ficar no final do arquivo.

**Nossa decisão:** a ideia de montar o menu antes das funções foi nossa. Assim, o programa já funcionava do início ao fim desde o segundo commit.

## 3. ✅ Onde fica o check-in

**Prompt:**

> Onde fica a lógica do check-in do idoso?

**Resposta da IA:** explicou que, no Python, o check-in aparece como dado (horas desde o último check-in), e que a ação de apertar o botão fica no dispositivo e na página. Sugeriu uma opção "Fazer check-in agora" no menu.

**Nossa decisão:** incluímos a opção, para que a jornada do idoso aparecesse no programa.

## 4. 🚦 Classificação e testes

**Prompt:**

> Ao terminar de implementar uma função, sempre sugira um teste.

**Resposta da IA:** criou `testar_classificar()`, com um caso para cada um dos 9 estados, casos de fronteira (como 28 °C e 85 % exatos) e um caso de prioridade. Depois fez o mesmo para o resumo e para a entrada de números.

**Nossa decisão:** passamos a exigir um teste em cada passo. Os 14 casos da classificação também vão servir para conferir a versão em JavaScript no Web Development.

## 5. 📊 Resumo do dia

**Prompt:**

> Por que você não usou max()?

**Resposta da IA:** explicou que o `max()` não devolve a hora do pico e que, com registros em lista, precisaria de `lambda`, que ainda não vimos. Mostrou também uma versão simples com `max()` e `index()`.

**Nossa decisão:** mantivemos o laço, que guarda a hora do pico e mostra o raciocínio de forma explícita.

## 6. 💾 Guardar o check-in

**Prompt:**

> Quando fazemos o check-in, os dados passados do dia não são guardados em lugar nenhum. Queresmo que durante a execução as entradas do usuário sejam guardadas com append(). Verifique as alterações que fizemos no código abaixo e sugira as alterações que achar pertinente.

**Resposta da IA:** confirmou que não, e que a própria lista só existe enquanto o programa está aberto. Apresentou duas opções: guardar na lista durante a execução ou gravar em arquivo.

**Nossa decisão:** escolhemos guardar na lista com `append()`. Gravar em arquivo ficou como melhoria futura no README.

## 7. 🕐 Formato da hora

**Prompt:**

> E se a pessoa digitar 10:30, por exemplo? O programa não quebra, mas fica estranho.

**Resposta da IA:** explicou que o programa não quebra, mas mostra uma mensagem confusa. Propôs uma função com `split(":")` para aceitar o formato 10:30.

**Nossa decisão:** não adotamos essa versão, porque acrescentava ainda mais complexidade que nesse primeiro momento não queremos. Mantivemos a hora como número de 0 a 24 e registramos a limitação no README.

## 8. 📄 README

**Prompt:**

> Agora podemos ir para o README. Gostaria que você deixasse o README bem bonito, utilizando emojis nas seções.

## **Nossa decisão:** adotamos a estrutura apresentada e fizemos algums alterações como criar a pasta /assets para adicionar as imagens do programa em execução.

## 🔗 Antes do código: regras compartilhadas com o Edge

Antes do Python, usamos a IA para alinhar as regras com o dispositivo do Edge Computing:

- **Limites:** definimos os limites de temperatura, umidade e check-in. A IA apontou que o PERIGO de check-in em 24 h repetia o caso real que queríamos evitar, e ajustamos para 13 h.
- **Umidade alta:** perguntamos sobre as implicações da umidade alta para idosos. Decidimos tratar umidade alta junto com calor como PERIGO. Afinal, o risco que queremos evitar é o imediato, ou seja, idoso não ficar sem socorro por muito tempo quando estiver passando mal.
- **Código do Edge:** perguntamos se seria complexo mudar o código do Arduino. A IA mostrou o bloco `else if` necessário, e nós aplicamos a mudança no C++ e testamos no Wokwi.

Por isso o Python usa os mesmos nomes de constantes, os mesmos limites, a mesma ordem de decisão e as mesmas mensagens do LCD.
