# -*- coding: utf-8 -*-
"""
A ginga dos números: livro de exercícios
Lista 3: Três algoritmos por dentro

Versão em script do caderno cap03_tres_algoritmos.ipynb, com o mesmo código e os mesmos comentários.
Autor: Bruno Menezes  |  https://brunoleomenezes.github.io/
Repositório: https://github.com/brunoleomenezes/ginga-dos-numeros

Como usar: o mais simples é abrir o caderno .ipynb no Google Colab. Este arquivo serve para quem
prefere rodar no próprio computador (python cap03_tres_algoritmos.py) ou ler o código em um editor. Os blocos
marcados com "# %%" são as células do caderno, na mesma ordem; os textos explicativos aparecem
como comentários. Para ver o resultado de cada bloco, rode o arquivo inteiro: os gráficos abrem
em janelas próprias.
"""



# %% [markdown]
# ## Parte 1. Sete ferramentas novas de Python


# %% [markdown]
# ### B1. Percorrer duas listas ao mesmo tempo
#
# Nos exercícios deste capítulo, quase sempre temos duas listas que andam juntas: os nomes e os
# valores, os pedidos e os preços. O comando **enumerate** entrega a posição de cada item junto
# com o item, e o comando **zip** costura duas listas e entrega um par de cada vez.


# %%
# Cria uma lista (vários valores entre colchetes, em ordem) com três nomes
nomes = ["Ana", "Bruno", "Carla"]
# Cria outra lista com as notas, na mesma ordem dos nomes
notas = [2, 4, 5]

# Laço for: repete o bloco recuado para cada item; enumerate entrega (posição, item)
for i, nome in enumerate(nomes):
    # print mostra na tela a posição e o nome da volta atual
    print(i, nome)

# Mostra uma linha de separação entre as duas partes da saída
print("---")

# zip costura as duas listas e entrega um par (nome, nota) a cada volta
for nome, nota in zip(nomes, notas):
    # Mostra o nome, o texto "tirou" e a nota correspondente
    print(nome, "tirou", nota)


# %% [markdown]
# O enumerate começa a contar em zero, como as listas. O zip para quando a lista mais curta acaba.


# %% [markdown]
# **SUA VEZ**
#
# 1. Acrescente uma quarta pessoa às duas listas e execute de novo.
# 2. Use zip com três listas ao mesmo tempo: nomes, notas e uma lista de turmas que você inventar.
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ### B2. Repetir até uma condição ser verdadeira
#
# O **for** repete um número de vezes que você já sabe. O **while** repete enquanto uma condição
# for verdadeira, e é exatamente o que precisamos para algoritmos que param quando nada mais muda,
# como o K-means.


# %%
# Valor inicial que vamos dividir ao meio várias vezes
valor = 100
# Contador de passos, começa em zero
passos = 0

# Laço while: repete o bloco enquanto a condição valor > 1 for verdadeira
while valor > 1:
    # Divide o valor por 2 e guarda o resultado na mesma variável
    valor = valor / 2
    # Soma 1 ao contador a cada volta do laço
    passos = passos + 1

# Fora do laço (sem recuo): mostra quantos passos foram dados e onde o valor parou
print("passos:", passos, "valor final:", valor)


# %% [markdown]
# Cuidado: se a condição nunca ficar falsa, o while roda para sempre. Se isso acontecer, use o
# botão de parar à esquerda da célula no Colab.


# %% [markdown]
# **SUA VEZ**
#
# 1. Troque a condição para valor > 10 e veja quantos passos são necessários.
# 2. Crie um while que conte de 1 até 5 e mostre cada número.
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ### B3. Descobrir qual item é o menor
#
# No K-means, cada ponto precisa descobrir **qual centro está mais perto**. Para isso usamos
# **min** com a opção **key**, aplicada sobre as posições da lista. Ela devolve a posição do menor
# valor, e não o valor em si.


# %%
# Distâncias de um ponto até três centros (como no K-means)
distancias = [0.9055, 1.0012, 0.9220]

# range(3) gera as posições 0, 1 e 2; min com key escolhe a posição de menor distância.
# lambda é uma função curta sem nome: recebe j e devolve distancias[j]
mais_perto = min(range(3), key=lambda j: distancias[j])

# Mostra a posição escolhida (não o valor)
print("posição do menor:", mais_perto)
# Usa a posição entre colchetes para buscar o valor na lista (indexação)
print("menor valor:", distancias[mais_perto])


# %% [markdown]
# Leia assim: entre as posições 0, 1 e 2, escolha a que tem o menor distancias[j]. Como a contagem
# começa em zero, a posição 0 corresponde ao primeiro centro.


# %% [markdown]
# **SUA VEZ**
#
# 1. Troque a lista por [3.2, 1.1, 2.5, 0.7] e mude range(3) para range(4).
# 2. Use max no lugar de min e diga com suas palavras o que mudou.
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ### B4. Listas dentro de listas: montar os grupos
#
# Um grupo de pontos é uma lista, e vários grupos são uma lista de listas. O comando **append**
# acrescenta um item ao fim de uma lista, e **sum** dividido por **len** dá a média do grupo, que
# é a posição do novo centro.


# %%
# Seis pontos numa reta: três pequenos e três grandes
pontos = [1, 2, 3, 10, 11, 12]
# Lista de listas: dois grupos, cada um começando vazio
grupos = [[], []]

# Percorre cada ponto da lista
for p in pontos:
    # Expressão condicional (if ... else numa linha): grupo 0 se p < 6, senão grupo 1
    j = 0 if p < 6 else 1
    # append acrescenta o ponto ao fim da lista do grupo j
    grupos[j].append(p)

# Mostra os dois grupos montados
print(grupos)
# Compreensão de lista: calcula sum/len (a média) de cada grupo; é o novo centro no K-means
print("médias:", [sum(g) / len(g) for g in grupos])


# %% [markdown]
# A linha j = 0 if p < 6 else 1 significa: j vale 0 quando p é menor que 6, e vale 1 caso
# contrário.


# %% [markdown]
# **SUA VEZ**
#
# 1. Acrescente o ponto 6 à lista de pontos. Em qual grupo ele cai?
# 2. Mude para três grupos: separe em menores que 5, entre 5 e 10, e maiores que 10.
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ### B5. Copiar e comparar listas
#
# Para saber se o K-means terminou, comparamos a lista de grupos desta rodada com a da rodada
# anterior. Duas listas são iguais quando têm os mesmos itens na mesma ordem, e o sinal **==** faz
# essa comparação. Para guardar uma lista antiga, é preciso fazer uma **cópia** com **.copy()**.


# %%
# Lista com os grupos de uma rodada anterior
antes = [0, 0, 1]
# .copy() cria uma lista nova e independente, com os mesmos itens
agora = antes.copy()

# == compara item a item; mostra True porque as listas são iguais
print(agora == antes)

# Troca o item da posição 2 (o terceiro) só na cópia
agora[2] = 2
# Agora as listas diferem, então mostra False
print(agora == antes)
# Mostra as duas: a original continua intacta graças ao .copy()
print(antes, agora)


# %% [markdown]
# Sem o .copy(), as duas variáveis apontariam para a mesma lista, e mudar uma mudaria a outra. É
# um dos erros mais comuns de quem começa.


# %% [markdown]
# **SUA VEZ**
#
# 1. Refaça a célula trocando agora = antes.copy() por agora = antes. Execute e explique, por
# escrito, o que mudou no resultado.
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ### B6. Contas com colunas inteiras: NumPy
#
# Na regressão, fazemos a mesma conta para oito atendimentos de uma vez. A biblioteca **NumPy**,
# já instalada no Colab, guarda uma coluna de números em um **array** e deixa fazer contas com a
# coluna inteira, sem precisar de um for.


