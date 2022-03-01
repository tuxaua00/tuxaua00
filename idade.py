#EXERCICIO - IDENTIFICAR IDADE DA PESSOA
from sys import exit

print('SEJA BEM VINDO!\n')

idade = int(input('Quantos anos vocês tem?\n'))
cond1 = 'Criança'
cond2 = 'Aborrecente'
cond3 = 'Adulto'
cond4 = 'Idoso'


if idade >= 0 and idade <= 10:
    print('Você tem',idade,'anos e é considerado', cond1)
elif idade > 10 and idade < 18:
    print('Você tem',idade,'anos e é considerado:',cond2)
elif idade >=18 and idade < 60:
    print('Você tem',idade,'anos e é considerado:',cond3)
elif idade >= 60 and idade < 80:
    print('Você tem',idade,'anos e é considerado:',cond4)
elif idade >= 80 and idade < 120:
    print('VOCÊ É UM ANCIÃO, MEUS PARABÉNS PELA SÁUDE!')
elif idade < 0:
    print('IDADE INVALIDA, POR FAVOR REINICIE O PROGRAMA!')
    exit(1)
elif idade > 120:
    print('IDADE INVALIDA, POR FAVOR REINICIE O PROGRAMA!')
    exit(1)



