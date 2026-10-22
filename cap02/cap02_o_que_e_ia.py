# -*- coding: utf-8 -*-
"""
A ginga dos números: livro de exercícios
Lista de Exercícios do Capítulo 2

Versão em script do caderno cap02_o_que_e_ia.ipynb, com o mesmo código e os mesmos comentários.
Autor: Bruno Menezes  |  https://brunoleomenezes.github.io/
Repositório: https://github.com/brunoleomenezes/ginga-dos-numeros

Como usar: o mais simples é abrir o caderno .ipynb no Google Colab. Este arquivo serve para quem
prefere rodar no próprio computador (python cap02_o_que_e_ia.py) ou ler o código em um editor. Os blocos
marcados com "# %%" são as células do caderno, na mesma ordem; os textos explicativos aparecem
como comentários. Para ver o resultado de cada bloco, rode o arquivo inteiro: os gráficos abrem
em janelas próprias.
"""



# %% [markdown]
# > *Os dez exemplos numéricos do capítulo, executados por você em Python. E, no fim, a descoberta
# de que uma biblioteca faz em três linhas aquilo que você acabou de construir do zero.*


# %% [markdown]
# ---
#
# ## Como usar esta lista


# %% [markdown]
# Esta lista continua de onde a do Capítulo 1 parou. Se você fez aquela, já sabe tudo o que
# precisa para começar: abrir o Colab, digitar em uma célula e executar com Shift e Enter. Se não
# fez, vale voltar nela primeiro, porque o básico não será repetido aqui.


# %% [markdown]
# A lista tem quatro partes. A Parte 0 prepara o ambiente em três passos rápidos. A Parte 1
# apresenta sete ferramentas novas de Python, todas necessárias para os exercícios seguintes. A
# Parte 2 traz os dez exercícios, um para cada exemplo numérico do capítulo. A Parte 3 é a mais
# interessante: refazemos quatro exercícios usando a biblioteca scikit-learn e comparamos os
# resultados com o que você calculou à mão.


# %% [markdown]
# **Três combinados, os mesmos de sempre**


# %% [markdown]
# 1. **Digite o código, não copie.** Digitar é o que ensina. Errar ao digitar faz parte, e o Anexo
# A explica como resolver os erros mais comuns.
# 2. **Execute na ordem.** Nesta lista, várias células dependem de variáveis criadas antes. Pular
# uma célula é a causa número um de erro.
# 3. **Compare com a saída esperada.** Cada código traz a resposta que deve aparecer. Os números
# precisam bater com os do livro.


# %% [markdown]
# > **O que esta lista tem de diferente da anterior**
# >
# > Na lista do Capítulo 1 você programou a história da IA. Aqui você vai programar os algoritmos
# em si. Ao final da Parte 2 terá construído, do zero, uma regressão linear, um classificador por
# vizinhos, uma árvore de decisão, um agrupador e um avaliador de modelos. A Parte 3 mostra que
# tudo isso já existe pronto em uma biblioteca, e que os resultados coincidem até a quarta casa
# decimal. Essa coincidência é o ponto da aula: você vai usar a biblioteca sabendo o que ela faz
# por dentro.


# %% [markdown]
# ---
#
# ## Parte 0. Preparando o ambiente


# %% [markdown]
# **Passo 1. Abra um caderno novo**
#
# Acesse colab.research.google.com com a sua conta Google da escola e clique em Novo notebook.
# Nada precisa ser instalado.


# %% [markdown]
# **Passo 2. Dê o nome correto ao caderno**
#
# Clique no nome que aparece no alto da tela e troque por: Lista 2 seguido do seu nome. Exemplo:
# Lista 2 Maria Silva. O caderno é salvo sozinho no seu Google Drive.


# %% [markdown]
# **Passo 3. Confirme que as bibliotecas estão disponíveis**
#
# Digite em uma célula o comando import sklearn seguido de print(sklearn.__version__) e execute.
# Se aparecer um número de versão, está tudo certo. O Colab já vem com o scikit-learn, o
# matplotlib e o numpy instalados, e usaremos os três nesta lista.


# %% [markdown]
# ---
#
# ## Parte 1. Sete ferramentas novas de Python


# %% [markdown]
# Os exercícios do Capítulo 2 trabalham com tabelas de dados, e para isso precisamos de recursos
# que ainda não usamos. São sete células curtas. Digite cada uma separadamente e execute antes de
# passar para a próxima.


# %% [markdown]
# ### A1. Uma tabela é uma lista de listas (*aquecimento*)


# %% [markdown]
# Para guardar uma tabela em Python, colocamos uma lista dentro da outra. Cada lista interna é uma
# linha. Para acessar uma célula específica usamos dois colchetes: o primeiro escolhe a linha, o
# segundo escolhe a coluna.


# %%
# Uma tabela é uma lista de listas: cada lista interna é uma linha da tabela.
# Os colchetes externos abrem a lista grande; cada linha guarda nome, horas e nota.
alunos = [["Ana",   1, 2],     # linha 0
          ["Bruno", 2, 4],     # linha 1
          ["Carla", 3, 5]]     # linha 2

# Mostra a tabela inteira, com todos os colchetes
print(alunos)
# Um colchete só escolhe a linha: alunos[0] é a primeira linha (a da Ana)
print(alunos[0])
# Dois colchetes: linha 0, depois coluna 0, ou seja, o nome da Ana
print(alunos[0][0])
# Linha 1 (Bruno), coluna 2 (a nota); a contagem começa em zero
print(alunos[1][2])
# len conta os itens: len(alunos) dá o número de linhas, len(alunos[0]) o de colunas
print(len(alunos), "linhas e", len(alunos[0]), "colunas")


# %% [markdown]
# Repare que **alunos[1][2]** devolveu 4: linha de índice 1, que é o Bruno, coluna de índice 2,
# que é a nota. A contagem começa em zero nas duas dimensões.


# %% [markdown]
# **Sua vez**
#
# 1. Mostre a nota da Carla usando dois colchetes.
# 2. Acrescente uma quarta linha com o seu nome, suas horas e sua nota, e imprima a tabela
# inteira.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### A2. Percorrendo uma tabela linha por linha (*aquecimento*)


# %% [markdown]
# O comando **for** percorre a tabela entregando uma linha por vez. E existe um atalho muito útil:
# se você escrever três nomes de variáveis separados por vírgula, o Python separa a linha
# automaticamente para você. Isso se chama desempacotamento.


# %%
# Laço for: repete o bloco recuado uma vez para cada linha da tabela
for linha in alunos:
    # Pega a coluna 0 da linha atual (o nome)
    nome = linha[0]
    # Pega a coluna 1 (as horas de estudo)
    horas = linha[1]
    # Pega a coluna 2 (a nota)
    nota = linha[2]
    # f-string: o f antes das aspas troca cada {variável} pelo seu valor
    print(f"{nome} estudou {horas} horas e tirou {nota}")

# Imprime um separador para dividir as duas versões na saída
print("---")

# Desempacotamento: o Python separa a linha em variáveis automaticamente.
for nome, horas, nota in alunos:
    # {nome:>6} alinha o nome à direita num espaço de 6 caracteres
    print(f"{nome:>6}  {horas}h  nota {nota}")


# %% [markdown]
# A notação **{nome:&gt;6}** alinha o texto à direita em seis espaços. É o que deixa as colunas
# alinhadas nas saídas desta lista.


# %% [markdown]
# **Sua vez**
#
# 1. Troque o alinhamento de 6 para 10 e veja o que muda.
# 2. Escreva um for que some todas as notas da tabela e mostre a média.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### A3. Dicionários: guardando pares (*aquecimento*)


