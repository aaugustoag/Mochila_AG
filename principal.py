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
    populacao_m=funcoes.mutacao(populacao[1:],itens,tx_mutacao)

    funcoes.imprime_cruzamento(populacao, g+1)

    populacao=deepcopy(populacao_e)+deepcopy(populacao_c)

    funcoes.imprime_mutacao(populacao, g+1)

    populacao[1:]=deepcopy(populacao_m)

    funcoes.imprime_geracao(populacao, g+1)

    '''
    #fazendo selecao dos melhores
    populacao_s=[]
    for ind in populacao[1:]:
        tx_infactibilidade=1
        if (ind[0][1] > mochila):
            tx_infactibilidade = mochila/ind[0][1]
        selecao = ind[0][0]/populacao[0][0][0]*100*tx_selecao*tx_infactibilidade
        if randint(0, 99) <= selecao:
            populacao_s.append(ind)
    pior=[0,0]
    while len(populacao_c)>tam_pop:
      for i,ind in enumerate(populacao):
        if (item[0] < pior[0]):
          pior = item
          pior_indice = i
        populacao.remove(pior)
    print("Selecao"+str(g)+"("+str(len(populacao_s))+"):"+str([item[0] for item in populacao_s]))
    #fim

    '''

    # verificando possiveis candidatos
    funcoes.verifica_candidatos(populacao, mochila)
    # fim