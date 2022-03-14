import math
import statistics
import sys

print('Seja bem vindo!\n')

qtd_cd = int(input('Informe quantos CDs você comprou: '))
while qtd_cd < 0:
    print('Quantidade de CDs invalida! informe novamente')
    qtd_cd = int(input('Informe quantos CDs você comprou: '))
while qtd_cd > 25:
    print('valor máximo por operação excedido! informe novamente')
    qtd_cd = int(input('Informe quantos CDs você comprou: '))

lista_cds = []
cont = 0
lista_precos = []

for i in range(qtd_cd):

    cont = cont + 1
    lista_cds.append(cont)

kont = 0
for i in range(qtd_cd):

    kont = kont + 1
    print('CD - NÚMERO',kont)
    lista_precos.append(int(input('Informe o valor em R$ do cd: ')))

kont = 0
for i in range(qtd_cd):

    kont = kont + 1
    print('\nCD - NÚMERO',kont,'|','VALOR:',lista_precos[i],'R$')




