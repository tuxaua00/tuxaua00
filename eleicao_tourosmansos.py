import sys
import statistics

print('Seja bem vindo!\n')

print('ELEIÇÃO DOS TOUROS MANSOS!\n')

qtd_eleitores = int(input('Informe a quantidade de eleitores nessa eleição: '))
while (qtd_eleitores < 0):
    print('Quantidade de eleitores invalida! por favor, informe novamente')
    qtd_eleitores = int(input('Informe a quantidade de eleitores nessa eleição: '))
while (qtd_eleitores > 50):
    print('Muitos eleitores para uma aplicação... informe um número menor!')
    qtd_eleitores = int(input('Informe a quantidade de eleitores nessa eleição: '))

print('1° CANDIDATO: THEO | 2° CANDIDATO: CARLOS | 3° CANDIDATO: ROBSON\n')
votos = []

def votacao(x):

    voto_final = 0

    if x == 1:

        voto_final = 1

    elif x == 2:

        voto_final = 2

    elif x == 3:

        voto_final = 3

    elif x == 0:

        voto_final = voto_final

    return votos.append(voto_final)

for i in range(qtd_eleitores):

    num = int(input('INFORME O NÚMERO DO CANDIDATO QUE VOCÊ DESEJA VOTAR: '))
    while num < 0 or num > 3:
        print('Número de candidato invalido! informe novamente')
        num = int(input('INFORME O NÚMERO DO CANDIDATO QUE VOCÊ DESEJA VOTAR: '))

    votacao(num)

contagem = statistics.mode(votos)
if contagem == 1:
    ganhador = 'THEOMARIO, NOVO TOURO MANSO!'
elif contagem == 2:
    ganhador = 'ROBSON, NOVO TOURO MANSO!'
elif contagem == 3:
    ganhador = 'CARLOS, NOVO TOURO MANSO!'
else:
    ganhador = 'NINGUEM GANHOU ><'


print('\nRESULTADO DA ELEIÇÃO')
print('THEO:',votos.count(1),'VOTOS','|','ROBSON:',votos.count(2),'VOTOS',
      '|','CARLOS:',votos.count(3),'VOTOS','|','VOTOS NULOS:',votos.count(0))
print('GANHADOR DA ELEIÇÃO:',ganhador)