# %% [markdown]
# Um dicionário guarda pares de chave e valor, usando chaves em vez de colchetes. Em vez de
# acessar por posição, acessamos por nome. Vamos usar dicionários para contar votos no Exercício
# 6.


# %%
# Um dicionário guarda pares de chave e valor, escritos entre chaves { }.
notas = {"Ana": 2, "Bruno": 4, "Carla": 5}

# Mostra o dicionário inteiro
print(notas)
# Acessa o valor pela chave (o nome), e não pela posição
print(notas["Bruno"])

# Atribuir a uma chave nova acrescenta o par ao dicionário
notas["Daniel"] = 3
# Mostra o dicionário já com o Daniel
print(notas)

# Um for sobre um dicionário percorre as chaves, uma por vez
for nome in notas:
    # Usa a chave para buscar a nota correspondente
    print(nome, "tirou", notas[nome])


# %% [markdown]
# **Sua vez**
#
# 1. Adicione mais duas pessoas ao dicionário.
# 2. Escreva um for que mostre apenas as pessoas com nota maior ou igual a 4.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### A4. Funções que devolvem várias coisas (*aquecimento*)


# %% [markdown]
# Uma função pode devolver mais de um valor de uma só vez, separando por vírgula no **return**. Na
# hora de chamar, recebemos todos com o mesmo desempacotamento da célula A2. Os comandos **sum**,
# **min** e **max** já vêm prontos no Python.


# %%
# def cria uma função chamada estatisticas, que recebe uma lista de valores
def estatisticas(valores):
    # sum soma todos os itens da lista
    total = sum(valores)
    # A média é a soma dividida pela quantidade de itens
    media = total / len(valores)
    # return devolve quatro coisas de uma vez, separadas por vírgula
    return total, media, min(valores), max(valores)

# Chama a função e desempacota os quatro resultados em quatro variáveis
t, m, menor, maior = estatisticas([2, 4, 5, 4, 5])

# Mostra a soma
print("soma  :", t)
# Mostra a média
print("media :", m)
# Mostra o menor valor (calculado por min)
print("menor :", menor)
# Mostra o maior valor (calculado por max)
print("maior :", maior)


# %% [markdown]
# **Sua vez**
#
# 1. Acrescente à função o cálculo da amplitude, que é o maior menos o menor, e devolva esse valor
# também.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### A5. Ordenando uma lista (*aquecimento*)


# %% [markdown]
# O comando **sorted** ordena uma lista. Quando os itens são duplas, precisamos dizer por qual
# elemento ordenar, e é isso que faz o trecho **key=lambda item: item[1]**. Leia assim: ordene
# usando o item de índice 1 de cada dupla. Isso será essencial no algoritmo dos vizinhos mais
# próximos.


# %%
# Lista de duplas (tuplas): cada uma tem um nome e uma distância
distancias = [("A", 2.83), ("B", 2.24), ("C", 1.41), ("D", 3.61), ("E", 5.00)]

# sorted ordena; key=lambda item: item[1] manda ordenar pela distância (posição 1)
ordenada = sorted(distancias, key=lambda item: item[1])

# Percorre a lista ordenada, desempacotando nome e distância
for nome, d in ordenada:
    # Mostra cada par, do mais perto ao mais longe
    print(f"{nome}: {d}")

# Fatia: ordenada[:3] pega os itens das posições 0, 1 e 2 (os três primeiros)
print("os tres mais proximos:", ordenada[:3])


# %% [markdown]
# A notação **ordenada[:3]** pega os três primeiros itens da lista. É chamada de fatia.


# %% [markdown]
# **Sua vez**
#
# 1. Ordene do maior para o menor acrescentando reverse=True dentro do sorted.
# 2. Pegue apenas os dois primeiros usando uma fatia.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### A6. Criando listas em uma linha (*aquecimento*)


# %% [markdown]
# A compreensão de lista permite construir uma lista nova a partir de outra, em uma única linha.
# Leia da esquerda para a direita: faça isto, para cada item daquela lista, opcionalmente só se
# tal condição for verdadeira.


# %%
# Lista com as horas de estudo
horas = [1, 2, 3, 4, 5]

# Compreensão de lista: monta uma lista nova com h * 2 para cada h de horas
dobro = [h * 2 for h in horas]
# Mostra os dobros
print(dobro)

# Com if no final, só entram na lista nova os valores maiores que 2
acima = [h for h in horas if h > 2]
# Mostra os valores filtrados
print(acima)

# ** é a potência: h ** 2 é h ao quadrado
quadrados = [h ** 2 for h in horas]
# Soma os quadrados (1 + 4 + 9 + 16 + 25)
print("soma dos quadrados:", sum(quadrados))


# %% [markdown]
# **Sua vez**
#
# 1. Crie uma lista com o triplo de cada valor.
# 2. Crie uma lista apenas com os valores pares. Dica: um número é par quando h % 2 resulta em
# zero.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### A7. Um gráfico de pontos (*aquecimento*)


# %% [markdown]
# O comando **scatter** desenha pontos soltos, em vez da linha contínua que usamos no Capítulo 1.
# É a forma padrão de visualizar pares de valores.


# %%
# Importa a parte de gráficos do matplotlib, com o apelido plt
import matplotlib.pyplot as plt

# Horas de estudo dos cinco alunos (eixo horizontal)
horas = [1, 2, 3, 4, 5]
# Notas dos mesmos cinco alunos, na mesma ordem (eixo vertical)
notas = [2, 4, 5, 4, 5]

# scatter desenha um ponto solto para cada par (horas, nota)
plt.scatter(horas, notas)
# Nome do eixo horizontal
plt.xlabel("horas de estudo")
# Nome do eixo vertical
plt.ylabel("nota")
# Título do gráfico
plt.title("Cinco alunos")
# Liga a grade de fundo, que ajuda a ler os valores
plt.grid(True)
# Mostra o gráfico abaixo da célula
plt.show()


# %% [markdown]
# A saída aqui não é texto e sim um gráfico, desenhado logo abaixo da célula. Guarde esse gráfico:
# no Exercício 4 vamos traçar a reta que passa no meio desses cinco pontos.


# %% [markdown]
# **Sua vez**
#
# 1. Acrescente plt.axis([0, 6, 0, 6]) antes do plt.show() para fixar a escala dos eixos.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ---
#
# ## Parte 2. Os dez exercícios do capítulo


# %% [markdown]
# Cada exercício a seguir reproduz um exemplo numérico do Capítulo 2. Os números na sua tela devem
# ser idênticos aos do livro. Confira sempre.


# %% [markdown]
# ### 1. Por que a escala dos números importa (*Exemplo 1 do capítulo*)


# %% [markdown]
# Queremos saber quem se parece mais com a pessoa de referência R. A intuição diz que é P, que tem
# apenas 1 ano de diferença. Vamos ver o que o computador acha.


# %%
# Importa o módulo math, que traz funções matemáticas como a raiz quadrada
import math

# Pessoa de referência: (idade, salário)
R = (30, 3000)
# P: só 1 ano mais velha que R, mas ganha 1000 a mais
P = (31, 4000)
# Q: 30 anos mais velha que R, e também ganha 1000 a mais
Q = (60, 4000)

# Função que calcula a distância em linha reta (euclidiana) entre dois pontos
def distancia(a, b):
    # Diferença na primeira coordenada (idade)
    dif1 = a[0] - b[0]
    # Diferença na segunda coordenada (salário)
    dif2 = a[1] - b[1]
    # Soma das diferenças ao quadrado (o teorema de Pitágoras)
    soma = dif1 ** 2 + dif2 ** 2
    # math.sqrt tira a raiz quadrada e devolve a distância
    return math.sqrt(soma)

