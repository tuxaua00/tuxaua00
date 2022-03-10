import numpy as np

def desconto_ir(salario):

    salario1 = 0

    if salario < 900:

        salario1 = salario

    elif salario > 900 and salario <= 1500:

        salario1 = (salario-(salario*(5/100)))

    elif salario > 1500 and salario <= 2500:

        salario1 = (salario-(salario*(10/100)))

    elif salario > 2500:

        salario1 = (salario-(salario*(20/100)))

    return salario1

def desconto_sindicato(salario):

    desc_sind = (salario-(salario*(3/100)))

    return desc_sind

def fgts(salario):

    fgts_mensal = (salario-(salario*(11/100)))

    return fgts_mensal

def menu():

    print('Seja bem vindo!\n')

    nome = input('Por favor, informe seu nome:')
    matricula = int(input('Informe sua matricula: '))
    d_hr = int(input('Informe quanto você ganha por hora: '))
    h_sm = int(input('Informe quantas horas você trabalha por semana: '))

    salario_bruto = (d_hr*(h_sm*4))

    #DESCONTOS
    desc_ir = (salario_bruto-desconto_ir(salario_bruto))
    desc_sind = (salario_bruto-desconto_sindicato(salario_bruto))
    fg = (salario_bruto-fgts(salario_bruto))
    sl_liquido = (salario_bruto - (desc_ir+desc_sind))

    print('\nNOME:',nome.upper(),'|','MATRICULA:',matricula,'|','SALARIO_BRUTO:',salario_bruto,'R$')
    print('DESCONTO_IR: {:.2f}'.format(desc_ir),'|','DESCONTO_SINDICATO: {:.2f}'.format(desc_sind))
    print('FGTS: {:.2f}'.format(fg),'|','SALARIO_LIQUIDO: {:.2f}'.format(sl_liquido))

menu()



