from random import randint
from copy import deepcopy


# imprimindo geração
def imprime_geracao (populacao, g):
    print("Geração" + str(g) + "(" + str(len(populacao)) + "):" + str([item[0] for item in populacao]))
# fim

# imprimindo geração
def imprime_cruzamento (populacao, g):
    print("Cruzamento" + str(g) + "(" + str(len(populacao)) + "):" + str([item[0] for item in populacao]))
# fim

# imprimindo geração
def imprime_mutacao (populacao, g):
    print("Mutação" + str(g) + "(" + str(len(populacao)) + "):" + str([item[0] for item in populacao]))
# fim

# verificando possiveis candidatos
def verifica_candidatos (populacao, mochila):
    candidatos = []
    for i, ind in enumerate(populacao):
        if ind[0][1] <= mochila:
            candidatos.append(deepcopy(ind[0][0]))
    if len(candidatos) == 0:
        return 0
    return candidatos
# fim

# gerando individuo guloso
def guloso (itens, mochila):
    for item in itens:
        item.append(0)

    individuo = [[0, 0]]

    while individuo[0][1] < mochila:
        maior = [0, 1]
        for i, item in enumerate(itens):
            if (item[2] == 0):
                if (item[0] / item[1] > maior[0] / maior[1]):
                    maior = item
                    maior_indice = i
        itens[maior_indice][2] = 1
        individuo.append(maior_indice)
        individuo[0][0] += maior[0]
        individuo[0][1] += maior[1]
    individuo[0][0] -= itens[individuo[-1]][0]
    individuo[0][1] -= itens[individuo[-1]][1]
    individuo.pop()
    individuo[1:] = sorted(individuo[1:])

    for item in itens:
        item.pop()
    return individuo
# fim

# gerando individuo aleatorio
def populacao_aleatoria (itens, mochila):
    individuo = [[0, 0]]
    while individuo[0][1] < mochila:
        item = randint(0, len(itens)-1)
        if not (item in individuo):
            individuo.append(item)
            individuo[0][0] += itens[item][0]
            individuo[0][1] += itens[item][1]
    if individuo[0][1] > mochila:
        individuo.remove(item)
        individuo[0][0] -= itens[item][0]
        individuo[0][1] -= itens[item][1]
    return individuo
# fim

# escolhendo o melhor individuo (elitismo)
def elitismo (populacao, mochila):
    populacao_e = []
    maior = [0, 0]
    maior_indice = 0
    for i, ind in enumerate(populacao):
        if (ind[0][1] <= mochila):
            if (ind[0][0] > maior[0]):
                maior = ind[0]
                maior_indice = i
    populacao_e.append(deepcopy(populacao[maior_indice]))
    populacao.remove(ind)
    return populacao_e
# fim

# fazendo cruzamento
def cruzamento (populacao, itens, tx_cruzamento):
    populacao_c = []
    while len(populacao) > 1:
        rand = randint(0,len(populacao)-1)
        populacao_c.append(populacao[rand])
        populacao_c.append(populacao[(rand+len(populacao))%len(populacao)])
        if randint(0, 99) <= tx_cruzamento * 100:
            filhos = []
            filhos.append(populacao[rand])
            filhos.append(populacao[(rand+len(populacao))%len(populacao)])
            for i in range(int(len(itens) / 2)):
                if (i in filhos[0][1:]):
                    if not (i in filhos[1][1:]):
                        filhos[1].append(i)
                        filhos[1][0][0] += itens[i][0]
                        filhos[1][0][1] += itens[i][1]
                        filhos[0].remove(i)
                        filhos[0][0][0] -= itens[i][0]
                        filhos[0][0][1] -= itens[i][1]
                else:
                    if (i in filhos[1][1:]):
                        filhos[0].append(i)
                        filhos[0][0][0] += itens[i][0]
                        filhos[0][0][1] += itens[i][1]
                        filhos[1].remove(i)
                        filhos[1][0][0] -= itens[i][0]
                        filhos[1][0][1] -= itens[i][1]
            populacao_c.append(deepcopy(filhos[0]))
            populacao_c.append(deepcopy(filhos[1]))
        populacao.remove(populacao[rand])
        populacao.remove(populacao[(rand+len(populacao))%len(populacao)])
    if len(populacao) > 0:
        populacao_c.append(populacao[0])

    return populacao_c
# fim

# fazendo mutacao
def mutacao (populacao, itens, tx_mutacao):
    populacao_m = []
    qde_cromossomos = int(len(itens)/5)
    for ind in populacao:
        if randint(0, 99) <= tx_mutacao * 100:
            mutante = deepcopy(ind)
            cromossomo = randint(0, len(itens)-1)
            for i in range(qde_cromossomos):
                if int((cromossomo + i * qde_cromossomos) % len(itens)) in mutante:
                    mutante.remove(int((cromossomo + i * qde_cromossomos) % len(itens)))
                    mutante[0][0] -= itens[int((cromossomo + i * qde_cromossomos) % len(itens))][0]
                    mutante[0][1] -= itens[int((cromossomo + i * qde_cromossomos) % len(itens))][1]
                else:
                    mutante.append(int((cromossomo + i * qde_cromossomos) % len(itens)))
                    mutante[0][0] += itens[int((cromossomo + i * qde_cromossomos) % len(itens))][0]
                    mutante[0][1] += itens[int((cromossomo + i * qde_cromossomos) % len(itens))][1]
            populacao_m.append(deepcopy(mutante))
        else:
            populacao_m.append(deepcopy(ind))

    return populacao_m
# fim

# fazendo competicao roleta x5
def selecao (populacao, mochila, tam_pop):
    populacao_s = []
    valor_total = 0
    peso_total = 0
    valor_acumulado = 0
    populacao_s.append(populacao[0])
    maior_v = 0
    maior_p = 0

    populacao = sorted(populacao)

    for ind in populacao:
        if ind[0][0] == 0:
            populacao.remove(ind)
        valor_total += ind[0][0]
        peso_total += ind[0][1]
        if ind[0][0] > maior_v:
            maior_v = ind[0][0]
        if ind[0][1] > maior_p:
            maior_p = ind[0][1]

    #funcao aptidao
    for ind in populacao:
        valor_acumulado += int(ind[0][0] - valor_total / ind[0][1] * (ind[0][1] - mochila) + valor_total)
        ind[0].append(valor_acumulado)
    print(populacao)

    #selecao por roleta de 5
    roleta = 5
    while len(populacao_s) < tam_pop-1:
        vitorioso = [int(randint(0, int(valor_acumulado)))]
        for i in range(roleta-1):
            vitorioso.append(vitorioso[i]+int(valor_acumulado)%roleta)
        for ind in populacao:
            for i in range(roleta):
                if (vitorioso[i] != 0):
                    if ind[0][2] >= vitorioso[i]:
                        populacao_s.append(ind)
                        vitorioso[i] = 0
    while len(populacao_s) > tam_pop:
        populacao_s.pop()
    for ind in populacao:
        ind[0].pop()

    print(populacao_s)

    populacao_s = sorted(populacao_s, reverse=True)

    return populacao_s
# fim