# Título da primeira parte da saída
print("SEM NORMALIZAR")
# :.4f dentro da f-string mostra o número com 4 casas decimais
print(f"  d(R,P) = {distancia(R, P):.4f}")
# Distância de R até Q, que deveria ser bem maior
print(f"  d(R,Q) = {distancia(R, Q):.4f}")
# A diferença mínima mostra que o salário (números grandes) engoliu a idade
print(f"  diferenca entre as duas = {distancia(R,Q) - distancia(R,P):.4f}")


# %% [markdown]
# As duas distâncias são praticamente iguais, embora Q tenha 30 anos a mais. O salário, medido em
# milhares, engoliu completamente a idade. Agora vamos normalizar, colocando as duas grandezas na
# mesma faixa entre 0 e 1:


# %%
# Normalização mín-máx: leva cada grandeza para a faixa de 0 a 1
def normalizar(p, min1, max1, min2, max2):
    # Idade: subtrai o mínimo e divide pela amplitude (máximo menos mínimo)
    a = (p[0] - min1) / (max1 - min1)
    # Salário: a mesma conta, com o mínimo e o máximo do salário
    b = (p[1] - min2) / (max2 - min2)
    # Devolve o ponto normalizado como uma tupla
    return (a, b)

# Normaliza R usando idade entre 30 e 60 e salário entre 3000 e 4000
Rn = normalizar(R, 30, 60, 3000, 4000)
# Normaliza P com os mesmos limites
Pn = normalizar(P, 30, 60, 3000, 4000)
# Normaliza Q com os mesmos limites
Qn = normalizar(Q, 30, 60, 3000, 4000)

# Título da lista de valores normalizados
print("valores normalizados")
# Mostra as duas coordenadas de R, já entre 0 e 1
print(f"  R = ({Rn[0]:.4f} ; {Rn[1]:.4f})")
# Mostra as coordenadas de P
print(f"  P = ({Pn[0]:.4f} ; {Pn[1]:.4f})")
# Mostra as coordenadas de Q
print(f"  Q = ({Qn[0]:.4f} ; {Qn[1]:.4f})")
# Título da segunda parte
print("DEPOIS DE NORMALIZAR")
# Reaproveita a função distancia da célula anterior, agora com pontos normalizados
print(f"  d(R,P) = {distancia(Rn, Pn):.4f}")
# Agora Q fica claramente mais longe de R do que P
print(f"  d(R,Q) = {distancia(Rn, Qn):.4f}")


# %% [markdown]
# **Sua vez**
#
# 1. Troque o salário de Q de 4000 para 3050 e execute a primeira célula de novo. O problema de
# escala desaparece? Por quê?
# 2. Acrescente uma terceira pessoa, com 32 anos e salário 3100, e calcule a distância dela até R
# antes e depois da normalização.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### 2. Decorar não é aprender (*Exemplo 2 do capítulo*)


# %% [markdown]
# Vamos escrever um pequeno diagnosticador automático. Ele recebe o erro de treino e o de teste de
# cada modelo e decide se houve subajuste, sobreajuste ou equilíbrio.


# %%
# Tabela de modelos: nome, erro no treino e erro no teste
modelos = [["A. Reta simples",          2.10, 2.30],
           ["B. Curva de grau 3",       0.40, 0.55],
           ["C. Curva de grau 12",      0.01, 3.90],
           ["D. Memoriza cada exemplo", 0.00, 5.20]]

# Cabeçalho: :26s reserva 26 espaços para o texto e :>7 alinha à direita em 7
print(f"{'modelo':26s} {'treino':>7} {'teste':>7} {'lacuna':>7}   diagnostico")
# Percorre cada modelo, desempacotando nome e os dois erros
for nome, treino, teste in modelos:
    # Lacuna: quanto o erro piora ao sair do treino para o teste
    lacuna = teste - treino
    # if: se erra muito já no treino, o modelo é simples demais (subajuste)
    if treino > 1.0:
        # Guarda o diagnóstico de subajuste
        diag = "subajuste"
    # elif (senão, se): treino bom mas lacuna grande indica que decorou
    elif lacuna > 1.0:
        # Guarda o diagnóstico de sobreajuste
        diag = "SOBREAJUSTE"
    # else: nenhum dos dois casos, então o modelo está equilibrado
    else:
        # Guarda o diagnóstico de equilíbrio
        diag = "equilibrado"
    # :7.2f mostra o número em 7 espaços com 2 casas decimais
    print(f"{nome:26s} {treino:7.2f} {teste:7.2f} {lacuna:7.2f}   {diag}")


# %% [markdown]
# O modelo D acertou tudo no treino e é o pior de todos no teste. O programa que você acabou de
# escrever detecta isso sozinho, olhando para a lacuna entre os dois erros.


# %% [markdown]
# **Sua vez**
#
# 1. Acrescente um modelo E com erro de treino 0,90 e erro de teste 0,95. Que diagnóstico ele
# recebe? Você concorda?
# 2. As regras de decisão usam os limites 1,0 para o treino e 1,0 para a lacuna. Esses números
# foram escolhidos por mim, não calculados. Mude-os e observe como o diagnóstico muda. O que isso
# mostra sobre limiares definidos por humanos?
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### 3. Descendo a montanha (*Exemplo 3 do capítulo*)


# %% [markdown]
# A descida do gradiente é o motor de quase todo o aprendizado moderno. Aqui está a versão mínima,
# com um único peso.


# %%
# Peso inicial: começamos o chute em zero
w = 0.0
# Taxa de aprendizado (eta): o tamanho de cada passo morro abaixo
eta = 0.1

# Função de custo: mede o erro; é mínima (zero) quando w vale 3
def custo(w):
    # Distância até 3, ao quadrado
    return (w - 3) ** 2

# Gradiente: a inclinação do custo no ponto w (a derivada de (w - 3) ao quadrado)
def gradiente(w):
    # Negativo quando w < 3, indicando que é preciso aumentar w
    return 2 * (w - 3)

# range(1, 6) gera os números 1, 2, 3, 4 e 5: cinco passos
for passo in range(1, 6):
    # Custo no peso atual
    J = custo(w)
    # Inclinação no peso atual
    g = gradiente(w)
    # Regra da descida do gradiente: anda no sentido contrário da inclinação
    w_novo = w - eta * g
    # Mostra os números do passo, com 4 casas decimais
    print(f"PASSO {passo}:  w={w:.4f}  J={J:.4f}  grad={g:.4f}  w_novo={w_novo:.4f}")
    # O peso novo vira o peso atual do próximo passo
    w = w_novo


# %% [markdown]
# Os cinco passos batem exatamente com o Exemplo 3 do livro. Agora rode sessenta passos e veja a
# curva de aprendizado:


# %%
# Recomeça do zero, para medir sessenta passos desde o início
w = 0.0
# Lista vazia que vai guardar o custo de cada passo
historico = []

# range(60) gera 0, 1, ..., 59: sessenta repetições
for passo in range(60):
    # append acrescenta o custo atual ao final da lista
    historico.append(custo(w))
    # Dá um passo da descida do gradiente (mesma regra da célula anterior)
    w = w - eta * gradiente(w)

# Mostra o peso final com 6 casas decimais
print(f"depois de 60 passos, w = {w:.6f}")
# Mostra o custo final com 8 casas decimais
print(f"custo final = {custo(w):.8f}")

# Importa o matplotlib (repetido aqui para a célula funcionar sozinha)
import matplotlib.pyplot as plt
# plot liga os pontos com uma linha: é a curva de aprendizado
plt.plot(historico)
# Nome do eixo horizontal
plt.xlabel("passo")
# Nome do eixo vertical
plt.ylabel("custo J")
# Título do gráfico
plt.title("A descida do gradiente")
# Liga a grade de fundo
plt.grid(True)
# Mostra o gráfico
plt.show()


