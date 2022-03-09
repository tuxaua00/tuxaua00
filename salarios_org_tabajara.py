import numpy as np

#CRIADO POR: MARCOS ANDRÉ M. CELESTINO - UNINORTE
#CANAL: TUXAUA CONCURSEIRO

def aumento_salarial(salario_atual):

    novo_salario = 0

    if salario_atual <= 280:

        novo_salario = (salario_atual+(salario_atual*(20/100)))

    elif salario_atual > 280 and salario_atual <= 700:

        novo_salario = (salario_atual+(salario_atual*(15/100)))

    elif salario_atual > 700 and salario_atual <= 1500:

        novo_salario = (salario_atual+(salario_atual*(10/100)))

    elif salario_atual > 1500:

        novo_salario =(salario_atual+(salario_atual*(5/100)))

    return novo_salario


def interacao():

    print('Seja bem vindo às organizações tabajara!\n')

    nome = input('Digite seu nome: ')
    salario_atual = int(input('Informe seu salario atual em R$: '))

    valor_aum = aumento_salarial(salario_atual) - salario_atual

    if salario_atual <= 280:

        print('\nNOME:',nome.upper(),'|','SALARIO ATUAL:',salario_atual,'|','VALOR DO AUMENTO: {:.2f}'.format(valor_aum))
        print('TAXA DE REAJUSTE: 20% | SÁLARIO REAJUSTADO:',aumento_salarial(salario_atual))

    elif salario_atual > 280 and salario_atual <= 700:

        print('\nNOME:', nome.upper(), '|', 'SALARIO ATUAL:', salario_atual, '|','VALOR DO AUMENTO: {:.2f}'.format(valor_aum))
        print('TAXA DE REAJUSTE: 15% | SÁLARIO REAJUSTADO:', aumento_salarial(salario_atual))

    elif salario_atual > 700 and salario_atual <= 1500:

        print('\nNOME:', nome.upper(), '|', 'SALARIO ATUAL:', salario_atual, '|','VALOR DO AUMENTO: {:.2f}'.format(valor_aum))
        print('TAXA DE REAJUSTE: 10% | SÁLARIO REAJUSTADO:', aumento_salarial(salario_atual))

    elif salario_atual > 1500:

        print('\nNOME:', nome.upper(), '|', 'SALARIO ATUAL:', salario_atual, '|','VALOR DO AUMENTO: {:.2f}'.format(valor_aum))
        print('TAXA DE REAJUSTE: 5% | SÁLARIO REAJUSTADO:', aumento_salarial(salario_atual))

#VAMOS CHAMAR A FUNÇÃO AGORA!

interacao()

#ESSE FICOU BONITO RSRS