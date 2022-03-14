import numpy as np
import random

print('Seja bem vindo!\n')

nota1 = 0
nota2 = 0
cont = 0

notas = int(input('Quantas notas bimestrais aleatorias deseja gerar: '))
while (notas > 100) or (notas < 0):
    print('Extensão de notas invalida! informe novamente!')
    notas = int(input('Quantas notas bimestrais aleatorias deseja gerar: '))

for i in range(notas):

    nota1 = random.randint(1,10)
    nota2 = random.randint(1,10)
    media = ((nota1 + nota2) / 2)
    cont = cont + 1
    print('NOTA',cont,':','NOTA 1:',nota1,'|','NOTA 2:',nota2,'|','MÉDIA:',media)