# %%
# import carrega a biblioteca NumPy e lhe dá o apelido np
import numpy as np

# np.array transforma a lista em um array, que aceita contas com a coluna inteira
x = np.array([2, 3, 5, 6, 8, 9, 11, 12])
# Segunda coluna: os minutos de cada atendimento
y = np.array([20, 20, 32, 31, 43, 46, 52, 60])

# .mean() calcula a média de cada array
print(x.mean(), y.mean())
# Subtrai a média de cada número e multiplica as colunas item a item, sem laço for
print((x - x.mean()) * (y - y.mean()))
# ** 2 eleva ao quadrado cada item; np.sum soma tudo (a soma dos desvios ao quadrado)
print(np.sum((x - x.mean()) ** 2))
# np.exp aplica a exponencial: aqui, e elevado a -1
print(np.exp(-1))


# %% [markdown]
# Repare que x - x.mean() subtraiu a média de cada um dos oito números de uma vez. Essa é a
# vantagem do array em relação à lista comum.


# %% [markdown]
# **SUA VEZ**
#
# 1. Calcule a soma dos valores de y com np.sum.
# 2. Calcule o maior valor de x com x.max() e o menor com x.min().
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ### B7. Gráficos com cores e escala logarítmica
#
# Para mostrar grupos, desenhamos cada grupo com uma cor. Para mostrar uma curva que cai muito (ou
# explode), usamos a escala logarítmica no eixo vertical, que dá o mesmo espaço para cada
# multiplicação por 10.


# %%
# Carrega a parte de gráficos do matplotlib com o apelido plt
import matplotlib.pyplot as plt

# scatter desenha pontos soltos (x, y); c escolhe a cor e label dá o nome na legenda
plt.scatter([1, 2, 3], [1, 3, 2], c="blue", label="grupo 1")
# Segundo grupo, desenhado em laranja no mesmo gráfico
plt.scatter([10, 11, 12], [9, 11, 10], c="orange", label="grupo 2")
# Mostra a legenda com os nomes dados em label
plt.legend()
# Desenha o primeiro gráfico abaixo da célula
plt.show()

# plot liga os valores com uma linha; cada valor é 10 vezes o anterior
plt.plot([1, 10, 100, 1000, 10000])
# Escala logarítmica no eixo vertical: cada multiplicação por 10 ocupa o mesmo espaço
plt.yscale("log")
# Desenha o segundo gráfico
plt.show()


# %% [markdown]
# A saída aqui são dois gráficos, desenhados logo abaixo da célula. No segundo, os pontos formam
# uma reta porque a escala vertical é logarítmica.


# %% [markdown]
# **SUA VEZ**
#
# 1. Acrescente um terceiro grupo com outra cor.
# 2. Tire a linha plt.yscale("log") e compare os dois gráficos da curva.
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ## Parte 2. Os dez exercícios do capítulo


# %% [markdown]
# ### Exercício 1. Por que a escala dos números importa
# *Exemplo 1 do capítulo*
#
# Queremos saber quem se parece mais com a Ana: o Diego, que compra pouco e gasta pouco como ela,
# ou a Elis, que faz oito vezes mais pedidos. Primeiro vamos ver o que o computador acha com os
# números crus.


# %%
# Carrega o módulo math, que traz funções matemáticas como a raiz quadrada
import math

# def cria uma função chamada distancia, que recebe dois pontos a e b
def distancia(a, b):
    # Acumulador da soma, começa em zero
    soma = 0
    # Percorre as posições de cada coordenada (len dá o tamanho do ponto)
    for i in range(len(a)):
        # Soma o quadrado da diferença em cada coordenada
        soma = soma + (a[i] - b[i]) ** 2
    # return devolve o resultado: a raiz da soma é a distância euclidiana
    return math.sqrt(soma)

# Tupla (valores entre parênteses): (pedidos, ticket em reais) da Ana
ana = (2, 90)
# Diego: compra pouco e gasta pouco, parecido com a Ana
diego = (6, 110)
# Elis: oito vezes mais pedidos que a Ana, mesmo ticket
elis = (16, 90)

# Título da saída
print("SEM NORMALIZAR")
# f-string (f antes das aspas) encaixa o valor entre chaves; :.4f mostra 4 casas decimais
print(f"  d(Ana, Diego) = {distancia(ana, diego):.4f}")
# Mesma conta para Ana e Elis: os reais dominam e a Elis parece mais perto
print(f"  d(Ana, Elis)  = {distancia(ana, elis):.4f}")


# %% [markdown]
# A conta diz que a Ana está mais perto da Elis do que do Diego, o que é falso para o negócio. Os
# reais esmagaram a contagem de pedidos. Agora vamos normalizar a base inteira, com os doze
# clientes:


# %%
# Lista com os doze clientes; a lista continua na linha de baixo até fechar o colchete
nomes = ["Ana", "Bruno", "Carla", "Diego", "Elis", "Fábio",
         "Gina", "Hugo", "Iara", "João", "Kelly", "Lucas"]
# Número de pedidos de cada cliente, na mesma ordem dos nomes
pedidos = [2, 4, 2, 6, 16, 18, 20, 22, 4, 6, 2, 8]
# Ticket médio de cada cliente, em reais
ticket = [90, 130, 150, 110, 90, 130, 50, 110, 390, 450, 410, 430]

# Função que aplica a normalização min-max a uma coluna de números
def normalizar(coluna):
    # min encontra o menor valor da coluna
    menor = min(coluna)
    # max encontra o maior valor da coluna
    maior = max(coluna)
    # Leva cada valor para a faixa de 0 a 1: o menor vira 0 e o maior vira 1
    return [(v - menor) / (maior - menor) for v in coluna]

# Pedidos normalizados (eixo x)
x = normalizar(pedidos)
# Tickets normalizados (eixo y)
y = normalizar(ticket)
# Junta x e y em pares (x, y); list transforma o resultado do zip em lista
pontos = list(zip(x, y))

# Percorre nomes e pontos ao mesmo tempo
for nome, p in zip(nomes, pontos):
    # :6s reserva 6 espaços para o nome; p[0] e p[1] são as duas coordenadas do ponto
    print(f"{nome:6s} ({p[0]:.2f} ; {p[1]:.2f})")

# print vazio pula uma linha
print()
# Título da segunda parte
print("DEPOIS DE NORMALIZAR")
# Ana está na posição 0 e Diego na 3; agora a distância respeita o bom senso
print(f"  d(Ana, Diego) = {distancia(pontos[0], pontos[3]):.4f}")
# Elis está na posição 4 e agora fica bem mais longe da Ana
print(f"  d(Ana, Elis)  = {distancia(pontos[0], pontos[4]):.4f}")


# %% [markdown]
# Agora o Diego está bem mais perto da Ana do que a Elis, quase três vezes e meia mais perto. A
# conta concorda com o bom senso. Guarde a lista pontos: ela será usada em quase todos os
# exercícios seguintes.


# %% [markdown]
# **SUA VEZ**
#
# 1. Troque o ticket do Diego de 110 para 1000 e refaça a primeira célula. O problema de escala
# aparece de novo? Por quê?
# 2. Acrescente um décimo terceiro cliente com 100 pedidos e ticket 100. O que acontece com os
# valores normalizados dos outros doze? Escreva por que o min-max é sensível a valores extremos.
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ### Exercício 2. Uma rodada completa de K-means
# *Exemplo 2 do capítulo*
#
# Vamos calcular, uma a uma, as 36 distâncias da primeira rodada, partindo dos centros Gina, Hugo
# e João. Depois transformamos tudo em uma função e deixamos o algoritmo rodar até convergir.


# %%
# Centros iniciais do K-means: os pontos da Gina, do Hugo e do João
centros = [pontos[6], pontos[7], pontos[9]]   # Gina, Hugo, João

