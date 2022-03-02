# LISTA DE EXERCICIO - PYTHON INICIANTE
#CRIADO POR MARCOS ANDRÉ MARQUES CELESTINO
#YOUTUBE: TUXAUA CONCURSEIRO
#15

import datetime
from sys import exit

print('GERADOR DE FOLHA SALARIAL EM REGIME BRASILEIRO (CLT)\n')

print('SEJA BEM VINDO!\n')

#PERGUNTAS ESSENCIAIS
nome = input('Por favor, digite seu nome: ')
matricula = int(input('Informe sua matricula:'))

#PERGUNTAS TECNICAS
hora_trab = int(input('Informe o valor da sua hora/trabalho: '))
ch_semanal = int(input('Informe quantas horas trabalha por semana: '))
p_sind = input('Você contribui com o sindicato do trabalho? responda em MAIUSCULO (S ou N): ')
print('\n')

#VARIAVEIS
calculo_salariobruto = (hora_trab*(ch_semanal*4))
imposto_renda = (calculo_salariobruto*(11/100))
inss = (calculo_salariobruto*(8/100))
sindicato = (calculo_salariobruto*(5/100))

#CONDICIONAIS
if calculo_salariobruto >= 4375 and p_sind == 'S': #ATUALIZADO 02/09/2021 PL 2337
    calculo_liquido= (calculo_salariobruto-(imposto_renda+inss+sindicato))
    print('Funcionário:', nome, '| Matricula:', matricula, '| Salário Bruto:', calculo_salariobruto, 'R$')
    print('Desconto - IMPOSTO DE RENDA:', imposto_renda,'R$')
    print('Desconto - INSS (PREVIDÊNCIA):', inss,'R$')
    print('Desconto - SINDICATO:', sindicato,'R$')
    print('Salário Líquido Mensal: {:.2f}'.format((calculo_liquido)),'R$')
elif calculo_salariobruto >= 4375 and p_sind == 'N': #ATUALIZADO 02/09/2021 PL 2337
    calculo_liquido = (calculo_salariobruto - (imposto_renda + inss))
    print('Funcionário:', nome, '| Matricula:', matricula, '| Salário Bruto:', calculo_salariobruto, 'R$')
    print('Desconto - IMPOSTO DE RENDA:', imposto_renda,'R$')
    print('Desconto - INSS (PREVIDÊNCIA):', inss,'R$')
    print('Salário Líquido Mensal: {:.2f}'.format((calculo_liquido)),'R$')
if calculo_salariobruto < 4375 and p_sind == 'S': #ATUALIZADO 02/09/2021 PL 2337
    calculo_liquido = (calculo_salariobruto-(inss+sindicato))
    print('Funcionário:', nome, '| Matricula:', matricula, '| Salário Bruto:', calculo_salariobruto, 'R$')
    print('Desconto - INSS (PREVIDÊNCIA):', inss,'R$')
    print('Desconto - SINDICATO:', sindicato,'R$')
    print('Salário Líquido Mensal: {:.2f}'.format((calculo_liquido)),'R$')
elif calculo_salariobruto < 4375 and p_sind == 'N': #ATUALIZADO 02/09/2021 PL 2337
    calculo_liquido = (calculo_salariobruto - inss)
    print('Funcionário:', nome, '| Matricula:', matricula, '| Salário Bruto:', calculo_salariobruto, 'R$')
    print('Desconto - INSS (PREVIDÊNCIA):', inss,'R$')
    print('Salário Líquido Mensal: {:.2f}'.format((calculo_liquido)),'R$')

print('\n')
print('Essa aplicação foi utilizada em: ',datetime.date.today())


