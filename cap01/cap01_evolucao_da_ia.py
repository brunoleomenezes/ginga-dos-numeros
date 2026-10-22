# -*- coding: utf-8 -*-
"""
A ginga dos números: livro de exercícios
Lista de Exercícios do Capítulo 1

Versão em script do caderno cap01_evolucao_da_ia.ipynb, com o mesmo código e os mesmos comentários.
Autor: Bruno Menezes  |  https://brunoleomenezes.github.io/
Repositório: https://github.com/brunoleomenezes/ginga-dos-numeros

Como usar: o mais simples é abrir o caderno .ipynb no Google Colab. Este arquivo serve para quem
prefere rodar no próprio computador (python cap01_evolucao_da_ia.py) ou ler o código em um editor. Os blocos
marcados com "# %%" são as células do caderno, na mesma ordem; os textos explicativos aparecem
como comentários. Para ver o resultado de cada bloco, rode o arquivo inteiro: os gráficos abrem
em janelas próprias.
"""



# %% [markdown]
# > *Oito exemplos numéricos do capítulo, agora executados por você em Python. Esta é também a sua
# primeira aula de programação, e ela não exige nenhum conhecimento anterior.*


# %% [markdown]
# ---
#
# ## Como usar esta lista


# %% [markdown]
# Você não precisa saber programar para começar. Não precisa instalar nada no computador, não
# precisa comprar nada e não precisa de cartão de crédito. Tudo acontece dentro do navegador,
# usando a sua conta Google da escola.


# %% [markdown]
# A lista está dividida em quatro partes. A Parte 0 prepara o ambiente. A Parte 1 ensina o mínimo
# de Python necessário, em nove células curtas. A Parte 2 traz os oito exercícios propriamente
# ditos, um para cada exemplo numérico do capítulo. A Parte 3 tem três desafios para quem terminar
# antes.


# %% [markdown]
# **Três combinados importantes**


# %% [markdown]
# 1. **Digite o código, não copie.** Digitar é o que ensina. Quem copia e cola termina mais rápido
# e aprende menos. Errar ao digitar faz parte, e o Anexo A explica como resolver os erros mais
# comuns.
# 2. **Execute uma célula de cada vez, na ordem.** Várias células dependem do resultado das
# anteriores. Pular uma célula é a causa mais frequente de erro nesta lista.
# 3. **Compare sempre com a saída esperada.** Cada código traz a resposta que ele deve produzir.
# Se a sua saída for diferente, existe algo errado no que foi digitado.


# %% [markdown]
# Ao final, você terá reproduzido em código, com suas próprias mãos, oitenta anos de história da
# Inteligência Artificial: do neurônio de 1943 ao mecanismo de atenção de 2017.


# %% [markdown]
# ---
#
# ## Parte 0. Preparando o Google Colab


# %% [markdown]
# O Google Colab é um caderno de programação que funciona no navegador. Ele já vem com o Python
# instalado e com tudo o que vamos usar. Siga os cinco passos abaixo uma única vez, no início da
# aula.


# %% [markdown]
# **Passo 1. Entre na sua conta Google da escola**
#
# Abra o navegador e confirme que está conectado com a conta institucional. Se houver mais de uma
# conta conectada, use o seletor no canto superior direito para escolher a da escola. Isso garante
# que o seu trabalho fique salvo no lugar certo.


# %% [markdown]
# **Passo 2. Acesse o endereço do Colab**
#
# Digite na barra de endereços: colab.research.google.com e pressione Enter. Não é preciso
# instalar nem baixar nada.


# %% [markdown]
# **Passo 3. Crie um caderno novo**
#
# Na janela que aparece, clique em Novo notebook, no canto inferior direito. Se a janela não
# aparecer, use o menu Arquivo e depois Novo notebook. Um caderno em branco será aberto, com uma
# única célula vazia.


# %% [markdown]
# **Passo 4. Dê um nome ao caderno**
#
# No alto da tela está escrito algo como Untitled0.ipynb. Clique nesse nome e troque por: Lista 1
# seguido do seu nome. Exemplo: Lista 1 Maria Silva. O caderno é salvo sozinho no seu Google
# Drive, na pasta Colab Notebooks.


# %% [markdown]
# **Passo 5. Aprenda o gesto mais importante**
#
# Clique dentro da célula, digite o código e pressione as teclas Shift e Enter ao mesmo tempo.
# Isso executa a célula e cria uma nova logo abaixo. Você também pode clicar no botão de play que
# aparece à esquerda da célula. Este gesto será repetido dezenas de vezes hoje.


# %% [markdown]
# > **Se aparecer a mensagem de conexão**
# >
# > Na primeira execução o Colab precisa reservar uma máquina para você, o que leva alguns
# segundos. Um círculo fica girando no canto superior direito. Espere ele parar. Isso acontece
# apenas uma vez por sessão.


# %% [markdown]
# ### Como esta lista mostra os códigos


# %% [markdown]
# Ao longo da lista, você vai encontrar sempre a mesma sequência de três elementos. Primeiro o
# código que deve ser digitado em uma célula. Depois a saída esperada, que é exatamente o que deve
# aparecer na sua tela. Por fim, um bloco chamado Sua vez, com modificações que você mesmo deve
# fazer no código.


# %% [markdown]
# ---
#
# ## Parte 1. Aquecimento: nove células para quem nunca programou


# %% [markdown]
# As nove células desta parte ensinam tudo o que é necessário para os oito exercícios seguintes.
# Nada além disso será cobrado. Digite cada uma em uma célula separada e execute com Shift e Enter
# antes de passar para a próxima.


# %% [markdown]
# ### A1. Mandar o computador escrever algo (*aquecimento*)


# %% [markdown]
# O comando **print** mostra na tela aquilo que estiver entre parênteses. Textos vão sempre entre
# aspas.


# %%
# Tudo que começa com # é um comentário.
# O Python ignora comentários: eles existem só para explicar o código a quem lê.

# print é uma função (um comando pronto do Python) que mostra na tela o que está entre
# parênteses. O texto vai entre aspas: em programação, texto entre aspas se chama "string".
print("Ola! Este e o meu primeiro codigo em Python.")
# Um segundo print escreve em uma nova linha. O Python executa as linhas de cima para baixo.
print("Estou no curso de Inteligencia Artificial Aplicada.")


# %% [markdown]
# **Sua vez**
#
# 1. Troque a segunda frase pelo seu nome completo e execute de novo.
# 2. Acrescente uma terceira linha com print e escreva a data de hoje.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### A2. Fazer contas (*aquecimento*)


# %% [markdown]
# O Python é uma calculadora. Repare que o separador decimal é o ponto, e não a vírgula. Isso vale
# para todos os números desta lista.


