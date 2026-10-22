# A ginga dos números: código dos exercícios

Notebooks do **livro de exercícios** que acompanha o livro-texto *A ginga dos números: inteligência artificial conta a conta*, de Bruno Menezes.

Cada caderno refaz em Python, passo a passo, os exemplos numéricos de um capítulo do livro-texto. Todo o código está **comentado linha a linha**, pensando em quem nunca programou. Os números que aparecem na tela devem ser os mesmos do livro.

## Abrir no Google Colab

Basta uma conta Google: nada é instalado e nada é pago. Clique no botão do capítulo, depois em **Arquivo, Salvar uma cópia no Drive** para guardar as suas alterações.

| Capítulo | Assunto | Abrir | Script |
| --- | --- | --- | --- |
| 1. A evolução da inteligência artificial | neurônio de 1943, perceptron, XOR, retropropagação, recompensa e atenção | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/brunoleomenezes/ginga-dos-numeros/blob/main/cap01/cap01_evolucao_da_ia.ipynb) | [cap01_evolucao_da_ia.py](cap01/cap01_evolucao_da_ia.py) |
| 2. O que é inteligência artificial | escala, sobreajuste, gradiente, regressão, sigmoide, vizinhos, árvore, k-médias e métricas | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/brunoleomenezes/ginga-dos-numeros/blob/main/cap02/cap02_o_que_e_ia.ipynb) | [cap02_o_que_e_ia.py](cap02/cap02_o_que_e_ia.py) |
| 3. Três algoritmos por dentro | K-means, regressão linear e rede neural com retropropagação | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/brunoleomenezes/ginga-dos-numeros/blob/main/cap03/cap03_tres_algoritmos.ipynb) | [cap03_tres_algoritmos.py](cap03/cap03_tres_algoritmos.py) |
| 4. Do texto ao número | BPE, contagem, TF-IDF, PPMI, SVD, bigramas, perplexidade e temperatura | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/brunoleomenezes/ginga-dos-numeros/blob/main/cap04/cap04_do_texto_ao_numero.ipynb) | [cap04_do_texto_ao_numero.py](cap04/cap04_do_texto_ao_numero.py) |
| 5. A atenção por dentro | consulta, chave e valor, softmax, máscara causal, cabeças e o bloco do Transformer | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/brunoleomenezes/ginga-dos-numeros/blob/main/cap05/cap05_a_atencao_por_dentro.ipynb) | [cap05_a_atencao_por_dentro.py](cap05/cap05_a_atencao_por_dentro.py) |
| 6. Como nasce um assistente | perda, gradiente, treino, custo de escala, cache, top-k e top-p, ajustes e Wilson | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/brunoleomenezes/ginga-dos-numeros/blob/main/cap06/cap06_como_nasce_um_assistente.ipynb) | [cap06_como_nasce_um_assistente.py](cap06/cap06_como_nasce_um_assistente.py) |
| 7. Agentes: quando o modelo age | laço do agente, validador, confiabilidade, custo, memória, plano, risco e avaliação | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/brunoleomenezes/ginga-dos-numeros/blob/main/cap07/cap07_agentes.ipynb) | [cap07_agentes.py](cap07/cap07_agentes.py) |
| 8. O Jev: decisão calibrada | softmax restrito, calibração, ECE, Brier, temperatura, porta de confiança e verificador | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/brunoleomenezes/ginga-dos-numeros/blob/main/cap08/cap08_jev_decisao_calibrada.ipynb) | [cap08_jev_decisao_calibrada.py](cap08/cap08_jev_decisao_calibrada.py) |

O Capítulo 9, de considerações finais, não tem lista de exercícios.

## Como estudar com estes cadernos

1. Leia o capítulo no livro-texto e refaça os exemplos com a calculadora, prevendo o resultado antes de olhar a resposta.
2. Abra o caderno do capítulo e **digite** o código em um caderno seu, em vez de copiar: digitar é o que ensina. Use este caderno, que já traz as saídas, para conferir.
3. Execute as células **na ordem**: quase todas dependem das anteriores. Se algo der errado, use *Ambiente de execução, Reiniciar sessão e executar tudo*.
4. Responda aos blocos **Sua vez** em células de texto, com as suas palavras.

## Estrutura

```
ginga-dos-numeros/
├── README.md
├── requirements.txt
├── cap01/
│   ├── cap01_evolucao_da_ia.ipynb   (caderno executado, com as saídas)
│   └── cap01_evolucao_da_ia.py      (mesmo código, em script)
├── cap02/
│   ├── cap02_o_que_e_ia.ipynb   (caderno executado, com as saídas)
│   └── cap02_o_que_e_ia.py      (mesmo código, em script)
├── cap03/
│   ├── cap03_tres_algoritmos.ipynb   (caderno executado, com as saídas)
│   └── cap03_tres_algoritmos.py      (mesmo código, em script)
├── cap04/
│   ├── cap04_do_texto_ao_numero.ipynb   (caderno executado, com as saídas)
│   └── cap04_do_texto_ao_numero.py      (mesmo código, em script)
├── cap05/
│   ├── cap05_a_atencao_por_dentro.ipynb   (caderno executado, com as saídas)
│   └── cap05_a_atencao_por_dentro.py      (mesmo código, em script)
├── cap06/
│   ├── cap06_como_nasce_um_assistente.ipynb   (caderno executado, com as saídas)
│   └── cap06_como_nasce_um_assistente.py      (mesmo código, em script)
├── cap07/
│   ├── cap07_agentes.ipynb   (caderno executado, com as saídas)
│   └── cap07_agentes.py      (mesmo código, em script)
└── cap08/
    ├── cap08_jev_decisao_calibrada.ipynb   (caderno executado, com as saídas)
    └── cap08_jev_decisao_calibrada.py      (mesmo código, em script)
```

Os arquivos `.py` usam o formato de células `# %%`: abrem como caderno no VS Code e no Spyder, e rodam inteiros com `python capNN_....py`.

## Rodar no próprio computador (opcional)

```bash
pip install -r requirements.txt
python cap01/cap01_evolucao_da_ia.py
```

Todos os cadernos foram executados do início ao fim, sem erros, com Python 3.13, NumPy 2.5, SciPy 1.18, scikit-learn 1.9 e matplotlib 3.11. Em versões diferentes, alguns números podem variar na última casa decimal.

## Autor

Bruno Menezes · [brunoleomenezes.github.io](https://brunoleomenezes.github.io/) · [Currículo Lattes](http://lattes.cnpq.br/7671983530035555) · [ORCID](https://orcid.org/0000-0001-6249-2395)

O cenário da empresa ServiPro Soluções Administrativas, usado nos exemplos, é fictício.
