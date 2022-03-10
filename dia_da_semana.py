import numpy as np
import calendar
import sys

ano = int(input('Informe o ano: '))
mes = int(input('Informe o mês: '))
dia = int(input('Informe o dia: '))

dia_semana = (calendar.weekday(ano,mes,dia))
print('\n')

if dia_semana == 0:

    print('Hoje é:',dia,'/',mes,'/',ano,'e estamos em uma SEGUNDA-FEIRA!')

elif dia_semana == 1:

    print('Hoje é:', dia, '/', mes, '/', ano, 'e estamos em uma TERÇA_FEIRA!')

elif dia_semana == 2:

    print('Hoje é:', dia, '/', mes, '/', ano, 'e estamos em uma QUARTA-FEIRA!')

elif dia_semana == 3:

    print('Hoje é:', dia, '/', mes, '/', ano, 'e estamos em uma QUINTA-FEIRA!')

elif dia_semana == 4:

    print('Hoje é:', dia, '/', mes, '/', ano, 'e estamos em uma SEXTA-FEIRA!')

elif dia_semana == 5:

    print('Hoje é:', dia, '/', mes, '/', ano, 'e estamos em um SÁBADO!')

elif dia_semana == 6:

    print('Hoje é:', dia, '/', mes, '/', ano, 'e estamos em um DOMINGO!')