# %%
# Soma: o Python faz a conta primeiro e o print mostra o resultado (8).
print(3 + 5)
# Subtração: o sinal de menos funciona como na calculadora.
print(10 - 4)
# Multiplicação: no Python o sinal de vezes é o asterisco *.
print(6 * 7)
# Divisão: a barra / divide. O resultado sai com ponto decimal (2.5), não com vírgula.
print(10 / 4)
# Potência: dois asteriscos ** elevam à potência. Aqui é 2 elevado a 10 (1024).
print(2 ** 10)


# %% [markdown]
# O sinal ***** multiplica, a barra **/** divide e os dois asteriscos ****** elevam a uma
# potência. A última linha calculou 2 elevado a 10.


# %% [markdown]
# **Sua vez**
#
# 1. Calcule quanto é 2 elevado a 64, que é o número de grãos da lenda do tabuleiro de xadrez.
# 2. Descubra o que acontece se você digitar 10 / 0 e leia a mensagem de erro.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### A3. Guardar valores em variáveis (*aquecimento*)


# %% [markdown]
# Uma variável é um nome que guarda um valor. O sinal de igual não significa igualdade matemática:
# ele significa guarde este valor neste nome.


# %%
# Variável: um nome que guarda um valor. O sinal = significa "guarde 1 no nome peso1".
peso1 = 1
# Outra variável, com o peso da segunda entrada do neurônio.
peso2 = 1
# O limiar é o valor mínimo que a soma precisa atingir para o neurônio disparar.
limiar = 2

# O Python lê os valores guardados em peso1 e peso2, soma e guarda o resultado em soma.
soma = peso1 + peso2
# O print pode misturar texto e variável, separados por vírgula; ele põe um espaço entre eles.
print("A soma dos pesos e:", soma)
# Mostra o limiar do mesmo jeito: primeiro o texto, depois o valor guardado na variável.
print("O limiar e:", limiar)


# %% [markdown]
# Repare que dentro do print podemos misturar um texto entre aspas e uma variável, separando os
# dois por vírgula.


# %% [markdown]
# **Sua vez**
#
# 1. Troque peso1 para 3 e execute de novo. O que muda na soma?
# 2. Crie uma variável chamada seu_nome guardando o seu nome entre aspas e mostre com print.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### A4. Tomar decisões com if e else (*aquecimento*)


# %% [markdown]
# O comando **if** significa se. O **else** significa senão. Este é o comando que faz um neurônio
# artificial decidir se dispara ou não.


# %%
# Guarda a soma que chegou ao neurônio.
soma = 2
# Guarda o limiar, o valor mínimo para o neurônio disparar.
limiar = 2

# if significa "se". O sinal >= quer dizer "maior ou igual".
# Os dois pontos no fim da linha são obrigatórios.
if soma >= limiar:
    # Esta linha tem 4 espaços de recuo: ela só roda quando a condição do if for verdadeira.
    print("O neuronio disparou. Saida = 1")
# else significa "senão": o bloco abaixo roda quando a condição do if for falsa.
else:
    # Também recuada com 4 espaços, pois pertence ao else.
    print("O neuronio nao disparou. Saida = 0")


# %% [markdown]
# > **Os quatro espaços são obrigatórios**
# >
# > As linhas que ficam dentro do if e do else precisam começar deslocadas para a direita, com
# quatro espaços. Esse recuo não é enfeite: é assim que o Python entende o que está dentro e o que
# está fora da decisão. Esquecer o recuo é o erro número um de quem está começando, e produz a
# mensagem IndentationError.


# %% [markdown]
# **Sua vez**
#
# 1. Troque o valor de soma para 1 e execute. A resposta muda?
# 2. Troque o sinal >= por > e execute com soma igual a 2. Explique por escrito o que aconteceu.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### A5. Guardar vários valores em uma lista (*aquecimento*)


# %% [markdown]
# Uma lista guarda vários valores em sequência, entre colchetes. A contagem das posições começa em
# zero, e não em um.


# %%
# Lista: vários valores em sequência, entre colchetes e separados por vírgula.
entradas = [0, 1, 1, 0]

# Mostra a lista inteira, com os colchetes.
print(entradas)
# Os colchetes depois do nome pegam um item pela posição. A contagem começa em 0 (primeiro item).
print(entradas[0])
# Posição 1 é o segundo item da lista.
print(entradas[1])
# len (de "length", comprimento) conta quantos itens a lista tem: aqui são 4.
print(len(entradas))


# %% [markdown]
# O comando **len** informa quantos itens a lista tem.


# %% [markdown]
# **Sua vez**
#
# 1. Mostre o último item da lista usando entradas[3].
# 2. Tente mostrar entradas[4] e leia com atenção a mensagem de erro que aparece.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### A6. Repetir com for (*aquecimento*)


# %% [markdown]
# O comando **for** repete um trecho de código para cada item de uma lista. Um for dentro de outro
# percorre todas as combinações possíveis, que é exatamente o que precisamos para testar um
# neurônio.


# %%
# Laço for: repete o bloco recuado uma vez para cada item da lista [0, 1].
# A cada volta, a variável valor recebe o item da vez (primeiro 0, depois 1).
for valor in [0, 1]:
    # Esta linha está dentro do laço (recuada), então roda uma vez para cada valor.
    print("valor atual:", valor)

# Esta linha não tem recuo: está fora do laço e roda uma única vez, depois que ele termina.
print("---")

# Um laço dentro de outro: para cada x1, o laço de dentro percorre todos os valores de x2.
for x1 in [0, 1]:
    # Laço interno: com x1 fixo, x2 assume 0 e depois 1.
    for x2 in [0, 1]:
        # Oito espaços de recuo: está dentro dos dois laços. Roda 2 x 2 = 4 vezes.
        print("combinacao:", x1, x2)


# %% [markdown]
# Guarde bem esse segundo bloco: as quatro combinações que ele produziu são exatamente as quatro
# linhas da tabela do Exemplo 1 do capítulo.


# %% [markdown]
# **Sua vez**
#
# 1. Acrescente o valor 2 nas duas listas e conte quantas combinações aparecem agora.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### A7. Criar suas próprias funções (*aquecimento*)


# %% [markdown]
# Uma função é um pedaço de código que recebe valores, faz alguma coisa e devolve um resultado. O
# comando **def** cria a função e o **return** devolve a resposta.


# %%
# def cria uma função chamada somar, que recebe dois valores (a e b), chamados parâmetros.
def somar(a, b):
    # Dentro da função (recuado): soma os dois valores recebidos e guarda em resultado.
    resultado = a + b
    # return devolve o resultado para quem chamou a função, e encerra a função.
    return resultado

# Chama a função com a=2 e b=3; o valor devolvido (5) vai direto para o print.
print(somar(2, 3))
# A mesma função, reaproveitada com outros valores: devolve 35.
print(somar(10, 25))


