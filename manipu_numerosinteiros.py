# LISTA DE EXERCICIO - PYTHON INICIANTE
#11
import datetime
from sys import exit

print('MANIPULAÇÃO DE NÚMEROS INTEIROS\n')

num1 = int(input('Informe um número de 0 a 9: '))
if num1 < 0 and num1 > 9:
    exit(1)
num2 = int(input('Informe um número de 0 a 9: '))
if num2 < 0 and num2 > 9:
    exit(1)
num3 = int(input('Informe um número de 0 a 9: '))
if num3 < 0 and num3 > 9:
    exit(1)

produto_nums = ((num1*2)*(num2/2))
soma_nums = ((num1*3)+num3)
cubo_nums = (num3**3)

print('\n')
print('O produto do dobro do primeiro número com metade do segundo número: ',produto_nums)
print('A soma do triplo do primeiro número com o terceiro: ',soma_nums)
print('O terceiro elevado ao cubo: ', cubo_nums)

print('\n')
print('Essa aplicação foi utilizada em: ',datetime.date.today())
