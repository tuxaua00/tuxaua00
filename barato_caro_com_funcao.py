import numpy as np


def mais_caro(x,y,z):

    caro = x

    if y > caro:
        caro = y
    if z > caro:
        caro = z

    return caro

def mais_barato(x,y,z):

    barato = x

    if y < barato:
        barato = y
    if z < barato:
        barato = z

    return barato

def menu():

    print('Seja bem vindo!\n')

    x = int(input('Informe o valor do produto 1 em R$: '))
    y = int(input('Informe o valor do produto 2 em R$: '))
    z = int(input('Informe o valor do produto 3 em R$: '))

    print('\nEsse aqui é o valor do mais caro: ', mais_caro(x,y,z),'R$')
    print('\nEsse aqui é o valor do mais barato: ', mais_barato(x,y,z),'R$')

menu()
