from random import randint
from Principal import funcoes
from copy import deepcopy

#        0     1     2     3     4     5     6     7     8     9     10    11
itens=[[3,5],[7,2],[4,5],[6,8],[3,6],[6,6],[7,1],[1,7],[1,1],[3,3],[3,2],[4,1]]

tam_pop=10
geracoes=5
tx_mutacao=0.1
tx_selecao=0.9
tx_cruzamento=0.9

populacao=[]
mochila=20
individuo=[[0,0]]

#gerando melhor individuo com guloso
populacao.append(funcoes.guloso(itens,mochila))
#fim

#gerando o restante da populacao inicial
for i in range(tam_pop-1):
    populacao.append(funcoes.populacao_aleatoria(itens))
#fim

g=0
funcoes.imprime_geracao(populacao,g)

# verificando possiveis candidatos
funcoes.verifica_candidatos(populacao, mochila)
# fim

for g in range(geracoes):

    populacao_e=funcoes.elitismo(populacao, mochila)
    populacao_c=funcoes.cruzamento(populacao[1:],itens,tx_cruzamento)
    populacao=deepcopy(populacao_e)+deepcopy(populacao_c)
    funcoes.imprime_cruzamento(populacao, g+1)

    populacao_m=funcoes.mutacao(populacao[1:],itens,tx_mutacao)
    populacao[1:]=deepcopy(populacao_m)
    funcoes.imprime_mutacao(populacao, g+1)

    populacao_s=funcoes.selecao(populacao[1:],mochila,tx_selecao,tam_pop)
    populacao[1:]=deepcopy(populacao_s)
    funcoes.imprime_geracao(populacao, g+1)



    # verificando possiveis candidatos
    funcoes.verifica_candidatos(populacao, mochila)
    # fim