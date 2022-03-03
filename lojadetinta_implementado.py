#CRIADO POR: MARCOS ANDRÉ MARQUES CELESTINO
#CANAL NO YTB: TUXAUA CONCURSEIRO
#17

import datetime
import random
import numpy as np
import math

print('Aplicação para loja de tintas - Calculo de Custo em Área Pintada (IMPLEMENTADO)\n')

cond1 = input('Você sabe o tamanho em M2 da área a ser pintada? responda com S ou N: ')
area = 0

#CONDIÇÕES_1

if cond1 == 'N':
    largura = int(input('Informe a largura da área: '))
    altura = int(input('Informe a altura da área: '))
    comprimento = int(input('Informe o comprimento da área: '))
    calculo_area = (largura*altura*comprimento)
    area = calculo_area
elif cond1 == 'S':
    area = int(input('Informe o valor em M2 da sua área: '))

#1L PARA 3 METROS QUADRADOS
#18L PARA 54 METROS QUADRADOS

formula_lata = round(area/108) ## VAI DAR IGUAL O NUMERO DE LATAS
formula_galao = round(area/21.6)
formula_preco_lata = (formula_lata*80)
formula_preco_galao = (formula_galao*25)

print('Você quer comprar a tinta em LATA ou GALÃO?\n')
cond2 = input('Responda com L (PARA LATA) ou G (PARA GALÃO) ou D (PARA COMPRAR OS DOIS): ')
print('\n')

#CONDIÇÕES_2

#COMPRA EM LATA
if cond2 == 'L':
    print('Sr/Sra. Fulano, Você tem uma área de: {:.2f}'.format(area),'Metros Quadrados\n')
    print('Você terá que comprar', formula_lata, 'LATA de tinta')
    print('E você pagará', formula_preco_lata, 'R$')
#COMPRA EM GALÃO
elif cond2 == 'G':
    print('Sr/Sra. Fulano, Você tem uma área de: {:.2f}'.format(area),'Metros Quadrados\n')
    print('Você terá que comprar', formula_galao, 'GALÃO de tinta')
    print('E você pagará', formula_preco_galao, 'R$')
#COMPRAR OS DOIS
elif cond2 == 'D':
    
print('\n')
print('Essa aplicação foi utilizada em: ',datetime.date.today())