# %% [markdown]
# Depois de sessenta passos o peso chegou a 2,999995, praticamente no valor exato de 3, e o custo
# caiu a quase zero. O gráfico mostra a queda rápida no começo e lenta no fim, que é o formato
# típico de toda curva de treinamento.


# %% [markdown]
# **Sua vez**
#
# 1. Troque eta para 0.01 e execute. Quantos passos seriam necessários agora?
# 2. Troque eta para 1.1 e observe o que acontece com o custo. Por que o algoritmo passa a piorar
# em vez de melhorar? Este é um dos erros mais comuns em projetos reais.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### 4. A reta que aprende com cinco alunos (*Exemplo 4 do capítulo*)


# %% [markdown]
# Este é o algoritmo supervisionado mais simples que existe. Vamos calcular a reta de mínimos
# quadrados fazendo todas as contas na tela, coluna por coluna.


# %%
# x: horas de estudo de cada aluno
horas = [1, 2, 3, 4, 5]
# y: nota de cada aluno, na mesma ordem
notas = [2, 4, 5, 4, 5]
# n: quantidade de alunos
n = len(horas)

# Média das horas
media_x = sum(horas) / n
# Média das notas
media_y = sum(notas) / n
# Mostra as duas médias
print(f"media de x = {media_x}   media de y = {media_y}")

# Acumulador da soma dos produtos (o numerador da inclinação)
numerador = 0
# Acumulador da soma dos quadrados de x - média (o denominador)
denominador = 0
# print vazio pula uma linha
print()
# Cabeçalho da tabela (os rótulos usam as médias 3 e 4 já calculadas)
print("aluno   x-3    y-4   produto   (x-3)^2")
# range(n) gera os índices 0 a 4, um para cada aluno
for i in range(n):
    # Quanto as horas do aluno i se afastam da média
    dx = horas[i] - media_x
    # Quanto a nota do aluno i se afasta da média
    dy = notas[i] - media_y
    # Produto dos dois desvios
    produto = dx * dy
    # Troca um eventual -0.0 por 0.0, para não aparecer "-0" na tabela
    if produto == 0:
        # Zero sem sinal
        produto = 0.0
    # Acumula o produto no numerador
    numerador = numerador + produto
    # Acumula o desvio de x ao quadrado no denominador
    denominador = denominador + dx * dx
    # Mostra a linha do aluno; :4.0f usa 4 espaços e nenhuma casa decimal
    print(f"  {i+1}    {dx:4.0f}   {dy:4.0f}   {produto:7.0f}   {dx*dx:7.0f}")

# Mostra as duas somas embaixo das colunas
print(f"                       soma={numerador:.0f}   soma={denominador:.0f}")

# Inclinação de mínimos quadrados: soma dos produtos dividida pela soma dos quadrados
w = numerador / denominador
# Intercepto: faz a reta passar pelo ponto das médias
b = media_y - w * media_x
# Pula uma linha
print()
# Mostra a conta da inclinação
print(f"inclinacao w = {numerador:.0f} / {denominador:.0f} = {w}")
# Mostra a conta do intercepto
print(f"intercepto b = {media_y} - {w} * {media_x} = {b}")
# Mostra a reta aprendida
print(f"reta: nota = {w} * horas + {b}")


# %% [markdown]
# A tabela e os valores 0,6 e 2,2 são exatamente os do Exemplo 4. Agora conferimos os erros de
# previsão:


# %%
# Cabeçalho da tabela de erros
print("aluno  horas  real  previsto   erro")
# Acumulador da soma dos erros ao quadrado
soma_erros2 = 0
# Percorre os cinco alunos pelo índice
for i in range(n):
    # Usa a reta aprendida para prever a nota
    previsto = w * horas[i] + b
    # Resíduo: nota real menos nota prevista
    erro = notas[i] - previsto
    # Eleva o erro ao quadrado (some o sinal) e acumula
    soma_erros2 = soma_erros2 + erro ** 2
    # Mostra a linha do aluno com 1 casa decimal
    print(f"  {i+1}      {horas[i]}     {notas[i]}    {previsto:6.1f}   {erro:6.1f}")

# Pula uma linha
print()
# Soma dos erros ao quadrado, a quantidade que a reta torna a menor possível
print(f"soma dos erros ao quadrado = {soma_erros2:.2f}")
# Erro quadrático médio: a soma dividida pelo número de alunos
print(f"erro quadratico medio      = {soma_erros2 / n:.2f}")
# Usa a reta para prever a nota de quem estudar 6 horas
print(f"previsao para 6 horas      = {w * 6 + b:.1f}")


# %% [markdown]
# **Sua vez**
#
# 1. Acrescente um sexto aluno que estudou 6 horas e tirou nota 6. Recalcule tudo. A reta ficou
# mais inclinada ou menos?
# 2. Desenhe o gráfico: use plt.scatter para os pontos reais e plt.plot para a reta prevista, no
# mesmo gráfico. Assim você enxerga os resíduos.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### 5. De uma nota para uma probabilidade (*Exemplo 5 do capítulo*)


# %% [markdown]
# Quando a pergunta é sim ou não, usamos a sigmoide, que espreme qualquer número para dentro do
# intervalo entre 0 e 1.


# %%
# Importa o math, que traz a exponencial math.exp
import math

# Sigmoide: espreme qualquer número z para o intervalo entre 0 e 1
def sigmoide(z):
    # math.exp(-z) é o número e elevado a -z
    return 1 / (1 + math.exp(-z))

# Peso do modelo: quanto cada hora de estudo soma na pontuação z
peso = 0.5
# Intercepto: ponto de partida da pontuação
intercepto = -1

# Percorre três casos: 1, 2 e 4 horas de estudo
for h in [1, 2, 4]:
    # Pontuação linear, como na reta do Exercício 4
    z = peso * h + intercepto
    # Transforma a pontuação em probabilidade
    p = sigmoide(z)
    # if em uma linha: APROVADO se p for pelo menos 0.5, senão REPROVADO
    classe = "APROVADO" if p >= 0.5 else "REPROVADO"
    # p*100 converte a probabilidade em porcentagem
    print(f"{h}h:  z = {z:5.2f}   sigmoide = {p:.4f}  ({p*100:.2f}%)  {classe}")


# %% [markdown]
# Repare no caso de 2 horas: a sigmoide devolve exatamente 0,5000, o modelo está em cima do muro.
# Esse é o ponto de fronteira de decisão.


# %% [markdown]
# **Sua vez**
#
# 1. Percorra as horas de 0 a 10 com um for e mostre a probabilidade de cada uma. A partir de
# quantas horas o modelo aprova?
# 2. Desenhe o gráfico da sigmoide para z indo de menos 6 a 6. Use uma compreensão de lista para
# gerar os valores.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### 6. Classificando pelos vizinhos (*Exemplo 6 do capítulo*)


# %% [markdown]
# O algoritmo dos k vizinhos mais próximos não treina nada. Ele guarda os exemplos e, quando chega
# um caso novo, copia a resposta da maioria dos mais próximos.


# %%
# Importa o math para usar a raiz quadrada
import math

# Base de exemplos: nome, atributo 1, atributo 2 e a classe já conhecida
base = [("A", 1, 1, "barato"),
        ("B", 2, 1, "barato"),
        ("C", 2, 2, "barato"),
        ("D", 6, 5, "caro"),
        ("E", 7, 6, "caro")]

# O imóvel novo, cuja classe queremos descobrir
novo = (3, 3)

