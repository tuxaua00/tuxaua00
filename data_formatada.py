import calendar
import sys

print('Seja bem vindo!\n')

dia = int(input('Por favor, informe o dia: '))
if dia > 31 or dia < 1:
    print('Valor invalido!')
    exit(1)
mes = int(input('Por favor, informe o mês: '))
if mes > 12 or mes < 1:
    print('Valor invalido!')
    exit(1)
ano = int(input('Por favor, informe o ano: '))
if ano > 10000 or ano < 1:
    print('Valor invalido!')
    exit(1)

print('DATA INFORMADA:',dia,'/',mes,'/',ano)


