# LISTA DE EXERCICIO - PYTHON INICIANTE
#CRIADO POR MARCOS ANDRÉ MARQUES CELESTINO
#13

import datetime
from sys import exit

print('Calculo de multa por KG excendente')

valor_kg = float(input('Informe o valor do KG do peixe atual: '))
kg_pescado = float(input('Informe quantos KGs você pescou: '))
pagamento = (valor_kg*kg_pescado)

if kg_pescado < 50:
    print('Você vai pagar: {:.2f} R$ ao total!'.format(pagamento))

elif kg_pescado >= 50:
    kg_excedente = (kg_pescado - 50)
    formula_excedente = (50*valor_kg+(kg_excedente*4))

    print('Você vai pagar: {:.2f} R$, incluso multa por KG excendente (Acima de 50KG)'.format(formula_excedente))

print('\n')
print('Essa aplicação foi utilizada em: ',datetime.date.today())