# Lista vazia que vai guardar (nome, distância, classe) de cada imóvel
resultados = []
# Cabeçalho da tabela
print("imovel   conta                    quadrado   distancia   classe")
# Percorre a base, desempacotando os quatro campos de cada imóvel
for nome, x1, x2, classe in base:
    # Diferença no atributo 1
    d1 = novo[0] - x1
    # Diferença no atributo 2
    d2 = novo[1] - x2
    # Soma dos quadrados das diferenças
    quad = d1 ** 2 + d2 ** 2
    # Raiz quadrada: a distância euclidiana, a mesma do Exercício 1
    dist = math.sqrt(quad)
    # Guarda o resultado deste imóvel como uma tupla
    resultados.append((nome, dist, classe))
    # Monta, como texto, a conta feita (só para exibir)
    conta = f"({novo[0]}-{x1})^2+({novo[1]}-{x2})^2"
    # :22s reserva 22 espaços para o texto; :5d mostra um inteiro em 5 espaços
    print(f"  {nome}      {conta:22s}   {quad:5d}     {dist:.4f}    {classe}")

# Ordena pela distância (posição 1 de cada tupla), como na célula A5
resultados = sorted(resultados, key=lambda item: item[1])
# Pula uma linha
print()
# Título da lista ordenada
print("ordem do mais perto para o mais longe:")
# Percorre a lista já ordenada
for nome, dist, classe in resultados:
    # Mostra cada imóvel com sua distância e classe
    print(f"  {nome}  {dist:.4f}  {classe}")


# %% [markdown]
# As cinco distâncias conferem com o Exemplo 6. Agora vem a votação, e é aqui que o dicionário da
# célula A3 entra em ação:


# %%
# Função que faz a votação entre os k vizinhos mais próximos
def votar(resultados, k):
    # Fatia: como a lista já está ordenada, os k primeiros são os mais próximos
    vizinhos = resultados[:k]
    # Dicionário vazio para contar os votos de cada classe
    votos = {}
    # Percorre os vizinhos escolhidos
    for nome, dist, classe in vizinhos:
        # Se a classe já tem votos no dicionário...
        if classe in votos:
            # ...soma mais um voto
            votos[classe] = votos[classe] + 1
        # Senão, é o primeiro voto dessa classe
        else:
            # Cria a chave com um voto
            votos[classe] = 1
    # max com key escolhe a chave (classe) que tem mais votos
    vencedora = max(votos, key=lambda c: votos[c])
    # Devolve a contagem e a classe vencedora
    return votos, vencedora

# Testa três valores de k
for k in [1, 3, 5]:
    # Chama a função e desempacota os dois resultados
    votos, vencedora = votar(resultados, k)
    # upper() passa o texto para letras maiúsculas
    print(f"k = {k}:  votos = {votos}   ->   {vencedora.upper()}")


# %% [markdown]
# Note que com k igual a 5 aparecem votos das duas classes, 3 contra 2, e mesmo assim barato
# vence. Com k igual a 1, a decisão depende de um único vizinho, o que torna o modelo instável.


# %% [markdown]
# **Sua vez**
#
# 1. Classifique o ponto (5 ; 4) em vez de (3 ; 3). O resultado muda conforme o k?
# 2. Multiplique por 1000 o segundo atributo de todos os imóveis (e também o do ponto novo),
# simulando uma coluna em outra unidade, e refaça a classificação. Relacione o que acontece com o
# Exercício 1.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### 7. Qual pergunta a árvore faz primeiro (*Exemplo 7 do capítulo*)


# %% [markdown]
# Uma árvore de decisão escolhe a pergunta que mais reduz a incerteza. E incerteza se mede com a
# entropia, a mesma grandeza de Shannon vista no Capítulo 1.


# %%
# Importa o math para usar o logaritmo na base 2 (math.log2)
import math

# Entropia de Shannon de um grupo com 'sim' respostas sim e 'nao' respostas não
def entropia(sim, nao):
    # Tamanho do grupo
    total = sim + nao
    # Se só há um tipo de resposta, não existe dúvida: entropia zero
    if sim == 0 or nao == 0:
        # 0.0 com ponto decimal, para ser um número real
        return 0.0
    # Proporção de sim
    p = sim / total
    # Proporção de não
    q = nao / total
    # Fórmula da entropia em bits: menos a soma de p vezes log2 de p
    return -(p * math.log2(p) + q * math.log2(q))

# Seis dias: número do dia, choveu?, ventou?, houve jogo? (a resposta)
dias = [(1, "nao", "sim", "sim"),
        (2, "nao", "nao", "sim"),
        (3, "nao", "sim", "sim"),
        (4, "sim", "nao", "sim"),
        (5, "sim", "sim", "nao"),
        (6, "sim", "nao", "nao")]

# Conta os dias com jogo: soma 1 para cada dia cuja coluna 3 é "sim"
sim = sum(1 for d in dias if d[3] == "sim")
# Os demais dias são os sem jogo
nao = len(dias) - sim
# Incerteza antes de fazer qualquer pergunta
H_inicial = entropia(sim, nao)
# Mostra a contagem
print(f"conjunto todo: {sim} sim e {nao} nao")
# Mostra a entropia inicial em bits
print(f"entropia inicial H = {H_inicial:.4f} bits")


# %% [markdown]
# Agora a parte central: uma função que calcula o ganho de informação de qualquer atributo, e a
# aplicamos aos dois candidatos.


# %%
# Ganho de informação: quanto a pergunta sobre uma coluna reduz a incerteza
def ganho(dias, coluna):
    # Número total de dias
    total = len(dias)
    # Acumulador da entropia média depois da divisão
    H_depois = 0
    # Lista para guardar os números de cada ramo, só para exibir
    detalhes = []
    # Cada pergunta tem dois ramos: resposta "sim" e resposta "nao"
    for valor in ["sim", "nao"]:
        # Compreensão de lista com filtro: os dias que caem neste ramo
        grupo = [d for d in dias if d[coluna] == valor]
        # Se o ramo ficou vazio, não há o que medir
        if len(grupo) == 0:
            # continue pula direto para o próximo valor do laço
            continue
        # Dias com jogo neste ramo
        s = sum(1 for d in grupo if d[3] == "sim")
        # Dias sem jogo neste ramo
        nn = len(grupo) - s
        # Entropia deste ramo
        h = entropia(s, nn)
        # Soma a entropia do ramo pesada pela fração de dias que ele contém
        H_depois = H_depois + (len(grupo) / total) * h
        # Guarda os números do ramo
        detalhes.append((valor, len(grupo), s, nn, h))
    # Ganho = incerteza antes menos incerteza depois (usa H_inicial da célula anterior)
    return H_inicial - H_depois, H_depois, detalhes

# Testa os dois atributos candidatos: chuva (coluna 1) e vento (coluna 2)
for nome, coluna in [("chuva", 1), ("vento", 2)]:
    # Calcula o ganho e desempacota os três resultados
    g, hd, det = ganho(dias, coluna)
    # Título do atributo em maiúsculas
    print(f"ATRIBUTO {nome.upper()}")
    # Percorre os detalhes de cada ramo
    for valor, tam, s, nn, h in det:
        # Mostra o tamanho, a contagem e a entropia do ramo
        print(f"   {nome}={valor}: {tam} dias, {s} sim e {nn} nao, H = {h:.4f}")
    # Mostra a entropia média depois da pergunta
    print(f"   entropia media depois = {hd:.4f}")
    # Mostra a conta do ganho
    print(f"   GANHO = {H_inicial:.4f} - {hd:.4f} = {g:.4f} bits")
    # Pula uma linha entre os atributos
    print()


# %% [markdown]
# A chuva reduz a incerteza em 0,4591 bits. O vento não reduz nada. A árvore escolheria a chuva.
# Repare também no ramo em que não choveu: a entropia caiu para exatamente zero, o que significa
# que ali não sobrou dúvida alguma e o ramo vira uma folha.


