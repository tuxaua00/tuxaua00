import math
import statistics
import random

print('Seja bem vindo!\n')

qtd_turma = int(input('Quantas turmas existem na escola: '))

lista_alunos_turma = []
cont = 0

for i in range(qtd_turma):

    cont = cont + 1
    print('TURMA',cont)
    qtd_alunos = int(input('Informe quantos alunos da turma: '))
    while (qtd_alunos < 0) or (qtd_alunos > 40):
        print('Quantidade de alunos invalida! informe novamente')
        qtd_alunos = int(input('Informe quantos alunos da turma: '))
    lista_alunos_turma.append(qtd_alunos)

mediaTurmas = (sum(lista_alunos_turma)/qtd_turma)

print('\nMÉDIA DE ALUNOS POR TURMA: {:.2f}'.format(mediaTurmas))
ko = 0

for i in range(qtd_turma):

    ko = ko + 1
    print ('ALUNOS DA TURMA',ko,':',lista_alunos_turma[i])