# Cabeçalho da tabela
print("cliente  posição        dist C1  dist C2  dist C3  grupo")
# Para cada cliente, faz o Passo A do K-means
for nome, p in zip(nomes, pontos):
    # Compreensão de lista: as três distâncias do ponto até cada centro
    d = [distancia(p, c) for c in centros]
    # Escolhe a posição (0, 1 ou 2) do centro mais perto
    j = min(range(3), key=lambda k: d[k])
    # end="   " troca a quebra de linha por espaços, e a linha continua no próximo print
    print(f"{nome:6s}  ({p[0]:.2f} ; {p[1]:.2f})", end="   ")
    # Completa a linha com as distâncias e o grupo; j + 1 porque os grupos são G1, G2, G3
    print(f"{d[0]:.4f}   {d[1]:.4f}   {d[2]:.4f}   G{j + 1}")


# %% [markdown]
# Cada linha é o Passo A para um cliente: três distâncias e a escolha da menor. Agora o algoritmo
# completo, com as duas contas alternadas até ninguém mudar de grupo:


# %%
# Passo A: atribui cada ponto ao centro mais próximo e mede a inércia
def atribuir(pontos, centros):
    # Lista que vai guardar o número do grupo de cada ponto
    grupos = []
    # Inércia: soma das distâncias ao quadrado de cada ponto até o seu centro
    inercia = 0
    # Percorre todos os pontos
    for p in pontos:
        # Distância ao quadrado do ponto até cada centro
        quadrados = [distancia(p, c) ** 2 for c in centros]
        # Posição do centro com a menor distância ao quadrado
        j = min(range(len(centros)), key=lambda k: quadrados[k])
        # Anota o grupo deste ponto
        grupos.append(j)
        # Soma a parcela deste ponto na inércia
        inercia = inercia + quadrados[j]
    # Uma função pode devolver dois valores de uma vez (sai como uma tupla)
    return grupos, inercia

# Passo B: move cada centro para a média dos pontos do seu grupo
def mover(pontos, grupos, k):
    # Lista dos novos centros
    novos = []
    # Repete para cada um dos k grupos
    for j in range(k):
        # Compreensão de lista com if: só os pontos cujo grupo g é igual a j
        membros = [p for p, g in zip(pontos, grupos) if g == j]
        # Média das coordenadas x dos membros (soma dividida pela quantidade)
        mx = sum(m[0] for m in membros) / len(membros)
        # Média das coordenadas y dos membros
        my = sum(m[1] for m in membros) / len(membros)
        # O novo centro é o par de médias
        novos.append((mx, my))
    # Devolve a lista com os k novos centros
    return novos

# O K-means completo; mostrar=True é um valor padrão, usado se ninguém informar outro
def kmeans(pontos, centros, mostrar=True):
    # None significa "nada ainda": não há rodada anterior para comparar
    anterior = None
    # Contador de rodadas
    rodada = 0
    # while True repete para sempre; quem interrompe é o break lá embaixo
    while True:
        # Mais uma rodada
        rodada = rodada + 1
        # Passo A; os dois valores devolvidos vão para duas variáveis de uma vez
        grupos, inercia = atribuir(pontos, centros)
        # .count(j) conta quantos pontos caíram no grupo j
        tamanhos = [grupos.count(j) for j in range(len(centros))]
        # if executa o bloco só se a condição for verdadeira
        if mostrar:
            # Mostra o andamento da rodada
            print(f"rodada {rodada}  inércia = {inercia:.4f}  grupos de {tamanhos}")
        # Se ninguém mudou de grupo em relação à rodada anterior, o algoritmo convergiu
        if grupos == anterior:
            # Avisa que terminou
            print("CONVERGIU")
            # break sai do laço while imediatamente
            break
        # Guarda uma cópia dos grupos para comparar na próxima rodada
        anterior = grupos.copy()
        # Passo B: recalcula os centros a partir dos grupos
        centros = mover(pontos, grupos, len(centros))
    # Devolve os grupos finais, os centros finais e a inércia final
    return grupos, centros, inercia

# Roda o K-means partindo de Gina, Hugo e João e guarda os três resultados
grupos_bom, centros_bom, inercia_bom = kmeans(pontos, [pontos[6], pontos[7], pontos[9]])


# %% [markdown]
# A inércia cai a cada rodada e o algoritmo para quando a lista de grupos se repete. Agora
# traduzimos os centros de volta para pedidos e reais:


# %%
# Para cada centro final, com sua posição j
for j, c in enumerate(centros_bom):
    # Nomes dos clientes do grupo j (range(12) percorre as posições dos 12 clientes)
    membros = [nomes[i] for i in range(12) if grupos_bom[i] == j]
    # Desfaz a normalização: pedidos iam de 2 a 22 (faixa de 20)
    ped = 2 + c[0] * 20
    # Desfaz a normalização do ticket: ia de 50 a 450 (faixa de 400)
    tic = 50 + c[1] * 400
    # ', '.join junta os nomes em um só texto, separados por vírgula
    print(f"G{j + 1}: {', '.join(membros)}")
    # Mostra o centro em pedidos e reais; :.0f arredonda sem casas decimais
    print(f"    centro em pedidos e reais: {ped:.1f} pedidos, R$ {tic:.0f}")


# %% [markdown]
# A máquina devolveu três listas de clientes. Quem dá os nomes "ocasional", "de rotina" e
# "premium" é você.


# %% [markdown]
# **SUA VEZ**
#
# 1. Troque os centros iniciais para Ana, Hugo e Iara (posições 0, 7 e 8). O algoritmo chega aos
# mesmos grupos? Em quantas rodadas?
# 2. Calcule à mão, com a calculadora do celular, a distância da Elis até o centro C2 da rodada 1
# e confira com a saída da primeira célula.
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ### Exercício 3. O mesmo algoritmo com um chute pior
# *Exemplo 3 do capítulo*
#
# O K-means depende do sorteio inicial. Vamos rodar exatamente o mesmo código, com a mesma base,
# mas partindo de outros três clientes.


# %%
# Mesmo K-means, mas partindo de Ana, Iara e João (um chute pior)
grupos_ruim, centros_ruim, inercia_ruim = kmeans(pontos, [pontos[0], pontos[8], pontos[9]])

# Pula uma linha
print()
# Percorre os três grupos
for j in range(3):
    # Nomes dos clientes que ficaram no grupo j
    membros = [nomes[i] for i in range(12) if grupos_ruim[i] == j]
    # Mostra o grupo, o tamanho (len) e os nomes
    print(f"G{j + 1} ({len(membros)}): {', '.join(membros)}")

# Pula uma linha
print()
# Inércia da execução do Exercício 2
print(f"inércia da execução boa  = {inercia_bom:.4f}")
# Inércia desta execução: maior quer dizer grupos menos compactos
print(f"inércia da execução ruim = {inercia_ruim:.4f}")
# Divide uma pela outra para dizer quantas vezes a ruim é pior
print(f"a ruim é {inercia_ruim / inercia_bom:.2f} vezes pior")


# %% [markdown]
# Oito clientes diferentes foram espremidos em um grupo só, e o algoritmo considerou isso
# terminado. Ele não tem como saber que existe algo melhor. É uma falha silenciosa.


# %% [markdown]
# **SUA VEZ**
#
# 1. Escolha três clientes de partida à sua escolha e rode o algoritmo. Anote a inércia final.
# Você conseguiu encontrar um chute que dá resultado ainda pior do que 1.3334?
# 2. Escreva, com suas palavras, a defesa que se usa na prática contra esse problema, citando o
# k-means++ e o parâmetro n_init.
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ### Exercício 4. A reta que aprende com oito atendimentos
# *Exemplo 4 do capítulo*
#
# Agora existe uma coluna de resposta: os minutos foram cronometrados. Vamos calcular a reta de
# mínimos quadrados fazendo todas as contas na tela, coluna por coluna.


