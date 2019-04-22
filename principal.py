import matplotlib.pyplot as plt
from Principal import funcoes
from copy import deepcopy

#        0     1     2     3     4     5     6     7     8     9     10    11
#itens2=[[3,5],[7,2],[4,5],[6,8],[3,6],[6,6],[7,1],[1,7],[1,1],[3,3],[3,2],[4,1]]

itens=[]

arq = open('/home/alexandreaag/PycharmProjects/Mochila_AG/Principal/KNAPDATA100000.TXT', 'r')
texto = arq.readlines()
mochila = int(texto[0])
for linha in texto[2:]:
    linha_split=linha.split(",")
    linha_split[2]=linha_split[2][:-1]
    itens.append([int(linha_split[2]),int(linha_split[1])])
arq.close()

tam_pop=33
qde_geracoes=100
tx_mutacao=0.2
tx_cruzamento=0.9

populacao=[]
individuo=[[0,0]]

dispersao=[]
convergencia=[]
geracoes=[]

#gerando melhor individuo com guloso
#populacao.append(funcoes.guloso(itens,mochila))
#fim

#gerando o restante da populacao inicial
for i in range(tam_pop):
    populacao.append(funcoes.populacao_aleatoria(itens))
#fim

g=0
funcoes.imprime_geracao(populacao,g)

# armazenando possiveis candidatos
dispersao.append(funcoes.verifica_candidatos(populacao, mochila))
if funcoes.verifica_candidatos(populacao, mochila) != 0:
    convergencia.append(max(funcoes.verifica_candidatos(populacao, mochila)))
# fim

for g in range(qde_geracoes):

    populacao_e=funcoes.elitismo(populacao, mochila)

    populacao_c=funcoes.cruzamento(populacao,itens,tx_cruzamento)
    populacao=deepcopy(populacao_e)+deepcopy(populacao_c)
    funcoes.imprime_cruzamento(populacao, g+1)

    populacao_m=funcoes.mutacao(populacao,itens,tx_mutacao)
    populacao=deepcopy(populacao_e)+deepcopy(populacao_m)
    funcoes.imprime_mutacao(populacao, g+1)

    populacao_s=funcoes.selecao(populacao,mochila,tam_pop)
    populacao=deepcopy(populacao_s)
    funcoes.imprime_geracao(populacao, g+1)

    # armazenando possiveis candidatos
    if g%(100) == 0:
        dispersao.append(funcoes.verifica_candidatos(populacao, mochila))
    if funcoes.verifica_candidatos(populacao, mochila) != 0:
        convergencia.append(max(funcoes.verifica_candidatos(populacao, mochila)))
    # fim

print("Melhor Solução: " + str(funcoes.elitismo(populacao, mochila)[0]))

'''
# plota boxplots das geracoes
fig = plt.figure(1, figsize=(12, 6))
ax = fig.add_subplot(111)
plt.xlabel("Geracoes x 10")
plt.ylabel("Dispersao")
bp = ax.boxplot(dispersao)
# fim

# plota curva de convergencia
fig = plt.figure(2, figsize=(12, 6))
plt.plot(convergencia)
plt.xlabel("Geracoes")
plt.ylabel("Melhor Resultado")
plt.show()
# fim
'''