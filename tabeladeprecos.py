import statistics
import math

print('Seja bem vindo!\n')
print('LOJAS QUASE DOIS... ><\n')

preco = 1.99
prod = 0
lista_preco = [1.99]

for i in range(49):
    preco = (preco + 1.99)
    lista_preco.append(preco)

for i in range(50):
    prod = prod + 1
    print('PRODUTO -', prod, '|', 'PREÇO: {:.2f}'.format(lista_preco[i]), 'R$')