import sys
import os
from math import prod

#TA COM GAMBIARRA, SE FOR USAR NÃO TENTE ALTERAR MUITO!

print('Seja bem vindo!\n')

def fatorial():
    print('\n')
    num = int(input('Digite o numero que deseja executar um fatorial(!): '))
    while (num > 16) or (num < 0):
        print('Valor invalido! informe novamente')
        num = int(input('Digite o numero que deseja executar um fatorial(!): '))

    lista = []
    for i in range(1,num+1):

        lista.append(i)

    print('\nFATORIAL DE',num,':',prod(lista[::-1]))

fatorial()

def retorno(n):

    if n.upper() == 'S':
        fatorial()
    elif n.upper() == 'N':
        exit(0)

x = 0

while (x < 100):
    x += 1
    print('\nDeseja calcular outro fatorial?')
    cond=input('S para SIM | N para NÃO: ')
    retorno(cond.upper())


