#CRIADO POR: MARCOS ANDRÉ MARQUES CELESTINO
#CANAL NO YTB: TUXAUA CONCURSEIRO
#16

import datetime
import random
import numpy as np
import math

print('Aplicação para loja de tintas - Calculo de Custo em Área Pintada\n')

cond1 = input('Você sabe o tamanho em M2 da área a ser pintada? responda com S ou N: ')
area = 0

#CONDIÇÕES
if cond1 == 'N':
    largura = int(input('Informe a largura da área: '))
    altura = int(input('Informe a altura da área: '))
    comprimento = int(input('Informe o comprimento da área: '))
    calculo_area = (largura*altura*comprimento)
    print('A área em M2 do local é: {:.2f}'.format(calculo_area))
    area = calculo_area
elif cond1 == 'S':
    area = int(input('Informe o valor em M2 da sua área: '))

#1L PARA 3 METROS QUADRADOS
#18L PARA 54 METROS QUADRADOS

formula_lata = round(area/54) ## VAI DAR IGUAL O NUMERO DE LATAS
formula_preco = (formula_lata*80)

print('Sr/Sra. Fulano, Você tem uma área de: {:.2f}'.format(area),'\n')
print('Você terá que comprar',formula_lata,'de tinta')
print('E você pagará',formula_preco,'R$')

print('\n')
print('Essa aplicação foi utilizada em: ',datetime.date.today())