# %%
# Importa math de novo (já veio no Exercício 1; repetir não causa problema)
import math

# Nomes dos oito clientes atendidos
clientes = ["Alice", "Breno", "Célia", "Davi", "Eva", "Felipe", "Gabi", "Heitor"]
# x: quantos documentos cada cliente trouxe
docs = [2, 3, 5, 6, 8, 9, 11, 12]
# y: quantos minutos durou cada atendimento (a resposta cronometrada)
mins = [20, 20, 32, 31, 43, 46, 52, 60]
# n é o número de atendimentos
n = len(docs)

# Média dos documentos
media_x = sum(docs) / n
# Média dos minutos
media_y = sum(mins) / n
# Mostra as duas médias
print(f"média de x = {media_x}   média de y = {media_y}")
# Pula uma linha
print()

# Acumulador da soma dos produtos dos desvios (Sxy)
sxy = 0
# Acumulador da soma dos desvios de x ao quadrado (Sxx)
sxx = 0
# Cabeçalho da tabela (o 7 e o 38 são as médias calculadas acima)
print("cliente     x    y   x-7  y-38  produto  (x-7)^2")
# Percorre as três listas juntas: nome, documentos e minutos
for nome, x, y in zip(clientes, docs, mins):
    # Desvio de x: quanto este cliente está acima ou abaixo da média
    dx = x - media_x
    # Desvio de y em relação à média dos minutos
    dy = y - media_y
    # Acumula o produto dos desvios
    sxy = sxy + dx * dy
    # Acumula o desvio de x ao quadrado
    sxx = sxx + dx * dx
    # :4d reserva 4 espaços para um inteiro; :5.0f mostra o número sem casas decimais
    print(f"{nome:8s} {x:4d} {y:4d} {dx:5.0f} {dy:5.0f} {dx * dy:8.0f} {dx * dx:8.0f}")
# {'':32s} encaixa um texto vazio ocupando 32 espaços, para alinhar as somas
print(f"somas{'':32s}{sxy:5.0f} {sxx:8.0f}")

# Inclinação da reta de mínimos quadrados: Sxy dividido por Sxx
b = sxy / sxx
# Intercepto: a reta passa pelo ponto das médias
a = media_y - b * media_x
# Pula uma linha
print()
# Mostra a conta da inclinação
print(f"inclinação b = {sxy:.0f} / {sxx:.0f} = {b}")
# Mostra a conta do intercepto
print(f"intercepto a = {media_y} - {b} * {media_x} = {a}")
# Mostra a reta final
print(f"reta: minutos = {a} + {b} * documentos")


# %% [markdown]
# A tabela e os valores 4 e 10 são exatamente os do Exemplo 4. Agora conferimos o erro de cada
# previsão e avaliamos o modelo:


# %%
# Cabeçalho da tabela de previsões
print("cliente   docs  real  previsto  resíduo")
# Soma dos erros ao quadrado (SSE), começa em zero
sse = 0
# Percorre cada atendimento
for nome, x, y in zip(clientes, docs, mins):
    # Valor que a reta prevê para este número de documentos
    previsto = a + b * x
    # Resíduo: o real menos o previsto (o erro da reta neste caso)
    residuo = y - previsto
    # Acumula o resíduo ao quadrado
    sse = sse + residuo ** 2
    # Mostra a linha da tabela
    print(f"{nome:8s} {x:5d} {y:5d} {previsto:9.1f} {residuo:8.1f}")

# SST: soma dos desvios ao quadrado em torno da média (a variação total dos minutos)
sst = sum((y - media_y) ** 2 for y in mins)
# MSE: erro quadrático médio (SSE dividido pelo número de casos)
mse = sse / n
# Pula uma linha
print()
# Mostra o SSE
print(f"SSE  = {sse:.2f}")
# Mostra o MSE
print(f"MSE  = {mse:.4f}")
# RMSE: raiz do MSE, volta para a unidade original (minutos)
print(f"RMSE = {math.sqrt(mse):.4f} minutos")
# Mostra o SST
print(f"SST  = {sst:.0f}")
# R²: fração da variação dos minutos que a reta explica
print(f"R²   = {1 - sse / sst:.4f}")
# Usa a reta para prever um caso novo, com 10 documentos
print(f"previsão para 10 documentos = {a + b * 10:.1f} minutos")


# %% [markdown]
# O RMSE de 1.9365 é o erro típico *dentro da amostra*. Ele não é a incerteza de uma previsão
# nova: para 10 documentos, o intervalo de predição de 95% vai de cerca de 43.9 a 56.1 minutos
# (veja o capítulo).


# %% [markdown]
# **SUA VEZ**
#
# 1. Acrescente um nono atendimento: 13 documentos e 58 minutos. Recalcule tudo. A reta mudou
# muito?
# 2. Peça a previsão para 200 documentos. Escreva por que você não deve confiar nesse número.
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ### Exercício 5. Descendo a montanha: o gradiente descendente
# *Exemplo 5 do capítulo*
#
# Mesmos oito atendimentos, outro caminho. Em vez da fórmula, ajustamos a e b aos poucos, dando
# passos contra o gradiente. Antes, normalizamos os documentos, como o capítulo explica.


# %%
# Carrega o NumPy (de novo, por segurança, caso esta célula seja executada sozinha)
import numpy as np

# Documentos como array de números decimais (dtype=float)
x = np.array(docs, dtype=float)
# Minutos como array de números decimais
y = np.array(mins, dtype=float)
# Normaliza os documentos para a faixa de 0 a 1
xn = (x - 2) / 10      # documentos normalizados: 2 vira 0.0 e 12 vira 1.0

# Gradiente descendente; max_rodadas e limite têm valores padrão
def descer(taxa, max_rodadas=100000, limite=0.001):
    # Começa com a reta mais boba possível: a = 0 e b = 0 (atribuição dupla)
    a, b = 0.0, 0.0
    # Lista para registrar o que acontece em cada rodada
    historico = []
    # Rodadas numeradas de 1 até max_rodadas
    for rodada in range(1, max_rodadas + 1):
        # Resíduos dos oito casos de uma vez, com a reta atual
        residuo = y - (a + b * xn)
        # Derivada do MSE em relação a a (n = 8 vem do Exercício 4)
        grad_a = (-2 / n) * residuo.sum()
        # Derivada do MSE em relação a b
        grad_b = (-2 / n) * (residuo * xn).sum()
        # Dá um passo contra o gradiente, do tamanho da taxa
        novo_a = a - taxa * grad_a
        # Mesmo passo para b
        novo_b = b - taxa * grad_b
        # abs tira o sinal; mede o maior passo dado nesta rodada
        mudanca = max(abs(novo_a - a), abs(novo_b - b))
        # Atualiza a e b ao mesmo tempo
        a, b = novo_a, novo_b
        # np.mean calcula a média dos erros ao quadrado com a nova reta
        mse = np.mean((y - (a + b * xn)) ** 2)
        # Registra a rodada como uma tupla de seis valores
        historico.append((rodada, grad_a, grad_b, a, b, mse))
        # Se o passo ficou menor que o limite, consideramos que parou de andar
        if mudanca < limite:
            # Sai do laço for
            break
    # Devolve todo o histórico
    return historico

# Roda o gradiente descendente com taxa 0.5
h = descer(0.5)
# Cabeçalho da tabela
print("rodada    grad_a    grad_b         a         b       MSE")
# Desempacota cada tupla do histórico em seis variáveis
for rod, ga, gb, aa, bb, ee in h:
    # in verifica se a rodada está na tupla de rodadas escolhidas para mostrar
    if rod in (1, 2, 3, 5, 10, 20, 40, 60, len(h)):
        # Mostra a linha; :9.4f usa 9 espaços e 4 casas decimais
        print(f"{rod:6d} {ga:9.4f} {gb:9.4f} {aa:9.4f} {bb:9.4f} {ee:9.4f}")