# %% [markdown]
# Criamos a função uma única vez e podemos usá-la quantas vezes quisermos, com valores diferentes.
# No Exercício 1 vamos criar uma função chamada neuronio exatamente assim.


# %% [markdown]
# **Sua vez**
#
# 1. Crie uma função chamada multiplicar que receba dois números e devolva o produto.
# 2. Crie uma função chamada media que receba três notas e devolva a média.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### A8. Escrever textos com números dentro (*aquecimento*)


# %% [markdown]
# Colocando a letra **f** antes das aspas, podemos deixar buracos no texto usando chaves e
# preencher com variáveis. Também é possível controlar quantas casas decimais aparecem.


# %%
# Guarda um texto (string) na variável nome. Textos sempre vão entre aspas.
nome = "Ana"
# Guarda um número com casas decimais. Repare no ponto como separador decimal.
nota = 8.5

# f-string: com a letra f antes das aspas, o que está entre chaves {} é trocado pelo valor.
print(f"A aluna {nome} tirou {nota}")
# Dentro das chaves, :.2f significa "mostre com 2 casas decimais" (8.50).
print(f"Com duas casas decimais: {nota:.2f}")
# :.5f mostra 5 casas decimais. Usaremos isso para comparar com os números do livro.
print(f"Com cinco casas decimais: {nota:.5f}")


# %% [markdown]
# A parte **:.5f** significa mostre com cinco casas decimais. Vamos usar isso o tempo todo para
# conferir os números do capítulo.


# %% [markdown]
# **Sua vez**
#
# 1. Mostre a nota com apenas uma casa decimal.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### A9. Usar a caixa de ferramentas matemática (*aquecimento*)


# %% [markdown]
# Algumas operações não vêm prontas e precisam ser buscadas em um módulo. O comando **import
# math** traz raiz quadrada, logaritmos e a função exponencial.


# %%
# import traz um módulo (uma caixa de ferramentas extra). O módulo math tem funções matemáticas.
import math

# math.sqrt calcula a raiz quadrada. Raiz de 2 aparece na fórmula da atenção (Exercício 7).
print(math.sqrt(2))
# math.log2 é o logaritmo na base 2. log2(0.5) dá -1, pois 2 elevado a -1 é 0.5.
print(math.log2(0.5))
# math.exp(1) calcula e elevado a 1, ou seja, o próprio número e (cerca de 2,718).
print(math.exp(1))


# %% [markdown]
# A primeira linha é a raiz de 2, que aparece na fórmula da atenção. A segunda é o logaritmo na
# base 2, usado na entropia. A terceira é o número e, base dos logaritmos naturais.


# %% [markdown]
# **Sua vez**
#
# 1. Calcule a raiz quadrada de 144.
# 2. Calcule math.log(0.5), sem o número 2, e compare com math.log2(0.5). Os valores são
# diferentes porque a base do logaritmo é outra.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ---
#
# ## Parte 2. Os oito exercícios do capítulo


# %% [markdown]
# A partir daqui, cada exercício reproduz em código um dos exemplos numéricos do Capítulo 1. Os
# números que aparecerem na sua tela devem ser idênticos aos do livro. Confira sempre.


# %% [markdown]
# ### 1. O neurônio de 1943 (*Exemplo 1 do capítulo*)


# %% [markdown]
# Vamos construir o neurônio de McCulloch e Pitts e testá-lo nas quatro combinações possíveis de
# entrada, exatamente como na página do Exemplo 1.


# %%
# Cria a função neuronio, o modelo de McCulloch e Pitts (1943). Recebe duas entradas
# (x1, x2), dois pesos (w1, w2) e o limiar, e devolve 1 (dispara) ou 0 (não dispara).
def neuronio(x1, x2, w1, w2, limiar):
    # multiplica cada entrada pelo seu peso e soma tudo (a soma ponderada)
    soma = w1 * x1 + w2 * x2
    # compara a soma com o limiar e decide se dispara
    if soma >= limiar:
        # Soma chegou ao limiar: o neurônio dispara e a função devolve 1.
        return 1
    # Caso contrário, a soma ficou abaixo do limiar.
    else:
        # O neurônio não dispara e a função devolve 0.
        return 0

# os três números que uma pessoa escolheu em 1943
# Peso da primeira entrada.
w1 = 1
# Peso da segunda entrada.
w2 = 1
# Limiar 2: com pesos 1 e 1, só dispara quando as duas entradas valem 1 (a operação E).
limiar = 2

# Imprime o cabeçalho da tabela, com o nome de cada coluna.
print("x1  x2   soma   saida")
# Laço for externo: x1 assume 0 e depois 1.
for x1 in [0, 1]:
    # Laço interno: para cada x1, x2 assume 0 e 1. Juntos, geram as 4 combinações.
    for x2 in [0, 1]:
        # Calcula a soma aqui também, só para mostrá-la na tabela.
        soma = w1 * x1 + w2 * x2
        # Chama a função neuronio com a combinação da vez e guarda a resposta (0 ou 1) em y.
        y = neuronio(x1, x2, w1, w2, limiar)
        # f-string monta uma linha da tabela; os espaços no texto alinham as colunas.
        print(f" {x1}   {x2}      {soma}      {y}")


# %% [markdown]
# A saída só vale 1 quando as duas entradas valem 1. O neurônio realizou a operação lógica E.


# %% [markdown]
# **Sua vez**
#
# 1. Troque apenas o limiar de 2 para 1 e execute de novo. Que operação lógica o neurônio passou a
# calcular? Escreva a resposta em uma célula de texto.
# 2. Troque o limiar para 3. O que acontece com a coluna da saída? Explique por quê.
# 3. Volte o limiar para 1 e troque w2 para menos 1, escrevendo w2 = -1. Monte a tabela e descreva
# com suas palavras a regra que esse neurônio passou a seguir.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### 2. Medindo a surpresa (*Exemplo 2 do capítulo*)


# %% [markdown]
# A entropia de Shannon mede o tamanho médio da surpresa. Vamos calcular os dois valores do
# capítulo e mais um.


# %%
# Traz o módulo math, que tem o logaritmo na base 2 (math.log2).
import math

# Função que calcula a entropia de Shannon para um evento com dois resultados possíveis.
def entropia(p):
    # p é a probabilidade de um resultado; q é a do outro
    # As duas probabilidades somam 1, então a do outro resultado é 1 - p.
    q = 1 - p
    # Fórmula do capítulo: H = -(p*log2(p) + q*log2(q)). O resultado é medido em bits.
    return -(p * math.log2(p) + q * math.log2(q))

# Chama a função dentro da f-string e mostra 5 casas decimais. Moeda honesta: 1 bit.
print(f"Moeda honesta  (p=0,5):  {entropia(0.5):.5f} bits")
# Moeda viciada (90% de chance de um lado): mais previsível, então menos surpresa.
print(f"Moeda viciada  (p=0,9):  {entropia(0.9):.5f} bits")
# Quase certeza: a surpresa média fica perto de zero.
print(f"Quase certeza  (p=0,99): {entropia(0.99):.5f} bits")


