import numpy as np
import pandas as pd


print('Seja bem vindo!\n')

nome = input('Por favor, informe seu nome: ')
print('\nInforme seu turno: MATUTINO = M | VESPERTINO = V | INTEGRAL = I | NOTURNO = N')
turno = input('Informe a sigla do seu turno: ')

if turno.upper() == 'M':
    print('\nOlá',nome,'tenha um bom dia!')
elif turno.upper() == 'V':
    print('\nOlá',nome,'tenha uma boa tarde!')
elif turno.upper() == 'I':
    print('\nOlá',nome,'tenha um ótimo dia!')
elif turno.upper() == 'N':
    print('\nOlá',nome,'tenha uma boa noite!')
else:
    print('\nTurno informado inexistente, volte ao começo!')
    exit(1)