# %% [markdown]
# O primeiro passo salta o intercepto de 0 para 38, a média dos minutos, e o MSE despenca de
# 1631.75 para 173.92. Depois a queda fica lenta. Agora devolvemos os coeficientes à escala
# original:


# %%
# h[-1] é a última rodada (índice negativo conta do fim); [3] é a e [4] é b
a_norm, b_norm = h[-1][3], h[-1][4]
# Volta b para a escala original: x foi dividido por 10, então b também é
b_original = b_norm / 10
# Volta a: o deslocamento de 2 documentos vira 2/10 = 0.2 vezes b normalizado
a_original = a_norm - 0.2 * b_norm

# Quantas rodadas o método usou
print(f"parou na rodada {len(h)}")
# Coeficientes na escala normalizada
print(f"escala normalizada: a = {a_norm:.4f}   b = {b_norm:.4f}")
# Coeficientes na escala original, comparáveis aos do Exercício 4
print(f"escala original:    a = {a_original:.4f}   b = {b_original:.4f}")
# Os valores exatos da fórmula fechada, para comparar
print(f"fórmula fechada:    a = {a}   b = {b}")

# Carrega a biblioteca de gráficos
import matplotlib.pyplot as plt
# Desenha o MSE de cada rodada (posição 5 de cada tupla do histórico)
plt.plot([r[5] for r in h])
# Escala logarítmica, para ver a queda grande e a lenta no mesmo gráfico
plt.yscale("log")
# Nome do eixo horizontal
plt.xlabel("rodada")
# Nome do eixo vertical
plt.ylabel("MSE (escala log)")
# Título do gráfico
plt.title("A curva de aprendizado")
# Liga a grade de fundo
plt.grid(True)
# Desenha o gráfico
plt.show()


# %% [markdown]
# O gradiente chegou perto de 10 e 4, mas não aterrissou exatamente: é a natureza do método.
# Rodando mais, chegaria mais perto, e nunca chegaria.


# %% [markdown]
# **SUA VEZ**
#
# 1. Troque o limite de 0.001 para 0.00001. Quantas rodadas são necessárias agora, e quão perto de
# 10 e 4 chegamos?
# 2. Rode o mesmo método com os documentos crus (use x no lugar de xn) e taxa 0.016. Quantas
# rodadas passam antes de a mudança ficar abaixo do limite? Compare com as rodadas do caso
# normalizado.
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ### Exercício 6. Passo curto demais, passo longo demais
# *Exemplo 6 do capítulo*
#
# A taxa de aprendizado é o único número que o ser humano escolhe, e escolher errado estraga tudo.
# Vamos ver as duas formas de errar.


# %%
# Taxa pequena demais; limite=0 obriga a rodar todas as 300 rodadas
lento = descer(0.01, max_rodadas=300, limite=0)
# Título do primeiro bloco
print("taxa = 0.01")
# Percorre o histórico da taxa lenta
for rod, ga, gb, aa, bb, ee in lento:
    # Mostra só algumas rodadas escolhidas
    if rod in (1, 50, 150, 300):
        # Mostra a, b e o MSE da rodada
        print(f"  rodada {rod:3d}   a = {aa:.4f}   b = {bb:.4f}   MSE = {ee:.2f}")
# O alvo é o resultado da taxa 0.5 do Exercício 5
print(f"  alvo        a = {a_norm:.4f}   b = {b_norm:.4f}   MSE = {h[-1][5]:.2f}")

# Pula uma linha
print()
# Taxa grande demais, só 8 rodadas
explosivo = descer(0.9, max_rodadas=8, limite=0)
# Título do segundo bloco
print("taxa = 0.9")
# Mostra todas as rodadas da taxa explosiva
for rod, ga, gb, aa, bb, ee in explosivo:
    # a e b trocam de sinal a cada rodada e o MSE cresce
    print(f"  rodada {rod}   a = {aa:9.2f}   b = {bb:9.2f}   MSE = {ee:10.2f}")


# %% [markdown]
# Com taxa 0.01, depois de 300 rodadas ainda estamos longe. Com taxa 0.9, o sinal de a e de b
# alterna entre positivo e negativo, e o MSE é multiplicado por cerca de 1.7 a cada rodada. Agora
# os três lado a lado em um gráfico:


# %%
# Curva da taxa 0.5 nas primeiras 60 rodadas
plt.plot([r[5] for r in descer(0.5, max_rodadas=60, limite=0)], label="taxa 0.5")
# lento[:60] é uma fatia: pega só as 60 primeiras rodadas da taxa 0.01
plt.plot([r[5] for r in lento[:60]], label="taxa 0.01")
# Curva da taxa 0.9 (só 8 rodadas, subindo)
plt.plot([r[5] for r in explosivo], label="taxa 0.9")
# Escala logarítmica no eixo vertical
plt.yscale("log")
# Nome do eixo horizontal
plt.xlabel("rodada")
# Nome do eixo vertical
plt.ylabel("MSE (escala log)")
# Legenda com os nomes dados em label
plt.legend()
# Grade de fundo
plt.grid(True)
# Desenha o gráfico
plt.show()


# %% [markdown]
# Compare a falha escandalosa da taxa 0.9 com a falha silenciosa do K-means no Exercício 3.


# %% [markdown]
# **SUA VEZ**
#
# 1. Teste as taxas 0.1, 0.3, 0.7 e 0.78, 0.79. Em qual valor o algoritmo começa a divergir? O
# capítulo calcula que o limite é 0.7844.
# 2. Escreva, com suas palavras, por que a falha da taxa grande demais é mais fácil de perceber do
# que a do sorteio ruim no K-means.
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ### Exercício 7. Um neurônio sozinho diante da regra da discordância
# *Exemplo 7 do capítulo*
#
# A regra da ServiPro: se o sistema e o atendente discordam, o processo vai para revisão. Se
# concordam, não. São quatro casos, e a resposta certa é o OU exclusivo (XOR). Vamos treinar um
# único neurônio com sigmoide.


# %%
# Carrega o math para usar math.exp
import math

# Sigmoide: espreme qualquer número z para a faixa entre 0 e 1
def sigmoide(z):
    # math.exp(-z) é e elevado a -z
    return 1 / (1 + math.exp(-z))

# Os quatro casos do XOR: (sistema, atendente, resposta certa)
casos = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)]   # x1, x2, resposta certa

# Treina um único neurônio com sigmoide; semente fixa o sorteio dos pesos iniciais
def treinar_neuronio(semente, rodadas=20000, taxa=0.5):
    # Gerador de números aleatórios do NumPy; mesma semente, mesmo sorteio
    rng = np.random.default_rng(semente)
    # Sorteia 3 números entre -0.5 e 0.5 e distribui em w1, w2 e b
    w1, w2, b = rng.uniform(-0.5, 0.5, 3)
    # _ é o nome usado quando não precisamos do número da rodada
    for _ in range(rodadas):
        # Zera os três gradientes de uma vez (atribuição encadeada)
        g1 = g2 = gb = 0.0
        # Percorre os quatro casos
        for x1, x2, certo in casos:
            # Saída do neurônio: soma ponderada mais viés, passada pela sigmoide
            o = sigmoide(w1 * x1 + w2 * x2 + b)
            # Derivada do erro médio em relação à soma (o * (1 - o) é a derivada da sigmoide)
            d = (-2 / 4) * (certo - o) * o * (1 - o)
            # Acumula o gradiente do peso w1
            g1 = g1 + d * x1
            # Acumula o gradiente do peso w2
            g2 = g2 + d * x2
            # Acumula o gradiente do viés b
            gb = gb + d
        # Passo contra o gradiente para w1
        w1 = w1 - taxa * g1
        # Passo contra o gradiente para w2
        w2 = w2 - taxa * g2
        # Passo contra o gradiente para b
        b = b - taxa * gb
    # Saídas do neurônio treinado para os quatro casos
    saidas = [sigmoide(w1 * x1 + w2 * x2 + b) for x1, x2, certo in casos]
    # Erro quadrático médio nos quatro casos
    erro = sum((certo - o) ** 2 for (x1, x2, certo), o in zip(casos, saidas)) / 4
    # Devolve as saídas e o erro
    return saidas, erro

