itens=[[3,5],[7,2],[4,5],[6,8],[3,6],[6,6],[7,1],[1,7],[1,1],[3,3],[3,2],[4,1]]

tam_pop=10
geracoes=100
mutacao=0.1
cruzamento=0.8

populacao=[]
populacao_valor=[]
mochila=20
i0=[[0,0]]

itens_guloso = itens

for item in itens_guloso:
  item.append(0)

while i0[0][1] < mochila:
  maior = [0,1]
  for i,item in enumerate(itens_guloso):
    if (item[2]==0):
      if (item[0]/item[1] > maior[0]/maior[1]):
        maior = item
        maior_indice = i
  itens_guloso[maior_indice][2]=1
  i0.append(itens[maior_indice])
  i0[0][0]+=maior[0]
  i0[0][1]+=maior[1]
print(i0)
i0[0][0]-=i0[-1][0]
i0[0][1]-=i0[-1][1]
i0.pop()
print(i0)
