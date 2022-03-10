import numpy as np
import sys
import math
import cmath


def calc_equacao(a,b,c):

    equacao = (b*b - (4*a*c))

    return equacao

def menu():

    print('Seja bem vindo!\n')
    print('Equação do 2° GRAU : b**2 - 4*a*c \n')

    a = int(input('Informe o valor do A: '))
    if a == 0:
        print('\nnão existe equação para esse valor!')
        exit(1)
    b = int(input('Informe o valor de B: '))
    c = int(input('Informe o valor de C: '))

    resultado = calc_equacao(a,b,c)
    delta = cmath.sqrt(resultado)

    #FORMULA DAS RAIZES
    raiz1 = ((-b - delta)/2*a)
    raiz2 = ((-b + delta)/2*a)

    if resultado < 0:

        print('\nO resultado da descriminante:',resultado,'não possue raizes reais!')
        exit(1)

    elif resultado == 0:

        print('\nO resultado da descriminante:',resultado,'possui uma raiz real:')
        print('X1:',raiz2)

    elif resultado > 0:

        print('\nO resultado da descriminante:', resultado, 'possui uma raiz real:')
        print('X1:{:.2f}'.format(raiz1),'|','X2:{:.2f}'.format(raiz2))

menu()