# %% [markdown]
# **Sua vez**
#
# 1. Acrescente uma coluna nova aos dias, por exemplo se era fim de semana, invente os valores, e
# calcule o ganho dela. Ela seria escolhida antes da chuva?
# 2. Modifique o dia 4 para que não tenha havido jogo. Recalcule os dois ganhos. A árvore muda de
# escolha?
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### 8. Encontrando grupos sem gabarito (*Exemplo 8 do capítulo*)


# %% [markdown]
# Aqui não existe resposta certa para o algoritmo copiar. Ele precisa descobrir a estrutura
# sozinho. É o primeiro exercício de aprendizado não supervisionado da lista.


# %%
# Seis valores para agrupar, sem rótulo nenhum (aprendizado não supervisionado)
dados = [1, 2, 3, 10, 11, 12]
# Centro inicial do grupo 1
c1 = 1
# Centro inicial do grupo 2
c2 = 10

# Faz no máximo cinco iterações do k-médias
for iteracao in range(1, 6):
    # Começa a iteração com o grupo 1 vazio
    grupo1 = []
    # E o grupo 2 também vazio
    grupo2 = []
    # Mostra o número da iteração e os centros atuais
    print(f"ITERACAO {iteracao}   (c1 = {c1}, c2 = {c2})")
    # Passo 1: atribui cada valor ao centro mais próximo
    for valor in dados:
        # abs dá o valor absoluto: a distância até c1, sem sinal
        dist1 = abs(valor - c1)
        # Distância até c2
        dist2 = abs(valor - c2)
        # Se está mais perto de c1 (ou empatado), vai para o grupo 1
        if dist1 <= dist2:
            # Acrescenta o valor ao grupo 1
            grupo1.append(valor)
            # Anota o destino, só para exibir
            destino = 1
        # Senão, vai para o grupo 2
        else:
            # Acrescenta o valor ao grupo 2
            grupo2.append(valor)
            # Anota o destino
            destino = 2
        # Monta o texto da linha; :2d mostra um inteiro em 2 espaços
        linha = f"   valor {valor:2d}: ate c1 = {dist1:2.0f}, ate c2 = {dist2:2.0f}"
        # Mostra a linha com o grupo escolhido
        print(f"{linha}  -> grupo {destino}")

    # Passo 2: o novo centro do grupo 1 é a média dos seus valores
    novo_c1 = sum(grupo1) / len(grupo1)
    # O novo centro do grupo 2 é a média dos seus valores
    novo_c2 = sum(grupo2) / len(grupo2)
    # Mostra o grupo 1 e seu novo centro
    print(f"   grupo 1 = {grupo1}  novo centro = {novo_c1}")
    # Mostra o grupo 2 e seu novo centro
    print(f"   grupo 2 = {grupo2}  novo centro = {novo_c2}")

    # Se os centros não mudaram, o algoritmo convergiu (and exige as duas condições)
    if novo_c1 == c1 and novo_c2 == c2:
        # Avisa a convergência
        print("   CONVERGIU")
        # break interrompe o laço for antes das cinco iterações
        break
    # Atualiza o centro 1 para a próxima iteração
    c1 = novo_c1
    # Atualiza o centro 2
    c2 = novo_c2
    # Pula uma linha entre as iterações
    print()

# Custo J: soma das distâncias ao quadrado de cada valor até o centro do seu grupo
custo = sum((v - c1) ** 2 for v in grupo1) + sum((v - c2) ** 2 for v in grupo2)
# Mostra o custo final
print(f"custo final J = {custo}")


# %% [markdown]
# O algoritmo convergiu em duas iterações, com centros em 2 e 11, exatamente como no Exemplo 8.
# Perceba que na segunda iteração nada mudou, e é isso que significa convergir.


# %% [markdown]
# **Sua vez**
#
# 1. Troque os centros iniciais para c1 igual a 1 e c2 igual a 2, os dois no grupo da esquerda. O
# algoritmo ainda encontra a resposta certa? Em quantas iterações?
# 2. Acrescente o valor 6, que fica no meio do caminho entre os dois grupos, e execute de novo. Em
# qual grupo ele cai? Você concorda com a escolha do algoritmo?
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### 9. A acurácia que engana (*Exemplo 9 do capítulo*)


# %% [markdown]
# Este é o exercício mais importante da lista para a vida profissional. Um modelo detecta uma
# doença em 100 pacientes, dos quais 10 estão realmente doentes.


# %%
# Verdadeiros positivos: doentes que o modelo apontou como doentes
VP = 8
# Falsos negativos: doentes que o modelo deixou passar como saudáveis
FN = 2
# Falsos positivos: saudáveis que o modelo apontou como doentes (alarme falso)
FP = 5
# Verdadeiros negativos: saudáveis reconhecidos como saudáveis
VN = 85

# Título da matriz de confusão
print("MATRIZ DE CONFUSAO")
# Primeira linha do cabeçalho
print("                       o modelo disse:")
# Segunda linha do cabeçalho: as colunas são a resposta do modelo
print("                    DOENTE    SAUDAVEL")
# Linha dos realmente doentes; :2d mostra o inteiro em 2 espaços
print(f"  realmente doente     {VP:2d}        {FN:2d}")
# Linha dos realmente saudáveis
print(f"  realmente saudavel   {FP:2d}        {VN:2d}")
# Pula uma linha
print()

# Total de pacientes
total = VP + FN + FP + VN
# Acurácia: fração de todos os acertos
acuracia = (VP + VN) / total
# Precisão: dos alarmes dados, quantos eram doentes de verdade
precisao = VP / (VP + FP)
# Revocação: dos doentes de verdade, quantos o modelo encontrou
revocacao = VP / (VP + FN)
# F1: média harmônica de precisão e revocação, um resumo das duas
f1 = 2 * (precisao * revocacao) / (precisao + revocacao)

# Mostra a acurácia como fração e como porcentagem
print(f"acuracia  = ({VP} + {VN}) / {total} = {acuracia:.4f}   ou {acuracia*100:.2f}%")
# Mostra a precisão
print(f"precisao  = {VP} / ({VP} + {FP}) = {precisao:.4f}   ou {precisao*100:.2f}%")
# Mostra a revocação
print(f"revocacao = {VP} / ({VP} + {FN}) = {revocacao:.4f}   ou {revocacao*100:.2f}%")
# Mostra o F1
print(f"F1        = {f1:.4f}")


# %% [markdown]
# Uma acurácia de 93 por cento parece ótima. Mas a precisão é de apenas 61,54 por cento, ou seja,
# quatro em cada dez alarmes são falsos. Agora o golpe final: vamos construir o modelo mais burro
# possível, aquele que responde saudável para todo mundo.


# %%
# Função que calcula e mostra as métricas para qualquer matriz de confusão
def metricas(VP, FN, FP, VN, rotulo):
    # Total de pacientes
    total = VP + FN + FP + VN
    # Acurácia
    ac = (VP + VN) / total
    # Revocação; o if em uma linha evita dividir por zero quando não há doentes
    rc = VP / (VP + FN) if (VP + FN) > 0 else 0
    # A precisão só existe se o modelo apontou ao menos um doente
    if (VP + FP) > 0:
        # Já guarda a precisão formatada como texto com 4 casas
        pr = f"{VP / (VP + FP):.4f}"
    # Se nunca apontou ninguém, a conta seria zero dividido por zero
    else:
        # Por isso a precisão fica indefinida
        pr = "indefinida"
    # Mostra o nome do modelo
    print(f"{rotulo}")
    # Mostra a acurácia
    print(f"   acuracia  = {ac:.4f}")
    # Mostra a revocação
    print(f"   revocacao = {rc:.4f}")
    # Mostra a precisão (já é texto, por isso não leva formatação)
    print(f"   precisao  = {pr}")

