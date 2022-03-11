from math import prod

print('Seja bem vindo!\n')

num = int(input('Digite o numero que deseja executar um fatorial(!): '))
lista = []
for i in range(1,num+1):

    lista.append(i)

print('FATORIAL DE',num,':',prod(lista[::-1]))