# %% [markdown]
# Os dois primeiros valores são exatamente os do Exemplo 2. Quanto mais previsível o resultado,
# menor a surpresa.


# %% [markdown]
# **Sua vez**
#
# 1. Calcule a entropia para p igual a 0,6 e para p igual a 0,7.
# 2. Use um for para calcular a entropia de p indo de 0,1 até 0,9. Em qual valor de p a entropia é
# maior? Isso faz sentido?
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### 3. O perceptron aprendendo sozinho (*Exemplo 3 do capítulo*)


# %% [markdown]
# Este é o exercício central da lista. O problema é o mesmo do Exercício 1, mas agora ninguém
# informa os pesos. A máquina começa do zero e descobre os valores apenas errando e corrigindo.


# %%
# cada item traz as duas entradas e a resposta certa
# É uma lista de tuplas. Tupla é um grupo de valores entre parênteses, parecido com uma lista.
# Cada item tem a forma ((x1, x2), resposta). Aqui a resposta é a da operação E.
dados = [((0, 0), 0),
         ((0, 1), 0),
         ((1, 0), 0),
         ((1, 1), 1)]

# O perceptron começa sem saber nada: todos os pesos valem zero.
w1 = 0     # peso da primeira entrada
# Peso da segunda entrada, também começando em zero.
w2 = 0     # peso da segunda entrada
# Termo de ajuste (viés): soma-se a ele, e decide-se comparando com zero em vez de um limiar.
b = 0      # termo de ajuste, que faz o papel do limiar
# A taxa de aprendizado diz o tamanho de cada correção.
eta = 1    # taxa de aprendizado

# range(1, 7) gera os números de 1 a 6 (o 7 fica de fora). Cada volta é uma passagem pelos dados.
for passagem in range(1, 7):
    # Variável lógica (booleana): só pode ser True ou False. Começa cada passagem em False.
    houve_correcao = False
    # Percorre os 4 exemplos. Cada item é separado em duas variáveis: entrada e a resposta y.
    for entrada, y in dados:
        # Pega a primeira entrada da tupla (posição 0).
        x1 = entrada[0]
        # Pega a segunda entrada da tupla (posição 1).
        x2 = entrada[1]
        # Soma ponderada mais o termo de ajuste b.
        soma = w1 * x1 + w2 * x2 + b
        # Se a soma for maior ou igual a zero, o perceptron prevê 1.
        if soma >= 0:
            # Guarda a previsão 1.
            y_previsto = 1
        # Senão, a soma é negativa.
        else:
            # Guarda a previsão 0.
            y_previsto = 0
        # O erro é a resposta certa menos a prevista: vale 0 (acertou), 1 ou -1 (errou).
        erro = y - y_previsto
        # O sinal != significa "diferente de". Entra aqui só quando houve erro.
        if erro != 0:
            # so corrige quando erra
            # Regra do perceptron: o peso muda na direção do erro, só se a entrada x1 for 1.
            w1 = w1 + eta * erro * x1
            # Mesma regra para o segundo peso.
            w2 = w2 + eta * erro * x2
            # O termo de ajuste é corrigido sempre que há erro (como se tivesse entrada fixa 1).
            b = b + eta * erro
            # Anota que, nesta passagem, pelo menos uma correção aconteceu.
            houve_correcao = True
    # Fora do laço interno: ao fim de cada passagem, mostra os pesos. :>2 alinha b em 2 espaços.
    print(f"Passagem {passagem}: w1={w1} w2={w2} b={b:>2} corrigiu={houve_correcao}")


# %% [markdown]
# Compare com a tabela do Exemplo 3 do capítulo: os seis valores são idênticos. Na sexta passagem
# não houve nenhuma correção, o que significa que a máquina acertou tudo. Agora confira o
# resultado em uma nova célula:


# %%
# Cabeçalho da tabela de conferência. Usa os pesos finais aprendidos na célula anterior.
print("x1  x2   soma   saida   esperado")
# Percorre de novo os 4 exemplos, agora sem corrigir nada: só para testar.
for entrada, y in dados:
    # Primeira entrada do exemplo.
    x1 = entrada[0]
    # Segunda entrada do exemplo.
    x2 = entrada[1]
    # Soma ponderada com os pesos aprendidos (w1=2, w2=1, b=-3).
    soma = w1 * x1 + w2 * x2 + b
    # Mesma regra de decisão do treinamento.
    if soma >= 0:
        # Soma não negativa: prevê 1.
        y_previsto = 1
    # Soma negativa.
    else:
        # Prevê 0.
        y_previsto = 0
    # Mostra a linha: se a coluna saida for igual à esperado, a máquina acertou.
    print(f" {x1}   {x2}    {soma:>2}      {y_previsto}        {y}")


# %% [markdown]
# **Sua vez**
#
# 1. A máquina chegou a w1 = 2, w2 = 1 e b = -3, valores diferentes dos que a pessoa escolheu no
# Exercício 1, e mesmo assim acertou tudo. Escreva o que isso mostra sobre a ideia de resposta
# certa em aprendizado de máquina.
# 2. Troque eta para 0.5 e execute novamente. Os pesos finais mudaram? E o número de passagens
# necessárias?
# 3. Troque a tabela de dados para a operação OU, ou seja, respostas 0, 1, 1 e 1. O perceptron
# consegue aprender? Em quantas passagens?
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### 4. O XOR resolvido com uma camada oculta (*Exemplo 4 do capítulo*)


# %% [markdown]
# Agora usamos dois neurônios de 1943 lado a lado, formando uma camada oculta, e um terceiro para
# combinar os dois.


# %%
# Define de novo o neurônio de 1943, igual ao do Exercício 1, mas sem os comentários internos.
def neuronio(x1, x2, w1, w2, limiar):
    # Soma ponderada das duas entradas.
    soma = w1 * x1 + w2 * x2
    # Compara com o limiar.
    if soma >= limiar:
        # Dispara.
        return 1
    # Senão.
    else:
        # Não dispara.
        return 0

# Cabeçalho: entradas, os dois neurônios ocultos (h1, h2), a saída da rede e o alvo certo.
print("x1 x2 | h1 h2 | saida | alvo")
# Laço externo para x1.
for x1 in [0, 1]:
    # Laço interno para x2: as 4 combinações.
    for x2 in [0, 1]:
        # Primeiro neurônio oculto: pesos 1 e 1 com limiar 1 dá a operação OU.
        h1 = neuronio(x1, x2, 1, 1, 1)      # camada oculta: um OU
        # Segundo neurônio oculto: pesos 1 e 1 com limiar 2 dá a operação E.
        h2 = neuronio(x1, x2, 1, 1, 2)      # camada oculta: um E
        # Neurônio de saída: recebe h1 e h2 (não x1 e x2). Peso -1 em h2 faz "OU mas não E".
        y = neuronio(h1, h2, 1, -1, 1)      # saida: h1 menos h2
        # O sinal % dá o resto da divisão. O resto de (x1 + x2) por 2 é o XOR correto.
        alvo = (x1 + x2) % 2                # o XOR de verdade, para conferir
        # Mostra a linha da tabela. As colunas saida e alvo devem ser iguais.
        print(f" {x1}  {x2} |  {h1}  {h2} |   {y}   |  {alvo}")