# Testa quatro sorteios diferentes (sementes 0, 1, 2 e 3)
for semente in range(4):
    # Treina e recebe as saídas e o erro
    saidas, erro = treinar_neuronio(semente)
    # round(o, 4) arredonda cada saída para 4 casas antes de mostrar
    print(f"semente {semente}: saídas = {[round(o, 4) for o in saidas]}   erro = {erro:.4f}")


# %% [markdown]
# Nos quatro sorteios o neurônio respondeu 0.5 para todos os casos e o erro parou em 0.2500. Não é
# bug nem taxa mal escolhida: é o melhor que uma reta consegue neste problema. Dê de ombros e olhe
# de novo: 0.5 é a forma matemática de dizer "não faço ideia".


# %% [markdown]
# **SUA VEZ**
#
# 1. Troque a taxa para 5.0 e para 0.05. O resultado muda? O que isso mostra?
# 2. Troque a tabela de casos para a operação E (respostas 0, 0, 0, 1). O neurônio consegue
# aprender? Por quê?
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ### Exercício 8. A passagem para frente com os pesos iniciais
# *Exemplo 8 do capítulo*
#
# A rede com dois neurônios ocultos tem nove números ajustáveis. Vamos calcular a resposta dela,
# caso a caso, com os pesos iniciais fixados.


# %%
# ordem dos nove parâmetros: p11, p12, p21, p22, b1, b2, q1, q2, b3
# Pesos iniciais da rede: 4 da entrada, 2 vieses ocultos, 2 da saída e 1 viés de saída
p = [0.5, -0.4, 0.9, 0.3, 0.2, -0.1, 0.6, -0.7, 0.1]

# Passagem para frente: calcula a resposta da rede para uma entrada (x1, x2)
def passagem_frente(p, x1, x2):
    # Desempacota a lista de nove números em nove variáveis com nome
    p11, p12, p21, p22, b1, b2, q1, q2, b3 = p
    # Soma ponderada que chega ao neurônio oculto 1
    z1 = x1 * p11 + x2 * p21 + b1
    # Soma ponderada que chega ao neurônio oculto 2
    z2 = x1 * p12 + x2 * p22 + b2
    # Saída do neurônio oculto 1
    h1 = sigmoide(z1)
    # Saída do neurônio oculto 2
    h2 = sigmoide(z2)
    # Soma ponderada que chega ao neurônio de saída
    z3 = h1 * q1 + h2 * q2 + b3
    # Resposta final da rede, entre 0 e 1
    o = sigmoide(z3)
    # Devolve todos os valores intermediários; a saída é o sexto (posição 5)
    return z1, h1, z2, h2, z3, o

# Erro quadrático médio da rede nos quatro casos
def erro_medio(p):
    # Acumulador
    soma = 0
    # Percorre os quatro casos
    for x1, x2, certo in casos:
        # [5] pega só a saída o entre os seis valores devolvidos
        o = passagem_frente(p, x1, x2)[5]
        # Soma o erro ao quadrado deste caso
        soma = soma + (certo - o) ** 2
    # Divide por 4 para obter a média
    return soma / 4

# Cabeçalho da tabela
print("x1 x2       z1      h1       z2      h2       z3   saída  certo    erro")
# Percorre os quatro casos
for x1, x2, certo in casos:
    # Calcula a passagem para frente e guarda os seis valores
    z1, h1, z2, h2, z3, o = passagem_frente(p, x1, x2)
    # Primeira metade da linha (camada oculta); end="  " mantém na mesma linha
    print(f"{x1}  {x2}  {z1:7.4f} {h1:7.4f}  {z2:7.4f} {h2:7.4f}", end="  ")
    # Segunda metade: soma de saída, saída, resposta certa e erro
    print(f"{z3:7.4f} {o:7.4f}  {certo}   {certo - o:7.4f}")

# Pula uma linha
print()
# Erro médio da rede com os pesos iniciais
print(f"erro quadrático médio = {erro_medio(p):.4f}")


# %% [markdown]
# As quatro saídas ficaram entre 0.52 e 0.57: a rede está em cima do muro em todos os casos, como
# se espera de pesos sorteados sem critério.


# %% [markdown]
# **SUA VEZ**
#
# 1. Confira o caso 4 com a calculadora do celular: refaça z1, h1, z2, h2, z3 e a saída, e compare
# com a tabela.
# 2. Troque o primeiro peso (p11) de 0.5 para 2.0. O erro quadrático médio sobe ou desce?
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ### Exercício 9. Uma rodada completa de retropropagação
# *Exemplo 9 do capítulo*
#
# A rede errou. De quem é a culpa, e em que proporção? A retropropagação reparte a culpa de trás
# para frente, e depois corrigimos os nove números.


# %%
# Uma rodada de retropropagação: calcula os gradientes e devolve os novos pesos
def uma_rodada(p, taxa):
    # Desempacota os nove parâmetros
    p11, p12, p21, p22, b1, b2, q1, q2, b3 = p
    # [0.0] * 9 cria uma lista com nove zeros, um gradiente para cada parâmetro
    g = [0.0] * 9
    # Lista para guardar as "culpas" de cada caso
    culpas = []
    # Percorre os quatro casos
    for x1, x2, certo in casos:
        # Passagem para frente com os pesos atuais
        z1, h1, z2, h2, z3, o = passagem_frente(p, x1, x2)
        # Quanto a rede errou neste caso
        erro = certo - o
        # Culpa do neurônio de saída (derivada do erro em relação a z3)
        d_saida = (-2 / 4) * erro * o * (1 - o)
        # Culpa do oculto 1: a da saída, vezes o peso q1 que o liga a ela, vezes a sigmoide'
        d_oculto1 = d_saida * q1 * h1 * (1 - h1)
        # Culpa do oculto 2, pelo mesmo raciocínio, com o peso q2
        d_oculto2 = d_saida * q2 * h2 * (1 - h2)
        # Guarda as três culpas deste caso como uma tupla
        culpas.append((d_saida, d_oculto1, d_oculto2))
        # += soma ao valor que já estava; gradiente de p11 (entrada x1 para o oculto 1)
        g[0] += d_oculto1 * x1
        # Gradiente de p12 (entrada x1 para o oculto 2)
        g[1] += d_oculto2 * x1
        # Gradiente de p21 (entrada x2 para o oculto 1)
        g[2] += d_oculto1 * x2
        # Gradiente de p22 (entrada x2 para o oculto 2)
        g[3] += d_oculto2 * x2
        # Gradiente do viés b1
        g[4] += d_oculto1
        # Gradiente do viés b2
        g[5] += d_oculto2
        # Gradiente de q1 (oculto 1 para a saída)
        g[6] += d_saida * h1
        # Gradiente de q2 (oculto 2 para a saída)
        g[7] += d_saida * h2
        # Gradiente do viés de saída b3
        g[8] += d_saida
    # Passo contra o gradiente para cada um dos nove parâmetros
    novo = [p[i] - taxa * g[i] for i in range(9)]
    # Devolve gradientes, novos pesos e culpas
    return g, novo, culpas

