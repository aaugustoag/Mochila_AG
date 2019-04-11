from random import randint

#        0     1     2     3     4     5     6     7     8     9     10    11
itens=[[3,5],[7,2],[4,5],[6,8],[3,6],[6,6],[7,1],[1,7],[1,1],[3,3],[3,2],[4,1]]

tam_pop=10
geracoes=10
tx_mutacao=0.1
tx_selecao=0.9
tx_cruzamento=0.9

populacao=[]
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

g=0

print("Geração"+str(g)+"("+str(len(populacao))+"):"+str([item[0] for item in populacao]))

# verificando possiveis candidatos
for i, ind in enumerate(populacao):
    if ind[0][1] <= mochila:
        print(i + 1, ind[0], ind[1:])
# fim

for k in range(geracoes):
    g=k+1

    #fazendo elitismo beneficio
    populacao_e=[]
    maior = [0,0]
    for j,ind in enumerate(populacao):
        if (ind[0][1] <= mochila):
            if(ind[0][0] > maior[0]):
                maior = ind[0]
                maior_indice = j
    populacao_e.append(populacao[maior_indice])
    print("Elite: "+str(populacao_e[0]))
    #fim
    '''
    #fazendo cruzamento
    pais=[]
    populacao_c=[]
    for ind in populacao[1:]:
        tx_infactibilidade=1
        if (ind[0][1] > mochila):
            tx_infactibilidade = mochila/ind[0][1]
        cruzamento = ind[0][0]/populacao[0][0][0]*100*tx_cruzamento*tx_infactibilidade
        if randint(0, 99) <= cruzamento:
            pais.append(ind)
        if len(pais) == 2:
            filhos=pais[:]
            for i in range(int(len(itens)/2)):
                if (i in filhos[0][1:]):
                    if not (i in filhos[1][1:]):
                        filhos[1].append(i)
                        filhos[0].remove(i)
                else:
                    if (i in filhos[1][1:]):
                        filhos[0].append(i)
                        filhos[1].remove(i)
            filhos[0][1:] = sorted(filhos[0][1:])
            filhos[1][1:] = sorted(filhos[1][1:])
            filhos[0][0]=[0,0]
            filhos[1][0]=[0,0]
            for item in filhos[0][1:]:
                filhos[0][0][0]+=itens[item][0]
                filhos[0][0][1]+=itens[item][1]
            for item in filhos[1][1:]:
                filhos[1][0][0]+=itens[item][0]
                filhos[1][0][1]+=itens[item][1]
            populacao_c.append(filhos[0])
            populacao_c.append(filhos[1])
            pais=[]
    print("Cruzamento"+str(g)+"("+str(len(populacao_c))+"):"+str([item[0] for item in populacao_c]))
    #fim
  '''
    #fazendo mutação
    populacao_m=[]
    for ind in populacao_m[1:]:
        if randint(0,99)<= tx_mutacao*100:
            mutante = ind
            for i in range(int(len(itens))):
                if randint(0,99)<= tx_mutacao*100:
                    if i in mutante:
                        mutante.remove(i)
                    else:
                        mutante.append(i)
                        mutante[1:]=sorted(mutante[1:])
                mutante[0]=[0,0]
                for item in mutante[1:]:
                    mutante[0][0]+=itens[item][0]
                    mutante[0][1]+=itens[item][1]
            populacao_m.remove(ind)
            populacao_m.append(mutante)
    print("Mutacao"+str(g)+"("+str(len(populacao_m))+"):"+str([item[0] for item in populacao_m]))
    #fim

    populacao=populacao_e[:]+populacao_m[:]
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

    # gerando o restante da populacao
    while len(populacao)<tam_pop:
        individuo = [[0, 0]]
        for j, item in enumerate(itens):
            if randint(0, 1) == 1:
                individuo.append(j)
                individuo[0][0] += item[0]
                individuo[0][1] += item[1]
        populacao.append(individuo)
    # fim
    '''
    print("Geração"+str(g)+"("+str(len(populacao))+"):"+str([item[0] for item in populacao]))

    #verificando possiveis candidatos
    for i,ind in enumerate(populacao):
        if ind[0][1] <= mochila:
            print(i+1, ind[0], ind[1:])
#fim
