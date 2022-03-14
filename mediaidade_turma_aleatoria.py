import numpy as np
import random

def identificador(x):

    result = ''

    if x > 0 and x < 25:

        result = 'JOVEM'

    elif x > 25 and x < 60:

        result = 'ADULTA'

    elif x > 60:

        result = 'IDOSA'

    return result

print('Seja bem vindo!\n')

qtd_pessoas = int(input('Com quantas pessoas você deseja falar: '))
while (qtd_pessoas < 0):
    print('Comando invalido! informe novamente ')
    qtd_pessoas = int(input('Com quantas pessoas você deseja falar: '))
while (qtd_pessoas > 40):
    print('Você quer falar com pessoas demais! diminua esse número ai ')
    qtd_pessoas = int(input('Com quantas pessoas você deseja falar: '))

idades = []
cont = 0

print('\n')

for i in range(qtd_pessoas):

    cont = cont + 1
    print('Pessoa N°',cont)
    idades.append(int(input('Qual a sua idade: ')))

mediaTurma = (sum(idades)/qtd_pessoas)

print('\nMÉDIA DE IDADE DA TURMA: {:.2f}'.format(mediaTurma))
print('ESSA TURMA É CONSIDERADA:',identificador(mediaTurma))