# Nomes dos parâmetros, na mesma ordem da lista p, para a tabela
nomes_p = ["p11", "p12", "p21", "p22", "b1", "b2", "q1", "q2", "b3"]
# Executa uma rodada com taxa 5.0
g, novo, culpas = uma_rodada(p, 5.0)

# Cabeçalho da tabela de culpas
print("caso   d_saída  d_oculto1  d_oculto2")
# enumerate dá a posição i; (ds, d1, d2) desempacota a tupla de culpas
for i, (ds, d1, d2) in enumerate(culpas):
    # i + 1 para numerar os casos de 1 a 4
    print(f"  {i + 1}  {ds:8.4f}  {d1:9.4f}  {d2:9.4f}")

# Pula uma linha
print()
# Cabeçalho da tabela de parâmetros
print("param     antes   gradiente    depois")
# zip com quatro listas: nome, valor antes, gradiente e valor depois
for nome, antes, grad, depois in zip(nomes_p, p, g, novo):
    # Mostra a linha do parâmetro
    print(f"{nome:5s} {antes:9.4f} {grad:11.4f} {depois:9.4f}")

# Pula uma linha
print()
# Erro com os pesos antigos
print(f"erro antes  = {erro_medio(p):.4f}")
# Erro com os pesos corrigidos: deve ser um pouco menor
print(f"erro depois = {erro_medio(novo):.4f}")


# %% [markdown]
# Repare no tamanho das correções: os pesos de entrada mudaram pouco, na segunda ou na terceira
# casa decimal, enquanto q1, q2 e b3 mudaram muito mais. No começo do treino, a camada mais
# próxima da resposta aprende primeiro.


# %% [markdown]
# **SUA VEZ**
#
# 1. Rode uma_rodada várias vezes em um for e imprima o erro a cada 10 rodadas. Ele cai de forma
# constante ou há trechos lentos?
# 2. Explique, com suas palavras, por que a culpa do neurônio oculto depende do peso que o liga à
# saída.
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ### Exercício 10. O que a rede descobriu sozinha, e o platô
# *Exemplo 10 do capítulo*
#
# Agora repetimos as rodadas até o erro cair abaixo de 0.004 e abrimos a caixa para ver o que cada
# neurônio oculto virou. Depois mudamos os pesos de partida.


# %%
# Repete rodadas de retropropagação até o erro cair abaixo de parar_em
def treinar(p, taxa=5.0, parar_em=0.004, max_rodadas=5000):
    # Lista com o erro de cada rodada
    historico = []
    # Rodadas numeradas de 1 até max_rodadas
    for rodada in range(1, max_rodadas + 1):
        # Erro com os pesos atuais
        erro = erro_medio(p)
        # Registra o erro
        historico.append(erro)
        # is not None: só testa a parada se um valor de parar_em foi informado
        if parar_em is not None and erro < parar_em:
            # Erro pequeno o bastante: sai do laço
            break
        # [1] pega só os novos pesos devolvidos por uma_rodada
        p = uma_rodada(p, taxa)[1]
    # Devolve os pesos finais e o histórico de erros
    return p, historico

# Treina a partir dos pesos iniciais do Exercício 8
p_final, hist = treinar(p)
# len(hist) é o número de rodadas registradas
print(f"o erro caiu abaixo de 0.004 na rodada {len(hist)}")
# Algumas rodadas escolhidas para mostrar a queda do erro
for r in (1, 25, 50, 100, 150, 200, 250, len(hist)):
    # hist[r - 1] porque a rodada 1 está na posição 0
    print(f"  rodada {r:3d}   erro = {hist[r - 1]:.4f}")

# Pula uma linha
print()
# Título
print("parâmetros finais:")
# range(0, 9, 3) gera 0, 3 e 6: começa uma linha a cada três parâmetros
for i in range(0, 9, 3):
    # join junta os três textos "nome = valor" da linha, separados por três espaços
    print("  " + "   ".join(f"{nomes_p[j]} = {p_final[j]:.4f}" for j in range(i, i + 3)))

# Pula uma linha
print()
# Cabeçalho da tabela
print("sistema atendente      h1      h2   saída  certo")
# Percorre os quatro casos
for x1, x2, certo in casos:
    # Passagem para frente com os pesos treinados
    z1, h1, z2, h2, z3, o = passagem_frente(p_final, x1, x2)
    # Mostra o que cada neurônio oculto virou e a saída final
    print(f"   {x1}        {x2}      {h1:7.4f} {h2:7.4f} {o:7.4f}  {certo}")


# %% [markdown]
# Arredonde h1 e h2 para 0 ou 1: h1 vale 0, 1, 1, 1 (pelo menos um aprovou) e h2 vale 0, 0, 0, 1
# (os dois aprovaram). Com q1 positivo e q2 negativo, a rede lê: precisa de revisão quando pelo
# menos um aprovou, mas não quando os dois aprovaram. Ninguém programou isso.


# %%
# Outros nove pesos iniciais, que levam a rede a um platô
p_ruim = [0.7, -0.6, 0.5, 0.8, -0.2, 0.3, 0.9, -0.8, 0.1]
# parar_em=None desliga a parada antecipada: roda as 1200 rodadas inteiras
p_ruim_final, hist_ruim = treinar(p_ruim, parar_em=None, max_rodadas=1200)

# Algumas rodadas escolhidas
for r in (1, 50, 200, 600, 1200):
    # :4d reserva 4 espaços para o número da rodada
    print(f"  rodada {r:4d}   erro = {hist_ruim[r - 1]:.4f}")

# Pula uma linha
print()
# Cabeçalho da tabela
print("sistema atendente   saída  certo")
# Percorre os quatro casos
for x1, x2, certo in casos:
    # Só a saída da rede (posição 5)
    o = passagem_frente(p_ruim_final, x1, x2)[5]
    # Mostra a saída ao lado da resposta certa
    print(f"   {x1}        {x2}       {o:7.4f}  {certo}")


# %% [markdown]
# A mesma rede, a mesma taxa, os mesmos quatro exemplos, só outros nove valores iniciais. O erro
# estaciona perto de 0.126 e a rede acerta 2 dos 4 casos, devolvendo 0.5 nos outros dois. O treino
# terminou, mas o modelo não acertou.


# %%
# Lista com o número de acertos de cada sorteio
acertos_por_semente = []
# Testa 20 sorteios de pesos iniciais
for semente in range(20):
    # Sorteia nove pesos entre -0.5 e 0.5; list transforma o array em lista comum
    pi = list(np.random.default_rng(semente).uniform(-0.5, 0.5, 9))
    # Treina 3000 rodadas; _ descarta o histórico, que não será usado
    pi_final, _ = treinar(pi, parar_em=None, max_rodadas=3000)
    # Conta os casos em que (saída >= 0.5) coincide com a resposta certa (bool vira 0/1 em
    # False/True); o comando continua na linha de baixo até fechar o parêntese
    certos = sum(1 for x1, x2, certo in casos
                 if (passagem_frente(pi_final, x1, x2)[5] >= 0.5) == bool(certo))
    # Guarda os acertos deste sorteio
    acertos_por_semente.append(certos)

# Mostra os acertos dos 20 sorteios
print(acertos_por_semente)
# .count(4) conta quantos sorteios acertaram os quatro casos
print(f"{acertos_por_semente.count(4)} de 20 sorteios acertaram os 4 casos")


# %% [markdown]
# Essa célula demora alguns segundos. Em 18 de 20 sorteios a rede aprende a regra; nos outros dois
# fica presa. É por isso que, na vida real, o treino é repetido com inicializações diferentes e
# alguém olha o resultado.


