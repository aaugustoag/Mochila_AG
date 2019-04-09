from Classes import Classes
from random import randint

#        0     1     2     3     4     5     6     7     8     9     10    11
itens=[[3,5],[7,2],[4,5],[6,8],[3,6],[6,6],[7,1],[1,7],[1,1],[3,3],[3,2],[4,1]]

tam_pop=10
geracoes=10
tx_mutacao=0.1
tx_selecao=0.9
tx_cruzamento=0.8

populacao=[]
populacao_g=[]
mochila=20
individuo=[[0,0]]

#gerando melhor individuo com guloso
for item in itens:
  item.append(0)

while individuo[0][1] < mochila:
  maior = [0,1]
  for i,item in enumerate(itens):
    if (item[2]==0):
      if (item[0]/item[1] > maior[0]/maior[1]):
        maior = item
        maior_indice = i
  itens[maior_indice][2]=1
  individuo.append(maior_indice)
  individuo[0][0]+=maior[0]
  individuo[0][1]+=maior[1]
individuo[0][0]-=itens[individuo[-1]][0]
individuo[0][1]-=itens[individuo[-1]][1]
individuo.pop()
individuo[1:]=sorted(individuo[1:])

for item in itens:
  item.pop()
populacao.append(individuo)

#fim

#gerando o restante da populacao inicial
for i in range(tam_pop-1):
    individuo= [[0,0]]
    for j, item in enumerate(itens):
        if randint(0,1)==1:
            individuo.append(j)
            individuo[0][0]+=item[0]
            individuo[0][1]+=item[1]
    populacao.append(individuo)
#fim
print(populacao)

g=0
print("Geração "+str(g)+": "+str(populacao))

#verificando possiveis candidatos
for i,ind in enumerate(populacao):
    if ind[0][1] <= mochila:
        print(i+1, ind[0], ind[1:])
#fim

#fazendo elitismo beneficio
maior = [0,0]
for i,ind in enumerate(populacao):
    if (ind[0][1] <= mochila):
        if(ind[0][0] > maior[0]):
            maior = ind[0]
            maior_indice = i
populacao_g.append(populacao[maior_indice])
#fim

print(populacao_g)

#fazendo selecao dos melhores
selecao = 0
for ind in populacao[1:]:
    selecao = ind[0][0]/populacao[0][0][0]*100*tx_selecao
    if (ind[0][1] <= mochila):
        if randint(0, 99) <= selecao:
            populacao_g.append(ind)
print(populacao_g)
#fim

#fazendo cruzamento dos melhores
for ind in populacao[1:]
    for i in range(0,len(itens),2):
        if i in

#fim
