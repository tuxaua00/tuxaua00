import math
import statistics

print('Seja bem vindo!\n')

print('Padaria do Babão\n')

preco = 0.18
cont = 0

lista_preco = [0.18]

for i in range(50):

    preco = preco + 0.18
    lista_preco.append(preco)

for i in range(50):

    cont = cont + 1
    print('PRODUTO -',cont,'|','PREÇO: {:.2f}'.format(lista_preco[i]),'R$')