# %% [markdown]
# **SUA VEZ**
#
# 1. Troque a taxa de aprendizado para 1.0 em treinar(p, taxa=1.0). Em quantas rodadas o erro cai
# abaixo de 0.004?
# 2. O que você diria a um colega que afirma: "o treino terminou, então o modelo está certo"? Use
# o exemplo da célula de p_ruim.
#
# *Escreva aqui as suas respostas e faça os testes na célula de código abaixo.*


# %%
# Espaço para os seus testes


# %% [markdown]
# ## Parte 3. A mesma coisa em poucas linhas (scikit-learn)


# %% [markdown]
# ### D1. K-means com a biblioteca
# *compare com os Exercícios 2 e 3*


# %%
# from ... import traz só a classe KMeans do scikit-learn
from sklearn.cluster import KMeans

# A biblioteca espera um array com uma linha por cliente e uma coluna por medida
X = np.array(pontos)

# Os mesmos centros iniciais do Exercício 2 (Gina, Hugo, João)
inicio_bom = np.array([pontos[6], pontos[7], pontos[9]])
# Cria o modelo com 3 grupos, esses centros e uma só execução; .fit roda o algoritmo
modelo = KMeans(n_clusters=3, init=inicio_bom, n_init=1).fit(X)
# labels_ traz o grupo de cada cliente
print("grupos da biblioteca:", modelo.labels_)
# inertia_ traz a inércia final
print(f"inércia da biblioteca: {modelo.inertia_:.6f}")
# Inércia calculada à mão no Exercício 2, para comparar
print(f"inércia na mão:        {inercia_bom:.6f}")

# Os mesmos centros ruins do Exercício 3 (Ana, Iara, João)
inicio_ruim = np.array([pontos[0], pontos[8], pontos[9]])
# Roda a biblioteca com o chute ruim
modelo2 = KMeans(n_clusters=3, init=inicio_ruim, n_init=1).fit(X)
# Inércia da biblioteca com o chute ruim
print(f"chute ruim, biblioteca: {modelo2.inertia_:.6f}")
# Inércia à mão com o chute ruim: a biblioteca cai na mesma armadilha
print(f"chute ruim, na mão:     {inercia_ruim:.6f}")


# %% [markdown]
# Com os mesmos centros iniciais, a biblioteca chega aos mesmos grupos e à mesma inércia. O
# parâmetro init recebe os centros de partida, e n_init=1 pede uma única execução. Sem init
# explícito, o padrão é o k-means++, que espalha os centros iniciais de propósito.


# %% [markdown]
# ### D2. Regressão linear com a biblioteca
# *compare com o Exercício 4*


# %%
# Traz a regressão linear do scikit-learn
from sklearn.linear_model import LinearRegression

# reshape(-1, 1) transforma a lista em uma coluna (o -1 deixa o NumPy contar as linhas)
X = np.array(docs).reshape(-1, 1)     # o scikit-learn espera uma coluna: lista de listas
# Cria o modelo e ajusta a reta aos documentos e minutos
modelo = LinearRegression().fit(X, mins)

# coef_ guarda a inclinação; [0] porque há uma só variável
print(f"inclinação: {modelo.coef_[0]:.4f}")
# intercept_ guarda o intercepto
print(f"intercepto: {modelo.intercept_:.4f}")
# .score devolve o R² do modelo nesses dados
print(f"R²:         {modelo.score(X, mins):.4f}")
# .predict recebe uma lista de listas ([[10]]) e devolve um array; [0] pega a previsão
print(f"previsão para 10 documentos: {modelo.predict([[10]])[0]:.1f} minutos")


# %% [markdown]
# Os mesmos 4 e 10 do Exercício 4, e o mesmo R² de 0.9800, em duas linhas de código. Repare que o
# X precisa ser uma coluna (lista de listas), mesmo quando há uma única variável: esquecer disso é
# a causa mais comum de ValueError.


# %% [markdown]
# ### D3. Um neurônio e uma rede, com a biblioteca
# *compare com os Exercícios 7 e 10*


# %%
# Regressão logística: equivale a um único neurônio com sigmoide
from sklearn.linear_model import LogisticRegression
# MLPClassifier: rede neural com camadas ocultas
from sklearn.neural_network import MLPClassifier

# As quatro entradas do XOR, uma linha por caso
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# As respostas certas do XOR
y = np.array([0, 1, 1, 0])

# Treina o neurônio único
neuronio = LogisticRegression().fit(X, y)
# predict_proba dá as probabilidades; [:, 1] pega a coluna da classe 1 em todas as linhas
print("neurônio único:", neuronio.predict_proba(X)[:, 1].round(4))

# Lista com os acertos de cada sorteio
acertos = []
# Testa 10 sementes diferentes
for semente in range(10):
    # Rede com 1 camada oculta de 2 neurônios sigmoides (logistic); o comando segue abaixo
    rede = MLPClassifier(hidden_layer_sizes=(2,), activation="logistic",
                         solver="lbfgs", random_state=semente, max_iter=2000).fit(X, y)
    # Compara previsões e respostas, soma os acertos e int converte para número inteiro
    acertos.append(int((rede.predict(X) == y).sum()))
# Mostra os acertos de cada semente
print("rede com 2 neurônios ocultos, acertos por semente:", acertos)


# %% [markdown]
# O neurônio único responde 0.5 para os quatro casos, como no Exercício 7. Na rede com dois
# neurônios ocultos, algumas sementes chegam a 4 acertos e outras ficam presas em 2 ou 3, como no
# Exercício 10. **O seu resultado pode ser diferente do mostrado aqui**, porque depende da versão
# da biblioteca, e é justamente esse o ponto: o resultado de uma rede depende do sorteio.


# %% [markdown]
# ### D4. Como escolher K: cotovelo e silhueta
# *compare com a seção 3.2 do capítulo*


# %%
# Os doze clientes normalizados como array
X_pontos = np.array(pontos)
# silhouette_score mede o quanto cada ponto está bem encaixado no seu grupo
from sklearn.metrics import silhouette_score

# Cabeçalho da tabela
print(" K   inércia   silhueta")
# Testa K de 1 a 6 grupos
for k in range(1, 7):
    # n_init=10 roda 10 vezes e fica com a melhor; random_state fixa o sorteio
    m = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X_pontos)
    # Com um só grupo a silhueta não existe
    if k == 1:
        # Mostra só a inércia e um traço no lugar da silhueta
        print(f"{k:2d}   {m.inertia_:.4f}      ---")
    # else: o bloco executado quando a condição do if é falsa
    else:
        # Mostra a inércia (para o cotovelo) e a silhueta
        print(f"{k:2d}   {m.inertia_:.4f}   {silhouette_score(X_pontos, m.labels_):.4f}")


# %% [markdown]
# A inércia despenca até K = 3 e depois cai pouco, o cotovelo. A silhueta é máxima em K = 3. As
# duas heurísticas apontam para o mesmo K, o que é conveniente, mas não é regra.


# %% [markdown]
# ### Desafio final, sem código pronto
# O quarteto de Anscombe vem com a biblioteca seaborn: `import seaborn as sns` e `df =
# sns.load_dataset("anscombe")` (colunas `dataset`, `x`, `y`).
#
# 1. Para cada um dos quatro conjuntos, ajuste uma `LinearRegression` e mostre inclinação,
# intercepto e R².
# 2. Desenhe os quatro gráficos de dispersão com a reta ajustada.
# 3. Em uma célula de texto, escreva o que os números sozinhos não mostram.


# %%
# Espaço para os seus testes


# %% [markdown]
# ---
# **Entrega:** *Ambiente de execução > Reiniciar sessão e executar tudo*, depois *Compartilhar >
# qualquer pessoa com o link pode visualizar*, e cole o link no espaço indicado pelo professor.