# %% [markdown]
# As colunas saída e alvo são iguais nas quatro linhas: o XOR foi resolvido. O sinal **%** devolve
# o resto da divisão, e o resto da divisão por 2 é justamente o XOR.


# %% [markdown]
# **Sua vez**
#
# 1. Olhe apenas para as colunas h1 e h2. Escreva as quatro duplas que aparecem ali. Por que agora
# é possível separar as classes com uma única reta, se antes não era?
# 2. Troque o peso da saída de -1 para +1 e execute. Que operação o conjunto passou a calcular?
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### 5. Uma rodada de retropropagação (*Exemplo 5 do capítulo*)


# %% [markdown]
# Os cinco passos do Exemplo 5, um a um, com os mesmos números do capítulo.


# %%
# Traz o módulo math, que tem a exponencial math.exp usada na sigmoide.
import math

# Valor que entra na rede.
x = 2.0      # entrada
# Peso que será ajustado pelo treinamento.
w = 0.5      # peso inicial
# Termo de ajuste (viés), mantido em zero neste exemplo.
b = 0.0
# Resposta que a rede deveria dar.
y = 1.0      # resposta esperada
# Tamanho do passo de correção.
eta = 1.0    # taxa de aprendizado

# PASSO 1: ida, calcular a resposta atual da rede
# z é a soma ponderada: peso vezes entrada, mais o viés.
z = w * x + b
# Sigmoide: 1 / (1 + e elevado a -z). Espreme qualquer número para ficar entre 0 e 1.
y_previsto = 1 / (1 + math.exp(-z))
# Mostra z com 6 casas decimais (:.6f), como no capítulo.
print(f"PASSO 1  z  = {z:.6f}")
# Mostra a resposta da rede (y chapéu, escrito y^).
print(f"PASSO 1  y^ = {y_previsto:.6f}")

# PASSO 2: medir o erro
# Erro quadrático: metade do quadrado da diferença. Elevar ao quadrado tira o sinal negativo.
E = 0.5 * (y - y_previsto) ** 2
# Mostra o erro inicial.
print(f"PASSO 2  E  = {E:.6f}")

# PASSO 3: volta, retropropagar o erro
# Derivada da sigmoide: y^ * (1 - y^). Diz o quanto a saída reage a uma mudança em z.
derivada = y_previsto * (1 - y_previsto)
# delta: quanto o erro muda quando z muda (regra da cadeia: diferença vezes derivada).
delta = (y_previsto - y) * derivada
# Gradiente: quanto o erro muda quando o peso w muda. Multiplica pela entrada x.
gradiente = delta * x
# Mostra a derivada.
print(f"PASSO 3  derivada  = {derivada:.6f}")
# Mostra o delta (negativo: a rede respondeu menos do que deveria).
print(f"PASSO 3  delta     = {delta:.6f}")
# Mostra o gradiente.
print(f"PASSO 3  gradiente = {gradiente:.6f}")

# PASSO 4: corrigir o peso
# Anda contra o gradiente: como ele é negativo, o peso aumenta. Isso é a descida do gradiente.
w = w - eta * gradiente
# Mostra o peso já corrigido.
print(f"PASSO 4  w novo = {w:.6f}")

# PASSO 5: conferir se melhorou
# Refaz a ida com o peso novo.
z = w * x + b
# Nova resposta da rede, de novo pela sigmoide.
y_previsto = 1 / (1 + math.exp(-z))
# Novo erro, com a mesma fórmula do Passo 2.
E_novo = 0.5 * (y - y_previsto) ** 2
# Se E novo for menor que E, a correção funcionou.
print(f"PASSO 5  E novo = {E_novo:.6f}")


# %% [markdown]
# Todos os oito números são idênticos aos do capítulo. Agora repita o ciclo trinta vezes em uma
# nova célula e veja o erro caindo:


# %%
# Traz o módulo math (para math.exp).
import math

# Recomeça com os mesmos valores do exemplo anterior: a entrada.
x = 2.0
# O peso inicial.
w = 0.5
# O viés.
b = 0.0
# A resposta esperada.
y = 1.0
# A taxa de aprendizado.
eta = 1.0

# Repete o ciclo de treinamento 30 vezes: range(1, 31) vai de 1 a 30.
for rodada in range(1, 31):
    # Ida: soma ponderada.
    z = w * x + b
    # Ida: sigmoide.
    y_previsto = 1 / (1 + math.exp(-z))
    # Erro desta rodada, calculado antes de corrigir o peso.
    E = 0.5 * (y - y_previsto) ** 2
    # Volta: o delta, agora numa linha só (diferença vezes a derivada da sigmoide).
    delta = (y_previsto - y) * y_previsto * (1 - y_previsto)
    # Corrige o peso: gradiente é delta vezes x.
    w = w - eta * delta * x
    # Só imprime de 5 em 5 rodadas (resto da divisão por 5 igual a zero) ou na rodada 1.
    # O sinal == compara se dois valores são iguais; or significa "ou".
    if rodada % 5 == 0 or rodada == 1:
        # Mostra o peso já corrigido e o erro medido no começo da rodada.
        print(f"rodada {rodada:>2}:  w = {w:.6f}   erro = {E:.6f}")


# %% [markdown]
# **Sua vez**
#
# 1. Aumente para 200 rodadas. O erro chega a zero? Descreva o comportamento.
# 2. Troque eta para 0.1 e depois para 5. O que acontece com a velocidade da queda do erro em cada
# caso?
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### 6. A recompensa caminhando para trás (*Exemplo 6 do capítulo*)


# %% [markdown]
# O corredor com quatro posições do Exemplo 6. O agente não sabe onde está a recompensa e precisa
# descobrir sozinho.


# %%
# alfa é a taxa de aprendizado: quanto do erro é corrigido a cada atualização.
alfa = 0.5    # tamanho da correcao
# gama é o fator de desconto: quanto vale uma recompensa futura comparada a uma imediata.
gama = 0.9    # peso do futuro

# valor de ir para a direita em cada posicao, tudo comecando em zero
# Dicionário: guarda pares chave: valor entre chaves. Aqui, cada posição tem seu valor Q.
Q = {"S1": 0.0, "S2": 0.0, "S3": 0.0}