# Métricas do modelo do exercício anterior
metricas(8, 2, 5, 85, "MODELO DE VERDADE")
# Pula uma linha
print()
# Modelo que diz "saudável" para todos: nenhum alarme, 10 doentes perdidos
metricas(0, 10, 0, 90, "CLASSIFICADOR PREGUICOSO (diz saudavel para todos)")


# %% [markdown]
# Um modelo que não faz absolutamente nada alcança 90 por cento de acurácia e encontra zero
# doentes. Guarde esta regra: acurácia sem a proporção das classes não informa nada.


# %% [markdown]
# **Sua vez**
#
# 1. Troque a doença para uma condição mais rara, com 1 doente em 100. Recalcule a acurácia do
# classificador preguiçoso. Quanto ela dá agora?
# 2. Modifique o modelo de verdade para VP igual a 10 e FP igual a 40. A revocação vira 100 por
# cento, o modelo encontra todos os doentes. Calcule a precisão e escreva em que situação real
# esse comportamento seria preferível.
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ### 10. Como a rede mede o próprio erro (*Exemplo 10 do capítulo*)


# %% [markdown]
# Quando o modelo devolve probabilidades, o erro é medido pela entropia cruzada. A regra pune de
# forma severa quem erra com confiança.


# %%
# Importa o math para usar o logaritmo natural (math.log)
import math

# Cada caso: (resposta certa, probabilidade de "1" que o modelo deu)
casos = [(1, 0.9), (1, 0.6), (0, 0.2)]

# Acumulador da soma dos custos
soma = 0
# Percorre os casos, desempacotando resposta certa e probabilidade
for y, p in casos:
    # Se a resposta certa é 1, o custo usa a probabilidade dada ao 1
    if y == 1:
        # Entropia cruzada: menos o logaritmo de p
        custo = -math.log(p)
        # Texto da conta, só para exibir
        conta = f"-ln({p})"
    # Se a resposta certa é 0, usa a probabilidade dada ao 0, que é 1 - p
    else:
        # Menos o logaritmo de 1 - p
        custo = -math.log(1 - p)
        # Texto da conta
        conta = f"-ln(1-{p})"
    # Acumula o custo do caso
    soma = soma + custo
    # Mostra o caso e o seu custo
    print(f"resposta certa = {y}, modelo disse {p}:  custo = {conta} = {custo:.4f}")

# Pula uma linha
print()
# Custo médio: a soma dividida pelo número de casos
print(f"custo medio = {soma:.4f} / {len(casos)} = {soma/len(casos):.4f}")
# Pula uma linha
print()
# Anuncia o caso de erro com muita confiança
print(f"e se errasse com confianca? y=1 e o modelo dissesse 0.01:")
# Custo enorme: o logaritmo pune quem erra com convicção
print(f"   custo = -ln(0.01) = {-math.log(0.01):.4f}")


# %% [markdown]
# Acertar com confiança custa 0,1054. Acertar com hesitação custa cinco vezes mais. E errar com
# muita confiança custa 4,6052, mais de quarenta vezes o primeiro caso. É essa assimetria que
# ensina o modelo a ser honesto sobre a própria incerteza.


# %% [markdown]
# **Sua vez**
#
# 1. Calcule o custo para uma probabilidade de 0,999 e para 0,001, ambas com resposta certa igual
# a 1. Compare os dois números.
# 2. Desenhe o gráfico do custo em função da probabilidade, para p indo de 0,01 a 0,99, com
# resposta certa igual a 1. Que formato tem a curva?
#
# Use a célula abaixo para testar, e uma célula de texto para responder.


# %%
# Espaço para os seus testes


# %% [markdown]
# ---
#
# ## Parte 3. A mesma coisa em três linhas


# %% [markdown]
# Você acabou de construir cinco algoritmos do zero. Agora vem a revelação: todos eles já existem
# prontos na biblioteca scikit-learn, que já vem instalada no Colab e é a ferramenta padrão da
# área. Os quatro desafios a seguir refazem exercícios da Parte 2 usando a biblioteca, e comparam
# os resultados.


# %% [markdown]
# > **Por que aprendemos na mão primeiro**
# >
# > Se a biblioteca faz tudo, por que gastar duas horas fazendo à mão? Porque quem só sabe chamar
# a função não percebe quando o resultado está errado. Você agora sabe que o k-NN é sensível à
# escala, que a acurácia engana em bases desbalanceadas e que a taxa de aprendizado alta demais
# faz o custo explodir. Nada disso aparece na documentação da biblioteca, e tudo isso vai aparecer
# no seu trabalho.


# %% [markdown]
# ### D1. Regressão linear com a biblioteca (*compare com o Exercício 4*)


# %%
# from ... import traz só a classe LinearRegression do scikit-learn
from sklearn.linear_model import LinearRegression
# numpy (apelido np) é a biblioteca de vetores e tabelas numéricas
import numpy as np

# np.array cria uma tabela; X tem uma coluna (horas), por isso cada item é [valor]
X = np.array([[1], [2], [3], [4], [5]])
# y: as notas, a resposta que o modelo deve aprender
y = np.array([2, 4, 5, 4, 5])

# Cria um modelo de regressão linear ainda sem treino
modelo = LinearRegression()
# fit treina: encontra a reta de mínimos quadrados, como no Exercício 4
modelo.fit(X, y)

# coef_ guarda as inclinações; [0] pega a única que existe
print(f"inclinacao encontrada pela biblioteca: {modelo.coef_[0]:.4f}")
# intercept_ guarda o intercepto b
print(f"intercepto encontrado pela biblioteca: {modelo.intercept_:.4f}")
# Pula uma linha
print()
# Lembra os valores obtidos à mão
print("no Exercicio 4, na mao, encontramos: 0.6 e 2.2")
# predict prevê a nota para 6 horas; [0] pega o único valor previsto
print(f"previsao para 6 horas: {modelo.predict([[6]])[0]:.4f}")


# %% [markdown]
# Os mesmos 0,6 e 2,2 que você calculou coluna por coluna no Exercício 4, obtidos aqui em duas
# linhas de código. A biblioteca resolve o mesmo problema matemático, apenas mais rápido e com
# mais casos tratados.


# %% [markdown]
# ### D2. Vizinhos mais próximos com a biblioteca (*compare com o Exercício 6*)


# %%
# Importa o classificador de k vizinhos mais próximos do scikit-learn
from sklearn.neighbors import KNeighborsClassifier

# Os mesmos cinco imóveis do Exercício 6, só com os dois atributos
X = [[1, 1], [2, 1], [2, 2], [6, 5], [7, 6]]
# As classes de cada imóvel, na mesma ordem
y = ["barato", "barato", "barato", "caro", "caro"]

# Testa os mesmos três valores de k
for k in [1, 3, 5]:
    # n_neighbors diz quantos vizinhos votam
    modelo = KNeighborsClassifier(n_neighbors=k)
    # fit, no k-NN, apenas guarda os exemplos
    modelo.fit(X, y)
    # Classifica o ponto (3, 3); [0] pega a única resposta
    resposta = modelo.predict([[3, 3]])[0]
    # Mostra a resposta em maiúsculas
    print(f"k = {k}:  a biblioteca respondeu {resposta.upper()}")


# %% [markdown]
# As três respostas coincidem com a sua votação manual do Exercício 6.


# %% [markdown]
# ### D3. Métricas de avaliação com a biblioteca (*compare com o Exercício 9*)


