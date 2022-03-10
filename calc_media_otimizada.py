import sys

def calc_nota(a,b,c):

    media = ((a+b+c)/3)
    return media

def situacao(x):

    td = ''

    if x > 7 and x < 10:
        td = 'APROVADO'
    if x < 7:
        td = 'REPROVADO'
    if x == 10:
        td = 'APROVADO COM DISTINÇÃO'

    return td

def menu():

    print('Seja bem vindo!\n')
    nome = input('Informe seu nome: ')
    matricula = input('Informe sua matricula: ')
    if len(matricula) > 5:
        print('\nMatricula Incorreta, tente novamente!')
        exit(1)
    nota_1 = int(input('Informe sua 1a nota: '))
    if nota_1 < 0 or nota_1 > 10:
        print('\nNota invalida!')
        exit(1)
    nota_2 = int(input('Informe sua 2a nota: '))
    if nota_2 < 0 or nota_2 > 10:
        print('\nNota invalida!')
        exit(1)
    nota_3 = int(input('Informe sua 3a nota: '))
    if nota_3 < 0 or nota_3 > 10:
        print('\nNota invalida!')
        exit(1)

    nota_final = calc_nota(nota_1,nota_2,nota_3)
    situacao_final = situacao(nota_final)

    print('\nNOME:',nome.upper(),'|','MATRICULA:',matricula)
    print('NOTA_FINAL: {:.2f}'.format(nota_final),'|','SITUAÇÃO:',situacao_final)

menu()


