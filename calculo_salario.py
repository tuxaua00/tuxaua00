# LISTA DE EXERCICIO - PYTHON INICIANTE
#8
import datetime

print('CALCULADORA DE SALÁRIO POR HORA TRABALHADA\n')

funcionario = input('Informe seu nome: ')
hora_trab = float(input('Informe quanto você ganha por hora trabalhada: '))
hora_sem = int(input('Informe quantas horas você trabalha por semana: '))
hora_mes = (hora_sem*4)
calculo_salario = (hora_trab*hora_mes)

print('\n')
print('Sr/Sra.',funcionario,'você trabalha ao todo:',hora_mes,'horas por mês!\n')
print('E o seu salário atual é:',calculo_salario)

print('\n')
print('Essa aplicação foi utilizada em: ',datetime.date.today())