# Função que aplica a regra de atualização do Q-learning em uma posição (estado).
def atualizar(estado, recompensa, valor_seguinte):
    # Lê no dicionário o valor atual da posição, usando a chave (ex.: Q["S3"]).
    antigo = Q[estado]
    # Regra do capítulo: novo = antigo + alfa * (recompensa + gama * valor_seguinte - antigo).
    novo = antigo + alfa * (recompensa + gama * valor_seguinte - antigo)
    # Grava o novo valor no dicionário, na mesma chave.
    Q[estado] = novo
    # Monta, com f-string, um texto que mostra a conta feita com os números de verdade.
    conta = f"{antigo} + {alfa}*[{recompensa} + {gama}*{valor_seguinte} - {antigo}]"
    # Mostra a conta e o resultado. Esta função não tem return: ela só imprime e atualiza Q.
    print(f"Q({estado}) = {conta} = {novo}")

# Episódio 1: em S3 o agente chega à meta e ganha recompensa 10; depois da meta não há nada.
atualizar("S3", 10, 0.0)      # episodio 1: chega na meta
# Episódio 2: S2 não tem recompensa, mas aprende com o valor que S3 já tem.
atualizar("S2", 0, Q["S3"])   # episodio 2: aprende com S3
# Episódio 3: S1 aprende com o valor de S2. A recompensa vai "escorrendo" para trás.
atualizar("S1", 0, Q["S2"])   # episodio 3: aprende com S2
# Episódio 4: S3 é atualizado de novo e se aproxima de 10.
atualizar("S3", 10, 0.0)      # episodio 4: reforca

# Mostra o dicionário inteiro com os valores finais.
print("Valores finais:", Q)


# %% [markdown]
# Os quatro números são os do capítulo. Repare que a recompensa existia apenas na Meta, mas o
# valor foi escorrendo para trás. Rode agora cinquenta episódios em outra célula:


# %%
# Zera de novo os valores. alfa e gama continuam os da célula anterior (rode-a antes).
Q = {"S1": 0.0, "S2": 0.0, "S3": 0.0}

# Repete 50 episódios: range(1, 51) vai de 1 a 50.
for episodio in range(1, 51):
    # Atualiza S1 olhando o valor de S2 (recompensa 0 ao passar por S1).
    Q["S1"] = Q["S1"] + alfa * (0 + gama * Q["S2"] - Q["S1"])
    # Atualiza S2 olhando o valor de S3 (recompensa 0).
    Q["S2"] = Q["S2"] + alfa * (0 + gama * Q["S3"] - Q["S2"])
    # Atualiza S3: recompensa 10 por chegar à meta, e nada depois dela (gama * 0).
    Q["S3"] = Q["S3"] + alfa * (10 + gama * 0 - Q["S3"])
    # Só mostra de 10 em 10 episódios, para a saída ficar curta.
    if episodio % 10 == 0:
        # Copia o valor de S1 para uma variável de nome curto, para usar na f-string.
        s1 = Q["S1"]
        # O mesmo para S2.
        s2 = Q["S2"]
        # O mesmo para S3.
        s3 = Q["S3"]
        # Mostra os três valores com 4 casas decimais; eles caminham para 8,1, 9 e 10.
        print(f"episodio {episodio:>2}:  S1={s1:.4f}  S2={s2:.4f}  S3={s3:.4f}")


# %% [markdown]
# Os valores estabilizaram em 10, 9 e 8,1. Repare que 9 é 0,9 vezes 10, e 8,1 é 0,9 vezes 9. O
# fator gama fez cada posição valer um pouco menos que a seguinte, porque está mais longe da
# recompensa.


# %% [markdown]
# **Sua vez**
#
# 1. Troque gama para 0.5 e execute. Os valores finais de S1 e S2 mudam? Por quê?
# 2. Troque gama para 1.0. O que acontece? O que isso significa em termos de dar ou não
# importância ao futuro?
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### 7. A atenção calculando os pesos na hora (*Exemplo 7 do capítulo*)


# %% [markdown]
# O mecanismo que está por trás de todos os modelos de linguagem atuais, com a frase de três
# palavras do Exemplo 7.


# %%
# Traz o módulo math (raiz quadrada e exponencial).
import math

# Lista com as três palavras da frase do Exemplo 7.
palavras = ["o", "gato", "dorme"]
# Lista de listas: a chave (k) de cada palavra, um vetor de dois números, na mesma ordem.
chaves = [[0, 1], [1, 0], [1, 1]]
# O valor (v) de cada palavra: é a informação que será misturada no final.
valores = [[1, 0], [0, 1], [1, 1]]
# A consulta (q): o que a palavra dorme está "procurando" nas outras.
q = [1, 0]      # a consulta da palavra dorme
# dk é o tamanho dos vetores; entra na fórmula como raiz de dk.
dk = 2          # os vetores tem duas dimensoes

# Produto escalar: multiplica posição a posição e soma. Mede o quanto dois vetores combinam.
def produto_escalar(a, b):
    # Para vetores de 2 números: a[0]*b[0] + a[1]*b[1].
    return a[0] * b[0] + a[1] * b[1]

# PASSO 1 e 2: escores divididos pela raiz de dk
# Começa com uma lista vazia, que será preenchida dentro do laço.
escores = []
# Percorre cada chave k da lista chaves.
for k in chaves:
    # Escore = produto escalar da consulta com a chave, dividido por raiz de 2.
    escore = produto_escalar(q, k) / math.sqrt(dk)
    # append acrescenta um item no fim da lista.
    escores.append(escore)
    # Mostra a chave e o seu escore com 5 casas decimais.
    print(f"escore de {k} = {escore:.5f}")

# PASSO 3: softmax
# Lista vazia para guardar e elevado a cada escore.
exponenciais = []
# Percorre cada escore e.
for e in escores:
    # math.exp(e) calcula e elevado ao escore; o resultado é sempre positivo.
    exponenciais.append(math.exp(e))

# sum soma todos os itens de uma lista.
soma = sum(exponenciais)
# Mostra a soma das exponenciais.
print(f"soma das exponenciais = {soma:.5f}")

# Lista vazia para os pesos de atenção.
pesos = []
# Percorre cada exponencial.
for e in exponenciais:
    # Divide pela soma para que os pesos fiquem entre 0 e 1 e somem 1 (o softmax).
    pesos.append(e / soma)

# range(3) gera 0, 1 e 2: as posições das três palavras.
for i in range(3):
    # Mostra cada palavra com o seu peso. :>5 alinha a palavra à direita em 5 espaços.
    print(f"peso de {palavras[i]:>5} = {pesos[i]:.5f}")