# %%
# Importa a matriz de confusão e a acurácia do scikit-learn
from sklearn.metrics import confusion_matrix, accuracy_score
# Importa precisão, revocação e F1
from sklearn.metrics import precision_score, recall_score, f1_score

# 1 significa doente, 0 significa saudável
# [1]*10 repete o 1 dez vezes; o + junta listas: 10 doentes e 90 saudáveis
real     = [1]*10 + [0]*90
# Respostas do modelo, na mesma ordem: 8 VP, 2 FN, 5 FP e 85 VN
previsto = [1]*8 + [0]*2 + [1]*5 + [0]*85

# Avisa a orientação da matriz que vem a seguir
print("matriz de confusao (linhas = real, colunas = previsto):")
# Calcula e mostra a matriz (a classe 0 vem primeiro)
print(confusion_matrix(real, previsto))
# Pula uma linha
print()
# Acurácia calculada pela biblioteca
print(f"acuracia  = {accuracy_score(real, previsto):.4f}")
# Precisão calculada pela biblioteca
print(f"precisao  = {precision_score(real, previsto):.4f}")
# Revocação calculada pela biblioteca
print(f"revocacao = {recall_score(real, previsto):.4f}")
# F1 calculado pela biblioteca
print(f"F1        = {f1_score(real, previsto):.4f}")


# %% [markdown]
# Os quatro números batem até a quarta casa decimal com o Exercício 9. Atenção a um detalhe que
# confunde muita gente: na matriz que a biblioteca imprime, a ordem das linhas e colunas é a
# classe 0 primeiro e a classe 1 depois, ao contrário da tabela que montamos no livro. Sempre
# confira a orientação da matriz antes de ler os números.


# %% [markdown]
# ### D4. Agrupamento com a biblioteca (*compare com o Exercício 8*)


# %%
# Importa o algoritmo k-médias (KMeans) do scikit-learn
from sklearn.cluster import KMeans
# Importa o numpy
import numpy as np

# Os mesmos seis valores do Exercício 8, cada um como uma linha de uma coluna
X = np.array([[1], [2], [3], [10], [11], [12]])

# Dois grupos; n_init=10 tenta 10 inícios; random_state fixa o sorteio
modelo = KMeans(n_clusters=2, n_init=10, random_state=0)
# Treina: encontra os grupos e os centros
modelo.fit(X)

# labels_ diz o número do grupo de cada ponto (a numeração 0 ou 1 é arbitrária)
print("grupo de cada ponto:", modelo.labels_)
# Pega a coordenada de cada centro e ordena, para mostrar do menor ao maior
centros = sorted(c[0] for c in modelo.cluster_centers_)
# Mostra os dois centros com 1 casa decimal
print(f"centros encontrados: {centros[0]:.1f} e {centros[1]:.1f}")
# Lembra os centros obtidos à mão
print("no Exercicio 8, na mao, encontramos: 2 e 11")


# %% [markdown]
# Centros em 2 e 11, exatamente como na sua conta manual. O parâmetro random_state fixa o sorteio
# inicial, garantindo que o resultado seja o mesmo toda vez que você executar.


# %% [markdown]
# ### Um último desafio, sem código pronto


# %% [markdown]
# Escolha um dos exercícios da Parte 2 que ainda não foi refeito com biblioteca, por exemplo a
# árvore de decisão do Exercício 7, e descubra sozinho como fazê-lo com o scikit-learn. Uma dica:
# a classe se chama DecisionTreeClassifier e fica dentro de sklearn.tree. Compare o atributo que a
# biblioteca escolheu para a primeira divisão com o que você calculou à mão. Escreva a comparação
# em uma célula de texto.


# %% [markdown]
# ---
#
# ## Anexo A. Erros mais comuns nesta lista


# %% [markdown]
# Esta lista tem duas armadilhas novas em relação à do Capítulo 1: as células dependem umas das
# outras, e agora usamos bibliotecas externas. A tabela abaixo cobre as duas.


# %% [markdown]
# **Tabela A.1. O que fazer quando dá erro**
#
# | A mensagem diz | Causa provável | Como resolver |
# | --- | --- | --- |
# | NameError: name 'distancia' is not defined | Você executou uma célula sem ter executado antes
# a que cria a função. | Volte e execute as células na ordem. Nesta lista, várias delas criam
# variáveis e funções usadas pelas seguintes. |
# | ModuleNotFoundError | Erro de grafia no nome da biblioteca. | Confira: é sklearn, tudo
# minúsculo, e não scikit-learn nem SKLearn. O nome do pacote e o nome de importação são
# diferentes. |
# | IndexError: list index out of range | Você pediu uma posição que não existe na lista. | Lembre
# que a contagem começa em zero. Em uma lista de 5 itens, as posições válidas vão de 0 a 4. |
# | KeyError | Você pediu uma chave que não existe no dicionário. | Confira a grafia exata da
# chave, incluindo maiúsculas e acentos. |
# | ValueError ao chamar fit | O formato dos dados não é o que a biblioteca espera. | O
# scikit-learn espera X como lista de listas, mesmo quando há uma única coluna. Repare que
# escrevemos [[1], [2], [3]] e não [1, 2, 3]. |
# | IndentationError | O recuo das linhas está errado. | Linhas dentro de if, for ou def precisam
# de quatro espaços, e todas alinhadas entre si. |
# | O gráfico não aparece | Faltou o comando final. | Toda sequência de matplotlib termina com
# plt.show(). |


# %% [markdown]
# > **A regra de ouro quando nada funciona**
# >
# > No menu Ambiente de execução, escolha Reiniciar sessão e executar tudo. Isso limpa a memória e
# roda todas as células na ordem, do começo ao fim. Resolve a maioria dos problemas causados por
# células executadas fora de ordem, que é o erro mais frequente nesta lista específica.


# %% [markdown]
# ---
#
# ## Anexo B. Entrega e avaliação


# %% [markdown]
# ### Como entregar


# %% [markdown]
# 1. Antes de tudo, use Ambiente de execução e depois Reiniciar sessão e executar tudo, e espere
# terminar. O caderno precisa ser entregue com todas as saídas visíveis.
# 2. Clique em Compartilhar, no canto superior direito.
# 3. Em Acesso geral, escolha a opção que permite a qualquer pessoa com o link visualizar.
# 4. Copie o link e cole no espaço indicado pelo professor, junto com seu nome e sua turma.


# %% [markdown]
# ### Critérios de avaliação


# %% [markdown]
# **Tabela B.1. Distribuição dos pontos**
#
# | O que será avaliado | Pontos |
# | --- | --- |
# | Parte 1 completa, com as sete células executadas e sem erro | 1,5 |
# | Exercícios 1 a 5 executados, com saídas idênticas às esperadas | 2,0 |
# | Exercícios 6 a 10 executados, com saídas idênticas às esperadas | 2,0 |
# | Blocos Sua vez respondidos em células de texto, com explicação escrita | 2,5 |
# | Parte 3 executada, com os quatro desafios comparados aos resultados manuais | 1,0 |
# | Organização do caderno: títulos, comentários no código e nome de arquivo correto | 1,0 |
# | Desafio final da Parte 3, a árvore de decisão com biblioteca (ponto extra) | até 1,0 |


# %% [markdown]
# **Uma observação final**


# %% [markdown]
# Ao terminar esta lista, você terá construído do zero, com as próprias mãos, os algoritmos que
# sustentam a maior parte dos sistemas de aprendizado de máquina em uso hoje nas empresas. Não os
# mais famosos, e sim os mais usados, que raramente são a mesma coisa. E terá visto que a
# biblioteca profissional chega exatamente aos mesmos números. A diferença entre você e alguém que
# só sabe chamar a função é que você sabe o que perguntar quando o resultado parecer estranho.
