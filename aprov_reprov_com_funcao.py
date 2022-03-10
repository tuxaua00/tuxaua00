import numpy as np

def calc_media(a,b):

    media = ((a+b)/2)

    return media

def aproveitamento(x):

    conceito = ''

    if x >= 9 and x <= 10:

        conceito = 'A'

    elif x >= 7.5 and x < 9:

        conceito = 'B'

    elif x >= 6 and x < 7.5:

        conceito = 'C'

    elif x >= 4 and x < 6:

        conceito = 'D'

    elif x >= 0 and x < 4:

        conceito = 'E'

    return conceito

def menu():

    print('Seja bem vindo!\n')

    nome = input('Por favor, informe seu nome: ')
    matricula = int(input('Informe sua matricula: '))

    nota1 = float(input('Informe sua 1a NOTA: '))
    nota2 = float(input('Informe sua 2a NOTA: '))

    x = calc_media(nota1,nota2)
    lista = aproveitamento(x)


    if lista == 'A' or lista == 'B' or lista == 'C':

        print('\nNOME:',nome.upper(),'|','MATRICULA:',matricula,'|','MEDIA: {:.2f}'.format(x))
        print('SITUAÇÃO: APROVADO','|','CONCEITO:',aproveitamento(x))

    elif lista == 'D' or lista == 'E':

        print('\nNOME:', nome.upper(), '|', 'MATRICULA:', matricula,'|','MEDIA: {:.2f}'.format(x))
        print('SITUAÇÃO: REPROVADO', '|', 'CONCEITO:', aproveitamento(x))

menu()