# PASSO 4: media ponderada dos valores
# A saída começa como o vetor (0, 0) e vai acumulando a contribuição de cada palavra.
saida = [0, 0]
# Percorre as três palavras pela posição i.
for i in range(3):
    # valores[i][0] é o primeiro número do valor da palavra i. Soma peso vezes esse número.
    saida[0] = saida[0] + pesos[i] * valores[i][0]
    # O mesmo para o segundo número. No fim, saida é a média ponderada dos valores.
    saida[1] = saida[1] + pesos[i] * valores[i][1]

# Mostra o vetor de saída da atenção para a palavra dorme.
print(f"saida = ({saida[0]:.5f} ; {saida[1]:.5f})")


# %% [markdown]
# Os pesos 0,19778 e 0,40111 são exatamente os do capítulo, e sua soma dá 1. O ponto central:
# esses pesos não estavam guardados em lugar nenhum, foram calculados agora, a partir desta frase.


# %% [markdown]
# **Sua vez**
#
# 1. Troque a consulta para q = [0, 1] e execute. Quais palavras passaram a receber mais peso?
# Explique olhando para as chaves.
# 2. Acrescente uma quarta palavra à frase, com chave e valor à sua escolha, e ajuste os laços que
# usam range(3) para range(4). Confira se a soma dos pesos continua dando 1.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### 8. O objetivo que treina os modelos de linguagem (*Exemplo 8 do capítulo*)


# %% [markdown]
# O último exercício mostra, em números, o que significa treinar um modelo de linguagem.


# %%
# Traz o módulo math (logaritmo natural math.log e exponencial math.exp).
import math

# antes do treinamento
# Probabilidade que o modelo dava à primeira palavra certa.
p1 = 0.20
# Probabilidade que o modelo dava à segunda palavra certa.
p2 = 0.50
# math.log é o logaritmo natural (ln).
# Somar os logaritmos equivale a multiplicar as probabilidades.
soma_antes = math.log(p1) + math.log(p2)
# Mostra cada logaritmo com 4 casas decimais. Logaritmo de número menor que 1 é negativo.
print(f"ANTES:  ln({p1}) = {math.log(p1):.4f}   ln({p2}) = {math.log(p2):.4f}")
# Mostra a soma dos logaritmos antes do treinamento.
print(f"ANTES:  soma dos logaritmos = {soma_antes:.4f}")

# depois de algum treinamento
# O modelo treinado dá probabilidade maior à primeira palavra certa.
p1 = 0.40
# E também à segunda.
p2 = 0.70
# Soma dos logaritmos depois do treinamento.
soma_depois = math.log(p1) + math.log(p2)
# Mostra os logaritmos novos.
print(f"DEPOIS: ln({p1}) = {math.log(p1):.4f}   ln({p2}) = {math.log(p2):.4f}")
# Mostra a soma nova.
print(f"DEPOIS: soma dos logaritmos = {soma_depois:.4f}")

# Treinar um modelo de linguagem é fazer essa soma crescer (ficar mais perto de zero).
if soma_depois > soma_antes:
    # Só imprime se a condição for verdadeira. Este if não tem else.
    print("O segundo modelo e melhor: a soma aumentou.")

# Perplexidade: e elevado a menos a média dos logaritmos (soma dividida por 2 palavras).
print(f"Perplexidade antes:  {math.exp(-soma_antes / 2):.3f}")
# Quanto menor a perplexidade, menos "perdido" o modelo fica na escolha da próxima palavra.
print(f"Perplexidade depois: {math.exp(-soma_depois / 2):.3f}")


# %% [markdown]
# **Sua vez**
#
# 1. Escreva com suas palavras por que menos 1,2730 é maior que menos 2,3026.
# 2. Troque p1 e p2 para 0.95 e 0.98. O que acontece com a soma e com a perplexidade?
# 3. Um modelo perfeito atribuiria probabilidade 1 a tudo. Teste com p1 = 1.0 e p2 = 1.0 e veja
# quanto vale a soma dos logaritmos nesse caso.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ---
#
# ## Parte 3. Três desafios


# %% [markdown]
# Os desafios não são obrigatórios, mas valem ponto extra e são a melhor parte da aula. Faça se
# sobrar tempo.


# %% [markdown]
# ### D1. A fábrica de portas lógicas (*desafio*)


# %% [markdown]
# Escreva uma função chamada **tabela** que receba w1, w2 e limiar, e mostre automaticamente a
# tabela completa das quatro combinações. Depois use essa função para descobrir quais valores
# produzem cada uma destas operações: E, OU, e uma que responde 1 sempre que as entradas forem
# diferentes. Esta última é possível com um único neurônio? Justifique.


# %% [markdown]
# ### D2. O experimento de 1969 (*desafio*)


# %% [markdown]
# Pegue o código do Exercício 3 e troque apenas a tabela de dados pelo XOR, ou seja, respostas 0,
# 1, 1 e 0. Aumente para trinta passagens e conte quantos erros ocorrem em cada uma. Este é,
# literalmente, o experimento que congelou a pesquisa em redes neurais por uma década.


# %%
# Mesma estrutura do Exercício 3, mas com as respostas do XOR: 1 só quando as entradas diferem.
dados_xor = [((0, 0), 0),
             ((0, 1), 1),
             ((1, 0), 1),
             ((1, 1), 0)]

# Peso da primeira entrada, começando em zero.
w1 = 0
# Peso da segunda entrada, começando em zero.
w2 = 0
# Termo de ajuste, começando em zero.
b = 0
# Taxa de aprendizado.
eta = 1

# Agora são 30 passagens pelos dados: range(1, 31) vai de 1 a 30.
for passagem in range(1, 31):
    # Contador de erros, zerado no começo de cada passagem.
    erros = 0
    # Percorre os 4 exemplos do XOR.
    for entrada, y in dados_xor:
        # Primeira entrada.
        x1 = entrada[0]
        # Segunda entrada.
        x2 = entrada[1]
        # Soma ponderada mais o termo de ajuste.
        soma = w1 * x1 + w2 * x2 + b
        # Regra de decisão do perceptron.
        if soma >= 0:
            # Prevê 1.
            y_previsto = 1
        # Senão.
        else:
            # Prevê 0.
            y_previsto = 0
        # Diferença entre a resposta certa e a prevista.
        erro = y - y_previsto
        # Só entra se errou.
        if erro != 0:
            # Soma 1 ao contador de erros desta passagem.
            erros = erros + 1
            # Corrige o primeiro peso (regra do perceptron).
            w1 = w1 + eta * erro * x1
            # Corrige o segundo peso.
            w2 = w2 + eta * erro * x2
            # Corrige o termo de ajuste.
            b = b + eta * erro
    # A cada 5 passagens, mostra quantos erros houve e os pesos atuais.
    if passagem % 5 == 0:
        # Os erros nunca chegam a zero: uma única reta não separa as classes do XOR.
        print(f"Passagem {passagem}: erros = {erros}   w1={w1} w2={w2} b={b}")


# %% [markdown]
# Quatro erros em toda passagem, para sempre. O perceptron erra as quatro respostas, corrige, e
# volta ao mesmo lugar. Ele nunca vai aprender o XOR, por mais passagens que você mande executar.
# Agora rode de novo o Exercício 4, com a camada oculta, e compare. Escreva um parágrafo
# relacionando esses dois resultados com a seção 1.4 do capítulo.


# %% [markdown]
# ### D3. O gráfico do erro caindo (*desafio*)


# %% [markdown]
# O Colab consegue desenhar gráficos. Guarde o erro de cada rodada em uma lista e desenhe a curva.


# %%
# Traz o módulo math (exponencial).
import math
# matplotlib.pyplot desenha gráficos. "as plt" dá a ele um apelido curto para digitar menos.
import matplotlib.pyplot as plt

# Mesmos valores iniciais do Exercício 5: a entrada.
x = 2.0
# O peso inicial.
w = 0.5
# O viés.
b = 0.0
# A resposta esperada.
y = 1.0
# A taxa de aprendizado.
eta = 1.0

# Lista vazia que vai guardar o erro de cada rodada, para desenhar depois.
historico = []
# range(60) gera os números de 0 a 59: são 60 rodadas.
for rodada in range(60):
    # Ida: soma ponderada.
    z = w * x + b
    # Ida: sigmoide.
    y_previsto = 1 / (1 + math.exp(-z))
    # Erro da rodada.
    E = 0.5 * (y - y_previsto) ** 2
    # Guarda o erro no fim da lista historico.
    historico.append(E)
    # Volta: delta (diferença vezes derivada da sigmoide).
    delta = (y_previsto - y) * y_previsto * (1 - y_previsto)
    # Corrige o peso.
    w = w - eta * delta * x

# plt.plot desenha uma linha: no eixo horizontal a posição na lista, no vertical o erro.
plt.plot(historico)
# Texto do eixo horizontal (x).
plt.xlabel("rodada de treinamento")
# Texto do eixo vertical (y).
plt.ylabel("erro")
# Título do gráfico.
plt.title("O erro caindo ao longo do treinamento")
# Liga a grade de fundo, que ajuda a ler os valores.
plt.grid(True)
# Mostra o gráfico logo abaixo da célula.
plt.show()


# %% [markdown]
# A saída não é texto, e sim um gráfico desenhado logo abaixo da célula. Ele mostra a curva de
# aprendizado descendo rápido no início e devagar no fim, que é o comportamento típico de qualquer
# treinamento de rede neural.


# %% [markdown]
# ---
#
# ## Anexo A. Os erros mais comuns e o que fazer


# %% [markdown]
# Errar é parte de programar. Toda mensagem de erro do Python informa o tipo do problema e a linha
# em que ele ocorreu. Leia sempre a última linha da mensagem primeiro: é ela que diz o que
# aconteceu.


# %% [markdown]
# **Tabela A.1. Mensagens de erro frequentes nesta lista**
#
# | A mensagem diz | O que aconteceu | Como resolver |
# | --- | --- | --- |
# | NameError | Você usou um nome que o Python não conhece. | Geralmente é erro de digitação no
# nome da variável, ou você esqueceu de executar a célula anterior que criava esse nome. |
# | IndentationError | O recuo das linhas está errado. | As linhas dentro de um if, else, for ou
# def precisam começar com quatro espaços. Confira se todas estão alinhadas entre si. |
# | SyntaxError | Falta ou sobra algum sinal. | Procure parênteses ou aspas que abriram e não
# fecharam, e confira se os dois pontos no final do if, do for e do def estão lá. |
# | TypeError | Você misturou tipos incompatíveis. | Normalmente é a tentativa de somar um texto
# com um número. Verifique se algum valor está entre aspas sem necessidade. |
# | ZeroDivisionError | Houve uma divisão por zero. | Confira o valor da variável que está no
# denominador. |
# | ModuleNotFoundError | O módulo pedido não foi encontrado. | Confira a grafia. Deve ser import
# math, tudo em letras minúsculas. |
# | Nada acontece | A célula não foi executada. | Clique dentro da célula e pressione Shift e
# Enter ao mesmo tempo. Verifique se o número entre colchetes apareceu à esquerda dela. |


# %% [markdown]
# > **A regra de ouro quando tudo parece errado**
# >
# > No menu Ambiente de execução, escolha Reiniciar sessão e executar tudo. Isso limpa a memória e
# roda todas as células na ordem, do começo ao fim. Resolve a maioria dos problemas causados por
# células executadas fora de ordem.


# %% [markdown]
# ---
#
# ## Anexo B. Entrega e critérios de avaliação


# %% [markdown]
# A entrega é o próprio caderno do Colab, compartilhado com o professor.


# %% [markdown]
# ### Como entregar


# %% [markdown]
# 1. No caderno, clique no botão Compartilhar, no canto superior direito.
# 2. Em Acesso geral, escolha a opção que permite a qualquer pessoa com o link visualizar.
# 3. Clique em Copiar link.
# 4. Cole o link no espaço indicado pelo professor, junto com o seu nome e a sua turma.


# %% [markdown]
# > **Antes de entregar, confira**
# >
# > O caderno precisa estar com todas as células executadas e com as saídas visíveis. Use Ambiente
# de execução e depois Reiniciar sessão e executar tudo, espere terminar e só então compartilhe.
# Um caderno entregue sem as saídas não pode ser avaliado.


# %% [markdown]
# ### Critérios de avaliação


# %% [markdown]
# **Tabela B.1. Distribuição dos pontos**
#
# | O que será avaliado | Pontos |
# | --- | --- |
# | Parte 1 completa, com as nove células executadas e sem erro | 2,0 |
# | Exercícios 1 a 4 executados, com saídas idênticas às esperadas | 2,0 |
# | Exercícios 5 a 8 executados, com saídas idênticas às esperadas | 2,0 |
# | Blocos Sua vez respondidos em células de texto, com explicação escrita | 3,0 |
# | Organização do caderno: títulos, comentários no código e nome do arquivo correto | 1,0 |
# | Desafios D1, D2 e D3 (ponto extra) | até 1,0 |


# %% [markdown]
# Para escrever as respostas em texto dentro do caderno, use o botão de célula de texto, que
# aparece no alto da tela ao lado do botão de célula de código. Ali você pode escrever
# normalmente, sem se preocupar com sintaxe de programação.


# %% [markdown]
# **Uma última observação**


# %% [markdown]
# Ao terminar esta lista, você terá escrito, com as próprias mãos, um neurônio de 1943, um
# perceptron que aprende sozinho, uma rede de duas camadas, uma rodada de retropropagação, um
# agente que aprende por recompensa e o mecanismo de atenção que sustenta os modelos de linguagem
# atuais. São menos de duzentas linhas de código no total, e elas atravessam oitenta anos de
# história. Guarde este caderno: ele será a base das próximas aulas.
